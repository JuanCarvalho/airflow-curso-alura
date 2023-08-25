import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
API_URLS = {
    'weather': f'{BASE_URL}/VisualCrossingWebServices/rest/services/timeline',
}
