#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gerar_nomes.py
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
import ast
def pega_nomes():
	arquivo = open('banco_nomes.txt','rt',encoding = 'utf-8')
	lista =''
	linha = (arquivo.readline()).strip()
	while linha != '':
		lista+=linha
		linha = (arquivo.readline()).strip()
	lista = (ast.literal_eval(lista))
	arquivo.close()
	return lista

def main(args):
	dic_aux = {}
	arquivo_nomes = open('script_nomes.txt','wt',encoding = 'utf-8')
	arquivo_enderecos = open('banco_enderecos.txt','rt',encoding = 'utf-8')
	lista = pega_nomes()
	codigo = 
	for i in lista:
		dic_aux = i
		print((dict(dic_aux))['nome'])
		codigo = 'INSERT INTO CLIENTE(NOME,CPF,RG,TELEFONE,EMAIL,DATA_NASC,LOGIN,SENHA) VALUES (' + (dic_aux))['nome'] + ',' + (dic_aux))['cpf'] + ',' + (dic_aux))['rg'] + ',' + (dic_aux))['celular']+ ',' + (dic_aux))['email']+ ',' + ((dic_aux))['data_nasc'])+ ',' + (dic_aux))['email']
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
