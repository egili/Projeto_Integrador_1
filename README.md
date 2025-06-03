<h1> CRUD Python + MySQL 🐬 </h1>

Projeto integrador do primeiro semestre do curso de Sistemas de Informação da PUCCAMP - 2025

<hr/>

<h2>Sobre o projeto</h2>
O projeto integrador tem como objetivo principal o desenvolvimento de um sistema de monitoramento de sustentabilidade pessoal, utilizando tecnologias como Python, MySQL para armazenar os dados (banco de dados), Git e GitHub para o versionamento do sistema e Trello para o gerenciamento do projeto.

<ul>
  <li>
    Coletar e analisar dados de consumo de água, energia elétrica, geração de resíduos e uso de transporte dos usuários.
  </li>
  <li>
    Desenvolver um algoritmo para calcular e classificar a sustentabilidade pessoal com base nos dados coletados.
  </li>
  <li>
    Implementar um banco de dados para armazenar registros diários de monitoramento de sustentabilidade.
  </li>
  <li>
    Utilizar o terminal para inserção e visualização das informações do sistema.
  </li>
  <li>
    Permitir que os usuários acompanhem suas médias de sustentabilidade ao longo do tempo.

  </li>
</ul>

<hr />

<h4>Modelo do versionamento - Todas as fases do projeto</h4>

```mermaid
gitGraph
    commit id: "Criação do repositório"

    branch release
    branch develop

    checkout develop
    commit id: "Commit em develop"

    branch feature/data
    checkout feature/data
    commit id: "Criada classe para validação de data"
    checkout develop
    merge feature/data 

    branch feature/classificacao_consumo
    checkout feature/classificacao_consumo
    commit id: "Criadas funções para classificação de sustentabilidade"
    checkout develop
    merge feature/classificacao_consumo


    branch feature/geracao_lixo
    checkout feature/geracao_lixo
    commit id: "Criada as funções para validação da inserção de dados relacionados à geração de lixo"
    checkout develop
    merge feature/geracao_lixo 

    branch feature/consumo_agua
    checkout feature/consumo_agua
    commit id: "Criada função para validar consumo de água"
    checkout develop
    merge feature/consumo_agua

    branch feature/consumo_energia
    checkout feature/consumo_energia
    commit id: "Criado arquivo para validação de consumo de energia"
    checkout develop
    merge feature/consumo_energia

    branch feature/uso_transportes
    checkout feature/uso_transportes
    commit id: "Recurso responsável por realizar a validação do uso dos transportes"
    checkout develop
    merge feature/uso_transportes 

    checkout release
    merge develop id: "Desenvolvimento da fase 1 incluído na release branch"

    checkout main
    merge release id: "Release v1.0.0a"

    checkout develop
    commit id: "Início da fase 2"

    branch feature/integracao_bd
    checkout feature/integracao_bd
    commit id: "Integração do código com BD"
    checkout develop
    merge feature/integracao_bd

    branch feature/create
    checkout feature/create
    commit id: "Criação (C) de registro no BD"
    checkout develop
    merge feature/create

    branch feature/read
    checkout feature/read
    commit id: "Visualização (R) de histórico no BD"
    checkout develop
    merge feature/read 

    branch feature/update
    checkout feature/update
    commit id: "Atualização (U) de registro no BD"
    checkout develop
    merge feature/update 

    branch feature/delete
    checkout feature/delete
    commit id: "Deleção (D) de registro no BD"
    checkout develop
    merge feature/delete 

    checkout release
    merge develop id: "Desenvolvimento da fase 2 incluído na release"

    checkout main
    merge release id: "Release v1.0.1a"

    checkout develop
    commit id: "Início da fase 3"

    branch feature/menu
    checkout feature/menu
    commit id: "Desenvolvimento do menu"
    checkout develop
    merge feature/menu 

    branch feature/media
    checkout feature/media
    commit id: "Desenvolvimento do calculo de média de consumo"
    checkout develop
    merge feature/media 

    branch feature/finalizacao
    checkout feature/finalizacao
    commit id: "Finalização do desenvolvimento e testes"
    checkout develop
    merge feature/finalizacao 

    checkout release
    merge develop id: "Inclusão da fase 3 na release branch"

    checkout main
    merge release id: "Release v1.0.2"


```

<hr/>
<h3>Autores:</h3>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/EduardoFagundesSilva">
        <img src="https://avatars.githubusercontent.com/u/154307451?v=4" width="100px;" alt="Eduardo"/><br>
        <sub>
          <b>Eduardo Fagundes</b>
        </sub>
      </a><br>
    </td>
     <td align="center">
      <a href="https://github.com/egili">
        <img src="https://avatars.githubusercontent.com/u/79612701?v=4" width="100px;" alt="egili"/><br>
        <sub>
          <b>Eliseu Gili</b>
        </sub>
      </a>
    </td>
     <td align="center">
      <a href="https://github.com/IgorFurtadoo">
        <img src="https://avatars.githubusercontent.com/u/159090246?v=4" width="100px;" alt="Igor"/><br>
        <sub>
          <b>Igor Furtado</b>
        </sub>
      </a><br>
    </td>
     <td align="center">
      <a href="https://github.com/LnXHero">
        <img src="https://avatars.githubusercontent.com/u/144855270?v=4" width="100px;" alt="Guilherme"/><br>
        <sub>
          <b>Guilherme Heron</b>
        </sub>
      </a><br>
    </td>
    <td align="center">
      <a href="https://github.com/lucasathanasio">
        <img src="https://avatars.githubusercontent.com/u/191253203?v=4" width="100px;" alt="Lucas"/><br>
        <sub>
          <b>Lucas Athanasio</b>
        </sub>
      </a><br>
    </td>
   </table>

<br>
<hr>
<br>

## 🚀 Como rodar a aplicação localmente?

### 📄 1. Configurar variáveis de ambiente

Crie um arquivo `.env` dentro do diretório `source/`, contendo as seguintes variáveis:

```bash
DB_HOST=ip_banco_de_dados\
DB_PORT=porta_banco_de_dados\
DB_USER=usuario_banco_de_dados\
DB_PASSWORD=senha_banco_de_dados 
DB_DATABASE=database_que_sera_utilizada
```


### 🐍 2. Criar e ativar o ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual:

- Linux/macOS:

```bash
source .venv/bin/activate
```

- Windows:

```
.venv\Scripts\activate
``` 

### 📦 3. Instalar dependências

```bash
pip install -r requirements.txt
``` 

### ▶️ 4. Executar a aplicação

```bash
python source/main.py
``` 
