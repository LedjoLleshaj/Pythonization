import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"

    def start_requests(self):  # returns an iterable
        return [
            scrapy.Request(
                url="http://books.toscrape.com",
                callback=self.parse,  # reference to a method
            )
        ]

    def parse(self, response):
        # wb = write binary
        with open("books.html", "wb") as file:
            file.write(response.body)
