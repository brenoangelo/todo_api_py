# Todo list api

A API de Todo em Python com SQLAlchemy e SQLite é uma API RESTful que permite a criação, leitura, atualização e exclusão de tarefas em uma lista de afazeres.

Ela utiliza o protocolo HTTP com os métodos GET, POST, PUT e DELETE para manipulação dos dados. Além disso, utiliza JSON para transmitir os dados de e para o servidor, o que a torna fácil de ser integrada em diferentes aplicações.

Com uma arquitetura RESTful, a API permite que os clientes se comuniquem com o servidor de maneira uniforme e padronizada, seguindo os princípios do REST.

## Tecnologias

- Python
- SQLAlchemy
- Postgres
- Marshmallow
- SQLite

## Routes

`/tasks`

### GET

  `/tasks`

  `/tasks/<task_id>`

  ```json
    {
      "id": 1, // Number
      "title": "Titulo legal", // String
      "description": "Descrição bacana", // String
      "completed": true // Boolean
    }
  ```

### POST

`/tasks`

```json
  {
    "title": "String de até 80 caracteres",
    "description": "String de ate 244 caracteres",
  }
```

- Title é obrigatório

### PUT

  `tasks/<task_id>`

  ```json
    {
      "title": "Titulo legal", // String
      "description": "Descrição bacana", // String
      "completed": true // Boolean
    }
  ```

### DELETE

  `tasks/<task_id>`

---
## Rodando o projeto

1. Criando o ambiente virtual:

    ```bash
      python -m venv <nome_do_ambiente>
    ```

2. Acessando o ambiente virtual

    ```bash
      source <nome_do_ambiente>/bin/activate
    ```

3. Instalando as dependências

    ```bash
      pip install -r requirements.txt
    ```

4. Rodando o projeto

    ```bash
      python app.py
    ```
