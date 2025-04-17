# 📊 Gerador de Boletim Escolar com Python e Excel

Este projeto foi desenvolvido como prática de lógica de programação e manipulação de planilhas com Python.  
A proposta é automatizar o processo de cálculo de médias escolares e determinar a situação dos alunos (Aprovado ou Reprovado) com base nas notas bimestrais.

---

## 🧠 Objetivos do Projeto

- Ler um arquivo Excel com nomes e notas de alunos
- Calcular a média final de cada aluno
- Verificar a situação (Aprovado ou Reprovado) com base na média
- Gerar um novo arquivo Excel com as colunas `Média` e `Situação`

---

## 🛠 Tecnologias utilizadas

- Python 3
- Pandas
- Openpyxl
- Excel (.xlsx)

---

## 📁 Estrutura esperada do arquivo de entrada

Nome do arquivo: `notas_alunos_exemplo.xlsx`

| Nome         | Nota1 | Nota2 | Nota3 | Nota4 |
|--------------|-------|-------|-------|-------|
| Ana Oliveira | 7.5   | 8.0   | 6.0   | 9.0   |
| João Pedro   | 5.0   | 4.5   | 6.0   | 5.5   |
| Lucas Costa  | 9.0   | 8.5   | 9.0   | 9.5   |

> As colunas devem manter os nomes exatos para que o código funcione corretamente.

---

## 💻 Como executar

1. Instale os pacotes necessários:

```bash
pip install pandas openpyxl
