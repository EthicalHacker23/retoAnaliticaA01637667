import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Abrir y leer los datos
df = pd.read_csv("datos_clientes.csv")

# Histogramas para cada variable
n = df.select_dtypes(include=[np.number]).columns
for j in n:
    plt.figure()
    sns.histplot(data=df, x=j, bins=20, kde=True)
    plt.title(f"Histograma para {j}")
    plt.show()

# Crear boxplots para cada variable
for i in n:
    plt.figure()
    sns.boxplot(data=df, y=i)
    plt.title(f"Boxplot de {i}")
    plt.show()

# Mapa de correlación entre variables
correlation = df[n].corr()
plt.figure()
sns.heatmap(data=correlation, vmin=-1, vmax=1, cmap="coolwarm", annot=True)
plt.title("Mapa de calor (correlación)")
plt.show()
