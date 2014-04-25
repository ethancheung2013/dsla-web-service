import psycopg2

DB_NAME = 'times_tracker'
DB_USER = 'sam'

conn = psycopg2.connect("dbname=%s user=%s" % (DB_NAME, DB_USER))

def search(term):
    cur = conn.cursor()
    # This is terrible, never do this in real code. For several reasons:
    #     1. Remember when we talked about SQL injection? How could this function be used to 
    #        compromise our database?
    #     2. Using LIKE queries is really slow. If you want to implement search, use something 
    #        like ElasticSearch, which is designed for this sort of thing.
    cur.execute('''SELECT url, section, byline, title, abstract FROM articles WHERE abstract LIKE '%%%s%%';'''% (term,))
    for result in cur:
        yield result
                
