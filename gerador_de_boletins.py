import pandas as pd

tabela = pd.read_excel("notas_alunos.xlsx")

tabela["Média"] = tabela[["Nota1", "Nota2", "Nota3", "Nota4"]].mean(axis=1)

tabela["Situação"] = tabela["Média"].apply(lambda x: "Aprovado" if x >= 7 else "Reprovado")

tabela.to_excel("boletim_final.xlsx", index=False)

print("✅ Boletim final gerado com sucesso!")