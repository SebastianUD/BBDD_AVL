import customtkinter as ctk
from tkinter import messagebox

def mostrar_busqueda_creditos_materia(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Buscar Materia por Créditos")
    ventana.geometry("500x440")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Buscar materia por número de créditos",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    entrada_creditos = ctk.CTkEntry(ventana, placeholder_text="Ingrese cantidad de créditos", width=340)
    entrada_creditos.pack(pady=10)

    resultado = ctk.CTkTextbox(ventana, width=440, height=180, font=("Courier", 11))
    resultado.pack(pady=10)
    resultado.configure(state="disabled")

    def buscar():
        try:
            creditos_buscados = int(entrada_creditos.get())
            materias = gestor.arbol.inorden_lista()
            encontrados = [m for m in materias if m.creditos == creditos_buscados]

            resultado.configure(state="normal")
            resultado.delete("1.0", "end")
            if encontrados:
                resultado.insert("end", f"[ENCONTRADOS] {len(encontrados)} materia(s) con créditos = {creditos_buscados}:\n")
                for m in encontrados:
                    resultado.insert("end", f"- {m}\n")
            else:
                resultado.insert("end", f"[NO ENCONTRADO] No se encontraron materias con créditos = {creditos_buscados}")
            resultado.configure(state="disabled")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número entero válido")

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
