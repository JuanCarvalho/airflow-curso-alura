import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
WEATHER_BASE_URL = 'https://weather.visualcrossing.com'
WEATHER_API_URLS = {
    'weather': f'{WEATHER_BASE_URL}/VisualCrossingWebServices/rest/services/timeline',
}

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
