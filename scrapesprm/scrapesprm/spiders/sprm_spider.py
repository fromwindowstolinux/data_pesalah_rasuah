import scrapy

class SPRMSpider(scrapy.Spider):
    name = "sprm"

    def start_requests(self):
        for i in range(1, 127):
            url = f"https://www.sprm.gov.my/index.php?r=site%2Findex&id=21&page_id=96&page={i}&per-page=8"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        div_pesalah = response.css('.div-pesalah')
 
        for pesalah in div_pesalah:

            tables = pesalah.css('table')

            # table1 = pesalah.css('table:nth-child(1)')

            info = tables[0]

            tertuduh = info.css('tr:nth-child(1) td:nth-child(2)::text').get()
            npd = info.css('tr:nth-child(2) td:nth-child(2)::text').get()
            jantina = info.css('tr:nth-child(3) td:nth-child(2)::text').get()
            warganegara = info.css('tr:nth-child(4) td:nth-child(2)::text').get()
            negeri = info.css('tr:nth-child(5) td:nth-child(2)::text').get()

            result = {
                'Tertuduh': tertuduh,
                'Nama Pengenalan Diri': npd,
                'Jantina': jantina,
                'Warganegara': warganegara,
                'Negeri': negeri,
                }

            # table2 = pesalah.css('table:nth-child(2)')

            info = tables[1]

            kategori = info.css('tr:nth-child(1) td:nth-child(2)::text').get()
            majikan = info.css('tr:nth-child(2) td:nth-child(2)::text').get()
            jawatan = info.css('tr:nth-child(3) td:nth-child(2)::text').get()
            mahkamah = info.css('tr:nth-child(4) td:nth-child(2)::text').get()
            hakim = info.css('tr:nth-child(5) td:nth-child(2)::text').get()
            tpr_pp = info.css('tr:nth-child(6) td:nth-child(2)::text').getall()
            pb = info.css('tr:nth-child(7) td:nth-child(2)::text').get()
            sl = info.css('tr:nth-child(8) td:nth-child(2)::text').get()
            tjh = info.css('tr:nth-child(9) td:nth-child(2)::text').get()
            rayuan = info.css('tr:nth-child(10) td:nth-child(2)::text').get()
                    
            result.update({
                'Kategori': kategori,
                'Majikan': majikan,
                'Jawatan': jawatan,
                'Mahkamah': mahkamah,
                'Hakim': hakim,
                'Timbalan Pendakwa Raya / Pegawai Pendakwa': tpr_pp,
                'Peguam Bela': pb,
                'Sabitan Lampau': sl,
                'Tarikh Jatuh Hukum': tjh,
                'Rayuan': rayuan,
            })

            # table3 = pesalah.css('table:nth-child(3)')

            info = tables[2]
            cases = []
            for case in info.css('tbody>tr'):
                no = case.css('td:nth-child(1)::text').get()
                no_kes = case.css('td:nth-child(2)::text').get()
                rp = case.css('td:nth-child(3)').get()
                kesalahan = case.css('td:nth-child(4)::text').get()
                hukuman = case.css('td:nth-child(5)::text').get()

                cases.append({
                    '#': no,
                    'No Kes': no_kes,
                    'Ringkasan Pertuduhan': rp,
                    'Kesalahan': kesalahan,
                    'Hukuman': hukuman,
                })

            result.update({
                'cases': cases
            })

            image = pesalah.css('img:nth-child(1)::attr(src)').get()

            result.update({
                'image': 'https://www.sprm.gov.my/'+image
            })

            yield result
