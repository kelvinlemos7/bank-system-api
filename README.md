# 🏦 Bank System API

Uma API REST estruturada para simulação de operações bancárias, com foco em boas práticas de arquitetura backend.
> Projeto focado em **boas práticas**, **organização**, **clareza de regras de negócio** e **evolução futura**.

---

## 🚀 Funcionalidades

### 👤 Usuários

* Criar usuário
* Listar usuários

### 💳 Contas

* Criar conta bancária
* Listar contas

### 💸 Transações

* Depósito
* Saque
* Transferência entre contas
* Validações de saldo
* Validação de conta de destino

---

## 🧱 Arquitetura do Projeto

O projeto segue uma arquitetura em camadas bem definida:

```
src/
├── controllers/      # Camada HTTP (orquestra requests e responses)
├── services/         # Regras de negócio
├── repositories/     # Acesso ao banco de dados
├── models/           # Models SQLAlchemy
├── schemas/          # Schemas Pydantic
├── routes/           # Definição das rotas
├── utils/            # Enums, erros e validações
├── database.py       # Conexão com o banco
└── app.py            # Inicialização da aplicação
```

### 🔁 Fluxo de uma requisição

```
Route → Controller → Service → Repository → Database
```

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**
* **FastAPI**
* **SQLAlchemy**
* **Pydantic**
* **MySQL**
* **Uvicorn**

---

## ▶️ Como Rodar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone <url-do-repositorio>
cd bank-system
```

### 2️⃣ Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Rode a aplicação

```bash
uvicorn src.app:app --reload
```
ou

```bash
$env:PYTHONPATH = "src"; uvicorn src.app:app --reload
```

### 5️⃣ Acesse a documentação

* Swagger UI: 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* OpenAPI JSON: 👉 [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

## 🚀 Como rodar com Docker
```bash
docker-compose up --build
```

Acesse: http://localhost:8000/docs

---

## 📌 Endpoints Principais

### 👤 Usuários

| Método | Rota         | Descrição      |
| ------ | ------------ | -------------- |
| GET    | `/api/users` | Lista usuários |
| POST   | `/api/users` | Cria usuário   |

### 💳 Contas

| Método | Rota            | Descrição    |
| ------ | --------------- | ------------ |
| GET    | `/api/accounts` | Lista contas |
| POST   | `/api/accounts` | Cria conta   |

### 💸 Transações

| Método | Rota                                                   | Descrição          |
| ------ | ------------------------------------------------------ | ------------------ |
| POST   | `/api/transactions`                                    | Cria transação     |
| GET    | `/api/transactions/accounts/{account_id}/transactions` | Histórico da conta |

---

## 🔐 Regras de Negócio

* ❌ Saques e transferências não podem exceder o saldo
* ❌ Transferências exigem conta de destino válida
* ✅ Depósitos aumentam o saldo
* ✅ Transferências debitam origem e creditam destino

---

## 📈 Próximas Evoluções (Ideias)

* Histórico de transações com paginação
* Extrato com saldo após cada transação
* Autenticação (JWT)
* Testes automatizados
* Banco PostgreSQL

---

## 🧠 Objetivo do Projeto

Este projeto foi criado com foco em **aprendizado real de backend**, organização de código, leitura profissional e preparação para sistemas maiores.

---

## 🧑‍💻 Autor

**Kelvin Kauan** 
