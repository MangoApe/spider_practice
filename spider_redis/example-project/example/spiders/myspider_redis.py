from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):#继承scrapy_redis.spiders.RedisSpider类
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    redis_key = 'myspider:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name':  response.css('title::text').extract_first(),
            'url': response.url,
        }
