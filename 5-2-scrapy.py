import scrapy


class Spider(scrapy.Spider):
    name = 'zy'
    start_urls = ['https://mofanpy.com/']

    def parse(self, response):
        yield {
            # extract_first返回匹配的第一个，是一个字符串
            # extract返回匹配的所有，是一个列表
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace('"', ''),
            'url': response.url
        }

        urls = response.css('a::attr(href)').re(r'^/.+?/$')
        for url in urls:
            yield response.follow(url, callback=self.parse)# 构建获取下一个链接


# lastly, run this in terminal
# scrapy runspider 5-2-scrapy.py -o res.json