
# -*- coding: utf-8 -*-

from random import randint


def gerarpessoas(lst_nomes,lst_tel,lst_endc,lst_cpfs,tam):
	
	#aqui irei gravar cada pessoa no arquivo de pessoas

	for i in range(tam):
		pessoa = ''
		pessoa += lst_nomes[i]+';'+lst_endc[i]+';'+lst_cpfs[i]+';'+lst_tel[i]+'\n'
		arq = open('/home/lucas/Documents/maladireta/pessoas.txt','a')
		arq.write(pessoa)
	
def gerarcpf(tam):
	lcpfs = []
	for i in range(tam):
		cpf = ''
		cpf += str(randint(99999999,1000000000))+'-'+str(randint(9,100))
		while (cpf in lcpfs):
			cpf = ''
			cpf += str(randint(99999999,1000000000))+'-'+str(randint(9,100))
		lcpfs.append(cpf)
	return lcpfs
	
def gerarendc(lruas,lbairros,lcidades,lestados,tam):
	
	lst_endc = []
	for i in range (tam):
		endc = []
		rua = str(lruas[randint(0,len(lruas)-1)])
		bairro = str(lbairros[randint(0,len(lbairros)-1)])
		city = str(lcidades[randint(0,len(lcidades)-1)])
		estado = str(lestados[randint(0,len(lestados)-1)])		
		
		end = [rua,str(randint(99,1000)),str(randint(9999,100000))+'-'+str(randint(99,1000)),bairro,city,estado]	 
		lst_endc.append(end)

	return lst_endc
	
def gerartel(tam):
	lst_tel = []
	for i in range (tam):
		numtel = '9'
		for j in range(8):
			num = randint(0,9)
			numtel += str(num)
		while (numtel in lst_tel):
			numtel = '9'
			for i in range(8):
				num = randint(0,9)
				numtel += str(num)
		lst_tel.append(numtel)
		

	return lst_tel
	
	
def gerarnomes(lnomes,lsbrnomes,qtd_nm):
	lst_nomes = []
	for i in range (qtd_nm):
		lnomec = []
		tam = randint(1,2)
		lnomec.append(lnomes[randint(0,len(lnomes)-1)])
		for i in range (tam):
			snm = lsbrnomes[randint(0,len(lsbrnomes)-1)]
			while (snm in lnomec):
				snm = lsbrnomes[randint(0,len(lsbrnomes)-1)]
			lnomec.append(snm)
		nome = ''
		for i in range(len(lnomec)):
			nome += lnomec[i] + ' '
		lst_nomes.append(nome)
		
	return lst_nomes
	
	
def main():
	tam = 50 #numero de pessoas geradas
	
	lst_nomes = []
	lst_cpf = []
	lst_tel = []
	lst_endc = []
	'''#gerar nomes
	#nomes
	arq = open('/home/lucas/Documents/maladireta/gerdaor de nomes/nomes.txt','r')
	lnomes = []
	for i in arq:
		lnomes.append(i.strip())
	arq.close()
	
	#sobrenomes
	arq = open('/home/lucas/Documents/maladireta/gerdaor de nomes/sobrenomes.txt','r')
	lsbrnomes = []
	for i in arq:
		lsbrnomes.append(i.strip())
	
	lst_nomes = gerarnomes(lnomes,lsbrnomes,tam)
	#gerar telefone
	lst_tel = gerartel(tam)'''
	
	#gerarendereço
	#ruas
	arq = open('ruas.txt','r')
	lruas = []
	for i in arq:
		lruas.append(i.strip())
	arq.close()
	#bairros
	arq = open('bairros.txt','r')
	lbairros = []
	for i in arq:
		lbairros.append(i.strip())
	arq.close()
	
	#cidades
	arq = open('cidades.txt','r')
	lcidades = []
	for i in arq:
		lcidades.append(i.strip())
	arq.close()
	
	#estados
	arq = open('estados.txt','r')
	lestados = []
	for i in arq:
		lestados.append(i.strip())
	arq.close()
	lst_endc = gerarendc(lruas,lbairros,lcidades,lestados,30)
	
	'''#gerar cpf
	lst_cpfs = gerarcpf(tam)'''
	
	#gerando as pessoas
	arq = open('enderecos.txt','w')
	sr = ''
	cod = 78
	for i in lst_endc:
		print(i)
	for i in range(len(lst_endc)):		
		sr+= 'INSERT INTO ENDERECOS VALUES ('+"'"+lst_endc[i][0]+"'"+','+str(lst_endc[i][1]+','+"'"+lst_endc[i][3]+"'"+','+"'"+lst_endc[i][4]+"'"+','+"'"+lst_endc[i][2])+"'"+','+"'"+lst_endc[i][5]+"'"+','+'null'+','+str(cod)+');\n'
		arq.write(sr)
		sr = ''
		cod+=1
if __name__ == '__main__':
	main()
