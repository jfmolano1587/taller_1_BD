# encoding=utf-8
import scrapy
from unidecode import unidecode

from tutorial.items import DmozItem
from tutorial.items import DependenciaItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["uniandes.edu.co"]
    start_urls = [
        "http://www.uniandes.edu.co/"
    ]

    def parse(self, response):
	#Submenus
	submenus = response.xpath('//ul[@class="dj-submenu2"]')
	submenu_facultades = submenus[4].xpath('li')
	submenu_deptos = submenus[5].xpath('li')
	lista_dependencias = submenu_facultades + submenu_deptos
        for dependencia in lista_dependencias:
		item = DependenciaItem()
		#nombre = unidecode(dependencia.xpath('a/text()').extract()[0])
		nombre = dependencia.xpath('a/text()').extract()[0].encode('utf8')
		print "nombre "+ nombre
		item['nombre'] = nombre
		link = dependencia.xpath('a/@href').extract()[0]
		print "link "+ link
		item['link'] = link
		yield item
