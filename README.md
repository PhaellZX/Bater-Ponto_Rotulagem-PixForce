# Registro de Trabalho da Rotulagem - PIX FORCE

Bem-vindo ao projeto "Registro de Trabalho da Rotulagem - PIX FORCE". Este projeto é uma aplicação simples em
Python para registrar o ponto de entrada e saída dos usuários em diferentes projetos. A aplicação também criptografa
os registros e oferece a funcionalidade de descriptografar esses dados.

![image](https://github.com/PhaellZX/Bater-Ponto_Rotulagem-PixForce/assets/48337836/a34e0e0a-9895-4f57-a285-16d6f419b4a8)

## Funcionalidades

1 - Registro de Entrada e Saída: Registra a hora de entrada e saída do usuário.

2 - Interface amigável: para interação com o usuário.

3 - Indicador de Status: Um pequeno quadrado que muda de cor (vermelho para verde) para indicar o status de entrada/saída.

## Requisitos

- Python 3.7+
- Bibliotecas Python: Pillow, cryptography, tkinter

## Instalação

1 - Clone este repositório:
```properties
  git clone https://github.com/SeuUsuario/RegistroDeTrabalhoPIXFORCE.git
```
2 - Navegue até o diretório do projeto:
```properties
 cd RegistroDeTrabalhoPIXFORCE
```
3 - Crie um ambiente virtual (opcional, mas recomendado):
```properties
 python -m venv venv
```
4 - Ative o ambiente virtual:
- No Windows
```properties
 venv\Scripts\activate
```
- No MacOS/Linux
```properties
 source venv/bin/activate
```
5 - Instale as dependências:
```properties
pip install -r requirements.txt
```
## Uso
## Executar a Aplicação
1 - Navegue até o diretório do projeto.

2 - Execute o script principal:
```properties
python RotulagemBaterPonto.py
```

## Interface Gráfica

 - Nome do Projeto: Insira o nome do projeto no qual você está trabalhando.
 - Bater Ponto!: Clique no botão para registrar a entrada ou saída.
 - Indicador de Status: Um quadrado que muda de cor:
 - Vermelho: Nenhuma entrada registrada ou saída registrada.
 - Verde: Entrada registrada.

