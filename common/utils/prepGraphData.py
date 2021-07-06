import pandas as pd
from cov19.models import UsStatesData, WorldData, StatesReport, WorldReport

def prepWorldData():
    """World Critical Resource Stats"""

    worldResources, totalStats, totalFigs, worldStats = prepCriticalResources(WorldReport, WorldData, columnsToGroupby=['country','geoID'])
    return {'worldResources': worldResources, 'totalStats': totalStats, 'totalFigs': totalFigs, 'worldStats': worldStats}

def prepStateData():
    """US States Critical Resource Stats"""

    stateResources, totalStateStats, totalStateFigs, stateStats = prepCriticalResources(StatesReport, UsStatesData, columnsToGroupby=['state', 'fips'])
    return {'stateResources': stateResources, 'totalStateStats': totalStateStats, 'totalStateFigs': totalStateFigs, 'stateStats': stateStats}


def prepCriticalResources(reportObj, dataObj, columnsToGroupby=['country','geoID']):
    """Prepare Stats for the web page"""

    # Get the latest Date for the Stats
    filterDate = reportObj.objects.values_list('date', flat=True).distinct().order_by('-date')[0]

    # Data for the map
    requiredColumns = ['date', 'tothospBedNeeded', 'totCriticCareNeeded', 'totVentNeeded']
    report = reportObj.objects.values(*(requiredColumns+columnsToGroupby))
    dataDF = pd.DataFrame(dataObj.objects.values('date', 'newCases', 'newDeaths'))

    # Total Critical Resource Stats
    reportDF = pd.DataFrame(report)
    resources = reportDF[reportDF['date']==filterDate].to_dict('r')
    totalStats = reportDF[reportDF['date']==filterDate].groupby('date').sum().reset_index().to_dict('r')[0]

    # Data for Timeline graph
    totalStatDF = reportDF.groupby('date').sum().reset_index()
    totalDataDF = dataDF.groupby('date').sum().reset_index()
    stats = pd.merge(totalStatDF, totalDataDF, on='date').to_dict('r')

    # Figures of cases and deaths
    # Get the latest Date for figures
    filterDate = dataObj.objects.values_list('date', flat=True).distinct().order_by('-date')[0]
    totalFigs = dataDF[dataDF['date']==filterDate].groupby('date').sum().reset_index().to_dict('r')[0]

    return resources, totalStats, totalFigs, stats