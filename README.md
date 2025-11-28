🏦 Banco Beto API

    Versão: 2.0 (FastAPI Migration)

    Status: Em Desenvolvimento 🚧

📖 Sobre o Projeto

Este projeto é uma evolução arquitetural de um sistema bancário acadêmico desenvolvido originalmente em Python puro (CLI). O objetivo desta nova versão é transformar as regras de negócio de Orientação a Objetos em uma API RESTful moderna, escalável e conectada a um banco de dados real.

O sistema permite o gerenciamento completo de um banco digital, incluindo agências, clientes (Pessoa Física e Jurídica), contas bancárias e autenticação segura.

🚀 Tecnologias Utilizadas

    Linguagem: Python 3.10+

    Framework Web: FastAPI (Alta performance e validação automática)

    Banco de Dados: MySQL 8.0

    ORM: SQLAlchemy (Mapeamento Objeto-Relacional)

    Validação de Dados: Pydantic (Schemas e validação de tipos/formatos)

    Segurança: Passlib + Bcrypt (Hashing de senhas)

    Servidor: Uvicorn (ASGI)

✨ Funcionalidades Implementadas

🏢 Agências (Branches)

    Cadastro de novas agências.

    Validação automática de formato de telefone (Regex).

    Listagem de agências existentes.

👥 Clientes (Clients)

    Cadastro de clientes com suporte a Single Table Inheritance (Tabela única para PF e PJ).

    Validação de regras de negócio:

        PF: Exige CPF.

        PJ: Exige CNPJ.

    Segurança: As senhas dos clientes são criptografadas (Hash) antes de serem salvas no banco.

    Associação automática com uma Agência.

💳 Contas (Accounts)

    Abertura de contas (Corrente ou Poupança).

    Herança de Agência: A conta é vinculada automaticamente à agência do cliente titular.

    Verificação de duplicidade: Impede que o mesmo cliente tenha duas contas do mesmo tipo.

🔐 Autenticação & Segurança

    Rota de Login (/auth/login).

    Verificação de credenciais (CPF/CNPJ + Senha) comparando com o hash no banco.

    Tratamento Global de Erros: Sistema centralizado para capturar exceções de negócio (ex: ClientDoesntExistException) e retornar JSONs de erro amigáveis (HTTP 400, 404, 409).

📂 Estrutura do Projeto

O projeto segue uma arquitetura limpa e modular:
Plaintext

banco_system/
├── config/             # Configurações de Banco de Dados e Dependências
├── models/             # Classes SQLAlchemy (Tabelas do Banco)
├── schemas/            # Classes Pydantic (Validação de Entrada/Saída)
├── routes/             # Endpoints da API (Controllers)
├── utils/              # Ferramentas auxiliares
│   ├── exceptions/     # Exceções Personalizadas e Handlers
│   ├── verifications/  # Lógica de validação (ex: Telefone)
│   └── security.py     # Lógica de Hashing de Senha
└── main.py             # Ponto de entrada da aplicação

⚙️ Como Rodar o Projeto

Pré-requisitos

    Python 3.x instalado.

    MySQL Server rodando.

    Um banco de dados vazio criado (ex: banco_beto_db).

Passo a Passo

    Clone o repositório:
    Bash

git clone https://github.com/seu-usuario/banco-beto-api.git
cd banco-beto-api

Instale as dependências:
Bash

pip install fastapi uvicorn sqlalchemy pymysql pydantic passlib[bcrypt] cryptography

Configure o Banco de Dados: Edite o arquivo config/database.py com suas credenciais do MySQL:
Python

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://SEU_USUARIO:SUA_SENHA@localhost/banco_beto_db"

Execute o Servidor:
Bash

    py -m uvicorn main:app --reload

    

        O FastAPI gera automaticamente uma interface interativa (Swagger UI) para você testar todas as rotas.

👤 Autor

Fernando Gomes

    Desenvolvedor Backend em formação

    Estudante de Análise e Desenvolvimento de Sistemas
