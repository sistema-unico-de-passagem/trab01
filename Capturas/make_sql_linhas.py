#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  make_sql_linhas.py
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
def pega_linhas():
	linhas = []
	arquivo = open('linhas_limpas.txt','rt',encoding = 'utf-8')
	linha = (arquivo.readline()).strip()
	while linha != '':
		linhas.append(linha)
		linha = (arquivo.readline()).strip()
	return linhas

def pega_nome_linhas():
	linhas = []
	arquivo = open('linhas_completas.txt','rt',encoding = 'utf-8')
	linha = (arquivo.readline()).strip()
	while linha != '':
		linhas.append(linha.split(',')[1])
		linha = (arquivo.readline()).strip()
	return linhas

def main(args):
	arquivo = open('script_linhas.txt','wt',encoding = 'utf-8')
	linhas = pega_linhas()
	nome_linhas = pega_nome_linhas()
	sentido = [' - IDA',' - VOLTA']
	horario = ['- DIA UTIL',' - SABADO',' - DOMINGOS E FERIADOS','- ATIPICOS']
	codigo_0 = "INSERT INTO LINHA(COD_LINHA,NUM_LINHA,DESCRICAO,FK_ITIN,FK_HR) VALUES ("
	lista = []
	cod =1;cod2=1
	iti = 1
	for i in range(len(linhas)):
		for j in range(1,3):
			lista.append(str(linhas[i]) + ",'" + str(nome_linhas[i])+ sentido[j-1] + "," + str(iti) +',')
			iti +=1
		for k in lista:
			#print(k.split(','))
			for m in range(1,5):
				final = codigo_0+str(cod)+','+k.split(',')[0]+','+k.split(',')[1]+horario[m-1]+"',"+k.split(',')[2]+','+ str(cod2) + ");"
				arquivo.write(final+'\n')
				cod+=1
				cod2 +=1
			#print(codigo)
		codigo_0 = "INSERT INTO LINHA(COD_LINHA,NUM_LINHA,DESCRICAO,FK_ITIN,FK_HR) VALUES ("
		lista= []
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
