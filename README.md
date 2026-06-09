# Recarga.Agora

## Autor
João Paulo
Curso: Ciência da Computação

---

## Nome do Sistema

Recarga.Agora

## Descrição do Projeto

O Recarga.Agora é uma plataforma web desenvolvida em Django que permite aos usuários cadastrar cartões de transporte público e realizar recargas de forma online.

O objetivo do sistema é facilitar o processo de recarga de cartões de ônibus, reduzindo filas e tornando o serviço mais acessível e prático para os usuários.

---

## Problema que o Sistema Resolve

Muitas pessoas precisam se deslocar até pontos físicos para realizar recargas em seus cartões de transporte.

O sistema busca solucionar esse problema permitindo que o usuário:

* Cadastre seus cartões;
* Consulte o saldo;
* Realize recargas;
* Visualize o histórico de recargas.

---

## Tipos de Usuários

### Usuário Comum

Pode:

* Criar conta;
* Fazer login;
* Cadastrar cartões;
* Visualizar saldo;
* Realizar recargas;
* Consultar histórico de recargas;
* Encerrar sessão (logout).

### Administrador

Pode:

* Acessar o painel administrativo do Django;
* Gerenciar usuários;
* Gerenciar cartões;
* Gerenciar recargas;
* Inserir dados de teste.

---

## Tecnologias Utilizadas

* Python 3.13.1
* Django 6.0.5
* SQLite3
* HTML
* CSS

---

## Instalação do Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/JoaoPaulo-Programador/Projeto-Django.git
```

### 2. Entrar na Pasta

```bash
cd Projeto-Django/Plataforma_Recarga
```

### 3. Criar Ambiente Virtual

Windows:

```bash
python -m venv venv
```

### 4. Ativar Ambiente Virtual

Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 6. Aplicar Migrações

```bash
python manage.py migrate
```

### 7. Criar Superusuário

```bash
python manage.py createsuperuser
```

### 8. Executar Servidor

```bash
python manage.py runserver
```

---

## Acesso ao Sistema

Página inicial:

```text
http://127.0.0.1:8000/
```

Painel administrativo:

```text
http://127.0.0.1:8000/admin/
```

---

## Principais Funcionalidades

### Cadastro de Usuário

Permite criar uma conta no sistema.

### Login

Permite acessar a plataforma utilizando email e senha.

### Cadastro de Cartão

Permite cadastrar cartões de transporte vinculados ao usuário.

### Recarga

Permite realizar recargas em cartões cadastrados.

### Histórico

Permite visualizar as recargas realizadas.

### Dashboard

Exibe:

* Cartões cadastrados;
* Saldo dos cartões;
* Histórico de recargas.

---

## Dados de Teste

Caso deseje testar rapidamente o sistema, é possível criar usuários diretamente pelo formulário de cadastro disponível na aplicação.

Também é possível cadastrar usuários, cartões e recargas através do painel administrativo do Django.

---

## Estrutura do Projeto

Apps utilizados:

### usuarios

Responsável por:

* Cadastro;
* Login;
* Logout;
* Gerenciamento de usuários.

### cartoes

Responsável por:

* Cadastro de cartões;
* Controle dos cartões do usuário.

### recarga

Responsável por:

* Dashboard;
* Recargas;
* Histórico de recargas.

### home

Responsável pela página inicial do sistema.

---

## Observações

Este projeto foi desenvolvido como atividade acadêmica da disciplina de Desenvolvimento Web utilizando Django.

Novas funcionalidades poderão ser adicionadas futuramente, como:

* Integração com gateways de pagamento;
* Recuperação de senha;
* Perfil do usuário;
* Edição de cartões;
* Relatórios de utilização.