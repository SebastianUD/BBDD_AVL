import customtkinter as ctk
from tkinter import messagebox
from Estudiante import Estudiante

def mostrar_formulario_agregar_estudiante(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Agregar Estudiante")
    ventana.geometry("500x520")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Formulario de Registro de Estudiante",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    entradas = {}

    def crear_entrada(nombre_campo, placeholder):
        ctk.CTkLabel(ventana, text=nombre_campo, font=("Segoe UI", 12), text_color="white").pack()
        entry = ctk.CTkEntry(ventana, placeholder_text=placeholder, width=320)
        entry.pack(pady=8)
        entradas[nombre_campo] = entry

    crear_entrada("Código", "Ej: 202210001")
    crear_entrada("Nombre", "Ej: Laura Sánchez")
    crear_entrada("Correo", "Ej: estudiante@email.com")
    crear_entrada("Facultad", "Ej: Ingeniería")
    crear_entrada("Carrera", "Ej: Sistemas")

    def guardar():
        try:
            codigo = int(entradas["Código"].get())
            nombre = entradas["Nombre"].get().strip()
            correo = entradas["Correo"].get().strip()
            facultad = entradas["Facultad"].get().strip()
            carrera = entradas["Carrera"].get().strip()

            if not all([nombre, correo, facultad, carrera]):
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            if "@" not in correo or "." not in correo:
                messagebox.showerror("Error", "Correo inválido.")
                return

            estudiante = Estudiante(codigo, nombre, correo, facultad, carrera)
            gestor.agregar_entidad(estudiante)
            messagebox.showinfo("Éxito", "Estudiante agregado correctamente.")
            limpiar()
        except ValueError:
            messagebox.showerror("Error", "El código debe ser un número entero.")

    def limpiar():
        for entry in entradas.values():
            entry.delete(0, ctk.END)

    def volver():
        ventana.destroy()
        from GUI_Estudiante import mostrar_interfaz_estudiantes
        mostrar_interfaz_estudiantes()

    ctk.CTkButton(
        ventana, text="Guardar Estudiante", command=guardar,
        font=("Segoe UI", 13), width=200, height=35
    ).pack(pady=15)

    ctk.CTkButton(
        ventana, text="Volver",
        command=volver,
        font=("Segoe UI", 13), width=200, height=35,
        fg_color="#e67e22", hover_color="#d35400"
    ).pack()