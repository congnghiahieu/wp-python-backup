# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from typing import List
import mysql.connector


class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        for field_name in adapter.field_names():
            if field_name != "description":
                value: str = adapter.get(field_name)
                adapter[field_name] = value.strip()

        lowercase_value_field_names = ["category", "product_type"]
        for field_name in lowercase_value_field_names:
            value: str = adapter.get(field_name)
            adapter[field_name] = value.lower()

        price_keys = ["price", "excl_tax", "incl_tax", "tax"]
        for price_key in price_keys:
            value: str = adapter.get(price_key)
            adapter[price_key] = float(value.replace("£", ""))

        adapter["reviews"] = int(adapter["reviews"])

        # "stars": "star-rating Five",
        star_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        star_str: str = adapter["stars"]
        adapter["stars"] = star_map[star_str.split(" ")[1].lower()]

        # "availability": "In stock (19 available)",
        avail_stock_splits: List[str] = adapter["availability"].split("(")
        if len(avail_stock_splits) < 2:
            adapter["availability"] = 0
        else:
            adapter["availability"] = int(avail_stock_splits[1].split(" ")[0])

        return item


class SaveToMySQLPineline:
    def __init__(self) -> None:
        # Remember to turn DB MySQL on

        db_conn_config = {
            "host": "localhost",
            "user": "root",
            "password": "hieu1234",
            "database": "books",
        }
        self.conn = mysql.connector.connect(**db_conn_config)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS books(
            id int NOT NULL auto_increment, 
            url VARCHAR(1000),
            category VARCHAR(255),
            category_link VARCHAR(1000),
            title text,
            price DECIMAL,
            stars INTEGER,
            img VARCHAR(1000),
            description text,
            upc VARCHAR(255),
            product_type VARCHAR(255),
            excl_tax DECIMAL,
            incl_tax DECIMAL,
            tax DECIMAL,
            availability INTEGER,
            reviews INTEGER,
            PRIMARY KEY (id)
        )
        """
        )

    def process_item(self, item, spider):
        # Define insert statement
        self.cur.execute(
            """INSERT INTO books (
            url,
            category,
            category_link,
            title,
            price,
            stars,
            img,
            description,
            upc,
            product_type,
            excl_tax,
            incl_tax,
            tax,
            availability,
            reviews
            ) values (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
                )""",
            (
                item["url"],
                item["category"],
                item["category_link"],
                item["title"],
                item["price"],
                item["stars"],
                item["img"],
                item["description"],
                item["upc"],
                item["product_type"],
                item["excl_tax"],
                item["incl_tax"],
                item["tax"],
                item["availability"],
                item["reviews"],
            ),
        )

        # Execute insert of data into database
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # Close cursor & connection to database
        self.cur.close()
        self.conn.close()
