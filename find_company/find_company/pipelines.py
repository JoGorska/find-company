# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class FindCompanyPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect("companies.db")
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS companies_names_tb""")
        self.curr.execute("""CREATE TABLE companies_names_tb(
            company_name text,
            company_website text,
            company_id text
        )""")


    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO companies_names_tb VALUES (?,?,?)""",(
            item['company_name'],
            item['company_website'],
            item['company_id']
        ))
        self.conn.commit()