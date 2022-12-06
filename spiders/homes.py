# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..utils import URL, cookie_parser, parse_new_url
from ..items import ZillowItem
import json

class HomesSpider(scrapy.Spider):
    name = 'homes'
    allowed_domains = ['www.zillow.com']
    
    def start_requests(self):
        yield scrapy.Request(
            url= URL,
            callback= self.parse,
            cookies=cookie_parser(),
            meta ={
                'currentPage': 1
            }
        )

    def parse(self, response):
        current_page = response.meta['currentPage']
        json_response= json.loads(response.body)
        homes = json_response.get('cat1').get('searchResults').get('listResults')

        for home in homes:
            loader = ItemLoader(item=ZillowItem())
            loader.add_value('id', home.get('id'))
            loader.add_value('img_urls', home.get('imgSrc'))
            loader.add_value('detail_url', home.get('detailUrl'))
            loader.add_value('status_type', home.get('statusType'))
            loader.add_value('status_text', home.get('statusText'))
            loader.add_value('address_state', home.get('addressState'))
            loader.add_value('country', home.get('hdpData').get('homeInfo').get('country'))
            loader.add_value('featured_listing', home.get('isFeaturedListing'))
            loader.add_value('rent_estimate', home.get('hdpData').get('homeInfo').get('rentZestimate'))
            loader.add_value('address', home.get('address'))
            loader.add_value('beds', home.get('beds'))
            loader.add_value('premier_builder', home.get('hdpData').get('homeInfo').get('isPremierBuilder'))
            loader.add_value('baths', home.get('baths'))
            loader.add_value('home_type', home.get('hdpData').get('homeInfo').get('homeType'))
            loader.add_value('area_in_sq_ft', home.get('hdpData').get('homeInfo').get('livingArea'))
            loader.add_value('estimated_market_value', home.get('zestimate'))
            loader.add_value('price', home.get('price'))
            loader.add_value('broker_name', home.get('brokerName'))
            yield loader.load_item()

        total_page_number = json_response.get('cat1').get('searchList').get('totalPages')

        if current_page <= total_page_number:
            current_page += 1
            yield scrapy.Request(
                url= parse_new_url(URL,next_page_number=current_page),
                callback=self.parse,
                cookies=cookie_parser(),
                meta={
                    'currentPage': current_page
                }
            )
    # def next_processing(self, response):        
    #     json_response = json.loads(response.body)
    #     next_page_url= json_response.get('user').get('searchList').get('pagination').get('nextUrl')

    #     yield scrapy.Request(
    #         next_url= f"https://www.zillow.com{next_page_url}",
    #         callback= self.parse,
    #         cookies= cookie_parser()
    #     )
        
    
