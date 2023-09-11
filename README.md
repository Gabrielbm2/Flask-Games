# Flask Game Catalog

Este projeto apresenta uma aplicação web simples desenvolvida em Python usando o framework Flask. A Flask Game Catalog permite aos usuários criar uma lista de jogos, autenticar-se e adicionar novos jogos ao catálogo.

## Funcionalidades

* Cadastrar novos jogos com informações como nome, categoria e console.

* Autenticar usuários para gerenciar sua própria lista de jogos.

* Listar jogos cadastrados.

## Arquitetura

A arquitetura do projeto segue uma abordagem modular, onde cada pacote é responsável por uma funcionalidade específica, o que ajuda a manter o código organizado e facilita a manutenção.

## Rotas da API

* `POST /api/games`: Cadastrar um novo jogo.

* `GET /api/games`: Listar todos os jogos cadastrados.

* `GET /api/games/:id`: Buscar informações de um jogo pelo ID.

* `PUT /api/games/:id`: Atualizar as informações de um jogo.

* `DELETE /api/games/:id`: Excluir um jogo pelo ID.

## Autenticação de Usuário

A autenticação é necessária para adicionar, atualizar ou excluir jogos. Use a rota `POST /login` para autenticar-se. O token de autenticação é enviado no cabeçalho `Authorization`.

## Documentação

A documentação detalhada da API pode ser encontrada através de um Swagger UI. Para acessá-la, acesse [http://localhost:5000/swagger](http://localhost:5000/swagger) após iniciar o aplicativo.

## Testes

A API permite criar novos jogos especificando seu nome, categoria e console, além de ver todos os jogos cadastrados. Também é possível realizar a autenticação de usuário para acessar as operações protegidas.

## Deploy

O projeto pode ser implantado em qualquer servidor web compatível com Flask. Para desenvolvimento local, basta executar `python app.py` e acessar o aplicativo em `http://localhost:5000`.

## Melhorias Possíveis

* Adição de validações de entrada para evitar erros de usuário.

* Implementação de um sistema de banco de dados para armazenar jogos e informações de usuário de forma persistente.

* Adição de um frontend para melhor interação do usuário com a API.

* Melhorias na documentação, incluindo exemplos de requisições e respostas esperadas.

## Considerações Finais

Este projeto foi desenvolvido para demonstrar habilidades de programação em Flask. Dúvidas ou sugestões podem ser encaminhadas por email para [seu-email@example.com](mailto:seu-email@example.com).
