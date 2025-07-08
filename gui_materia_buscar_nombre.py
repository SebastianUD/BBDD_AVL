import customtkinter as ctk
from tkinter import messagebox

def mostrar_busqueda_nombre_materia(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Buscar Materia por Nombre")
    ventana.geometry("500x440")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Buscar materia por nombre (coincidencia parcial)",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    entrada_nombre = ctk.CTkEntry(ventana, placeholder_text="Ingrese nombre o parte del nombre", width=340)
    entrada_nombre.pack(pady=10)

    resultado = ctk.CTkTextbox(ventana, width=440, height=160, font=("Courier", 11))
    resultado.pack(pady=10)
    resultado.configure(state="disabled")

    def buscar():
        nombre_buscado = entrada_nombre.get().strip().lower()
        if not nombre_buscado:
            messagebox.showerror("Error", "Por favor, ingrese un nombre")
            return

        materias = gestor.arbol.inorden_lista()
        encontrados = [m for m in materias if nombre_buscado in m.nombre.lower()]

        resultado.configure(state="normal")
        resultado.delete("1.0", "end")
        if encontrados:
            resultado.insert("end", f"[ENCONTRADOS] {len(encontrados)} materia(s) con nombre = {nombre_buscado}:\n")
            for m in encontrados:
                resultado.insert("end", f"- Código: {m.codigo}, Nombre: {m.nombre}, Créditos: {m.creditos}, Horas/semana: {m.horas_semana}\n")
        else:
            resultado.insert("end", f"[NO ENCONTRADO] No se encontraron materias con nombre = {nombre_buscado}")
        resultado.configure(state="disabled")

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
