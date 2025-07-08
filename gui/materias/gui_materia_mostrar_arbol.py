import customtkinter as ctk
from tkinter import messagebox
import io
from contextlib import redirect_stdout

def mostrar_arbol_avl_materias(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Árbol AVL - Materias")
    ventana.geometry("800x500")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Visualización del Árbol AVL",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    output_box = ctk.CTkTextbox(ventana, width=760, height=350, font=("Courier", 11))
    output_box.pack(pady=10)
    output_box.configure(state="normal")

    if gestor.arbol.raiz:
        # Capturamos la salida del print
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            gestor.arbol.mostrar_arbol_binarytree()
        contenido = buffer.getvalue()
        output_box.insert("end", contenido)
    else:
        output_box.insert("end", "El árbol está vacío")

    output_box.configure(state="disabled")

    def volver():
        ventana.destroy()
        from gui.core.GUI_Materia import mostrar_interfaz_materias
        mostrar_interfaz_materias()

    ctk.CTkButton(
        ventana, text="Volver", command=volver,
        font=("Segoe UI", 13), width=180, height=35,
        fg_color="#e67e22", hover_color="#d35400", corner_radius=8
    ).pack(pady=10)