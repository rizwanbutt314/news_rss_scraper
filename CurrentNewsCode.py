import os
import json
import time
from datetime import date

import requests
import mysql.connector
from bs4 import BeautifulSoup


today = date.today()
_time = time.localtime()
basepath = os.path.dirname(os.path.abspath(__file__))
filename = f"{today}@{_time.tm_hour}.{_time.tm_min}.{_time.tm_sec}.json"

# MYSQL Settings
DB_HOST = "localhost"
DB_USERNAME = "root"
DB_PASSWORD = "mysql123"
DB_DATABASE = "frx"
DB_TABLE = "news_data"

SITES_MAPPING = {
    "https://finance.yahoo.com/rss/topstories": {
        "name": "Yahoo Finance News Top 10 Plus Links",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": "https://finance.yahoo.com/news/"
    },
    "https://feeds.a.dj.com/rss/RSSMarketsMain.xml": {
        "name": "WSJ Market News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": "https://www.wsj.com/articles/"
    },
    "https://feeds.a.dj.com/rss/RSSWorldNews.xml": {
        "name": "WSJ World News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": "https://www.wsj.com/articles/"
    },
    "https://feeds.a.dj.com/rss/RSSWSJD.xml": {
        "name": "WSJ Technology News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": "https://www.wsj.com/articles/"
    },
    "http://feeds.bbci.co.uk/news/rss.xml": {
        "name": "BBC Home News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": ""
    },
    "http://feeds.bbci.co.uk/news/world/rss.xml": {
        "name": "BBC World News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": ""
    },
    "http://feeds.bbci.co.uk/news/business/rss.xml": {
        "name": "BBC Business News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": ""
    },
    "http://feeds.bbci.co.uk/news/technology/rss.xml": {
        "name": "BBC Techology News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": ""
    },
    "http://feeds.bbci.co.uk/news/world/africa/rss.xml": {
        "name": "BBC Africa News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": ""
    },
    "http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml": {
        "name": "BBC Entertainment and Arts News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": ""
    },
    "http://xml.fxstreet.com/news/forex-news/index.xml": {
        "name": "The FXStreet News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "",
        "field_date": "pubdate",
        "link_base": ""
    },
    "https://www.dailyfx.com/feeds/market-news": {
        "name": "The DailyFX News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": ""
    },
    "https://www.dailyfx.com/feeds/technical-analysis": {
        "name": "The DailyFX Trading Strategies (Opinions)",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": ""
    },
    "https://www.economist.com/finance-and-economics/rss.xml": {
        "name": "The Economist Finace and Economics News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "link",
        "field_date": "pubdate",
        "link_base": ""
    },
    "https://www.economist.com/business/rss.xml": {
        "name": "The Economist Business News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "link",
        "field_date": "pubdate",
        "link_base": ""
    },
    "https://www.economist.com/science-and-technology/rss.xml": {
        "name": "The Economist Science and Technology News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "link",
        "field_date": "pubdate",
        "link_base": ""
    },
    "https://www.economist.com/middle-east-and-africa/rss.xml": {
        "name": "The Economist Middle East and Africa News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "link",
        "field_date": "pubdate",
        "link_base": ""
    },
    "https://www.economist.com/special-report/rss.xml": {
        "name": "The Economist The World This Week News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "link",
        "field_date": "pubdate",
        "link_base": ""
    },
    "http://feeds.bbci.co.uk/sport/football/rss.xml?edition=uk": {
        "name": "BBC Football News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": ""
    },
    "http://feeds.bbci.co.uk/sport/tennis/rss.xml?edition=uk": {
        "name": "BBC Tennis News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": ""
    },
    "http://feeds.bbci.co.uk/sport/golf/rss.xml?edition=uk": {
        "name": "BBC Golf News",
        "field_title": "title",
        "field_description": "description",
        "field_link": "guid",
        "field_date": "pubdate",
        "link_base": ""
    }
}


def save_to_json(data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


def save_to_db(data, source):
    mydb = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        database=DB_DATABASE,
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor(buffered=True)

    # Check for duplicates
    filtered_data = list()
    for record in data:

        # Check existing entry
        sql = f"""SELECT * FROM {DB_TABLE} WHERE title = %s AND source = %s """
        val = (record['title'], source)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if not myresult:
            filtered_data.append(record)
        else:
            # Update the existing data
            sql = f"""UPDATE {DB_TABLE} SET description = %s, _date = %s WHERE title = %s AND source = %s"""
            val = (record['description'], record['date'],
                    record['title'], source)
            mycursor.execute(sql, val)
            mydb.commit()

    # INSERT data
    sql = f"INSERT INTO {DB_TABLE} (title, description, link, _date, source) VALUES (%s, %s, %s, %s, %s)"

    data_to_db = [(d["title"], d["description"], d["link"], d["date"], source)
                  for d in filtered_data]

    mycursor.executemany(sql, data_to_db)
    mydb.commit()


def get_text(html, field_name):
    txt = ""
    if not field_name:
        return txt
    try:
        txt = html.find(field_name).text
    except:
        pass

    return txt


def get_news_data(url, meta={}):
    data = list()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")
    items = soup.find_all('item')
    for item in items[0:]:
        data.append({
            "title": get_text(item, meta["field_title"]),
            "description": get_text(item, meta["field_description"]),
            "link": f"{meta['link_base']}{get_text(item, meta['field_link'])}" if meta["link_base"] else get_text(item, meta["field_link"]),
            "date": get_text(item, meta["field_date"])
        })

    return data


def main():
    all_data = list()
    for url, meta in SITES_MAPPING.items():
        print(
            f"{meta['name']} _______________________________")
        data = get_news_data(url, meta)
        print(f"Total News extracted: {len(data)}")
        all_data.extend(data)
        # Save to database
        save_to_db(data, meta['name'])
        print(f"END of {meta['name']} ______________________\n ")

    # Save to json file
    save_to_json(all_data)
    


if __name__ == "__main__":
    main()
