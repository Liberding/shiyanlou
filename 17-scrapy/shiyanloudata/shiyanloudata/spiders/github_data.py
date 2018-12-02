# -*- coding: utf-8 -*-
import scrapy
from shiyanloudata.items import ShiyanloudataItem

class GithubDataSpider(scrapy.Spider):
    name = 'github_data'

    @property
    def start_urls(self):
        url_tmpl = [
                'https://github.com/shiyanlou?tab=repositories']
        return url_tmpl

    def parse(self, response):
        for data in response.xpath('//li[contains(@class, "col-12")]'):
            item = ShiyanloudataItem()
            item['name'] = data.xpath('.//a/text()').extract_first().strip(),
            item['update_time'] = data.xpath('.//relative-time/@datetime').extract_first()
            repo_url = response.urljoin(
                    data.xpath('.//a/@href').extract_first())
            request = scrapy.Request(repo_url, callback=self.parse_repo)
            request.meta['item'] = item
            yield request

            #
            for url in response.xpath('//div[@class="pagination"]/a/@href'):
                yield response.follow(url, callback=self.parse)
    """
    def parse_repo(self, response):
        item = response.meta['item']
        for data1 in response.xpath('//ul[@class="numbers-summary"]'):
            s1 = data1.xpath('/li[1]/a/span/text()').re_first(r'\n\s*(.*)\n')
            s2 = data1.xpath('//li[2]/a/span/text()').re_first(r'\n\s*(.*)\n')
            s3 = data1.xpath('//li[3]/a/span/text()').re_first(r'\n\s*(.*)\n')
        
        item['commits'] = int(s1.replace(',', ''))
        item['branches'] = int(s2.replace(',', ''))
        item['releases'] = int(s3.replace(',', ''))
        """
       #     item['commits'] = int(data1.xpath('/li[1]/a/span/text()').re_first(r'\n\s*(.*)\n'))
       #     item['branches'] = int(data1.xpath('//li[2]/a/span/text()').re_first(r'\n\s*(.*)\n'))
       #     item['releases'] = int(data1.xpath('//li[3]/a/span/text()').re_first(r'\n\s*(.*)\n'))
        """
        yield item
    """
    def parse_repo(self, response):
        item = response.meta['item']
        for number in response.css('ul.numbers-summary li'):
            type_text = number.xpath('.//a/text()').re_first(r'\n\s*(.*)\n')
            number_text = number.xpath(
                        './/span[@class="num text-emphasized"]/text()').re_first(r'\n\s*(.*)\n')
            if type_text and number_text:
                number_text = number_text.replace(',', '')
                if type_text in ('commit', 'commits'):
                    item['commits'] = int(number_text)
                elif type_text in ('branch', 'branches'):
                    item['branches'] = int(number_text)
                elif type_text in ('release', 'releases'):
                    item['releases'] = int(number_text)
            yield item
