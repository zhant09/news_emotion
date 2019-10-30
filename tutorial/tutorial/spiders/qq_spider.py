""" 
Created by
@author: tao.zhan
@time: 2019/10/30 2:57 PM
"""

import codecs
import datetime
import scrapy


class QqSpider(scrapy.Spider):
    name = "qq"

    def start_requests(self):
        urls = [
            'http://www.qq.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        todo: 需要增加过滤条件
        :param response:
        :return:
        """
        link_result = response.css('a::text').getall()
        link_result = [res.strip() for res in link_result]

        date_str = datetime.datetime.now().strftime("%Y-%m-%d")

        filename = "qq-title." + date_str
        with codecs.open(filename, "w", encoding="utf8") as wf:
            for result in link_result:
                if len(result) > 5:
                    print(result)
                    wf.write(result + "\n")
