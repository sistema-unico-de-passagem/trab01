# TRABALHO 01:  Sistema Único de Passagens
Trabalho desenvolvido durante a disciplina de BD1

# Sumário

### 1. COMPONENTES<br>
Integrantes do grupo<br>
Jack Johnson Cummings Junior: info.jackjr@gmail.com<br>
Lucas Campista da Silva: lukascampista@hotmail.com<br>
Ágape Spagnol Rocha Campos: agape_spagnol@hotmail.com<br>
Matheus Aguiar Ximenes: aguiar007ax@gmail.com<br>


### 2.INTRODUÇÃO E MOTIVAÇAO<br>

<p align="justify"> A empresa <b>Brutec</b> tem como objetivo colaborar com as empresas de transportes públicos e privados para melhorar o pagamento de suas passagens por um meu único de pagamento com a utilização do <b>NFC</b> para a melhor facilidade de seus usuários.    Com esse sistema SUP a empresa <b>Brutec</b> vai ter um melhor gerenciamento das contas e passagens pagas para cada empresa. O sistema   <i>SUP</i> irá armazenar os dados dos seus usuários tais como senha, login, cpf entre outros para garantir a segurança de suas contas e <b>NFCs</b>  que seus usuários possam ter.</p> 

### 3.MINI-MUNDO Novo<br>

<p align="justify"> O sistema que foi proposto para <b>Brutec</b>, o usuário deverá obrigatoriamente ter um cadastro no sistema. Um usuário pode ser uma empresa ou uma pessoa física.Uma pessoa conterá nome, telefone, e-mail , endereço, CPF, RG. Um usuário poderá também cadastrar informações sobre seu banco, a fim de efetuar recargas do cartão.  No ato do cadastro, o usuário deverá também cadastrar seu rosto para reconhecimento facial. Um usuário possuirá um cartão e/ou uma chave <b>NFC</b> instalado no celular. Um usuário pode ter diferentes tipos de cartão, mas um cartão pertencerá a apenas um usuário. Um cartão pode conter o CPF do usuário, código do cartão, data de vencimento e foto. Acerca da recarga do cartão, poderá ser feita através de boletos bancários, descontos automáticos em contas bancárias, pagamento de cartões de crédito ou pagar fisicamente em um local dedicado ao fim. O sistema terá diversas empresa de ônibus cadastradas. Todas as empresas terão suporte para o uso da chave <b>NFC</b>, porém nem todas ultilizarão  cartão de passagem. Empresas também poderão se cadastrar como usuários. Uma empresa terá nome, CNPJ, endereço, telefone de contato e E-mail, além de informações a respeito de pagamentos. Cada pessoa pode estar associado a várias modalidades, podendo ser: Idoso, Estudante, Estudante Gratuito e Cartão de Empresa (isso para empresas que utilizam cartão de passagem, como a GVbus.). Empresas como Águia Branca utilizam apenas o <b>NFC</b> como passe.</p>

### 4.RASCUNHOS BÁSICOS DA INTERFACE (MOCKUPS)<br>
Neste ponto a codificação não e necessária, somente as ideias de telas devem ser criadas, o princípio aqui é pensar na criação da interface para identificar possíveis informações a serem armazenadas ou descartadas <br>

Sugestão: https://balsamiq.com/products/mockups/<br>

![Alt text](https://github.com/discipbd1/trab01/blob/master/balsamiq.png?raw=true "Title")
![Arquivo PDF do Protótipo Balsamiq feito para Empresa Brutec - Versão Mobile](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Mobile.pdf)

[Arquivo PDF do Protótipo Balsamiq feito para Empresa Brutec - Versão Desktop](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Sistema%20%C3%9Anico%20de%20Passagens.pdf)

#### 4.1 QUAIS PERGUNTAS PODEM SER RESPONDIDAS COM O SISTEMA PROPOSTO?
    a) O sistema proposto poderá fornecer quais tipos de relatórios e informaçes? 
    b) Crie uma lista com os 5 principais relatórios que poderão ser obtidos por meio do sistema proposto!
    
 A Empresa <b>Brutec</b> precisa inicialmente dos seguintes relatórios:
 
