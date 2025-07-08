import customtkinter as ctk
from tkinter import messagebox
from Materia import Materia

def mostrar_formulario_agregar_materia(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Agregar Materia")
    ventana.geometry("500x540")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Formulario de Registro de Materia",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    # Entradas
    entradas = {}
    campos = [
        ("Código", "codigo"),
        ("Nombre de la materia", "nombre"),
        ("Créditos", "creditos"),
        ("Horas semanales", "horas")
    ]

    for texto, clave in campos:
        ctk.CTkLabel(ventana, text=texto, text_color="white").pack(anchor="w", padx=40, pady=(8, 0))
        entrada = ctk.CTkEntry(ventana, width=380)
        entrada.pack(padx=40)
        entradas[clave] = entrada

    # Función guardar
    def guardar():
        try:
            codigo = int(entradas["codigo"].get())
            nombre = entradas["nombre"].get()
            creditos = int(entradas["creditos"].get())
            horas = int(entradas["horas"].get())

            if not nombre:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            nueva_materia = Materia(codigo, nombre, creditos, horas)
            gestor.agregar_entidad(nueva_materia)
            messagebox.showinfo("Éxito", "Materia agregada correctamente")
            ventana.destroy()
            from GUI_Materia import mostrar_interfaz_materias
            mostrar_interfaz_materias()

        except ValueError:
            messagebox.showerror("Error", "Código, créditos y horas deben ser números enteros")

    # Botones
    ctk.CTkButton(
        ventana, text="Guardar", command=guardar,
        font=("Segoe UI", 13), width=200, height=35, corner_radius=8
    ).pack(pady=20)

    ctk.CTkButton(
        ventana, text="Volver", command=lambda: volver(ventana),
        font=("Segoe UI", 13), width=200, height=35,
        fg_color="#e67e22", hover_color="#d35400", corner_radius=8
    ).pack()

def volver(ventana):
    ventana.destroy()
    from GUI_Materia import mostrar_interfaz_materias
    mostrar_interfaz_materias()