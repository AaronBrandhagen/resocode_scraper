# CLI for making search requests.
# pygoog will be the active command, followed by args.
# Pygoog will initiate the spider and the following arguments will make up the advanced search options.

import click
import scrapy
from scrapy.crawler import CrawlerProcess as CP
import resocode.spiders.rescode as rc
from bs4 import BeautifulSoup as bb
import requests

r = rc.RescodeSpider
r.download_delay=10

@click.command()
@click.option('--search', prompt='Enter search string here: ')
@click.option('--site', prompt='Would you like to search a specific site? If not, please press 1. Otherwise, '
                               'write the naem of the website, without a URL prefix or suffix: ')
def arrange_search_str(search, site):
    """
    A LOT of formatting needs to be done beforesearch can be passed to the queries argument.
    # Will ultimately lead to the formattedŒ`
    # string passed to r.queries (the
    # Spider's search arguments).

    formatted_search = ''
    :param search: google search string
    :return:
    """
    SITE = "site:"

    if site != '1':

        web = SITE + site + '.com'
        r.queries = web + ' ' + search
    else:
        r.queries = search
    proc = CP()
    proc.crawl(r())
    proc.start()

"""
Usage:
 
>>> pygoog how to remove duplicates in a list -sub duplicate+removal, -site stackoverflow, -mod scrapy -synt lists -lang python

>>> Returns the following google search: site:stackoverflow.com "scrapy" and (list and (duplicate OR **insert 
    synonyms) AND (remov* OR delet* OR **insert synonyms**)
    
>>> Synonyms used to broaden search:

>>> from nltk.corpus import wordnet as wn

>>> d = wn.synsets('release')
>>> for j, k in d:
>>> print(j, k)  
    
"""
"""
class MySpider(scrapy.Spider):
    # Your spider definition

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MySpider)
process.start() # the script will block here until the crawling is finished
"""

if __name__ == '__main__':
    arrange_search_str()