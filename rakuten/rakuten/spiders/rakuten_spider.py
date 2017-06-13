import scrapy


class QuotesSpider(scrapy.Spider):
    name = "rakuten_jp_bags"

    def start_requests(self):
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
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
