# -*- coding: utf-8 -*-
from datetime import timedelta
from link_crawler import link_crawler
from mongo_cache import MongoCache
from alexa_cn import AlexaCallback



def main():
    scrape_callback = AlexaCallback()
    cache = MongoCache(expires=timedelta())
    #cache.clear()
    link_crawler(scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache)


if __name__ == '__main__':
    main()