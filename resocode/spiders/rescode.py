
import time
from urllib.parse import urljoin, urlparse, parse_qsl

import requests
from bs4 import BeautifulSoup as bb
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.utils.misc import arg_to_iter
from scrapy.utils.response import get_base_url

COUNTRIES = {'ie': 'countryIE',
             'nl': 'countryNL'}

title_body_dict={}

class RescodeSpider(Spider):
    name, region = 'resocode', 'ie'
    download_html, limit_country = False, False
    queries = None
    # custom_settings = {
        # 'LOG_ENABLED': False,
    # }

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
    search_urls = requests.get(links).text # source of link from overridden 'parse" method
    html_link_parent = bb(search_urls).findAll('h3')

    for link_title in html_link_parent:
        link_title = link_title.find_next()
        url_strip = link_title.get('href')
        if '/url?q=' in url_strip and 'stackoverflow.com/questions/tagged' in url_strip: # checks to see if the url points to the specific page. If not, pass
            pass
        elif '/url?q=' in url_strip and 'stackoverflow.com/questions/' in url_strip:
            url_strip = url_strip[7:]

            if 'webcache' not in url_strip: # filters that are not desired.  Legit links  have the same url namespacing
                req = requests.get(url_strip).text

                soup = bb(req).find('div', {'class':'container'}) # Section containging question text for a
                for link_title in soup:
                    title = soup.find('a', {'class': 'question-hyperlink'}).text
                    title_body_dict = soup.find('div', {'class': 'post-text'}).text
                    time.sleep(3)  # wait before requests extractions the next site.

                    return dict.update(title, title_body_dict)

                    # TODO: make function to extract body text.


def get_body_request(link):
    pass

