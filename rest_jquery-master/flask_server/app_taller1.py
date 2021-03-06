# encoding=utf-8
import requests
from flask import Flask, jsonify, abort, make_response
import csv
import json
import io
import re
import codecs

app = Flask(__name__)

marcas = [
    {
        'Id': u'1',
        'Dato': u'A'
    },
    {
        'Id': u'2',
        'Dato': u'B'
    }
]

@app.route('/api/marcas2', methods=['GET'])
def get_marcas2():
	return jsonify(marcas), 201

@app.route('/api/marcas', methods=['GET'])
def get_marcas():
	#json_data=open("../../scrapy/items.json", encoding='utf-8').read()
	with io.open("../../scrapy/items.json",'r',encoding='utf-8') as f:
    		json_data = f.read()
	print json_data
	json_data = unicode(json_data)
	#json_data = json_data.replace(r"""\u00f1""","ñ")
	#data = json.loads(json_data)
	return jsonify(json.loads(json_data)), 201

@app.route('/api/eventos', methods=['GET'])
def get_eventos():
	#json_data=open("../../scrapy/items.json", encoding='utf-8').read()
	with io.open("eventos.json",'r',encoding='utf-8') as f:
    		json_data = f.read()
	print json_data
	json_data = unicode(json_data)
	#json_data = json_data.replace(r"""\u00f1""","ñ")
	#data = json.loads(json_data)
	return jsonify(json.loads(json_data)), 201

