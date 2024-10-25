# Projeto de Cadastro de Usuário com Geração de PDF

## Descrição do Projeto

Este projeto é uma aplicação Python que permite o cadastro de usuários e gera um documento PDF com os dados do usuário cadastrado. O sistema foi desenvolvido seguindo os princípios da **Clean Architecture**, proporcionando uma estrutura modular e de fácil manutenção.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
PDF_register/
├── entities/
│   └── user.py
├── use_cases/
│   └── user_registration.py
├── interface_adapters/
│   ├── user_repository.py
│   └── pdf_generator.py
├── frameworks_and_drivers/
│   └── main.py
```

### Pastas e Arquivos

- **entities/**: Contém as definições de entidades do domínio. Neste projeto, inclui o arquivo `user.py`, que define a classe `User`, representando os dados de um usuário.
  
- **use_cases/**: Contém a lógica de negócio da aplicação. O arquivo `user_registration.py` possui a classe `UserRegistration`, responsável por registrar o usuário e gerar o PDF.

- **interface_adapters/**: Implementa as interfaces para interagir com sistemas externos. Contém:
  - `user_repository.py`: Define a classe `UserRepository`, que gerencia a persistência dos dados do usuário no banco de dados.
  - `pdf_generator.py`: Define a classe `PDFGenerator`, que é responsável pela criação do PDF com os dados do usuário.

- **frameworks_and_drivers/**: Contém o ponto de entrada da aplicação, `main.py`, que executa o fluxo principal da aplicação.

## Tecnologias Usadas

1. **Python**: Linguagem de programação utilizada para desenvolver a aplicação. É conhecida pela sua simplicidade e eficiência.

2. **Psycopg2**: Biblioteca para interagir com bancos de dados PostgreSQL. Ela fornece uma interface para executar comandos SQL e gerenciar conexões com o banco.

3. **ReportLab**: Biblioteca para gerar documentos PDF em Python. Permite a criação de PDFs de maneira programática, ideal para gerar relatórios ou documentos a partir de dados.

4. **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional utilizado para armazenar as informações dos usuários. Ele é robusto e amplamente utilizado em aplicações que requerem uma estrutura de dados complexa.

5. **Railway**: Plataforma de deploy que facilita a hospedagem e a gestão de bancos de dados. No projeto, o Railway foi utilizado para provisionar e gerenciar o banco de dados PostgreSQL na nuvem, garantindo que a aplicação pudesse acessar os dados de forma remota e segura.

## Integração com Railway e PostgreSQL

O projeto foi configurado para usar um banco de dados PostgreSQL hospedado no Railway. O acesso ao banco de dados é feito através da classe `DatabaseConnection` no arquivo `user_repository.py`. Aqui está um exemplo de como a conexão é estabelecida:

```python
class DatabaseConnection:
    def __init__(self) :
        self.connection = psycopg2.connect(
            host="junction.proxy.rlwy.net",
            dbname="railway",
            user="postgres",
            password="QLrtaCWqyegozyvpBuPoHxQGwqTkVyNE",
            port="44943"
        )
```

### Detalhes da Conexão

- **Host**: O endereço do servidor onde o banco de dados PostgreSQL está hospedado. Neste caso, é fornecido pelo Railway.
  
- **dbname**: Nome do banco de dados que foi criado na plataforma Railway.

- **user**: Nome do usuário com permissão para acessar o banco de dados.

- **password**: Senha do usuário para autenticação.

- **port**: Porta utilizada para estabelecer a conexão com o banco de dados.

### Criação da Tabela de Usuários

Um exemplo de código SQL para criar a tabela de usuários no PostgreSQL seria:

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT NOT NULL
);
```

## Funcionalidades Implementadas

1. **Cadastro de Usuário**: O usuário pode fornecer seu nome, email e idade. Essas informações são encapsuladas em um objeto `User`.

2. **Persistência dos Dados**: Os dados do usuário são salvos em um banco de dados (PostgreSQL) utilizando a classe `UserRepository`, que executa as operações de inserção de dados.

3. **Geração de PDF**: Após o cadastro, um documento PDF é gerado com os dados do usuário, utilizando a classe `PDFGenerator`. O PDF contém informações como nome, email e idade, formatadas para apresentação.

## Como Executar o Projeto

Para executar o projeto, siga estas etapas:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seuusuario/PDF_register.git
   ```

2. **Instale as dependências** (se necessário):
   ```bash
   pip install psycopg2 reportlab
   ```

3. **Configure o Banco de Dados**: Ajuste a conexão com o banco de dados no arquivo `user_repository.py`, se necessário.

4. **Execute o Programa**:
   ```bash
   python main.py
   ```

5. **Siga as instruções no console para cadastrar um usuário**.

## Aplicação da Clean Architecture

A Clean Architecture foi aplicada para separar as preocupações do projeto, promovendo a escalabilidade e a manutenção. Aqui estão os princípios utilizados:

1. **Independência de Frameworks**: O código de negócio não depende de bibliotecas ou frameworks externos, permitindo que você troque facilmente a implementação, se necessário.

2. **Separação de Responsabilidades**: Cada camada tem uma responsabilidade específica:
   - **Entidades**: Representam as regras de negócio (classe `User`).
   - **Casos de Uso**: Contêm a lógica do aplicativo (classe `UserRegistration`).
   - **Adaptadores**: Interagem com o mundo externo, como o banco de dados e geração de PDF.

3. **Testabilidade**: A estrutura modular permite que cada parte do sistema seja testada independentemente. Isso é importante para garantir que a lógica de negócios funcione corretamente.

4. **Facilidade de Manutenção**: Com as responsabilidades bem definidas e separadas, qualquer alteração ou adição de funcionalidade pode ser realizada com menor risco de impacto em outras partes do sistema.

## Conclusão

Este projeto é uma demonstração prática de como implementar a Clean Architecture em uma aplicação simples de cadastro de usuários com geração de PDF. A estrutura modular e bem definida facilita a expansão e manutenção do sistema no futuro.

---
