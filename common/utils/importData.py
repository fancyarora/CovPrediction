import pandas as pd
from common.utils.helper import insertToDb
from cov19.models import UsStatesData, WorldData


def retrieveData():
    """Retrieve Covid Data from sources such as NY TIMES and ECDC"""

    #Retrive Covid Data for all US States
    df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
    df['date'] = pd.to_datetime(df['date'])
    df[['newCases', 'newDeaths']] = df[['state', 'fips', 'cases', 'deaths']].groupby(['state', 'fips']).diff()
    df = df.fillna(0)
    df[['newCases', 'newDeaths']] = df[['newCases', 'newDeaths']].astype(int)
    statesDataStatus = insertToDb(df, UsStatesData)

    #Retrieve Covid Data for all countries in the world
    df = pd.read_csv("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv")
    df['date'] = pd.to_datetime(df['dateRep'], format='%d/%m/%Y')
    df = df.drop(['dateRep', 'day', 'month', 'year', 'countryterritoryCode', 'popData2019', 'continentExp', 'Cumulative_number_for_14_days_of_COVID-19_cases_per_100000'], axis=1)
    df = df.rename(columns={'cases':'newCases', 'deaths':'newDeaths', 'countriesAndTerritories':'country', 'geoId':'geoID'}).fillna(0)
    worldDataStatus = insertToDb(df, WorldData)

    return statesDataStatus + '<br>' + worldDataStatus + '<br>' + "Data Sources Refreshed!"