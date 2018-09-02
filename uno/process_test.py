import sys

from alexa_cn import AlexaCallback
from mongo_cache import MongoCache
from process_crawler import process_crawler


def main(max_threads):
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    cache.clear()
    process_crawler(scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache, max_threads=max_threads, timeout=10)

if __name__ == '__main__':
    max_threads = int(sys.argv[1])
    main(max_threads)