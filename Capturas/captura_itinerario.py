#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  teste.py
#  
#  Copyright 2019 Jack <Jack@DESKTOP-N9D1A4F>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#

# Import libraries
import requests
import urllib.request
import time 
from bs4 import BeautifulSoup
import os

def extrair_pagina(n_onibus):
	url = 'https://sistemas.es.gov.br/webservices/ceturb/onibus/api/BuscaItinerarios/' + n_onibus
	arq = open(str(n_onibus)+'_bruto.txt','wt',encoding = 'utf-8')
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	soup.findAll('Descricao_Linha')
	texto = str(soup).replace('}','\n')
	arq.write(str(texto))
	arq.close
	return 0

def limpaArquivo(n_onibus):
	arq = open(str(n_onibus)+'_bruto.txt','rt',encoding = 'utf-8')
	arq_limpo_ida = open('ITINERARIOS/'+str(n_onibus)+'_IDA.txt','wt',encoding = 'utf-8')
	arq_limpo_volta = open('ITINERARIOS/'+str(n_onibus)+'_VOLTA.txt','wt',encoding = 'utf-8')
	linha = ((arq.readline())[2:].strip()).replace('"','')
	while linha != '':
		if (linha.split(',')[1]).strip() == 'Sentido:I':
			arq_limpo_ida.write(str(((linha.split(',')[4]).replace('Desc_Via:','')).strip())+'\n')
		else:
			if (linha.split(',')[1]).strip() == 'Sentido:V':
				arq_limpo_volta.write(str(((linha.split(',')[4]).replace('Desc_Via:','')).strip())+'\n')
		linha = ((arq.readline())[2:].strip()).replace('"','')
	arq.close()
	arq_limpo_ida.close()
	arq_limpo_volta.close()
	os.remove(str(n_onibus)+'_bruto.txt')
	return 0

def pega_linhas():
	linhas = []
	arquivo = open('linhas_limpas.txt','rt',encoding = 'utf-8')
	linha = (arquivo.readline()).strip()
	while linha != '':
		linhas.append(linha)
		linha = (arquivo.readline()).strip()
	return linhas
	
	

def main():
	linhas = pega_linhas()
	if not os.path.exists('ITINERARIOS'):
		os.mkdir('ITINERARIOS')
	for i in linhas:
		extrair_pagina(i)
		limpaArquivo(i)
	return 0
main()

