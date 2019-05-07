INSERT INTO CLIENTES (NOME,CPF,RG,TELEFONE,EMAIL,DATA_NASC,LOGIN,SENHA,FK_ENDERECO) VALUES
('Benício Nelson Lima',9111044,12209,999183490,'benicionelsonlima@baltico.com.br','06-01-1995','benicionelsonlima',MD5('9B4oiyxp62'),1),
('Mário Caleb Cauã das Neves',126393905,2834926,981446060,'mmariocalebcauadasneves@poolrescue.com.br','10-04-1997','mmariocalebcauadasneves',MD5('4Y7Glkbl8Z'),2),
('Maria Emanuelly Alice Almeida',553498677,9026202,996849374,'mariaemanuellyalicealmeida@fulltransport.com.br','27-02-1984','mariaemanuellyalicealmeida',MD5('1j6bES08Mh'),3),
('Henrique Vicente Viana',747707716,7649953,984318534,'henriquevicenteviana@fredericodiniz.com','19-12-1987','henriquevicenteviana',MD5('4MpmnYZpJJ'),4),
('Fabiana Carla Lopes',940391402,329266597,997622787,'fabianacarlalopes@alstom.com','07-08-1992','fabianacarlalopes',MD5('9Si3sjQpts'),5),
('Bernardo Daniel Brito',176850445,3710838,95982879,'bbernardodanielbrito@softcia.com.br','13-08-2001','bbernardodanielbrito',MD5('9fhzFkTzRH'),6),
('Allana Alessandra Cristiane Nogueira',016149910,5156178,992851729,'allanaalessandracristianenogueira@danzarin.com.br','22-10-1994','allanaalessandracristianenogueira',MD5('Ls5O1mXWhX'),7),
('Benedito Rodrigo Nicolas Figueiredo',167457769,8525511,981463304,'bbeneditorodrigonicolasfigueiredo@imeio.com','17-04-1981','bbeneditorodrigonicolasfigueiredo',MD5('L94YmqzLZl'),8),
('Heloise Mirella Carolina Moraes',800951317,1127464,996983549,'heloisemirellacarolinamoraes@jovempanfmtaubate.com.br','10-02-1980','heloisemirellacarolinamoraes',MD5('iqyXr1WR8o'),9),
('Mateus Carlos Eduardo Giovanni Alves',538662135,0336832,993151141,'mateuscarloseduardogiovannialves@realbit.com.br','08-09-1982','mateuscarloseduardogiovannialves',MD5('gihB3Wojnz'),10),
('Arthur Sérgio Aragão',63614837700,396623803,27993618329,'arthursergioaragao-83@freitas.net.br','08-09-1982','arthursergioaragao',MD5('gihB3Wojnz'),11);


INSERT INTO CARTAO VALUES
(9111044,5312933863315275,'18-11-2020','Débito',MD5('945')),
(126393905,6011851295615561,'18-06-2020','Crédito',MD5('7314')),
(553498677,4514160378241775,'18-10-2020','Débito',MD5('4343')),
(747707716,6363681183417844,'18-01-2021','Crédito',MD5('245')),
(940391402,6011685543408340,'18-12-2020','Débito',MD5('3182')),
(176850445,5202966769090090,'07-01-2020','Crédito',MD5('251')),
(016149910,6011209435180550,'07-05-2020','Débito',MD5('7220')),
(167457769,6363696645529721,'07-11-2019','Crédito',MD5('530')),
(800951317,6011352954291042,'07-02-2021','Débito',MD5('4477')),
(538662135,201437738548875,'07-08-2020','Crédito',MD5('464'));

insert into ENDERECOS(RUA,NUMERO,BAIRRO,CIDADE,CEP,ESTADO,COMPLEMENTO) values
('Avenida Dois',499,'Jardim Tropical','Serra','29162-003','ES',null),
('Rua Licínio Bastos',291,'Boa Vista','São Mateus','29931-665','ES',null),
('Rua E Oito',306,'Santa Lúcia','Vitória','29056-132','ES',null),
('Rua Antúlio',757,'São Marcos','Aracruz','29190-730','ES',null),
('Rua Sete',541,'Centro','Viana','29130-028','ES',null),
('Avenida Prefeito Epaminondas de Almeida',193,'Pontal de Santa Mônica','Guarapari','29215-540','ES',null),
('Rua Cairo',586,'Nova Campo Grande','Cariacica','29158-515','ES','proximo a padaria rei do pao'),
('Escadaria Felício Ferreira de Medeiros',337,'Gurigica','Vitória','29046-208','ES','proximo ao extrabom'),
('Rua São Francisco de Assis',306,'São Pedro','Vitória','29030-060','ES',null),
('Avenida Leopoldina Smarzaro',309,'Monte Cristo','Cachoeiro de Itapemirim','29312-035','ES',null),
('Travessa Aristides Dalla Bernardina',672,'São Silvano','Colatina','29312-035','ES',null),
('Avenida Francisco Lacerda De Aguiar',0,'Centro','Cachoeiro do Itapemirim','29304-900','ES',NULL),
('Avenida Alexandre Buaiz',350,'Ilha do Princípe','Vitória','29020-300','ES',NULL),
('Avenida America',1560,'Jardim America','Cariacica','29140-050','ES',NULL),
('Avenida Ernesto Canal',200,'Alvorada','Vila Velha','29117-762','ES',NULL),
('Avenida Nossa Senhora da Penha',1590,'Barro Vermelho','Vitória','29057-550','ES',NULL)
;

