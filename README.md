# nspide

A scrapy spider to extract news articles, currently from The Wall Street Journal (wsj.com).  The current behavior is to extract metadata from wsj (e.g., https://www.wsj.com/news/archive/20190701), and to send to the console.  The idea is to iterate through the dates and scrape metadata, followed by accessing the actual article.

Currently, nspide captures flashline, headline, link, and summary.  Out of the captured elements, link will be used to extract the content and any further details about specific article.

### dependencies

```
pip install scrapy
```

### important commands

```
cd /path/to/nspide
scrapy call wsj
```


