# API Sillicon Store

Essa é uma api feita para uma loja de eletrônicos, como celulares, placas de vídeo, etc.
Fiz ela procurando aprender mais sobre python e sobre a construção de apis.


# Certique-se de ter:
*** python3 ***
*** pip ***
*** Docker ***

# Como rodar o projeto

### Primeiramente, será necessário subir o banco de dados usando o docker

*** cd db_sillicon && docker compose up -d ***

#### Caso precise derrubar o banco de dados, execute o seguinte comando

*** cd db_sillicon && docker compose down ***

Feito isso, basta rodar a api.

### Para rodar a api, primeiro execute o comando para instalar as dependências necessárias:

*** pip install -r requirements.txt ***

Após isso, na pasta raiz do projeto, execute o seguinte comando

*** python3 api/main.py ***


# Senhas de acesso as contas do banco de dados

## Conta de Administrador da loja

Email: admin@silliconstore.com.br
Senha: AdminSillicon-2024