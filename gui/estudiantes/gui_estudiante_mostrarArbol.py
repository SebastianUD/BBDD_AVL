import customtkinter as ctk
from tkinter import messagebox
from io import StringIO
import sys

def mostrar_arbol_avl(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Árbol AVL de Estudiantes")
    ventana.geometry("1000x600")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Título
    ctk.CTkLabel(
        ventana,
        text="Estructura del Árbol AVL",
        font=("Segoe UI", 18, "bold"),
        text_color="white"
    ).pack(pady=10)

    # Scroll frame para contener el árbol
    scroll_frame = ctk.CTkScrollableFrame(ventana, width=940, height=470)
    scroll_frame.pack(pady=10)

    # Textbox dentro del scroll frame
    output_box = ctk.CTkTextbox(scroll_frame, width=900, height=450, font=("Courier New", 10), wrap="none")
    output_box.pack()
    output_box.configure(state="normal")

    # Captura la salida del árbol
    old_stdout = sys.stdout
    buffer = StringIO()
    sys.stdout = buffer

    try:
        gestor.arbol.mostrar_arbol_binarytree()
    except Exception as e:
        print(f"[ERROR] {e}")

    sys.stdout = old_stdout
    salida = buffer.getvalue()
    output_box.insert("end", salida if salida else "Árbol vacío.")
    output_box.configure(state="disabled")

    # Botón para volver
    def volver():
        ventana.destroy()
        from gui.core.GUI_Estudiante import mostrar_interfaz_estudiantes
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