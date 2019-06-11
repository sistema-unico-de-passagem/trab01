#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  make_sql.py
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
 

def main(args):
	lista_base = ['_saida_terminal_util.txt','_saida_terminal_sabado.txt','_saida_terminal_domingo.txt','_saida_terminal_atipico.txt','_saida_ptfinal_util.txt','_saida_ptfinal_sabado.txt','_saida_ptfinal_domingo.txt','_saida_ptfinal_atipico.txt']
	lista_linhas = pega_linhas()
	cod = 1
	arquivo_script = open('script.txt','wt',encoding = 'utf-8')
	for i in lista_linhas:
		for j in lista_base:
			arquivo = open('HORARIOS/'+i+j,'rt',encoding = 'utf-8')
			linha = arquivo.read()
			arquivo_script.write("INSERT INTO HORARIOS(COD_HORARIO,HORARIO) VALUES (" + str(cod) + ",'" + linha.strip()+ "');\n")
			#print(linha)
			cod +=1
			arquivo.close()
	arquivo_script.close()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
