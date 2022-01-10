### Description:
The purpose of this scraper is to extract the required information from following sites:
* https://finance.yahoo.com/rss/topstories
* https://feeds.a.dj.com/rss/RSSMarketsMain.xml
* https://feeds.a.dj.com/rss/RSSWorldNews.xml
* https://feeds.a.dj.com/rss/RSSWSJD.xml
* http://feeds.bbci.co.uk/news/rss.xml
* http://feeds.bbci.co.uk/news/world/rss.xml
* http://feeds.bbci.co.uk/news/business/rss.xml
* http://feeds.bbci.co.uk/news/technology/rss.xml
* http://feeds.bbci.co.uk/news/world/africa/rss.xml
* http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml
* http://xml.fxstreet.com/news/forex-news/index.xml
* https://www.dailyfx.com/feeds/market-news
* https://www.dailyfx.com/feeds/technical-analysis
* https://www.economist.com/finance-and-economics/rss.xml
* https://www.economist.com/business/rss.xml
* https://www.economist.com/science-and-technology/rss.xml
* https://www.economist.com/middle-east-and-africa/rss.xml
* https://www.economist.com/special-report/rss.xml
* http://feeds.bbci.co.uk/sport/football/rss.xml?edition=uk
* http://feeds.bbci.co.uk/sport/tennis/rss.xml?edition=uk
* http://feeds.bbci.co.uk/sport/golf/rss.xml?edition=uk

### PreReqs:
* Python: 3.6+

### Setup:
* create a virtual environment: `virtualenv -p /usr/bin/python3 env` (Optional)
* activate the environemnt: `source ./env/bin/activate` (Optional when you don't need first step)
* install requirements: `pip install -r requirements.txt`
* Edit `CurrentNewsCode.py` file to update the Datbase Settings according to yours
* Following are the Database variables which needs to be updated
```
DB_HOST = "localhost"
DB_USERNAME = "testUsername"
DB_PASSWORD = "testPassword"
DB_DATABASE = "testDatabase"
DB_TABLE = "testTable"
```

### Run:
* Command to run scraper: `python CurrentNewsCode.py`

### Note:
*  `requirements.txt` file contains the list of packages that are required to install.
* Extracted information will be saved in file: `year-month-day@hours.minutes.seconds.json`
* Plus the information will be saved in a MySQL database too.