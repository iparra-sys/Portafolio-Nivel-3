import pandas as pd
import matplotlib.pyplot as plt
import os

ARCHIVO = "ventas.csv"

# Si no existe, crear archivo con datos de ejemplo
if not os.path.exists(ARCHIVO):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.write("fecha,producto,cantidad,precio\n")
        f.write("2025-09-01,Teclado,3,50\n")
        f.write("2025-09-01,Mouse,5,25\n")
        f.write("2025-09-02,Monitor,2,200\n")
        f.write("2025-09-03,Teclado,1,50\n")
        f.write("2025-09-04,Mouse,3,25\n")
        f.write("2025-09-05,Auriculares,4,35\n")
        f.write("2025-09-05,Monitor,1,200\n")
    print("✅ Archivo ventas.csv creado con datos de ejemplo.")

# Leer CSV
df = pd.read_csv(ARCHIVO)

# Crear columna de ventas
df["Ventas"] = df["cantidad"] * df["precio"]

# --- Dashboard ---
print("📊 Resumen de ventas:")
print(df.groupby("producto")[["cantidad", "Ventas"]].sum())

# Gráfico de ventas por producto
df.groupby("producto")["Ventas"].sum().plot(kind="bar", title="Ventas por producto", ylabel="Total $")
plt.tight_layout()
plt.show()

# Gráfico de cantidad vendida por producto
df.groupby("producto")["cantidad"].sum().plot(kind="bar", color="orange", title="Cantidad vendida por producto", ylabel="Unidades")
plt.tight_layout()
plt.show()
