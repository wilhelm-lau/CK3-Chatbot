from pathlib import Path

import scrapy


class tenetsSpider(scrapy.Spider):
    name = "tenets"

    async def start(self):
        urls = [
            "https://ck3.paradoxwikis.com/Tenet",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")