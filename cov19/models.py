from django.db import models

# Create your models here.

class UsStatesData(models.Model):
    """Covid Case/Death Numbers from all US States"""

    class Meta:
        unique_together = (('date', 'state', 'fips'),)

    date = models.DateField(name='date', verbose_name='Date')
    state = models.CharField(name='state', verbose_name='State', max_length=200)
    fips = models.IntegerField(name='fips', verbose_name='Fips', default=0)
    cases = models.BigIntegerField(name='cases', verbose_name='Total Cases', null=True)
    deaths = models.BigIntegerField(name='deaths', verbose_name='Total Deaths', null=True)
    newCases = models.BigIntegerField(name='newCases', verbose_name='New Cases', null=True)
    newDeaths = models.BigIntegerField(name='newDeaths', verbose_name='New Deaths', null=True)

    def __str__(self):
        return self.state

    class Meta:
        db_table = 'us_states_data'
        managed = True


class WorldData(models.Model):
    """Covid Case/Death Numbers from all countries in the world"""

    class Meta:
        unique_together = (('date', 'country', 'geoID'),)

    date = models.DateField(name='date', verbose_name='Date')
    day = models.BigIntegerField(name='day', verbose_name='Day', null=True)
    month = models.BigIntegerField(name='month', verbose_name='Month', null=True)
    year = models.BigIntegerField(name='year', verbose_name='Year', null=True)
    newCases = models.BigIntegerField(name='newCases', verbose_name='New Cases', null=True)
    newDeaths = models.BigIntegerField(name='newDeaths', verbose_name='New Deaths', null=True)
    country = models.CharField(name='country', verbose_name='Country', max_length=200)
    geoID = models.CharField(name='geoID', verbose_name='Geo Location ID', max_length=200)

    def __str__(self):
        return self.country

    class Meta:
        db_table = 'world_data'
        managed = True

class StatesReport(models.Model):
    """Critical Resource Report from all US States"""

    class Meta:
        unique_together = (('date', 'state', 'fips'),)

    date = models.DateField(name='date', verbose_name='Date')
    state = models.CharField(name='state', verbose_name='State', max_length=200)
    fips = models.IntegerField(name='fips', verbose_name='fips', default=0)
    hospBedNeeded = models.BigIntegerField(name='hospBedNeeded', verbose_name='Hospital Beds Needed', null=True)
    criticCareNeeded = models.BigIntegerField(name='criticCareNeeded', verbose_name='Critical Care Needed', null=True)
    ventNeeded = models.BigIntegerField(name='ventNeeded', verbose_name='Ventilator Needed', null=True)
    tothospBedNeeded = models.BigIntegerField(name='tothospBedNeeded', verbose_name='Total Hospital Beds Needed on Date', null=True)
    totCriticCareNeeded = models.BigIntegerField(name='totCriticCareNeeded', verbose_name='Total Critical Care Needed on Date', null=True)
    totVentNeeded = models.BigIntegerField(name='totVentNeeded', verbose_name='Total Ventilator Needed on Date', null=True)

    def __str__(self):
        return self.state

    class Meta:
        db_table = 'state_report'
        managed = True


class WorldReport(models.Model):
    """Critical Resource Report from all countries in the world"""

    class Meta:
        unique_together = (('date', 'country', 'geoID'),)

    date = models.DateField(name='date', verbose_name='Date')
    country = models.CharField(name='country', verbose_name='Country', max_length=200)
    geoID = models.CharField(name='geoID', verbose_name='Geo Location ID', max_length=200)
    hospBedNeeded = models.BigIntegerField(name='hospBedNeeded', verbose_name='Hospital Beds Needed', null=True)
    criticCareNeeded = models.BigIntegerField(name='criticCareNeeded', verbose_name='Critical Care Needed', null=True)
    ventNeeded = models.BigIntegerField(name='ventNeeded', verbose_name='Ventilator Needed', null=True)
    tothospBedNeeded = models.BigIntegerField(name='tothospBedNeeded', verbose_name='Total Hospital Beds Needed on Date', null=True)
    totCriticCareNeeded = models.BigIntegerField(name='totCriticCareNeeded', verbose_name='Total Critical Care Needed on Date', null=True)
    totVentNeeded = models.BigIntegerField(name='totVentNeeded', verbose_name='Total Ventilator Needed on Date', null=True)

    def __str__(self):
        return self.country

    class Meta:
        db_table = 'world_report'
        managed = True