INSERT INTO EMPRESAS VALUES
('27.486.182/0088-60',12,'Viacao Aguia Branca S/A','(27)3322-8603',NULL);
('27.175.975/0173-44',13,'Viacao Itapemirim S/A','(28)2101-2624','faleconosco@itapemirimcorp.com.br'),
('27.390.160/0001-40',14,'Viacao Planeta LTDA','(27)3346-4255','jlgrillo@terra.com.br'),
('27.583.202/0001-60',15,'Viacao Sanremo LTDA','(27)3326-4149','faleconosco@vsanremo.com.br'),
('28.055.226/0001-09',15,'Viacao Alvorada Ltda - EPP','(27)3369-6636',NULL),
('28.503.894/0001-51',16,'COMPANHIA DE TRANSPORTES URBANOS DA GRANDE VITORIA','(27)3232-4500','ceturb@ceturb.es.gov.br')
;

INSERT INTO CARTAO_NFC VALUES
('47203C308A08E7','126393905','25-06-2018'),
('82CDF34FEAFF79','63614837700','07-01-2017'),
('663891E89CB4F9','940391402','04-12-2018'),
('D3A41265795AAD','9111044','12-03-2019'),
('6BA45C098238AC','747707716','18-05-2016'),
('C0692B0781CC59','538662135','01-01-2018'),
('34A24DD2E2DCB0','800951317','10-07-2011'),
('8A710B13A111F5','167457769','03-04-2018')
;

INSERT INTO MAQUINA_DECODIFICADORA VALUES
('40C0295AB9A6D0','27.486.182/0088-60','18-08-2018'),
('927E8F0DEB47B4','27.486.182/0088-60','18-04-2019'),
('A4D0978C26BD9E','27.175.975/0173-44','18-11-2018'),
('9C7994CE540285','27.175.975/0173-44','18-10-2017'),
('B49B2728F9ABFB','27.390.160/0001-40','18-09-2020'),
('122455214679EB','27.390.160/0001-40','18-01-2019'),
('05C94AAFE77393','27.583.202/0001-60','18-12-2018'),
('285F3D41E2CCD2','27.583.202/0001-60','18-02-2019'),
('FC341F61E62050','28.055.226/0001-09','18-09-2018'),
('F9A5BDAF6B4905','28.055.226/0001-09','18-01-2019'),
('07FDF88A01E4A3','28.503.894/0001-51','23-02-2019'),
('C2DD589A626CE3','28.503.894/0001-51','12-04-2019')
;

INSERT INTO TRANSACAO(CARTAO_TRANSACAO,VALOR,CNPJ_TRANSACAO) VALUES
(6011851295615561,75.87,'27.486.182/0088-60'),
(5312933863315275,80.75,'27.486.182/0088-60'),
(5202966769090090,6.35,'27.175.975/0173-44'),
(6363696645529721,3.75,'27.175.975/0173-44'),
(5202966769090090,40.16,'27.390.160/0001-40'),
(201437738548875,10.00,'27.390.160/0001-40'),
(6011209435180550,45.00,'27.583.202/0001-60'),
(6011209435180550,16.45,'27.583.202/0001-60'),
(6011209435180550,3.47,'28.055.226/0001-09'),
(5312933863315275,99.30,'28.055.226/0001-09')
;

INSERT INTO VIAGEM(NUMERO_ONIBUS,NOME_VIAGEM,PLACA,FK_NFC_UID_MAQUINA,HORARIO_SAIDA,DIA_VIAGEM) VALUES
('800A','T. LARANJEIRAS / JARDIM CAMBURI VIA T. CARAPINA - CIRCULAR A','MPT-0657','C2DD589A626CE3','12:12:00','23-05-2019'),
('814','CASCATA / T. LARANJEIRAS VIA CASCATA II','MRB-7970','07FDF88A01E4A3','15:20:00','02-05-2019'),
('860','T. JACARAIPE / T. LARANJEIRAS VIA ROD. PAULO P. GOMES','MTS-1675','C2DD589A626CE3','16:20:00','28-04-2019'),
('1801','RODOVIÁRIA/JACARAIPE - VIA LARANJEIRAS','MSC-5590','07FDF88A01E4A3','17:00:00','14-06-2019'),
('501','T. JACARAIPE / T. VILA VELHA VIA T. CARAPINA/3ª PONTE','MPL-5661','C2DD589A626CE3','07:05:00','16-09-2019'),
('860','IFES / T. LARANJEIRAS','MSZ-6968','C2DD589A626CE3','05:54:00','25-01-2020'),
(NULL,'Vitória X Anchieta ES-060/VV [CONV]','FHF-9534','05C94AAFE77393','05:10:00','25-12-2019'),
(NULL,'Vitória X Cach. Itapemirim Via Belem e Rio Novo','DVW-5933','285F3D41E2CCD2','10:40:00','14-04-2019')
;

INSERT INTO PASSAGEM (FK_NFC_UID_USUARIO,FK_NFC_UID_MAQUINA,DATA_PASSAGEM,HORA_PASSAGEM) VALUES
('D3A41265795AAD','C2DD589A626CE3','23-05-2019','12:34:26'),
('47203C308A08E7','285F3D41E2CCD2','14-04-2019','11:07:42'),
('47203C308A08E7','07FDF88A01E4A3','02-05-2019','17:24:38'),
('47203C308A08E7','05C94AAFE77393','25-12-2019','06:01:02')
;
