import customtkinter as ctk
from tkinter import messagebox

def mostrar_profesores_inorden(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Listado de Profesores (Inorden)")
    ventana.geometry("700x460")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana,
        text="Profesores en Orden Ascendente (por Código)",
        font=("Segoe UI", 16, "bold"),
        text_color="white"
    ).pack(pady=20)

    caja_texto = ctk.CTkTextbox(ventana, width=620, height=280, font=("Courier", 11))
    caja_texto.pack(pady=10)

    caja_texto.configure(state="normal")
    profesores = gestor.arbol.inorden_lista()
    if profesores:
        for p in profesores:
            linea = f"- Código: {p.codigo}, Nombre: {p.nombre}, Correo: {p.correo}, Vinculación: {p.vinculacion}\n"
            caja_texto.insert("end", linea)
    else:
        caja_texto.insert("end", "No hay profesores registrados.")
    caja_texto.configure(state="disabled")

    # Botón volver
    ctk.CTkButton(
        ventana,
        text="Volver",
        command=lambda: volver(ventana),
        font=("Segoe UI", 13),
        width=200,
        height=35,
        fg_color="#e67e22",
        hover_color="#d35400"
    ).pack(pady=10)

def volver(ventana):
    ventana.destroy()
    from gui.core.GUI_Profesor import mostrar_interfaz_profesores
    mostrar_interfaz_profesores()