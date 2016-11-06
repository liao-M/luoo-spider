# -*- coding: utf-8 -*-

# Define your item pipelines here
#图片下载部分（自动增量）
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request

class LuooPipeline(ImagesPipeline):
   def get_media_requests(self,item,info):
       for image_url in item['image_urls']:
           yield Request(image_url)
   def item_completed(self,results,item,info):
       image_paths=[x['path'] for ok,x in results if ok]
       if not image_paths:
           raise DropItem('图片未下载好 ')
# class LuooPipeline(object):
#    def process_item(self, item, spider):
#        return item
