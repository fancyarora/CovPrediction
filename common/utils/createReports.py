import pandas as pd
from cov19.models import UsStatesData, WorldData, StatesReport, WorldReport
from common.utils.helper import insertToDb


def prepReport():
    """Prepare Critical Resource report"""

    #Prepare the State Report
    df = pd.DataFrame(UsStatesData.objects.values()).drop(columns=['id', 'cases', 'deaths', 'newDeaths'])
    df = calcCriticalResources(df, columnsToGroupby=['state', 'fips'])
    statesReportStatus = insertToDb(df, StatesReport)

    #Prepare the World Report
    df = pd.DataFrame(WorldData.objects.values().order_by('date')).drop(columns=['id', 'day', 'month', 'year', 'newDeaths'])
    df = calcCriticalResources(df, columnsToGroupby=['country','geoID'])
    worldReportStatus = insertToDb(df, WorldReport)

    return statesReportStatus + '<br>' + worldReportStatus + '<br>' + "Report Tables Refreshed!"


def calcCriticalResources(df, columnsToGroupby=['country','geoID']):
    """Calculate Critical Resources"""

    df['date'] = pd.to_datetime(df['date'])

    # Assumptions
    # 80% patients recover at home in approx 7 days. 20% Patients hospitalized
    hospBedNeeded = df.set_index('date').groupby(columnsToGroupby)['newCases'].shift(periods=7, freq="D")*0.2

    # 6% patients are in critical condition on 7th Day
    criticCareNeeded = df.set_index('date').groupby(columnsToGroupby)['newCases'].shift(periods=7, freq="D")*0.06

    # 1 out of 6 patients need ventilators on 8th day
    ventNeeded = df.set_index('date').groupby(columnsToGroupby)['newCases'].shift(periods=8, freq="D")*0.166

    # Total is the sum of last 18 days. Patient discharged on 18th day
    tothospBedNeeded = hospBedNeeded.reset_index(columnsToGroupby).groupby(columnsToGroupby).rolling(window=18).sum()
    totCriticCareNeeded = criticCareNeeded.reset_index(columnsToGroupby).groupby(columnsToGroupby).rolling(window=18).sum()

    # For total ventilators, it'll be sum of last 17days, because ventilator is needed on day 8th
    totVentNeeded = ventNeeded.reset_index(columnsToGroupby).groupby(columnsToGroupby).rolling(window=17).sum()

    df = pd.concat([hospBedNeeded, criticCareNeeded, ventNeeded, tothospBedNeeded, totCriticCareNeeded, totVentNeeded], axis=1, join="inner")
    df.columns = ['hospBedNeeded', 'criticCareNeeded', 'ventNeeded', 'tothospBedNeeded', 'totCriticCareNeeded', 'totVentNeeded']
    df = df.dropna(subset=['hospBedNeeded', 'criticCareNeeded', 'ventNeeded']).fillna(0).round().reset_index()
    return df