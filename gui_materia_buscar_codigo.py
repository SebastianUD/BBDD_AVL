import customtkinter as ctk
from tkinter import messagebox

def mostrar_busqueda_codigo_materia(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Buscar Materia por Código")
    ventana.geometry("500x400")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Buscar materia por código",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    entrada_codigo = ctk.CTkEntry(ventana, placeholder_text="Ingrese el código de la materia", width=300)
    entrada_codigo.pack(pady=10)

    resultado = ctk.CTkTextbox(ventana, width=420, height=120, font=("Courier", 11))
    resultado.pack(pady=10)
    resultado.configure(state="disabled")

    def buscar():
        try:
            codigo = int(entrada_codigo.get())
            materia = gestor.buscar_por_codigo(codigo)
            resultado.configure(state="normal")
            resultado.delete("1.0", "end")
            if materia:
                resultado.insert("end", f"[ENCONTRADO] {materia}")
            else:
                resultado.insert("end", f"[NO ENCONTRADO] No hay materia con código = {codigo}")
            resultado.configure(state="disabled")
        except ValueError:
            messagebox.showerror("Error", "El código debe ser un número entero")

    ctk.CTkButton(
        ventana, text="Buscar", command=buscar,
        font=("Segoe UI", 13), width=180, height=35, corner_radius=8
    ).pack(pady=10)

    ctk.CTkButton(
        ventana, text="Volver",
        command=lambda: volver(ventana),
        font=("Segoe UI", 13), width=180, height=35,
        fg_color="#e67e22", hover_color="#d35400", corner_radius=8
    ).pack()

def volver(ventana):
    ventana.destroy()
    from gui_materia_buscar import abrir_busqueda_por_campo_materia
    from Materia import Materia
    from GestorBDGenerico import GestorBDGenerico
    gestor = GestorBDGenerico("materias.json", Materia, "materia")
    abrir_busqueda_por_campo_materia(gestor)