- Relatório que informa em que época do ano foram feitas mais viagens.</p>

- Relatório dos usuários que mais utlizam o sistema e suas linhas mais usudas. </p>

- Relatório das cidades com mais ofertas de terminais/agências de viação. </p>

- Relatório das viações mais usadas e em qual época do ano. </p>

- Relatório dos tipos de pagamentos mais utilizados .</p>
 
 
#### 4.2 TABELA DE DADOS DO SISTEMA:

![Exemplo de Tabela de dados da Empresa Brutec](https://github.com/sistema-unico-de-passagem/trab01/blob/master/arquivos/%20TABELA%20DE%20DADOS%20DO%20SISTEMA.xlsx "Tabela - Empresa Brutec")
    
>## Marco de Entrega 01 em: (06/09/2018)<br>

### 5.MODELO CONCEITUAL<br>
    A) NOTACAO ENTIDADE RELACIONAMENTO 
        * Para nosso prótótipo limitaremos o modelo conceitual nas 6 principais entidades do escopo
        * O protótipo deve possui no mínimo duas relações N para N
        * o mínimo de entidades do modelo conceitual será igual a 5
        
![Alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/MODELO%20CONCEITUAL.png?raw=true)
    
    B) NOTACAO UML (Caso esteja fazendo a disciplina de analise)
    C) QUALIDADE 
        Garantir que a semântica dos atributos seja clara no esquema
        Criar o esquema de forma a garantir a redução de informação redundante, possibilidade de valores null, 
        e tuplas falsas
    
        
    
#### 5.1 Validação do Modelo Conceitual
    [Grupo01]: [Nomes dos que participaram na avaliação]
    [Grupo02]: [Nomes dos que participaram na avaliação]

#### 5.2 DECISÕES DE PROJETO
    [atributo]: [descrição da decisão]
    
    EXEMPLO:
    a) Campo Endereço: em nosso projeto optamos por um campo multivalorado e composto, pois a empresa 
    pode possuir para cada departamento mais de uma localização... 
    b) justifique!

>## Marco de Entrega 02 em: (17/09/2018)<br>
#### 5.3 DESCRIÇÃO DOS DADOS 
<B>CLIENTES</B> <br>
- NOME: Nome do usuário <br>
- TELEFONE: Número de telefone cadastrado do usuario <br>
- CPF: CPF do usuário <br>
- RG: RG do usuário <br>
- E-MAIL: Endereço eletrônico 
- ENDERECO: Endereço do usuário cadastrado <br>
- DATA_NASC: Data de nascimento <br>
- LOGIN: Login do usuário no sistema <br>
- SENHA: Senha do usuário no Sistema <br>

<B>CARTÃO NFC</B> <br>
- SALDO: Quantia de crédito em reais ainda no cartão nfc <br>
- DATA_CADASTRO: Data que se foi cadastrado o cartão e usuário <br>
- NFC_UID_USUARIO: Número de id do cartão nfc <br>
- CPF_PROPRIETARIO: CPF do dono da cartão NFC <br>
- DATA_VALIDADE: Data de validade do cartao <br>


<B>VIAGENS</B> <br>
- NOME_VIAGEM: Nome da viagem (Terminal de Laranjeiras, Ibes) <br>
- NÚMERO_ÔNIBUS: Número do ônibus (515, 572...) <br>
- COD_VIAGENS: Número do codigo da viagem realisada
- PLACA: Placa do veiculo <br>
- FK_NFC_UID_MAQUINA: Código do validador do ônibus <br>
- HORARIO_SAIDA: Horário de saída da viagem <br>
- DIA_VIAGEM: Dia da viagem <br>

<B>VALIDADOR</b> <br>
- NFC_UID_MAQUINA: Id do NFC que o usuário possui <br>
- DATA_CRIACAO: Data de criação do validador <br>
- CNPJ_PROPRIETARIO: Empresa propietaria do validador <br>

