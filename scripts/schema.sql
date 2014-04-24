CREATE TABLE articles (
       id SERIAL PRIMARY KEY,
       url TEXT,
       section TEXT,
       byline TEXT,
       title TEXT,
       abstract TEXT,
       published_date DATE);
