# # -*- coding: utf-8 -*-
# from urllib.parse import urljoin, urlparse, parse_qsl
# import datetime
# import scrapy
# from scrapy.http import Request
# from scrapy.selector import Selector
# from scrapy.utils.response import get_base_url
# from scrapy.utils.misc import arg_to_iter
# from scrapy.spiders import Spider, Rule, CrawlSpider
# # from scrapy.spiders import Spider
# from resocode.items import ResocodeItem
# from scrapy.linkextractors import LinkExtractor as LI
#
#
# COUNTRIES = {
#     'ie': 'countryIE',
#     'nl': 'countryNL'
# }
#
#
# class GoogleSpider(Spider ):
#     name = 'recode'
#     queries = ("python")
#     region = 'ie'
#     allowed_domains = ['google.com', 'stackoverflow.com']
#     start_urls = ['http://google.com']
#     download_delay = 5
#     base_url_fmt = 'http://www.google.{region}/search?hl=en&as_q=&as_epq={' \
#                     'query}&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr={' \
#                    'country}&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&tbs=&as_filetype=&as_rights='
#     download_html = True
#     limit_country = False
#     # rules = Rule(LI(allowe='')) # TODO: defines rules
#
#     # def from_crawler(cls, crawler, *args, **kwargs):
#
#
#     def start_requests(self):
#         for query in arg_to_iter(self.queries):
#             url = self.make_google_search_request(COUNTRIES[self.region], query)
#             yield Request(url=url, meta={'query': query})
#
#     def make_google_search_request(self, country, query):
#         if not self.limit_country:
#             country = ''
#             return self.base_url_fmt.format(country=country, region=self.region, query='+'.join(query.split()).strip(
#                 '+'))
#
#
#     def parse(self, response):
#         hxs = Selector(response)
#         next_page = hxs.xpath('//table[@id="nav"]//td[contains(@class, "b") and position() = last()]/a'
#                               )
#         if next_page:
#             url = self._build_absolute_url(response, next_page.xpath('.//@href').extract()[0])
#             print(url)
#             yield Request(url=url, callback=self.parse, meta={'query': response.meta['query']})
#
#
#     # def parse_item(self, response):
#     #     name = response.meta['name']
#     #     query = response.meta['query']
#     #     url = response.url
#         # if self.parse(url):
#         #     se = Selector(response)
#         #     for x in url:
#         #         link = x.select("//*[@id=\"rso\"]/div[1]/div/div[1]/div/div/h3/a").extract()
#         #         print(link)
#         #
#         #
#         # html = response.body[:1024 * 256]
#         # timestamp = datetime.datetime.utcnow().isoformat()
#
#         #
#         # yield ResocodeItem({'name': name,
#         #                     'url': url,
#         #                     'html': html,
#         #                     'region': self.region,
#         #                     'query': query,
#         #                     'crawled': timestamp})
#         #
#         #
#
#
#     def _build_absolute_url(self, response, url):
#         # pass
#         return urljoin(get_base_url(response), url)
#
#
#
# netlock=''
#
# def _get_region(url):
#     """
#     get country code from the url.
#     >>> _get_region('http://scrapinghub.ie')
#     'ie'
#     >>> _get_region('http://www.astoncarpets.ie/contact.htm')
#     'ie'
#     """
#     netloc = urlparse(url)[1]
#     return netloc.rpartition('.')[-1]
#
#
# def main():
#     import os
#
#     print(GoogleSpider.)
#     while True:
#        os.system('scrapy crawl resocode -a queries="python site:stackoverflow.com"')
#
#
#
#
# if __name__ == '__main__':
#     main()
#
#
#
#
#
#
