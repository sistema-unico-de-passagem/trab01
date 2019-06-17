
from random import *

def main():
	arq = open('uid_user.txt','r')
	lst_uid = arq.readlines()
	
	arq = open('id_cartao.txt','r')
	lst_cartao = arq.readlines()
	
	arq = open('SQL_TRANSACAO.txt','w')
	sr = ''
	id_c = 0
	for i in range(len(lst_uid)):
		
		sr = 'INSERT INTO TRANSACAO VALUES ('+ str(id_c) +','+ str(lst_cartao[i]) + ',' + str(randint(1,500)) +'.'+ str(randint(1,99)) +','+ "'" + str(randint(2013,2020))+'-'+str(randint(1,12))+'-'+str(randint(1,31))+ "'" + ',' + str(lst_uid[i]) + ');\n'
		arq.write(sr)
		sr = ''
		id_c +=1
if __name__ == '__main__':
	main()
