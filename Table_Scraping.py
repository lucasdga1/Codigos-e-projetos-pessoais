# Trazer bibliotecas
import pandas as pd
from bs4 import BeautifulSoup

# Arquivo salvo como html
with open("Filepath.html", "r", encoding="utf-8") as f:
    conteudo = f.read()

# Criação de parser
soup = BeautifulSoup(conteudo, "html.parser")

# Extração de tabelas do html usando pandas
tabelas = pd.read_html(str(soup))

# Exibe a quantidade de tabelas encontradas
print(f"Foram encontradas {len(tabelas)} tabelas")

# Exibe a tabela selecionada
print(tabelas[17])

# Salva a tabela selecionada em CSV
df = tabelas[17]
# Somente as 30 primeiras colunas
df_30 = df.iloc[:, :30]
df_30.to_csv("Tabela_stats.csv", index=False, encoding="utf-8")