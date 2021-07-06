from django.http import HttpResponse
from django.shortcuts import render
from common.utils.importData import retrieveData
from common.utils.createReports import prepReport
from common.utils.prepGraphData import prepWorldData, prepStateData

# Create your views here.


def index(request):
    """Index/World Map Page"""
    return render(request, 'index.html', prepWorldData())


def usStates(request):
    """US States Map Page"""
    return render(request, 'usStates.html', prepStateData())


def refresh(request):
    """Refresh Page"""
    return render(request, 'refreshPage.html', {})


def refreshData(request):
    """Refresh Data Sources"""
    return HttpResponse(retrieveData())


def refreshReport(request):
    """Refresh Reports"""
    return HttpResponse(prepReport())