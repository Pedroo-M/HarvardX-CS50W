# 📚 CS50W - Project 1: Wiki

Uma aplicação web estilo Wikipedia desenvolvida em **Python** com o framework **Django**, como parte dos requisitos do curso **CS50’s Web Programming with Python and JavaScript** da Harvard/edX.

---

## 📌 Sobre o Projeto

O **Wiki** é uma enciclopédia online que permite aos usuários visualizar, pesquisar, criar, editar e excluir artigos. O conteúdo de cada artigo é escrito e armazenado no formato **Markdown** e convertido dinamicamente para HTML no momento da renderização.

---

## ⚙️ Funcionalidades

- **Visualização de Entradas (Entry Page):** Acessar `/wiki/TITULO` exibe a página do artigo correspondente. Caso a entrada não exista, é exibida uma página de erro 404/not found.
- **Página Inicial (Index Page):** Exibe uma lista com hiperlinks para todas as entradas cadastradas no sistema.
- **Busca (Search):**
  - Se a busca for idêntica ao nome de uma entrada existente, o usuário é redirecionado diretamente para ela.
  - Se for uma substring de uma ou mais entradas, exibe uma lista de resultados contendo todas as páginas correspondentes.
- **Criar Nova Página (New Page):** Permite criar novos artigos informando um título e o conteúdo em sintaxe Markdown. Há validação para prevenir a sobrescrita de artigos já existentes.
- **Editar Página (Edit Page):** Permite alterar o conteúdo Markdown de qualquer artigo existente.
- **Página Aleatória (Random Page):** Redireciona o usuário para uma entrada escolhida aleatoriamente.
- **Excluir Página (Delete Page):** Permite a remoção permanente de um artigo da base de dados/sistema de arquivos.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Django** (Framework Web Backend)
- **Markdown2 / Markdown** (Conversão de Markdown para HTML)
- **HTML5 & CSS3**

---

## 📁 Estrutura de Arquivos

```text
wiki/
├── entries/              # Arquivos .md com os artigos (CSS.md, Python.md, Django.md, etc.)
├── encyclopedia/         # Aplicação principal Django
│   ├── templates/        # Templates HTML (index, entry, create, edit, delete, etc.)
│   ├── urls.py           # Mapeamento de rotas e URLs
│   ├── views.py          # Lógica das requisições e respostas
│   └── util.py           # Funções auxiliares para manipular arquivos Markdown
├── manage.py             # CLI do Django
└── requirements.txt      # Dependências do projeto
