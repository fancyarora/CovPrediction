# Covid Critical Resource Prediction

"Django Full Stack Web App to predict critical resources during the time of pandemic".

## Steps to run the project

### Setup virtualenv (optional)
cd venv/Scripts

activate

cd ../..


### Install dependencies for django & python

pip install -r requirements.txt

### Start Web Server

To start the web server you need to run the following sequence of commands.

python manage.py runserver

### Covid Data Sources
NY TIMES
US States: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

ECDC
World Data: https://opendata.ecdc.europa.eu/covid19/casedistribution/csv

### List of Critical Resource Predicted
Number of Hospital Beds needed

Number of Critical Care units needed

Number of Ventilators needed


### Assumptions from research while predicting Critical resources
80% patients recover at home in approx 7 days. 20% Patients hospitalized

6% patients are in critical condition on 7th Day

1 out of 6 patients need ventilators on 8th day

Total is the sum of last 18 days. Patient discharged on 18th day

For total ventilators, it'll be sum of last 17days, because ventilator is needed on day 8th
