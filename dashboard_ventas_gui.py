import pandas as pd
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def cargar_csv():
    global df
    archivo = filedialog.askopenfilename(
        title="Selecciona el archivo de ventas",
        filetypes=(("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*"))
    )
    if archivo:
        try:
            df = pd.read_csv(archivo)
            if not {"fecha", "producto", "cantidad", "precio"}.issubset(df.columns):
                messagebox.showerror("Error", "El archivo debe tener las columnas: fecha, producto, cantidad, precio")
                return
            
            df["Ventas"] = df["cantidad"] * df["precio"]
            mostrar_resumen()
            btn_graficar.config(state="normal")
        except Exception as e:
            messagebox.showerror("Error al cargar CSV", str(e))

def mostrar_resumen():
    for fila in tabla.get_children():
        tabla.delete(fila)
    resumen = df.groupby("producto")[["cantidad", "Ventas"]].sum().reset_index()
    for _, row in resumen.iterrows():
        tabla.insert("", "end", values=(row["producto"], row["cantidad"], f"${row['Ventas']:.2f}"))

def graficar():
    df.groupby("producto")["Ventas"].sum().plot(kind="bar", title="Ventas por producto", ylabel="Total $")
    plt.tight_layout()
    plt.show()

    df.groupby("producto")["cantidad"].sum().plot(kind="bar", color="orange", title="Cantidad vendida por producto", ylabel="Unidades")
    plt.tight_layout()
    plt.show()

# --- GUI ---
root = tk.Tk()
root.title("📊 Dashboard de Ventas")
root.geometry("600x400")
root.configure(bg="#1e1e1e")  # Fondo oscuro

# Botón para cargar CSV
btn_cargar = tk.Button(root, text="📂 Cargar CSV", command=cargar_csv, bg="#0078D7", fg="white", font=("Segoe UI", 11, "bold"))
btn_cargar.pack(pady=10)

# Tabla resumen
frame_tabla = tk.Frame(root, bg="#1e1e1e")
frame_tabla.pack(pady=10, fill="both", expand=True)

tabla = ttk.Treeview(frame_tabla, columns=("Producto", "Cantidad", "Ventas"), show="headings")
tabla.heading("Producto", text="Producto")
tabla.heading("Cantidad", text="Cantidad")
tabla.heading("Ventas", text="Ventas")

tabla.pack(fill="both", expand=True)

# Estilo de la tabla
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#2d2d2d", fieldbackground="#2d2d2d", foreground="white")
style.configure("Treeview.Heading", background="#444444", foreground="white", font=("Segoe UI", 10, "bold"))

# Botón para graficar
btn_graficar = tk.Button(root, text="📊 Ver Gráficas", command=graficar, bg="#28A745", fg="white", font=("Segoe UI", 11, "bold"), state="disabled")
btn_graficar.pack(pady=10)

root.mainloop()
