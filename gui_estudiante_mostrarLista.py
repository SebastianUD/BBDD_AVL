import customtkinter as ctk
from tkinter import messagebox

def mostrar_estudiantes_inorden(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Estudiantes en orden ascendente")
    ventana.geometry("600x500")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana,
        text="Listado de estudiantes (ordenado por código)",
        font=("Segoe UI", 18, "bold"),
        text_color="white"
    ).pack(pady=20)

    texto = ctk.CTkTextbox(ventana, width=540, height=320, font=("Segoe UI", 12))
    texto.pack(pady=10)
    texto.configure(state="normal")

    estudiantes = gestor.arbol.inorden_lista()
    if estudiantes:
        for e in estudiantes:
            texto.insert("end", f"- Código: {e.codigo}, Nombre: {e.nombre}, Correo: {e.correo}, Facultad: {e.facultad}, Carrera: {e.carrera}\n\n")
    else:
        texto.insert("end", "No hay estudiantes registrados.")

    texto.configure(state="disabled")

    def volver():
        ventana.destroy()
        from GUI_Estudiante import mostrar_interfaz_estudiantes
        mostrar_interfaz_estudiantes()

    ctk.CTkButton(
        ventana,
        text="Volver",
        command=volver,
        font=("Segoe UI", 13),
        fg_color="#e67e22",
        hover_color="#d35400",
        width=150,
        height=35,
        corner_radius=8
    ).pack(pady=15)