import scrapy

class IMGSPRMSpider(scrapy.Spider):
    name = "imgsprm"

    def start_requests(self):
        for i in range(1, 127):
            url = f"https://www.sprm.gov.my/index.php?r=site%2Findex&id=21&page_id=96&page={i}&per-page=8"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        div_pesalah = response.css('.div-pesalah')
 
        for pesalah in div_pesalah:

            image = pesalah.css('img:nth-child(1)::attr(src)').get()

            result = {
                'img': 'https://www.sprm.gov.my/'+image
            }

            yield result
