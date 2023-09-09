import scrapy
from urllib.parse import urlencode
from bookscraper.items import BookItem

# Sử dụng Scraping Endpoint Service của ScrapeOps
SCRAPE_OPS_API_KEY = "c6b71a8e-e1a2-440e-b93b-ffa828052fd9"


def get_proxy_url(scraping_target_url: str):
    query_params = {
        "api_key": SCRAPE_OPS_API_KEY,
        "url": scraping_target_url,
    }
    proxy_url = f"https://proxy.scrapeops.io/v1?{urlencode(query_params)}"
    return proxy_url


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com", "proxy.scrapeops.io"]
    start_urls = ["https://books.toscrape.com/"]

    custom_settings = {
        "FEEDS": {
            "bookdata.json": {
                "format": "json",
                "overwrite": True,
            }
        }
    }

    def start_requests(self):
        yield scrapy.Request(url=get_proxy_url(self.start_urls[0]), callback=self.parse)

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            book_rel_url = book.css("h3 a").attrib["href"]
            prefix = "https://books.toscrape.com/"
            if not book_rel_url.startswith("catalogue/"):
                prefix = "https://books.toscrape.com/catalogue/"
            book_abs_url = f"{prefix}{book_rel_url}"

            yield scrapy.Request(
                get_proxy_url(book_abs_url), callback=self.parse_book_page
            )

        next_page = response.css("ul.pager li.next a ::attr(href)").get()

        if next_page is not None:
            prefix = "https://books.toscrape.com/"
            if not next_page.startswith("catalogue/"):
                prefix = "https://books.toscrape.com/catalogue/"
            next_page_url = f"{prefix}{next_page}"
            yield scrapy.Request(get_proxy_url(next_page_url), callback=self.parse)

    def parse_book_page(self, response):
        table_rows = response.css(".table.table-striped tr")
        category = response.xpath(
            "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()"
        ).get()
        category_rel_link: str = response.xpath(
            "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a"
        ).attrib["href"]
        category_abs_link = f'https://books.toscrape.com/catalogue/{category_rel_link.replace("../", "")}'
        img_rel_link: str = response.css(".item.active img").attrib["src"]
        img_abs_link = f'https://books.toscrape.com/{img_rel_link.replace("../", "")}'

        book_item = BookItem()

        book_item["url"] = response.url
        book_item["category"] = category
        book_item["category_link"] = category_abs_link
        book_item["title"] = response.css(".col-sm-6.product_main h1::text").get()
        book_item["price"] = response.css(".price_color::text").get()
        book_item["stars"] = response.css(".star-rating").attrib["class"]
        book_item["img"] = img_abs_link
        book_item["description"] = response.xpath(
            "//div[@id='product_description']/following-sibling::p/text()"
        ).get()
        book_item["upc"] = table_rows[0].css("td::text").get()
        book_item["product_type"] = table_rows[1].css("td::text").get()
        book_item["excl_tax"] = table_rows[2].css("td::text").get()
        book_item["incl_tax"] = table_rows[3].css("td::text").get()
        book_item["tax"] = table_rows[4].css("td::text").get()
        book_item["availability"] = table_rows[5].css("td::text").get()
        book_item["reviews"] = table_rows[6].css("td::text").get()

        yield book_item
