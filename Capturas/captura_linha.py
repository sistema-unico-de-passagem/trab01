#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  captura_linha.py
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

def extrair_pagina():
	url = 'https://sistemas.es.gov.br/webservices/ceturb/onibus/api/ConsultaLinha/'
	arq = open('linhas.txt','wt',encoding = 'utf-8')
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	soup.findAll('Linha')
	texto = str(soup).replace('}','\n')
	arq.write(str(texto))
	arq.close
	return 0
	
def limpaArquivo():
	arq = open('linhas.txt','rt',encoding = 'utf-8')
	arquivo_limpo = open('linhas_limpas.txt','wt',encoding = 'utf-8')
	arquivo_composto = open('linhas_completas.txt','wt',encoding = 'utf-8')
	linha = ((arq.readline())[2:].strip()).replace('"','')
	while linha != '':
		print(((linha.split(',')[0]).replace('Linha:','')).strip())
		arquivo_limpo.write(str(int(((linha.split(',')[0]).replace('Linha:','')).strip())) + '\n')
		arquivo_composto.write(str(int(((linha.split(',')[0]).replace('Linha:','')).strip())) + ',' + str(((linha.split(',')[1]).replace('Descricao:','')).strip()) + '\n')
		linha = ((arq.readline())[2:].strip()).replace('"','')
	return 0


def main():
	extrair_pagina()
	limpaArquivo()
	return 0

main()
