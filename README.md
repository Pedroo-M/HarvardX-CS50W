# HarvardX-CS50W
CS50's Web Programming with Python and JavaScript

# 🔍 CS50W - Project 0: Search

![CS50 Status](https://img.shields.io/badge/CS50W-Passed%20100%25-brightgreen)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)

Este repositório contém a minha solução para o **Project 0 (Search)** do curso **CS50’s Web Programming with Python and JavaScript** de Harvard.

O objetivo do projeto foi construir uma interface web que replica o comportamento e o visual de três páginas de busca do Google: a busca principal, a busca de imagens e a busca avançada.

---

## 📌 Páginas do Projeto

- **Google Search (`index.html`)**:
  - Permite realizar buscas padrão no Google.
  - Inclui os botões *"Google Search"* e *"I'm Feeling Lucky"*.
  - O botão *"I'm Feeling Lucky"* redireciona o usuário diretamente para o primeiro resultado relevante, simulando o efeito de redirecionamento do Google.

- **Google Image Search (`image.html`)**:
  - Interface focada na pesquisa de imagens.
  - Envia os parâmetros corretos para a aba de imagens do Google (`tbm=isch`).

- **Google Advanced Search (`advanced.html`)**:
  - Permite filtrar buscas por:
    - Todas as palavras (`as_q`)
    - Expressão exata (`as_epq`)
    - Qualquer uma das palavras (`as_oq`)
    - Nenhuma das palavras (`as_eq`)
  - Layout alinhado à esquerda com o botão de busca estilizado em azul com texto branco, seguindo o padrão do Google.

---

## 🎨 Design e Estilização

- **Fidelidade Visual**: As páginas foram projetadas para imitar as margens, fontes, cores e campos de busca originais do Google.
- **Navegação**: Links no canto superior direito permitem alternar facilmente entre a Busca Normal, Imagens e Busca Avançada.
- **CSS Modular**: Estilização limpa mantida em arquivo separado (`styles.css`), focando em alinhamentos nativos (Flexbox/CSS Grid).

---

## 🛠️ Tecnologias Utilizadas

- **HTML5**: Estruturação semântica dos formulários e inputs.
- **CSS3**: Estilização, regras de layout e alinhamento.

---
