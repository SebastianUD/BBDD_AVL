import customtkinter as ctk
from tkinter import messagebox

def abrir_busqueda_por_campo(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Buscar Estudiante por Campo")
    ventana.geometry("500x500")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana,
        text="Buscar estudiante por campo",
        font=("Segoe UI", 18, "bold"),
        text_color="white"
    ).pack(pady=25)

    # Campos disponibles
    opciones = {
        "Código": "codigo",
        "Nombre": "nombre",
        "Correo": "correo",
        "Facultad": "facultad",
        "Carrera": "carrera"
    }

    # Botones para buscar por cada campo    
    ctk.CTkButton(
        ventana,
        text="Código",
        command=lambda: abrir_busqueda_por_codigo(gestor),
        font=("Segoe UI", 14),
        width=280,
        height=40,
        corner_radius=10
    ).pack(pady=8)

    ctk.CTkButton(
        ventana,
        text="Nombre",
        command=lambda: abrir_busqueda_por_nombre(gestor),
        font=("Segoe UI", 14),
        width=280,
        height=40,
        corner_radius=10
    ).pack(pady=8)

    ctk.CTkButton(
        ventana,
        text="Correo",
        command=lambda: abrir_busqueda_por_correo(gestor),
        font=("Segoe UI", 14),
        width=280,
        height=40,
        corner_radius=10
    ).pack(pady=8)

    ctk.CTkButton(
        ventana,
        text="Facultad",
        command=lambda: abrir_busqueda_por_facultad(gestor),
        font=("Segoe UI", 14),
        width=280,
        height=40,
        corner_radius=10
    ).pack(pady=8)

    ctk.CTkButton(
        ventana,
        text="Carrera",
        command=lambda: abrir_busqueda_por_carrera(gestor),
        font=("Segoe UI", 14),
        width=280,
        height=40,
        corner_radius=10
    ).pack(pady=8)

    # Botón para volver
    def volver():
        ventana.destroy()
        from gui.core.GUI_Estudiante import mostrar_interfaz_estudiantes
        mostrar_interfaz_estudiantes()

    ctk.CTkButton(
        ventana,
        text="Volver",
        command=volver,
        font=("Segoe UI", 14),
        fg_color="#e74c3c",
        hover_color="#c0392b",
        width=280,
        height=40,
        corner_radius=10
    ).pack(pady=20)

    def abrir_busqueda_por_codigo(gestor):
        ventana.destroy()
        from gui.estudiantes.gui_estudiante_buscar_codigo import mostrar_busqueda_por_codigo
        mostrar_busqueda_por_codigo(gestor)
    def abrir_busqueda_por_nombre(gestor):
        ventana.destroy()
        from gui.estudiantes.gui_estudiante_buscar_nombre import mostrar_busqueda_por_nombre
        mostrar_busqueda_por_nombre(gestor)
    def abrir_busqueda_por_correo(gestor):
        ventana.destroy()
        from gui.estudiantes.gui_estudiante_buscar_correo import mostrar_busqueda_por_correo
        mostrar_busqueda_por_correo(gestor)
    def abrir_busqueda_por_facultad(gestor):
        ventana.destroy()
        from gui.estudiantes.gui_estudiante_buscar_facultad import mostrar_busqueda_por_facultad
        mostrar_busqueda_por_facultad(gestor)
    def abrir_busqueda_por_carrera(gestor):
        ventana.destroy()
        from gui.estudiantes.gui_estudiante_buscar_carrera import mostrar_busqueda_por_carrera
        mostrar_busqueda_por_carrera(gestor)
