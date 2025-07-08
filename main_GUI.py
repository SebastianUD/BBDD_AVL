import customtkinter as ctk
from tkinter import messagebox
from GUI_Estudiante import mostrar_interfaz_estudiantes
from GUI_Materia import mostrar_interfaz_materias
from GUI_Profesor import mostrar_interfaz_profesores

# --------------------- CONFIGURACIÓN DE TEMA Y APARIENCIA ---------------------
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema azul

# --------------------- FUNCIÓN PARA ABRIR MÓDULOS ---------------------
def abrir_modulo(nombre, ventana_principal):
    ventana_principal.destroy()

    if nombre == "Estudiantes":
        mostrar_interfaz_estudiantes()
    elif nombre == "Profesores":
        mostrar_interfaz_profesores()
    elif nombre == "Materias":
        mostrar_interfaz_materias() 

# --------------------- CONFIGURACIÓN INICIAL DE LA VENTANA ---------------------
def iniciar_menu_principal():
    ventana_principal = ctk.CTk()
    ventana_principal.title("Gestor de Base de Datos AVL")
    ventana_principal.geometry("500x480")
    ventana_principal.resizable(False, False)

    # --------------------- MENSAJE DE BIENVENIDA ---------------------
    mensaje = ctk.CTkLabel(
        ventana_principal,
        text="\n¡Bienvenido/a al Gestor de Base de Datos AVL!\nSelecciona una entidad para comenzar",
        font=("Segoe UI", 18, "bold"),
        text_color="white",
        justify="center"
    )
    mensaje.pack(pady=40)

    # --------------------- BOTONES DE MÓDULOS ---------------------
    botones = [
        ("Estudiantes", lambda: abrir_modulo("Estudiantes", ventana_principal)),
        ("Profesores", lambda: abrir_modulo("Profesores", ventana_principal)),
        ("Materias", lambda: abrir_modulo("Materias", ventana_principal)),
    ]

    for texto, accion in botones:
        b = ctk.CTkButton(
            ventana_principal,
            text=texto,
            command=accion,
            font=("Segoe UI", 14, "bold"),
            width=200,
            height=40,
            corner_radius=10
        )
        b.pack(pady=10)

    # --------------------- BOTÓN SALIR ---------------------
    boton_salir = ctk.CTkButton(
        ventana_principal,
        text="Salir",
        command=ventana_principal.destroy,
        font=("Segoe UI", 14, "bold"),
        width=200,
        height=40,
        fg_color="#D9534F",
        hover_color="#C9302C",
        corner_radius=10
    )
    boton_salir.pack(pady=30)

    ventana_principal.mainloop()

# --------------------- EJECUCIÓN PRINCIPAL ---------------------
if __name__ == "__main__":
    iniciar_menu_principal()
