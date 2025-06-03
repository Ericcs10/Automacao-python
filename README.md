# 🛠️ Automação de Cadastro de Produtos

Este repositório contém um projeto de automação desenvolvido em Python que lê dados de um arquivo de texto (ex: uma tabela de produtos) e utiliza essas informações para **preencher automaticamente um site de cadastro**.

> Embora o foco atual seja o cadastro de produtos, a estrutura do código foi pensada para ser **reutilizável em diversas automações web**, bastando adaptar os seletores e o formato de entrada.

---

## 📌 Funcionalidades

- Leitura de arquivos `.txt` contendo dados estruturados.
- Processamento dos dados para extração dos campos necessários.
- Preenchimento automático de campos em um formulário web.
- Suporte a diferentes formatos e estruturas de entrada com fácil modificação.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Selenium** (para automação de navegador)
- **time, os, sys** (bibliotecas padrão)

---

## 📝 Como Usar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/automacao-produtos.git
cd automacao-produtos
```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. **Execute a automação**

```bash
python src/automacao.py
```
