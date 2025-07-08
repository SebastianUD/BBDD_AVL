import customtkinter as ctk
from tkinter import messagebox
from models.Profesor import Profesor

def mostrar_formulario_agregar_profesor(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Agregar Profesor")
    ventana.geometry("500x520")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Formulario de Registro de Profesor",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    entradas = {}

    def crear_entrada(nombre_campo, placeholder):
        ctk.CTkLabel(ventana, text=nombre_campo, font=("Segoe UI", 12), text_color="white").pack()
        entry = ctk.CTkEntry(ventana, placeholder_text=placeholder, width=320)
        entry.pack(pady=8)
        entradas[nombre_campo] = entry

    crear_entrada("Código", "Ej: 1001")
    crear_entrada("Nombre", "Ej: Ana Torres")
    crear_entrada("Correo", "Ej: profesor@email.com")
    ctk.CTkLabel(ventana, text="Vinculación", font=("Segoe UI", 12), text_color="white").pack()
    opciones_vinculacion = ["Planta", "Catedrático", "Ocasional"]
    entrada_vinculacion = ctk.CTkOptionMenu(ventana, values=opciones_vinculacion, width=320)
    entrada_vinculacion.set("Planta") # Valor por defecto
    entrada_vinculacion.pack(pady=8)

    def guardar():
        try:
            codigo = int(entradas["Código"].get())
            nombre = entradas["Nombre"].get().strip()
            correo = entradas["Correo"].get().strip()
            vinculacion = entrada_vinculacion.get()

            if not all([nombre, correo, vinculacion]):
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            if "@" not in correo or "." not in correo:
                messagebox.showerror("Error", "Correo inválido.")
                return

            profesor = Profesor(codigo, nombre, correo, vinculacion)
            gestor.agregar_entidad(profesor)
            messagebox.showinfo("Éxito", "Profesor agregado correctamente.")
            limpiar()
        except ValueError:
            messagebox.showerror("Error", "El código debe ser un número entero.")

    def limpiar():
        for entry in entradas.values():
            entry.delete(0, ctk.END)

    ctk.CTkButton(
        ventana, text="Guardar Profesor", command=guardar,
        font=("Segoe UI", 13), width=200, height=35
    ).pack(pady=15)

    ctk.CTkButton(
        ventana, text="Volver",
        command=lambda: volver(ventana),
        font=("Segoe UI", 13), width=200, height=35,
        fg_color="#e67e22", hover_color="#d35400"
    ).pack()

def volver(ventana):
    ventana.destroy()
    from gui.core.GUI_Profesor import mostrar_interfaz_profesores
    mostrar_interfaz_profesores()