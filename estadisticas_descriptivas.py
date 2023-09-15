import pandas as pd


# Funcion para separar vista en terminal
def enter():
    print("\n")


# Abrir y leer archivo
df = pd.read_csv("datos_clientes.csv")


""" ----- Variables métricas (media, rango (min, max), desviacion estandar, etc) ----- """

# Media de puntos por rangos de edades en mujeres
f1 = df[(df['Edad'] > 20) & (df['Edad'] < 30) & (df['Genero'] == "Mujer")]  # Filtro cliente mujer, 20-30 años
f2 = df[(df['Edad'] > 30) & (df['Edad'] < 40) & (df['Genero'] == "Mujer")]  # Filtro cliente mujer, 30-40 años
f3 = df[(df['Edad'] > 40) & (df['Edad'] < 50) & (df['Genero'] == "Mujer")]  # Filtro cliente mujer, 40-50 años
print("Media de puntos por rango de edad en mujeres:\nEdad\tPuntos"
      f"\n20-30\t {round(f1['Puntos en compras (1-100)'].mean(), 2)}"
      f"\n30-40\t {round(f2['Puntos en compras (1-100)'].mean(), 2)}"
      f"\n40-50\t {round(f3['Puntos en compras (1-100)'].mean(), 2)}")
enter()

# Rango de datos con respecto a la edad
f4 = df[(df["Genero"] == "Mujer")]  # Filtro mujer
f5 = df[(df["Genero"] == "Hombre")]  # Filtro hombre
print(
  "Rango de edades\n\t\t\tMin\tMax\tMedia\tMediana"
  f"\nMujeres\t\t{f4['Edad'].min()}\t{f4['Edad'].max()}\t{round(f4['Edad'].mean(), 1)}\t{round(f4['Edad'].median(), 1)}"
  f"\nHombres\t\t{f5['Edad'].min()}\t{f5['Edad'].max()}\t{round(f5['Edad'].mean(), 1)}\t{round(f5['Edad'].median(), 1)}"
)
enter()


# Moda del genero con puntos 1.5 veces mayores al promedio
media = df['Puntos en compras (1-100)'].mean()
f6 = df[(df['Puntos en compras (1-100)'] > media * 1.5)]
f6m, f6h = f6[(f6["Genero"] == "Mujer")], f6[(f6["Genero"] == "Hombre")]
print(f"Los clientes con 1.5 veces los puntos del cliente promedio son {f6m['Genero'].count()} mujeres y "
      f"{f6h['Genero'].count()} hombres\nPor ello, los clientes con mayor cantidad por encima de la media son", end=" ")
print("mujeres" if (f6m["Genero"].count() > f6h["Genero"].count()) else "hombres")
enter()


# Desviación estandar
print(f"Edad del cliente promedio: {round(df['Edad'].mean(), 1)} años"
      f"\ndesviación estandar: {round(df['Puntos en compras (1-100)'].std(), 1)} años")

