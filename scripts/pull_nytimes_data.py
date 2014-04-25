import requests
import psycopg2
from datetime import datetime


# Reads your API key from a file
with open('API_KEY.txt') as inf:
    API_KEY = inf.read().strip()
DB_NAME = 'times_tracker'
DB_USER = 'sam'

conn = psycopg2.connect("dbname=%s user=%s" % (DB_NAME, DB_USER))

def most_popular_articles(category = 'mostemailed', section = 'all-sections', days = 1):
    query = 'http://api.nytimes.com/svc/mostpopular/v2/%s/%s/%d.json?api-key=%s' % (category, section, days, API_KEY)
    response = requests.get(query).json()
    return response

def save_result(result):
    url = result.get('url')
    section = result.get('section')
    byline = result.get('byline')
    title = result.get('title')
    abstract = result.get('abstract')
    published_date_str = result.get('published_date')
    try:
        published_date = datetime(*map(int, published_date_str.split('-')))
    except ValueError:
        published_date = None
    cur = conn.cursor()
    cur.execute('''INSERT INTO articles (url, section, byline, title, abstract, published_date) VALUES (%s, %s, %s, %s, %s, %s);''', (url, section, byline, title, abstract, published_date))
    conn.commit()

if __name__ == '__main__':
    response = most_popular_articles()
    for article in response['results']:
        save_result(article)
