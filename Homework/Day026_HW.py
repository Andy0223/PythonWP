import scrapy


class EttodaySpider(scrapy.Spider):
    name = 'ettoday'
    allowed_domains = ['www.ettoday.net'] #為一個list，當需要請求的domain不只一個時，可以將該domain加入allowed_domains裡
    start_urls = ['https://www.ettoday.net/news/20201004/1824032.htm',
                  'https://www.ettoday.net/news/20201009/1826868.htm']#爬蟲起始網站，是一個list，爬蟲的第一步會先對這個list內的全部網址依序進行請求，可以依照需求添加url

    def parse(self, response):
        title= response.xpath('//title/text()').get()
        content = response.xpath('//div[@itemprop="articleBody"]//p/text()').getall()
        print(title)
        print(content)
