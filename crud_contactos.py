import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

DB_NAME = "contactos.db"

def crear_base():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()

def insertar_contacto(nombre, telefono, email):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contactos (nombre, telefono, email) VALUES (?, ?, ?)", 
                   (nombre, telefono, email))
    conn.commit()
    conn.close()

def obtener_contactos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactos")
    contactos = cursor.fetchall()
    conn.close()
    return contactos

def eliminar_contacto(id_contacto):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contactos WHERE id = ?", (id_contacto,))
    conn.commit()
    conn.close()

def actualizar_contacto(id_contacto, nombre, telefono, email):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE contactos SET nombre=?, telefono=?, email=? WHERE id=?", 
                   (nombre, telefono, email, id_contacto))
    conn.commit()
    conn.close()

def cargar_lista():
    for fila in tree.get_children():
        tree.delete(fila)
    for contacto in obtener_contactos():
        tree.insert("", tk.END, values=contacto)

def agregar_contacto():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    if nombre and telefono:
        insertar_contacto(nombre, telefono, email)
        cargar_lista()
        limpiar_entradas()
    else:
        messagebox.showwarning("Campos requeridos", "Nombre y teléfono son obligatorios.")

def eliminar_seleccionado():
    seleccionado = tree.selection()
    if seleccionado:
        item = tree.item(seleccionado)
        id_contacto = item["values"][0]
        eliminar_contacto(id_contacto)
        cargar_lista()
    else:
        messagebox.showwarning("Atención", "Seleccione un contacto para eliminar.")

def editar_seleccionado():
    seleccionado = tree.selection()
    if seleccionado:
        item = tree.item(seleccionado)
        id_contacto, nombre, telefono, email = item["values"]
        entry_nombre.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_nombre.insert(0, nombre)
        entry_telefono.insert(0, telefono)
        entry_email.insert(0, email)
        btn_agregar.config(text="💾 Guardar", command=lambda: guardar_edicion(id_contacto), bg="#FF9800")
    else:
        messagebox.showwarning("Atención", "Seleccione un contacto para editar.")

def guardar_edicion(id_contacto):
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    if nombre and telefono:
        actualizar_contacto(id_contacto, nombre, telefono, email)
        cargar_lista()
        limpiar_entradas()
        btn_agregar.config(text="➕ Agregar", command=agregar_contacto, bg="#4CAF50")
    else:
        messagebox.showwarning("Campos requeridos", "Nombre y teléfono son obligatorios.")

def limpiar_entradas():
    entry_nombre.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# --- GUI ---
ventana = tk.Tk()
ventana.title("📋 Gestor de Contactos")
ventana.geometry("600x480")
ventana.configure(bg="#1E1E1E")

# Estilo oscuro para Treeview
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
                background="#2C2C2C",
                foreground="white",
                fieldbackground="#2C2C2C",
                rowheight=25,
                font=("Segoe UI", 10))
style.configure("Treeview.Heading",
                background="#333333",
                foreground="white",
                font=("Segoe UI", 10, "bold"))
style.map("Treeview",
          background=[("selected", "#444444")])

# Frame de entradas
frame_form = tk.Frame(ventana, bg="#1E1E1E")
frame_form.pack(pady=10)

def create_label(text, row):
    tk.Label(frame_form, text=text, bg="#1E1E1E", fg="white", font=("Segoe UI", 10)).grid(row=row, column=0, padx=5, pady=5, sticky="w")

create_label("Nombre:", 0)
entry_nombre = tk.Entry(frame_form, width=40, bg="#2C2C2C", fg="white", insertbackground="white", relief="flat")
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

create_label("Teléfono:", 1)
entry_telefono = tk.Entry(frame_form, width=40, bg="#2C2C2C", fg="white", insertbackground="white", relief="flat")
entry_telefono.grid(row=1, column=1, padx=5, pady=5)

create_label("Email:", 2)
entry_email = tk.Entry(frame_form, width=40, bg="#2C2C2C", fg="white", insertbackground="white", relief="flat")
entry_email.grid(row=2, column=1, padx=5, pady=5)

# Botón agregar/guardar
btn_agregar = tk.Button(ventana, text="➕ Agregar", command=agregar_contacto,
                        bg="#4CAF50", fg="white", font=("Segoe UI", 10), relief="flat")
btn_agregar.pack(pady=8, ipadx=10, ipady=3)

# Tabla
columns = ("ID", "Nombre", "Teléfono", "Email")
tree = ttk.Treeview(ventana, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(padx=10, pady=10, fill="x")

# --- Frame de botones inferiores ---
frame_botones = tk.Frame(ventana, bg="#1E1E1E")
frame_botones.pack(pady=5)

btn_editar = tk.Button(frame_botones, text="✏️ Editar", command=editar_seleccionado,
                       bg="#2196F3", fg="white", relief="flat", font=("Segoe UI", 10))
btn_editar.grid(row=0, column=0, padx=5, ipadx=8, ipady=3)

btn_eliminar = tk.Button(frame_botones, text="🗑️ Eliminar", command=eliminar_seleccionado,
                         bg="#F44336", fg="white", relief="flat", font=("Segoe UI", 10))
btn_eliminar.grid(row=0, column=1, padx=5, ipadx=8, ipady=3)

crear_base()
cargar_lista()

ventana.mainloop()