<B>EMPRESA</B> <br>
- CNPJ: Número do cnpj da empresa <br>
- NOME: Nome da empresa <br>
- FK_END: Código do endereço da empresa <br>
- TELEFONE: Número de telefone da empresa <br>
- E-MAIL: Endereço eletrônico da empresa

<B>LINHA</B> <br>
- NUM_LINHA: Número da linha <br>
- DESCRICAO: Descrição da linha <br>
- FK_INT: Código do itinerário dessa linha <br>
- FK_HR: Código dos horários dessa linha <br>
- COD_LINHA: Código da linha

<B>CARTAO</B> <br>
- CPF: CPF do dono do cartão <br>
- NUMERO_CARTAO: Número do cartão <br>
- VALIDADE_CARTAO: Data de validade do cartão <br>
- TIPO_CARTAO: Tipo do cartão (Debito,Crédito) <br> 
- SENHA_CARTAO: Senha do cartão <br>
- ID_CARTAO: Código do cartão <br>

<B>TERMINAIS</B> <br>
- NOME: Nome do terminal/agência <br>
- FK_ENDERECO: Código do endereço <br>
- LINHAS: Linhas que passam por esse terminal/agência <br>
- TEL: Telefone de contato <br>

<B>HORARIOS</B> <br>
- COD_HORARIO: Código do horário <br>
- HORARIO: Horário do ônibus

<B>LOG MAQUINA</B> <br>
- FK_NFC_UID_USUARIO: Chave nfc do usuário <br>
- FK_UID_MAQUINA: Nfc da máquina verificadora <br>
- DATA_PASSAGEM: Data da passagem <br>
- HORA_PASSAGEM: Hora da passagem <br>
- ID_LOG: Código do relatorio <br>

<B>TRANSACAO</B> <br>
- ID_TRANSACAO: Código da transação <br>
- FK_ID_CARTAO: Código do cartão do usuario <br>
- VALOR: Valor de recarga do cartão NFC <br>
- DATA_TRANSACAO: Data da transação <br>
- FK_FNC_CARTAO: Código do cartão NFC do usuario <br>

<B>ITINERARIOS</B> <br>
- COD_ITEINERARIO: Código do itinerario <br>
- LOCAIS: Locais pelos quais passa o ônibus <br>

<B>ENDERECOS</B> <br>
- RUA: Rua <br>
- NUMERO: Número da residência <br>
- BAIRRO: Bairro <br>
- CIDADE: Cidade <br>
- CEP: CEP <br>
- ESTADO: Estado <br>
- COMPLEMENTO: Informação complementar a respeito da residência do usuário <br>
- ID_ENDERECO: Código do endereço <br>

### 6	MODELO LÓGICO<br>
![Alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/LOGICO.png?raw=true)

        a) inclusão do modelo lógico do banco de dados
        b) verificação de correspondencia com o modelo conceitual 
        (não serão aceitos modelos que não estejam em conformidade)

### 7	MODELO FÍSICO<br>
        a) inclusão das instruções de criacão das estruturas DDL 
        (criação de tabelas, alterações, etc..)          
        
### 8	INSERT APLICADO NAS TABELAS DO BANCO DE DADOS<br>
#### 8.1 DETALHAMENTO DAS INFORMAÇÕES
        a) inclusão das instruções de inserção dos dados nas tabelas criadas pelo script de modelo físico 
        b) formato .SQL

#### 8.2 INCLUSÃO DO SCRIPT PARA CRIAÇÃO DE TABELAS E INSERÇÃO DOS DADOS
        a) Junção dos scripts anteriores em um único script 
        (create para tabelas e estruturas de dados + dados a serem inseridos)
        b) Criar um novo banco de dados para testar a restauracao 
        (em caso de falha na restauração o grupo não pontuará neste quesito)
        c) formato .SQL
#### 8.3 INCLUSÃO DO SCRIPT PARA EXCLUSÃO DE TABELAS EXISTENTES, CRIAÇÃO DE TABELA NOVAS E INSERÇÃO DOS DADOS
        a) Junção dos scripts anteriores em um único script
        (Drop para exclusão de tabelas + create para tabelas e estruturas de dados + dados a serem inseridos)
        b) Criar um novo banco de dados para testar a restauracao 
        (em caso de falha na restauração o grupo não pontuará neste quesito)
        c) formato .SQL
