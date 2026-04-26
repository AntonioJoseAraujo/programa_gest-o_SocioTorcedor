# 🏟️ Sócio Torcedor — Ibis Sport Club
 
> Projeto Integrado Multidisciplinar (PIM) — Faculdade UNIP, Ribeirão Preto/SP
 
Sistema de gerenciamento de sócios torcedores desenvolvido em Python, permitindo cadastro, consulta, alteração de planos e simulação de compra de ingressos com descontos exclusivos.
 
---
 
## 📋 Funcionalidades
 
- **Cadastro de sócios** — Registro com nome, sobrenome, idade e plano escolhido
- **Consulta de cadastro** — Acesso aos dados do sócio via ID
- **Alteração de plano** — Upgrade ou downgrade entre os planos disponíveis
- **Cancelamento de cadastro** — Remoção do sócio do sistema
- **Simulação de compra de ingressos** — Cálculo do valor final com desconto conforme o plano
- **Recuperação de ID** — Busca do número de sócio pelo nome e sobrenome
- **Múltiplas formas de pagamento** — PIX, cartão de crédito e boleto bancário
---
 
## 🎟️ Planos Disponíveis
 
| Plano | Mensalidade | Desconto em Ingressos | Desconto em Itens Oficiais | Benefícios Extras |
|---|---|---|---|---|
| 🥉 Bronze | R$ 9,90 | — | — | Pré-venda de ingressos |
| 🥈 Prata | R$ 19,90 | 20% | — | Pré-venda de ingressos |
| 🥇 Ouro | R$ 79,90 | 30% | 20% | Pré-venda de ingressos |
| 💎 Diamante | R$ 99,90 | 50% | 40% | Pré-venda + Sorteios do clube |
 
---
 
## 🗂️ Estrutura do Projeto
 
```
📦 socio-torcedor/
├── pim.py              # Ponto de entrada da aplicação
├── arquivospim.py      # Módulo principal com toda a lógica do sistema
└── socio_torcedor.txt  # Banco de dados local (gerado automaticamente)
```
 
---
 
## ▶️ Como executar
 
**Pré-requisitos:** Python 3.10 ou superior
 
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/socio-torcedor.git
 
# Acesse a pasta do projeto
cd socio-torcedor
 
# Execute o programa
python pim.py
```
 
> O arquivo `socio_torcedor.txt` é criado automaticamente na primeira execução.
 
---
 
## 🧭 Menu Principal
 
```
________________________________________
         PROGRAMA SÓCIO TORCEDOR        
           IBIS SPORT CLUB              
________________________________________
[1] - Mostrar planos disponíveis
[2] - Novo cadastro
[3] - Acessar seu cadastro
[4] - Esqueci meu ID
[0] - Sair
```
 
---
 
## 🛠️ Tecnologias Utilizadas
 
- **Python 3** — Linguagem principal
- **Módulos nativos:** `os`, `time`, `random`, `string`
- **Armazenamento:** arquivo `.txt` como banco de dados local
---
 
## 👨‍💻 Sobre o Projeto
 
Este sistema foi desenvolvido como parte do **Projeto Integrado Multidisciplinar (PIM)** do curso de **Análise e Desenvolvimento de Sistemas** da **Universidade Paulista (UNIP)** — unidade Ribeirão Preto/SP.
 
O objetivo foi aplicar na prática os conceitos de lógica de programação, estrutura de dados, manipulação de arquivos e organização modular de código em Python.
 
---
 
## 📄 Licença
 
Este projeto é de uso acadêmico.
