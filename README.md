# API Futbet (Trabalho FBD)

Uma API RESTful desenvolvida com FastAPI para gerenciar apostas (Futbet), utilizando PostgreSQL como banco de dados.

## Tecnologias Utilizadas

- **Python 3**
- **FastAPI**: Framework web moderno e rápido para construção de APIs.
- **Pydantic**: Validação de dados e serialização.
- **PostgreSQL**: Banco de dados relacional.
- **psycopg2**: Adaptador de banco de dados PostgreSQL para Python.

## Pré-requisitos

Certifique-se de ter o PostgreSQL rodando localmente. O banco de dados deve estar criado de acordo com as configurações no arquivo `db.py`:

- **Database**: `nome-do-banco`
- **User**: `nome-do-usuario`
- **Password**: `senha-do-banco`
- **Host**: `host-do-banco`

Além disso, é necessário ter a tabela `aposta` criada no banco de dados, com as colunas adequadas (`id_aposta`, `valor`, `data`, `cpf_usuario`, `id_bolao`).

Para instalar as dependências do projeto em Python, você pode usar:

```bash
pip install fastapi uvicorn psycopg2 pydantic
```

## Como Executar

Para iniciar o servidor de desenvolvimento, rode o seguinte comando na raiz do projeto:

```bash
python -m uvicorn main:app --reload
```

A API estará disponível em: `http://localhost:8000`

O FastAPI gera a documentação automática interativa (Swagger UI) que pode ser acessada em: `http://localhost:8000/docs`

## Endpoints

Todas as rotas possuem o prefixo `/api`.

### Apostas

- **GET `/api/apostas`**
  - Retorna uma lista com todas as apostas cadastradas.

- **GET `/api/apostas/{id_aposta}`**
  - Retorna os dados de uma aposta específica baseada em seu ID.

- **POST `/api/apostas`**
  - Cria uma nova aposta.
  - **Exemplo de Body (JSON):**
    ```json
    {
      "valor": 50,
      "data": "2024-05-10",
      "cpf_usuario": "12345678900",
      "id_bolao": 1
    }
    ```

- **PATCH `/api/apostas/{id_aposta}`**
  - Atualiza parcialmente uma aposta existente (permitido alterar `valor` e/se `data`).
  - **Exemplo de Body (JSON):**
    ```json
    {
      "valor": 75
    }
    ```

- **DELETE `/api/apostas/{id_aposta}`**
  - Remove uma aposta específica do banco de dados pelo seu ID.

## Estrutura do Projeto

- `main.py`: Inicializa o app FastAPI e inclui as rotas (routers).
- `db.py`: Configuração de conexão com o banco de dados via `psycopg2`.
- `models.py`: Modelos Pydantic para validação das requisições e respostas.
- `crud_aposta.py`: Funções responsáveis pela lógica de negócio e queries SQL (operações CRUD) relacionadas às apostas.
