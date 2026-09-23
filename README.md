# HarvardX-CS50W
CS50's Web Programming with Python and JavaScript

# 🛍️ CS50W - Project 2: Commerce

![CS50 Status](https://img.shields.io/badge/CS50W-Passed%20100%25-brightgreen)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)

Este repositório contém a minha solução para o **Project 2 (Commerce)** do curso **CS50’s Web Programming with Python and JavaScript** de Harvard.

O objetivo do projeto foi construir uma aplicação web de leilões e-commerce desenvolvida em Django, permitindo aos usuários criar anúncios de leilão, fazer lances, comentar em itens, gerenciar uma lista de desejos (*watchlist*) e encerrar leilões.

---

## 📌 Páginas e Funcionalidades do Projeto

- **Active Listings Page (`/`)**:
  - Exibe todos os leilões que estão atualmente ativos.
  - Apresenta título, descrição, imagem (caso fornecida) e o preço atual (lance mais alto ou preço inicial) de cada item.

- **Listing Page (`/auction/<int:auction_id>`)**:
  - Exibe detalhes completos de um anúncio específico.
  - **Watchlist**: Permite que usuários autenticados adicionem ou removam o item da sua lista de desejos.
  - **Bids**: Permite fazer lances em tempo real. Inclui validação para garantir que o valor seja superior a 0 e estritamente maior que o lance atual (ou maior/igual ao preço inicial).
  - **Close Auction**: O criador do leilão tem a opção de encerrá-lo, declarando o usuário com o maior lance como o vencedor final.
  - **Comments**: Seção interativa onde usuários logados podem adicionar comentários ao anúncio.

- **Create Listing (`/create/`)**:
  - Formulário para criação de novos leilões informando título, descrição, lance inicial, categoria e URL de imagem opcional.

- **Watchlist Page (`/watchlist/`)**:
  - Exibe exclusivamente os leilões que o usuário logado marcou e salvou na sua lista de desejos.

- **Categories (`/categories/`)**:
  - Lista todas as categorias existentes que possuem leilões abertos (`closed == False` ou `None`).
  - Ao selecionar uma categoria, redireciona para uma lista filtrada contendo apenas os anúncios ativos vinculados a ela.

- **Django Admin Interface (`/admin`)**:
  - Modelos devidamente registrados para permitir que administradores visualizem, editem e removam anúncios, lances, comentários e dados de usuários diretamente pelo painel do Django.

---

## 🎨 Design e Estilização

- **Layout Limpo & Responsivo**: Estrutura desenvolvida com auxílio de CSS e Bootstrap para garantir boa navegação em diferentes telas.
- **Feedback ao Usuário**: Tratamento de exceções e mensagens de erro amigáveis para lances inválidos ou campos preenchidos incorretamente.
- **Renderização Dinâmica**: Integração fluida entre os modelos do banco de dados (ORMs do Django) e as regras do Django Template Language.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem principal para desenvolvimento da lógica do sistema.
- **Django**: Framework web utilizado para roteamento, gestão de ORM, autenticação de usuários e controle das requisições.
- **SQLite3**: Banco de dados relacional nativo do Django para persistência de anúncios, lances, comentários e watchlists.
- **HTML5, CSS3 & Bootstrap**: Estruturação semântica e estilização dos componentes da interface.
- **Git & GitHub**: Controle de versão e hospedagem do código-fonte.
- 
