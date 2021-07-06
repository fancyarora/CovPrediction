"""
Definition of urls for CovPrediction.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cov19.urls')), #All urls from cov19 app are directed to the root path
]
