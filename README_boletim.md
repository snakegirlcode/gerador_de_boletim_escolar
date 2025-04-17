
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
```

2. Execute o script no terminal:

```bash
python boletim.py
```

3. O programa irá gerar o arquivo `boletim_final.xlsx` com os resultados.

---

## 📝 Explicações importantes

### 📌 Cálculo da média:

```python
tabela["Média"] = tabela[["Nota1", "Nota2", "Nota3", "Nota4"]].mean(axis=1)
```

Essa linha calcula a média das quatro notas de cada aluno.

### 📌 Situação do aluno:

```python
tabela["Situação"] = tabela["Média"].apply(lambda x: "Aprovado" if x >= 6 else "Reprovado")
```

Usamos `.apply()` com `lambda` para classificar automaticamente a situação com base na média.  
Se preferir uma versão alternativa com `for`, veja abaixo:

```python
situacoes = []

for media in tabela["Média"]:
    if media >= 6:
        situacoes.append("Aprovado")
    else:
        situacoes.append("Reprovado")

tabela["Situação"] = situacoes
```

---

## 📎 Arquivo de exemplo

Este repositório inclui o arquivo `notas_alunos_exemplo.xlsx` para testes e demonstrações.

---

## 👩‍💻 Sobre mim

Desenvolvido por **Thaís Campos**  
Professora de Matemática em transição para a área de tecnologia.  
Apaixonada por lógica, automação, educação digital e Python 🐍💻

🔗 GitHub: [github.com/snakegirlcode](https://github.com/snakegirlcode)  
🔗 LinkedIn: [linkedin.com/in/thais-campos-437462170](https://www.linkedin.com/in/thais-campos-437462170)
