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
 
- Relatório que informe quais são os gerentes de cada departamento incluindo as seguintes informações: número do departamento,  nome do departamento, e nome do gerente.</p>

- Relatório de empregados por projeto incluindo as seguintes informações: número do projeto, nome do projeto, rg do empregado, nome do empregado e quantidade de horas de trabalho do empregado alocadas ao projeto.</p>

- Relatório de empregados com dependentes incluindo as seguintes informações: rg do empregado, nome do empregado, nome do dependente, tipo de relação, data de nascimento do dependente e sexo do dependente.</p>

- Relatório com a quantidade de empregados por cada departamento incluindo as seguintes informações: nome do departamento, supervisor e quantidade de empregados alocados no departamento.</p>

- Relatório de supervisores e supervisionados incluindo as seguintes informações: nome do supervisor e nome do supervisionado.</p>
 
 
#### 4.2 TABELA DE DADOS DO SISTEMA:

![Exemplo de Tabela de dados da Empresa Brutec](https://github.com/sistema-unico-de-passagem/trab01/blob/master/arquivos/%20TABELA%20DE%20DADOS%20DO%20SISTEMA.xlsx "Tabela - Empresa Brutec")
    
>## Marco de Entrega 01 em: (06/09/2018)<br>

### 5.MODELO CONCEITUAL<br>
    A) NOTACAO ENTIDADE RELACIONAMENTO 
        * Para nosso prótótipo limitaremos o modelo conceitual nas 6 principais entidades do escopo
        * O protótipo deve possui no mínimo duas relações N para N
        * o mínimo de entidades do modelo conceitual será igual a 5
        
![Alt text]("https://github.com/sistema-unico-de-passagem/trab01/blob/master/CONCEITUAL.brM3")
    
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
- TELEFONE: número de telefone cadastrado do usuario <br>
- CPF: cpf do usuário <br>
- RG: rg do usuário <br>
- Telefone: Telefone(s) do usuário
- E-mail : Endereço eletrônico 
- ENDERECO: endereço do usuário cadastrado <br>
- NOME: nome do usuário <br>
- data_nasc: Data de nascimento <br>
- login: Login do usuário no sistema <br>
- Senha: Senha do usuário no Sistema <br>

<B>CARTÃO NFC</B> <br>
- saldo: quantia de crédito em reais ainda no cartão nfc <br>
- DATA_CADASTRO: data que se foi cadastrado o cartão e usuário <br>
- NFC_uid_usuario: número de id do cartão nfc <br>
- cpf_propietario: CPF do dono da cartão NFC <br>
- DATA_VALIDADE : Data de validade do cartao <br>


<B>VIAGENS</B> <br>
- nome_viagem: nome da viagem (terminal de laranjeiras, ibes) <br>
- NÚMERO_ÔNIBUS: número do ônibus (515, 572...) <br>
- COD_VIAGENS: número do codigo da viagem realisada
- placa: Placa do veiculo <br>
- fk_nfc_uid_maquina: Código do validador do ônibus <br>
- horario_saida: Horario de saida da viagem <br>
- dia_viagem: Dia da viagem <br>

<B>Validador</b> <br>
- NFC_UID_MAQUINA: id do nfc que o usuário possui <br>
- data_criacao: Data de criação do validador <br>
- CNPJ_Propietario: Empresa propietaria do validador <br>

<B>EMPRESA</B> <br>
- CNPJ: número do cnpj da empresa <br>
- NOME: nome da empresa <br>
- fk_end: codigo do endereço da empresa <br>
- TELEFONE: número de telefone da empresa <br>
- E-Mail: endereço eletrônico da empresa

<B>Linha</B> <br>
- num_linha: Numero da linha <br>
- descricao: Descrição da linha <br>
- fk_itin: Codigo do iinerario dessa linha <br>
- fk_hr: Codigo dos horarios dessa linha <br>
- cod_linha: Código da linha

<B>CARTAO</B> <br>
- CPF: CPF do dono do cartão <br>
- numero_cartao: NUmero do cartão <br>
- validade_cartao: Data de validade do cartão <br>
- tipo_cartao: Tipo do cartão(Debito,Crédito) <br> 
- senha_cartão: Senha do cartão <br>
- id_cartao: cdio do cartao <br>

<B>TERMINAIS</B> <br>
- nome: Nome do terminal/agencia <br>
- fk_endereco: Codigo do endereço <br>
- linhas: Linhas que passão por esse terminal/agência <br>
- tel: Telefone de contato <br>

<B>HORARIOS</B> <br>
- cod_horario: Codigo do horario <br>
- horario: Horario do ônibus

<B>log_maquina</B> <br>
- fk_nfc_uid_usuario: Chave nfc do usuario <br>
- fk_uid_maquina: nfc da maquina verificadora <br>
- data_passagem: data da passagem <br>
- hora_passagem: hora da passagem <br>
- id_log: codigo do relatorio <br>

<B>TRANSACAO</B> <br>
- id_transacao: Codigo da transação <br>
- fk_id_cartao: Codigo do cartao do usuario <br>
- valor: Valor de recarga do carato NFC <br>
- data_transacao: Data da transação <br>
- fk_nfc_catao: Código do cartão NFC do usuario <br>

<B>ITINERARIOS</B> <br>
- cod_itinerario: codigo do itinerario <br>
- Locais: Locais pelos quais passa o ônibus <br>

<B>ENDERECOS</B> <br>
- rua: Rua <br>
- numero: Número da residência <br>
- bairro: Bairro <br>
- cidade: Cidade <br>
- CEP: CEP <br>
- estado: Estado <br>
- complemento: Informação complementar a respeito da residência do usuário <br>
- id_endereco: Codgo do endereço <br>

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
        b) Quais as tabelas que conterão mais dados no sistema em densenvolvimento (mínimo 3)
        c) informe quais as 5 principais tabelas do sistema em densenvolvimento.
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


