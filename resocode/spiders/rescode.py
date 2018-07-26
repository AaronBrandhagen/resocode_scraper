
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.linkextractors import LinkExtractor as LI
from scrapy.utils.misc import arg_to_iter
from scrapy.http import Request
from urllib.parse import urljoin, urlparse, parse_qsl
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url


import requests

from bs4 import BeautifulSoup as bb

COUNTRIES = {'ie': 'countryIE',
             'nl': 'countryNL'}

class RescodeSpider(Spider):
    name, region = 'resocode', 'ie'
    download_html, limit_country = False, False
    queries = None
    download_delay = 5
    base_url_fmt = "http://www.google.{region}/search?hl=en&as_q=&as_epq={query}&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr={country}&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&tbs=&as_filetype=&as_rights="

    def start_requests(self):
        for query in arg_to_iter(self.queries):
            url = self.make_google_search_request(COUNTRIES[self.region], query)
            parse_requests(url)
            yield Request(url=url, meta={'query': query})

    def make_google_search_request(self, country, query):
        if not self.limit_country:
            country = ''
        return self.base_url_fmt.format(country=country, region=self.region, query='+'.join(query.split()).strip('+'))

    def parse(self, response):
        hxs = Selector(response)
        next_page = hxs.xpath('//table[@id="nav"]//td[contains(@class, "b") and position() = last()]/a')

        if next_page:
            url = self._build_absolute_url(response, next_page.xpath('.//@href').extract()[0])
            parse_requests(url)
            yield Request(url=url, callback=self.parse, meta={'query': response.meta['query']})

    def _build_absolute_url(self, response, url):
        # pass
         return urljoin(get_base_url(response), url)


def _parse_url(href):
    queries = dict(parse_qsl(urlparse(href).query))
    return queries.get('q', '')

def _get_region(url):
    netloc = urlparse(url)[1]
    return netloc.rpartition('.')[-1]

def parse_requests(links):
    r = requests.get(links).text
    # b = bb(r).findAll('a')
    b = bb(r).findAll('h3')
    for x in b:
        x = x.find_next()
        h = x.get('href')
        if '/url?q=' in h and 'stackoverflow.com/questions/tagged' in h:
            pass
        elif '/url?q=' in h and 'stackoverflow.com/questions/' in h:
            partial_title = x.getText()
            h = h[7:]

            if 'webcache' not in h:
                soup_func(h)

def soup_func(soup):
    page = requests.get(soup).text
    bs= bb(page)
    print(bs)
    for x in bs :
        print(x.find_all('p'))


