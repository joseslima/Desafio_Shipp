# Teste para para estágio na Shipp

A avaliação é composta por três testes simples que serão utilizados para avaliar a capacidade da pessoa de entender e resolver problemas. Os desafios "Índice remissivo" e "Validação de dados cadastrais" devem ser feitos em PYTHON e o desafio da "Piscina de Coisas Comportamentais" deve ser feito em javascript, css e html.

# Índice remissivo

O sistema de índice remissivo deve ter como entrada um arquivo "palavras.txt" e como saída o número de ocorrências de cada palavra dentro do arquivo.

Exemplo:
"Tema genérico é aquele que descreverá os fatos de uma maneira geral, sem focalizar e dar maior importância a A ou B."


| Palavra| Quantidade
|---| ---|
| e | 2|
| a| 2|
| tema | 1|
| generico | 1|
| ... | ...|

# Validação de dados cadastrais

1. Dado uma lista de clientes e de cartões o sistema deve validar se os dados validos.

2. Os dados que devem ser verificados são :

  - CPF (Verificar se o CPF do usuário e válido, implementar um validador de cpf). Regras de validação de cpf (http://www.macoratti.net/alg_cpf.htm)
  - Verificar se existem celulares duplicados na lista de cadastro.
  - Verificar se existem emails duplicados na lista de cadastro.
  - Número do Cartão (Verificar se o número do cartão é válido, o sistema só aceita VISA, MASTER, ELO, AMEX). 
     |Cartão|Prefixo|Tamanho|cvc
     |MASTERCARD|51-55|16|3|
     |VISA|4||13 ou 16|3|
     |AMEX|34 ou 37|15|4|
     |ELO|636368 ou 636369 ou 438935 ou 504175 ou 451416 ou 636297 ou 5067 ou 4576 ou 4011 ou 506699|16|3|
  - Validar o prazo de validade dos cartões.
    
A entrada do sistema é uma lista "clientes.csv" e "cartoes.txt" com os campos separados por ponto e virgula.
A saida devera ser: 
 1- Lista de clientes validos. Deve se levar em conta a primeira ocorrencia do cliente caso ele esteja duplicado.
 2- Lista de cartões validos. Os cartões que pertencem a clientes que foram excluidos por duplicidade devem ser atualizados com o novo id de cliente caso exista caso contrario deverar ser excluido.

## Piscina de Coisas Comportamentais

Verificar a pasta desafio_front_shipp no repositório, dentro dela esta contido o desafio.

## Avaliação

Os programas serão avaliados levando em conta os seguintes critérios:

| Critério|
|---|
| Legibilidade do código | 
| Resolução do problema| 
| Tratamento de erros| 
| Tempo de execução| 

## Entregas 

Os códigos devem ser enviados em formato zip, separados por pastas. Cada pasta deve conter o nome do desafio correspondente. Email: pedro.lecchi@shipp.delivery, assunto DESAFIO SHIPP.

