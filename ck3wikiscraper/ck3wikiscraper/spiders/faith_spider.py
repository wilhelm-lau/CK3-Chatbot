from pathlib import Path
import scrapy


class TenetsSpider(scrapy.Spider):
    name = "tenets"
    start_urls = [
        "https://ck3.paradoxwikis.com/Tenet",
    ]

    def parse(self, response):
        for tenet in response.css('tr[id]'):
            # Name and alternative names (all text after <br> in first <td>)
            name_td = tenet.css('td:nth-child(1)')
            name_parts = name_td.xpath('.//br/following-sibling::text()').getall()
            name = ' '.join([part.strip() for part in name_parts if part.strip()])

            # Effects (list items in 2nd <td>)
            effects = []
            for li in tenet.css('td:nth-child(2) li'):
                value = li.css('b::text').get()
                # Remove the value from the description if present
                desc_parts = li.xpath('.//text()').getall()
                desc = ' '.join([part.strip() for part in desc_parts if part.strip() and part.strip() != value])
                effects.append({
                    'value': value,
                    'description': desc
                })

            # Requirements (list items in 5th <td>)
            requirements = tenet.css('td:nth-child(5) li::text').getall()
            requirements = [r.strip() for r in requirements if r.strip()]

            yield {
                'name': name,
                'effects': effects,
                'requirements': requirements,
            }