#### 8.4 Principais fluxos de informação e principais tabelas do sistema

        a) Quais os principais fluxos de dados de informação no sistema em densenvolvimento (mínimo 3)
        - Transação bancária para recarga de créditos no sistema (tabela transação).
        - Viagens feitas pelos usuãrios (tabela Viagem).
        - Relatórios obtidos dos validadores presentes nos ônibus (tabela log_máquina).
        
        b) Quais as tabelas que conterão mais dados no sistema em densenvolvimento (mínimo 3)
        - Linhas
        - Transacao
        - Enderecos
        
        c) informe quais as 5 principais tabelas do sistema em densenvolvimento.
        - Linhas
        - Terminais
        - Transacao
        - log_máquina
        - Usuários
        
>## Marco de Entrega 03 em: (27/09/18) <br>

### 9	TABELAS E PRINCIPAIS CONSULTAS<br>
    OBS: Incluir para cada tópico as instruções SQL + imagens (print da tela) mostrando os resultados.<br>
    
#### 9.1	CONSULTAS DAS TABELAS COM TODOS OS DADOS INSERIDOS (Todas) <br>
![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Print/print%201%20-%20insert%20cartao.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Print/print%201%20-%20insert%20cartao_nfc.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Print/print%201%20-%20insert%20empresas.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Print/print%201%20-%20insert%20enderecos.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Print/print%201%20-%20insert%20transacao.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Print/print%201%20-%20insert%20viagem.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Print/clientes.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Print/horarios.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Print/itras.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Print/linhas.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Print/log_maquina.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Print/terminais.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/Print/valida.png?raw=true)



#### 9.2	CONSULTAS DAS TABELAS COM FILTROS WHERE (Mínimo 4)<br>
![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.2/9.2%20-%201.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.2/9.3%20-%202.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.2/9.3%20-%203.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.2/9.4%20-%204.png?raw=true)

#### 9.3	CONSULTAS QUE USAM OPERADORES LÓGICOS, ARITMÉTICOS E TABELAS OU CAMPOS RENOMEADOS (Mínimo 11)

    a) Criar 5 consultas que envolvam os operadores lógicos AND, OR e Not
![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.3/9.3%20-%201.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.3/9.3%20-2.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.3/9.3%20-%203.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.3/9.3%20-%204.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.3/9.3%20-%205.png?raw=true)

    b) Criar no mínimo 3 consultas com operadores aritméticos 
![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.3%20-%20b/9.3%20-%20b%20-%201.png?raw=true) 

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.3%20-%20b/9.3%20-%20b%20-%202.png?raw=true)  

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.3%20-%20b/9.3%20-%20b%20-%203.png?raw=true)  

    c) Criar no mínimo 3 consultas com operação de renomear nomes de campos ou tabelas
![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.3%20-%20c/9.3%20-%20c%20-%201.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.3%20-%20c/9.3%20-%20c%20-%202.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.3%20-%20c/9.3%20-%20c%20-%203.png?raw=true)
        
#### 9.4	CONSULTAS QUE USAM OPERADORES LIKE E DATAS (Mínimo 12) <br>

    a) Criar outras 5 consultas que envolvam like ou ilike
![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.4%20-%20a/9.4%20-%20a%20-%201.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.4%20-%20a/9.4%20-%20a%20-2.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.4%20-%20a/9.4%20-%20a%20-%203.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.4%20-%20a/9.4%20-%20a%20-%204.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.4%20-%20a/9.4%20-%20a%20-%205.png?raw=true)

    b) Criar uma consulta para cada tipo de função data apresentada.

#### 9.5	ATUALIZAÇÃO E EXCLUSÃO DE DADOS (Mínimo 6)<br>

>## Marco de Entrega 04 em: (18/10/2017)<br>

#### 9.6	CONSULTAS COM JUNÇÃO E ORDENAÇÃO (Mínimo 6)<br>
        a) Uma junção que envolva todas as tabelas possuindo no mínimo 3 registros no resultado
        b) Outras junções que o grupo considere como sendo as de principal importância para o trabalho
