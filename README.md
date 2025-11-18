🏦 Sistema Bancário Orientado a Objetos (POO)

📜 Descrição do Projeto

Este projeto foi desenvolvido durante o Terceiro Semestre do curso de Análise e Desenvolvimento de Sistemas. O objetivo é reconstruir e refatorar um projeto de sistema bancário simples feito no semestre anterior, aplicando conceitos avançados de Programação Orientada a Objetos (POO), padrões de design estrutural, e um tratamento robusto de Exceções.

O foco principal é na correta modelagem da hierarquia de classes, relacionamentos (Agregação, Composição, Herança) e Injeção de Dependência (DI).

🛠️ Estrutura e Tecnologias

O projeto é modelado em UML e implementado em Python, utilizando uma estrutura de pacotes modular.

Estrutura de Pastas

A organização segue o princípio de coesão, agrupando classes por responsabilidade:

banco_system/ ├── core/ # Classes estruturais (Bank, Branch) ├── client/ # Hierarquia de Clientes (Client, PhysicalClient, CompanyClient) ├── account/ # Hierarquia de Contas (Account, CurrentAccount, SavingsAccount) │ └── interfaces/ # Mixins/Interfaces (Authenticate, Tax, Earning) └── utils/ └── exceptions/ # Todas as classes de Exceção personalizadas

Principais Tecnologias

Linguagem: Python

Modelagem: Diagrama de Classes UML

Conceitos: Orientação a Objetos (POO), Herança, Polimorfismo.

🏗️ Design e Arquitetura

O projeto utiliza uma arquitetura baseada em Herança e Injeção de Dependência para garantir flexibilidade e manutenibilidade.

    Hierarquia de Classes

Módulo Classes Abstratas (ABC) Subclasses / Implementações Relacionamento Chave Clientes Client PhysicalClient, CompanyClient Herança Contas Account, Authenticate CurrentAccount, SavingsAccount Herança e Mixins (Implementação de Comportamento)

    Padrões Aplicados

    Herança (Generalização): Usada extensivamente para clientes e contas para herdar atributos e métodos comuns, mas permitir regras específicas (ex: Taxas vs. Rendimentos).

    Agregação/Composição: Bank é composto por Branch, e Branch agrega Account e Client.

    Injeção de Dependência (DI): As lógicas de Tax e Earning são injetadas nas classes de conta correspondentes, garantindo baixo acoplamento e alta testabilidade.

    Tratamento de Erros (Exceptions)

Foram implementadas classes de exceção personalizadas para lidar de forma clara com falhas específicas do sistema bancário:

InsufficientFundsError (Saldo insuficiente)

InvalidAccountError (Conta inexistente)

AuthenticationFailedError (Falha na autenticação)

👤 Autor FernandoGomesK
