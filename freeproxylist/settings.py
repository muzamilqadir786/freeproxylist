# -*- coding: utf-8 -*-

# Scrapy settings for freeproxylist project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'freeproxylist'

SPIDER_MODULES = ['freeproxylist.spiders']
NEWSPIDER_MODULE = 'freeproxylist.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'freeproxylist (+http://www.yourdomain.com)'
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
]

COOKIES_ENABLED = False
DOWNLOAD_DELAY = 0.25

# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
    # Fix path to this module
    'freeproxylist.randomproxy.RandomProxy': 100,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port

#PROXY_LIST = '/path/to/proxy/list.txt'
PROXY_LIST = './list.txt'
