import requests
import psycopg2

# Reads your API key from a file
with open('API_KEY.txt') as inf:
    API_KEY = inf.read().strip()

def most_popular_articles(category = 'mostemailed', section = 'all-sections', days = 1):
    query = 'http://api.nytimes.com/svc/mostpopular/v2/%s/%s/%d.json?api-key=%s' % (category, section, days, API_KEY)
    response = requests.get(query).json()
    return response

def save_result(result):
    pass
    
