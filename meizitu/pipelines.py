'''
@File    :   pipelines.py
@Time    :   2020/06/28 20:22:40
@Author  :   Han YiKai 
@Version :   1.0
@Contact :   lucas.yikai.han@gmail.com
@Desc    :   None
'''

import os
import stat
import urllib.request
from abc import ABCMeta, abstractmethod

import pymongo
from itemadapter import ItemAdapter


class IPipeline(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def process_item(self, item, spider):
        pass


class LocalPipeline(IPipeline):
    base_save_dir = os.environ['HOME'] + "/meizi"

    def __init__(self):
        if not os.path.exists(self.base_save_dir):
            os.mkdir(self.base_save_dir)

    def process_item(self, item, spider):
        img_url = item['origin_url']
        file_suffix = os.path.splitext(img_url)[1]

        albumn_dir_path = self.base_save_dir + "/" + \
            item['sort_1'] + "/" + item['sort_2'] + '/' + item['name']
        if not os.path.exists(albumn_dir_path):
            os.makedirs(albumn_dir_path)

        img_save_path = albumn_dir_path + '/' + \
            str(item['order']) + file_suffix
        if not os.path.exists(img_save_path):
            if item['origin_url'].startswith('http'):
                urllib.request.urlretrieve(
                    item['origin_url'], filename=img_save_path)
            else:
                urllib.request.urlretrieve(
                    "http:" + item['origin_url'], filename=img_save_path)

        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass


class MongoPipeLine(IPipeline):
    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    def process_item(self, item, spider):
        print(self.db[self.collection_name].insert_one(
            ItemAdapter(item).asdict()))
        return item

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def close_spider(self, spider):
        self.client.close()


class Dumplicate(IPipeline):
    def __init__(self, mongo_uri, mongo_db):
        pass

    def process_item(self, item, spider):
        pass
