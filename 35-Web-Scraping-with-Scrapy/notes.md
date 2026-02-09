# Web Scraping with Scrapy - Study Notes

Scrapy is a powerful Python framework for extracting data from websites.

## Core Concepts
- **Spider**: A class that defines how to follow links and extract data.
- **`start_urls`**: A list of URLs where the crawler begins.
- **`parse(self, response)`**: The default callback method used by Scrapy to handle the response downloaded from each request.

## Extracting Data
Scrapy uses **CSS Selectors** (similar to jQuery) to locate elements.
```python
def parse(self, response):
    for book in response.css("article.product_pod"):
        yield {
            "title": book.css("h3 a::attr(title)").get(),
            "price": book.css("p.price_color::text").get(),
        }
```

## Following Links
To crawl multiple pages, find the link to the next page and yield a new `scrapy.Request`.
```python
next_page = response.css("li.next a::attr(href)").get()
if next_page:
    yield response.follow(next_page, callback=self.parse)
```

## Running the Spider
From the project root:
```bash
# Basic run
scrapy crawl <spider_name>

# Export to JSON
scrapy crawl <spider_name> -o output.json
```

## Scrapy Project Structure
- `scrapy.cfg`: Project configuration file.
- `items.py`: Definition of data structures.
- `middlewares.py`: Hooks into request/response processing.
- `pipelines.py`: Logic for processing/saving items (e.g., to a DB).
- `settings.py`: Project settings (concurrency, delays, etc.).
筋
