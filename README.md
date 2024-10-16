# Projeto TODO - Gerenciador de Tarefas

Este é um projeto de **Gerenciador de Tarefas** simples, desenvolvido com o framework Django. O sistema permite criar, editar, visualizar e deletar tarefas, além de filtrar e pesquisar tarefas com atualizações dinâmicas usando **AJAX**. O projeto também possui modais para facilitar a criação e edição de tarefas, e utiliza Bootstrap para responsividade e estilização.

## Funcionalidades Principais

- CRUD de tarefas (Criar, Ler, Atualizar, Deletar).
- Pesquisa e filtro de tarefas.
- Interface moderna e responsiva utilizando Bootstrap.
- Funcionalidade de AJAX para operações dinâmicas sem recarregamento de página.
- Modais para criar e editar tarefas.
- Suporte para múltiplos status de tarefas (e.g., "Finalizado" com estilização diferenciada).

---

## Tecnologias Utilizadas

### Backend:
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

- **Django**: Framework web usado para o desenvolvimento do backend.
- **Python**: Linguagem de programação usada para construir toda a lógica de negócios.

### Frontend:
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![jQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)

- **Bootstrap 5**: Framework CSS usado para a estilização e responsividade do projeto.
- **jQuery/AJAX**: Biblioteca JavaScript para manipulação do DOM e fazer requisições AJAX.

### Banco de Dados:
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

- **SQLite**: Banco de dados relacional embutido.

---

## Requisitos

- **Python 3.8+**
- **Django 4.0+**
- **pip** (para instalar dependências)

---

## Configuração do Projeto

### Passos para rodar o projeto localmente:

### 1. Clonar o Projeto

Primeiramente, clone o repositório:

```bash
git clone https://github.com/jotap1101/django-to-do-list-with-ajax.git
cd seu-repositorio

```

### 2. Criar Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

### 3. Ativar Ambiente Virtual

Ative o ambiente virtual:

- No Windows:

```bash
venv\Scripts\activate
```

- No Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Instalar Dependências

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### 5. Gerar a secret key

Gere uma chave secreta para o projeto:

- Entre na pasta 'scripts' e execute o script 'generate_secret_key.py':

```bash
cd scripts
python generate_secret_key.py
```

- Copie a chave gerada.

### 6. Configurar Variáveis de Ambiente

Crie um arquivo `.env` de acordo com o arquivo `.env.example` e adicione a chave secreta gerada:

```env
SECRET_KEY = 'sua_secret_key'
```

### 7. Criar as migrações

Crie as migrações do banco de dados:

```bash
python manage.py makemigrations
```

### 8. Aplicar Migrações

Aplique as migrações no banco de dados:

```bash
python manage.py migrate
```

### 9. Criar Superusuário

Crie um superusuário para acessar o painel de administração:

```bash
python manage.py createsuperuser
```

### 10. Rodar o Servidor

Por fim, rode o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse o projeto em `http://127.0.0.1:8000/`

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

## Contato

- **Autor:** João Pedro Alves

- **LinkedIn:** [João Pedro Alves](https://www.linkedin.com/in/jotap1101/)

- **GitHub:** [jotap1101](https://www.github.com/jotap1101/)