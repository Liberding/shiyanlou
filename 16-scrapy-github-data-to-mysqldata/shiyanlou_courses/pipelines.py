# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from shiyanlou_courses.models import Course, engine
from datetime import datetime
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ShiyanlouCoursesPipeline(object):
    def process_item(self, item, spider):
        item['update_time'] = datetime.strptime(item['update_time'], '%Y-%m-%dT%H:%M:%SZ')
        self.session.add(Course(**item))
        return item

    def open_spider(self, spider):

        Session = sessionmaker(bind=engine)
        self.session = Session()


    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
