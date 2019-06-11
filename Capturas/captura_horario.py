#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  captura_horario.py
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
import requests
import urllib.request
import time 
from bs4 import BeautifulSoup
import os

def extrair_pagina(n_onibus):
	url = 'https://sistemas.es.gov.br/webservices/ceturb/onibus/api/BuscaHorarios/' + n_onibus
	arq = open(str(n_onibus)+'_bruto.txt','wt',encoding = 'utf-8')
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	soup.findAll('Hora_Saida')
	texto = str(soup).replace('}','\n')
	arq.write(str(texto))
	arq.close
	return 0

def pega_linhas():
	linhas = []
	arquivo = open('linhas_limpas.txt','rt',encoding = 'utf-8')
	linha = (arquivo.readline()).strip()
	while linha != '':
		linhas.append(linha)
		linha = (arquivo.readline()).strip()
	return linhas
	
def limpaArquivo(n_onibus):
	arq = open(str(n_onibus)+'_bruto.txt','rt',encoding = 'utf-8')
	arq_terminal_util = open('HORARIOS/'+str(n_onibus)+'_saida_terminal_util.txt','wt',encoding = 'utf-8')
	arq_terminal_sabado = open('HORARIOS/'+str(n_onibus)+'_saida_terminal_sabado.txt','wt',encoding = 'utf-8')
	arq_terminal_domingo = open('HORARIOS/'+str(n_onibus)+'_saida_terminal_domingo.txt','wt',encoding = 'utf-8')
	arq_terminal_atipico = open('HORARIOS/'+str(n_onibus)+'_saida_terminal_atipico.txt','wt',encoding = 'utf-8')
	arq_ptfinal_util = open('HORARIOS/'+str(n_onibus)+'_saida_ptfinal_util.txt','wt',encoding = 'utf-8')
	arq_ptfinal_sabado = open('HORARIOS/'+str(n_onibus)+'_saida_ptfinal_sabado.txt','wt',encoding = 'utf-8')
	arq_ptfinal_domingo = open('HORARIOS/'+str(n_onibus)+'_saida_ptfinal_domingo.txt','wt',encoding = 'utf-8')
	arq_ptfinal_atipico = open('HORARIOS/'+str(n_onibus)+'_saida_ptfinal_atipico.txt','wt',encoding = 'utf-8')
	linha = ((arq.readline())[2:].strip()).replace('"','')
	while linha != '':
		'''
		if (linha.split(',')[1]).strip() == 'Sentido:I' and (linha.split(',')[2]).strip() == 'Sequencia:1':
			print('IDA \n')
		else:
			if (linha.split(',')[1]).strip() == 'Sentido:V' and (linha.split(',')[2]).strip() == 'Sequencia:1':
				print('VOLTA \n')
		'''
		if (linha.split(',')[2]).strip() == 'Terminal_Seq:1':
			if (linha.split(',')[3]).strip() == 'TP_Horario:1':
				arq_terminal_util.write(str(((linha.split(',')[1]).replace('Hora_Saida:','')).strip())+':00\n')
			else:
				if (linha.split(',')[3]).strip() == 'TP_Horario:2':
					arq_terminal_sabado.write(str(((linha.split(',')[1]).replace('Hora_Saida:','')).strip())+':00\n')
				else:
					if (linha.split(',')[3]).strip() == 'TP_Horario:3':
						arq_terminal_domingo.write(str(((linha.split(',')[1]).replace('Hora_Saida:','')).strip())+':00\n')
					else:
						if (linha.split(',')[3]).strip() == 'TP_Horario:4':
							arq_terminal_atipico.write(str(((linha.split(',')[1]).replace('Hora_Saida:','')).strip())+':00\n')
		else:
			if (linha.split(',')[3]).strip() == 'TP_Horario:1':
				arq_ptfinal_util.write(str(((linha.split(',')[1]).replace('Hora_Saida:','')).strip())+':00\n')
			else:
				if (linha.split(',')[3]).strip() == 'TP_Horario:2':
					arq_ptfinal_sabado.write(str(((linha.split(',')[1]).replace('Hora_Saida:','')).strip())+':00\n')
				else:
					if (linha.split(',')[3]).strip() == 'TP_Horario:3':
						arq_ptfinal_domingo.write(str(((linha.split(',')[1]).replace('Hora_Saida:','')).strip())+':00\n')
					else:
						if (linha.split(',')[3]).strip() == 'TP_Horario:4':
							arq_ptfinal_atipico.write(str(((linha.split(',')[1]).replace('Hora_Saida:','')).strip())+':00\n')
		print(((linha.split(',')[1]).replace('Hora_Saida:','')).strip())
		linha = ((arq.readline())[2:].strip()).replace('"','')
	arq.close()
	arq_terminal_util.close()
	arq_terminal_sabado.close()
	arq_terminal_domingo.close()
	arq_terminal_atipico.close()
	arq_ptfinal_util.close()
	arq_ptfinal_sabado.close()
	arq_ptfinal_domingo.close()
	arq_ptfinal_atipico.close()
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
	
def main(args):
	linhas = pega_linhas()
	print(linhas)
	if not os.path.exists('HORARIOS'):
		os.mkdir('HORARIOS')
	for i in linhas:
		extrair_pagina(i)
		limpaArquivo(i)
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