@app.route('/api/rss/<A>', methods=['GET'])
def get_rss(A):
	busqueda = str(A)
	urlopinion= 'http://www.wsj.com/xml/rss/3_7041.xml'
	urlworldnews='http://www.wsj.com/xml/rss/3_7085.xml'
	urlusbusiness='http://www.wsj.com/xml/rss/3_7014.xml'
	urlopinionhuff= 'http://www.huffingtonpost.com/feeds/verticals/politics/index.xml'
	urlusbusinesshuff= 'http://www.huffingtonpost.com/feeds/verticals/politics/index.xml'
	urlworldnewshuff= 'http://www.huffingtonpost.com/feeds/verticals/world/index.xml'
	values={'s':'basics','submit':'search'}
	reqOpinion=requests.get(urlopinion)
	reqWorldNews=requests.get(urlworldnews)
	reqUsBusiness=requests.get(urlusbusiness)
	reqOpinionHuff=requests.get(urlopinionhuff)
	reqWorldNewsHuff=requests.get(urlworldnewshuff)
	reqUsBusinessHuff=requests.get(urlusbusinesshuff)
	respDataOpinion = reqOpinion.text.encode('ascii', 'ignore')
	respDataWorldNews = reqWorldNews.text.encode('ascii', 'ignore')
	respDataUsBusiness = reqUsBusiness.text.encode('ascii', 'ignore')
	respDataOpinionHuff = reqOpinionHuff.text.encode('ascii', 'ignore')
	respDataWorldNewsHuff = reqWorldNewsHuff.text.encode('ascii', 'ignore')
	respDataUsBusinessHuff = reqUsBusinessHuff.text.encode('ascii', 'ignore')
	items_opinion = re.findall(r'<item>[\s\S]*?<\/item>',str(respDataOpinion))
	items_world_news = re.findall(r'<item>[\s\S]*?<\/item>',str(respDataWorldNews))
	items_usbusiness = re.findall(r'<item>[\s\S]*?<\/item>',str(respDataUsBusiness))
	items_opinionHuff = re.findall(r'<item>[\s\S]*?<\/item>',str(respDataOpinionHuff))
	items_world_newsHuff = re.findall(r'<item>[\s\S]*?<\/item>',str(respDataWorldNewsHuff))
	items_usbusinessHuff = re.findall(r'<item>[\s\S]*?<\/item>',str(respDataUsBusinessHuff))
	items = []
	items2 = []
	items3 = []
	itemsH = []
	items2H = []
	items3H = []
	for eachP in items_opinion:
		resp = {}
		esta_en_titulo = re.findall(r'<title>(.*('+busqueda+').*)<\/title>',str(eachP))
		esta_en_descripcion = re.findall(r'<description>(.*('+busqueda+').*)<\/description>',str(eachP))
		if len(esta_en_titulo) > 0 or len(esta_en_descripcion) > 0:
			titulo = re.findall(r'<title>(.*?)<\/title>',str(eachP))
			resp['titulo'] = titulo[0].replace("<!","")
			items.append(resp)
	#print items
	for eachP in items_world_news:
		resp = {}
		esta_en_titulo2 = re.findall(r'<title>(.*('+busqueda+').*)<\/title>',str(eachP))
		esta_en_descripcion2 = re.findall(r'<description>(.*('+busqueda+').*)<\/description>',str(eachP))
		if len(esta_en_titulo2) > 0 or len(esta_en_descripcion2) > 0:
			titulo2 = re.findall(r'<title>(.*?)<\/title>',str(eachP))
			resp['titulo'] = titulo2[0].replace("<!","")
			items2.append(resp)
	#print items2
	for eachP in items_usbusiness:
		resp = {}
		esta_en_titulo3 = re.findall(r'<title>(.*('+busqueda+').*)<\/title>',str(eachP))
		esta_en_descripcion3 = re.findall(r'<description>(.*('+busqueda+').*)<\/description>',str(eachP))
		if len(esta_en_titulo3) > 0 or len(esta_en_descripcion3) > 0:
			titulo3 = re.findall(r'<title>(.*?)<\/title>',str(eachP))
			resp['titulo'] = titulo3[0].replace("<!","")
			items3.append(resp)
	#print items3
	for eachP in items_opinionHuff:
		resp = {}
		esta_en_tituloH = re.findall(r'<title>\s?[\s\S]?!\[CDATA\[\s?(.*('+busqueda+').*)\s?\]\]>\s?<\/title>',str(eachP))
		print "len(esta_en_tituloH) " + str(len(esta_en_tituloH))
		#esta_en_descripcion = re.findall(r'<description>(.*('+busqueda+').*)<\/description>',str(eachP))
		if len(esta_en_tituloH) > 0:
			tituloH = re.findall(r'<title>(.*?)<\/title>',str(eachP))
			print "tituloH[0]: " + tituloH[0]
			resp['titulo'] = tituloH[0].replace("<![CDATA","")
			print resp
			itemsH.append(resp)
		print itemsH
	#print itemsH
	for eachP in items_world_newsHuff:
		resp = {}
		esta_en_titulo2H = re.findall(r'<title>\s[\s\S]!\[CDATA\[\s(.*('+busqueda+').*)\s\]\]>\s<\/title>',str(eachP))
		#esta_en_descripcion = re.findall(r'<description>(.*('+busqueda+').*)<\/description>',str(eachP))
		if len(esta_en_titulo2H) > 0:
			titulo2H = re.findall(r'<title>(.*?)<\/title>',str(eachP))
			resp['titulo'] = titulo2H[0].replace("<![CDATA","")
			items2H.append(resp)
	#print items
	for eachP in items_usbusinessHuff:
		resp = {}
		esta_en_titulo3H = re.findall(r'<title>\s[\s\S]!\[CDATA\[\s(.*('+busqueda+').*)\s\]\]>\s<\/title>',str(eachP))
		#esta_en_descripcion = re.findall(r'<description>(.*('+busqueda+').*)<\/description>',str(eachP))
		if len(esta_en_titulo3H) > 0:
			titulo3H = re.findall(r'<title>(.*?)<\/title>',str(eachP))
			resp['titulo'] = titulo3H[0].replace("<![CDATA","")
			items3H.append(resp)
	lista_def = items+itemsH+items2+items2H+items3+items3H
#print items3H
	return jsonify(lista_def), 201

@app.route('/api/suma', methods=['POST'])
def dar_suma_post():
	if not request.json or not 'A' in request.json:
		abort(400)
	A = int(request.json['A'])
	B = int(request.json.get('B', ""))
	marca = {
	'Resultado': (A+B)
	}
	return jsonify({'marca': marca}), 201

@app.route('/api/resta/<A>/<B>', methods=['GET'])
def dar_marca_get(A,B):
	marca = {
	'Resultado': (int(A)-int(B))
	}
	return jsonify({'marca': marca}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(host= '127.0.0.1')
