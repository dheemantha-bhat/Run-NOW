from geopy.geocoders import Nominatim
import datetime as dt
import meteomatics.api as api


def run_now_raw(location,acc=10): 
    
    username = api_key
    password = secret_key

    coordinates = get_coordinates(location)
    parameters = ['precip_1h:mm']
    model = 'mix'
    enddate = dt.datetime.now(dt.UTC).replace(minute=0, second=0, microsecond=0)
    startdate  = enddate - dt.timedelta(hours=acc)
    interval = dt.timedelta(hours=1)

    df = api.query_time_series(coordinates, startdate, enddate, interval, parameters, username, password, model=model).reset_index()['precip_1h:mm'].values * 50

    water_log_score = waterlog_calculate(df)
    logging='High'
    if water_log_score<2:
        logging='Low'
    elif water_log_score<4:
        logging='Medium'
    else:
        logging='High'
    
    return logging

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(city_name)
    latlon=0
    if location:
        latlon = [(location.latitude, location.longitude)]
    else:
        latlon=[(0,0)]
    return latlon
    
def waterlog_calculate(x):
    log_num=0
    hours = len(x)

    for i in x:
        log = i - hours
        hours = hours -1
        if log<0:
            log_num=0
    return log_num