import scrapy


class BagsSpider(scrapy.Spider):
    name = "rakuten_jp_bags"

    def start_requests(self):
        self.nb_page = getattr(self, 'nb_page', None)
        self.nb_page = int(self.nb_page) if self.nb_page is not None else -1
        urls = [
            'http://search.rakuten.co.jp/search/mall/luxury+bag/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for bags_info in response.css('div.rsrSResultSect'):
            yield {
                'url':
                    bags_info.css('div.rsrSResultItemTxt a::attr(href)').extract_first(),
                'description':
                    bags_info.css('div.rsrSResultItemTxt a::text').extract_first(),
                'price':
                    bags_info.css('p.price a::text').extract_first(),
                'picture_url':
                    bags_info.css('div.rsrSResultPhoto img::attr(src)').extract_first(),
                'seller_name':
                    bags_info.css('span.txtIconShopName a::text').extract_first(),
                'seller_url':
                    bags_info.css('span.txtIconShopName a::attr(href)').extract_first(),
            }
        next_page = response.css('div.nextPage a::attr(href)').extract_first()
        self.nb_page -= 1 if self.nb_page > 0 else 0
        if ((next_page is not None) and (self.nb_page != 0)):
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