#### 9.7	CONSULTAS COM GROUP BY E FUNÇÕES DE AGRUPAMENTO (Mínimo 6)<br>
![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.7/9.7%20-%201.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.7/9.7%20-%202.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.7/9.7%20-%203.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.7/9.7%20-%204.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.7/9.7%20-%205.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.7/9.7%20-%206.png?raw=true)
            
#### 9.8	CONSULTAS COM LEFT E RIGHT JOIN (Mínimo 4)<br>
![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.8/9.8%20-%201.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.8/9.8%20-%202.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.8/9.8%20-%203.png?raw=true)

![alt text](https://github.com/sistema-unico-de-passagem/trab01/blob/master/9.8/9.8%20-%204.png?raw=true)
            
#### 9.9	CONSULTAS COM SELF JOIN E VIEW (Mínimo 6)<br>
        a) Uma junção que envolva Self Join
        b) Outras junções com views que o grupo considere como sendo de relevante importância para o trabalho
#### 9.10	SUBCONSULTAS (Mínimo 3)<br>
### 10	ATUALIZAÇÃO DA DOCUMENTAÇÃO DOS SLIDES PARA APRESENTAÇAO FINAL (Mínimo 6 e Máximo 10)<br>

### 11 Backup completo do banco de dados postgres 
    a) deve ser realizado no formato "backup" 
        (Em Dump Options #1 Habilitar opções Don't Save Owner e Privilege)
    b) antes de postar o arquivo no git o mesmo deve ser testado/restaurado por outro grupo de alunos/dupla
    c) informar aqui o grupo de alunos/dupla que realizou o teste.

### 12	TUTORIAL COMPLETO DE PASSOS PARA RESTAURACAO DO BANCO E EXECUCAO DE PROCEDIMENTOS ENVOLVIDOS NO TRABALHO PARA OBTENÇÃO DOS RESULTADOS<br>
        a) Outros grupos deverão ser capazes de restaurar o banco 
        b) executar todas as consultas presentes no trabalho
        c) executar códigos que tenham sido construídos para o trabalho 
        d) realizar qualquer procedimento executado pelo grupo que desenvolveu o trabalho
        
### 13   DIFICULDADES ENCONTRADAS PELO GRUPO<br>
>## Marco de Entrega Final em: (08/11/2018)<br>
        
### 14  FORMATACAO NO GIT: https://help.github.com/articles/basic-writing-and-formatting-syntax/
<comentario no git>
    
##### About Formatting
    https://help.github.com/articles/about-writing-and-formatting-on-github/
    
##### Basic Formatting in Git
    
    https://help.github.com/articles/basic-writing-and-formatting-syntax/#referencing-issues-and-pull-requests
    
    
##### Working with advanced formatting
    https://help.github.com/articles/working-with-advanced-formatting/
#### Mastering Markdown
    https://guides.github.com/features/mastering-markdown/



    

    
### OBSERVAÇÕES IMPORTANTES

#### Todos os arquivos que fazem parte do projeto (Imagens, pdfs, arquivos fonte, etc..), devem estar presentes no GIT. Os arquivos do projeto vigente não devem ser armazenados em quaisquer outras plataformas.
1. <strong>Caso existam arquivos com conteúdos sigilosos<strong>, comunicar o professor que definirá em conjunto com o grupo a melhor forma de armazenamento do arquivo.

#### Todos os grupos deverão fazer Fork deste repositório e dar permissões administrativas ao usuário do git "profmoisesomena", para acompanhamento do trabalho.

#### Os usuários criados no GIT devem possuir o nome de identificação do aluno (não serão aceitos nomes como Eu123, meuprojeto, pro456, etc). Em caso de dúvida comunicar o professor.


Link para BrModelo:<br>
http://www.sis4.com/brModelo/download.html
<br>


Link para curso de GIT<br>
![https://www.youtube.com/curso_git](https://www.youtube.com/playlist?list=PLo7sFyCeiGUdIyEmHdfbuD2eR4XPDqnN2?raw=true "Title")


