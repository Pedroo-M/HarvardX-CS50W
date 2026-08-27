# HarvardX-CS50W
CS50's Web Programming with Python and JavaScript

# 📚 CS50W - Project 1: Wiki

![CS50 Status](https://img.shields.io/badge/CS50W-Passed%20100%25-brightgreen)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=flat&logo=markdown&logoColor=white)

Este repositório contém a minha solução para o **Project 1 (Wiki)** do curso **CS50’s Web Programming with Python and JavaScript** de Harvard.

O objetivo do projeto foi construir uma aplicação web estilo Wikipedia desenvolvida em Django, permitindo criar, editar, visualizar e pesquisar artigos armazenados em formato Markdown, renderizando-os dinamicamente para HTML.

---

## 📌 Páginas e Funcionalidades do Projeto

- **Entry Page (`/wiki/TITLE`)**:
  - Exibe o conteúdo formatado do artigo solicitado.
  - Converte o texto escrito em Markdown para HTML.
  - Exibe uma mensagem de erro personalizada caso a entrada não exista.

- **Index Page (`/`)**:
  - Lista todas as páginas enciclopédicas cadastradas.
  - Permite clicar em qualquer item para ser direcionado diretamente à entrada correspondente.

- **Search (`/search/`)**:
  - Se a consulta for idêntica ao nome de uma entrada, o usuário é direcionado diretamente para ela.
  - Se for uma substring, exibe uma lista de resultados que contêm o termo pesquisado.

- **New Page (`/create/`)**:
  - Formulário para criar um novo artigo com campos de título e área de texto em Markdown.
  - Valida se o artigo já existe para evitar duplicações de conteúdo.

- **Edit Page (`/edit/TITLE`)**:
  - Permite editar o conteúdo Markdown de qualquer entrada existente.
  - Pré-carrega o conteúdo atual da página na área de edição.

- **Random Page (`/random/`)**:
  - Seleciona e redireciona o usuário para uma página aleatória da enciclopédia.

- **Delete Page (`/delete/`)**:
  - Funcionalidade adicional para exclusão de artigos da base de dados com feedback visual do estado da ação.

---

## 🎨 Design e Estilização

- **Layout Limpo**: Menu lateral fixo (*sidebar*) com navegação simples e direta para as principais rotas da aplicação.
- **Renderização Dinâmica**: Integração fluida entre o processamento do backend (Django) e os templates HTML.
- **CSS Modular**: Estilização mantida em arquivos CSS dedicados para garantir um visual padronizado em todas as páginas.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem principal para desenvolvimento da lógica no backend.
- **Django**: Framework web para roteamento, renderização de templates e controle das requisições.
- **Markdown2 / Markdown**: Biblioteca Python para conversão de sintaxe Markdown em HTML.
- **HTML5 & CSS3**: Estruturação semântica e estilização visual das páginas.
