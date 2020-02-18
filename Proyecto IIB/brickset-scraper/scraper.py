import scrapy

class BrickSetSpider(scrapy.Spider):
    name = 'brick_spider'
    start_urls = ['http://brickset.com/sets/year-2019']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 ::text'
            RATING_SELECTOR = '.rating ::attr(title)'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            OWN_SELECTOR = './/dl[dt/text() = "Our community"]/dd/a/text()'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'rating': brickset.css(RATING_SELECTOR).extract_first(),
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'ownthisset': brickset.xpath(OWN_SELECTOR).extract_first(),
            }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )