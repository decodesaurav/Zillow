# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class ZillowItem(scrapy.Item):
    id = scrapy.Field(
        output_processor=TakeFirst()
    )
    img_urls = scrapy.Field(
        output_processor = TakeFirst()
    )
    # images = scrapy.Field()     
    
    detail_url = scrapy.Field(
        output_processor=TakeFirst()
    )
    status_type = scrapy.Field(
        output_processor=TakeFirst()
    )
    status_text = scrapy.Field(
        output_processor=TakeFirst()
    )
    address_state = scrapy.Field(
        output_processor=TakeFirst()
    )
    country = scrapy.Field(
        output_processor=TakeFirst()
    )
    featured_listing = scrapy.Field(
        output_processor=TakeFirst()
    )
    rent_estimate = scrapy.Field(
        output_processor=TakeFirst()
    )
    address = scrapy.Field(
        output_processor=TakeFirst()
    )
    beds = scrapy.Field(
        output_processor=TakeFirst()
    )
    premier_builder = scrapy.Field(
        output_processor=TakeFirst()
    )
    baths = scrapy.Field(
        output_processor=TakeFirst()
    )
    home_type = scrapy.Field(
        output_processor=TakeFirst()
    )
    area_in_sq_ft = scrapy.Field(
        output_processor=TakeFirst()
    )
    estimated_market_value = scrapy.Field(
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        output_processor=TakeFirst()
    )
    broker_name = scrapy.Field(
        output_processor=TakeFirst()
    )
