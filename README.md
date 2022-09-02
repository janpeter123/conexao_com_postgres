# Conexão simples com postgres
O Escopo deste repositório é disponibilizar um script básico de conexão a um banco de dados Postgres SQL instanciado na IBM Cloud. para aumentar a minha produtividade quando houver algum caso de uso de um banco de dados deste tipo.

## Estrutura dos diretórios

```
── acesso_ao_bd.py
└── cert.pem
```

Em `acesso_ao_bd.py` temos um script de acesso ao banco de dados.
Todas as credenciais do script foram apagadas, para utilizar o script basta colocar as credenciais obtidas nas variáveis respectivas.

O Script faz uma conexão ao banco de dados, cria uma tabela, depois lista as tabelas existentes e por último faz um commit.

`cert.pem` é o certificado de acesso ao banco de dados. Ele pode ser encontrado na página da sua instância na IBM Cloud.


#### 🚨 Aviso: A maneira mais segura de colocar as credenciais no script é por meio de variáveis de ambiente.

## Bibliotecas utilizadas
 - Psycopg2
 
