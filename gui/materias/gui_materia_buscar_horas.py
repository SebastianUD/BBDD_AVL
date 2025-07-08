import customtkinter as ctk
from tkinter import messagebox

def mostrar_busqueda_horas_materia(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Buscar Materia por Horas/Semana")
    ventana.geometry("500x440")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Buscar materia por horas semanales",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    entrada_horas = ctk.CTkEntry(ventana, placeholder_text="Ingrese cantidad de horas/semana", width=340)
    entrada_horas.pack(pady=10)

    resultado = ctk.CTkTextbox(ventana, width=440, height=180, font=("Courier", 11))
    resultado.pack(pady=10)
    resultado.configure(state="disabled")

    def buscar():
        try:
            horas_buscadas = int(entrada_horas.get())
            materias = gestor.arbol.inorden_lista()
            encontrados = [m for m in materias if m.horas_semana == horas_buscadas]

            resultado.configure(state="normal")
            resultado.delete("1.0", "end")
            if encontrados:
                resultado.insert("end", f"[ENCONTRADOS] {len(encontrados)} materia(s) con horas/semana = {horas_buscadas}:\n")
                for m in encontrados:
                    resultado.insert("end", f"- {m}\n")
            else:
                resultado.insert("end", f"[NO ENCONTRADO] No se encontraron materias con horas/semana = {horas_buscadas}")
            resultado.configure(state="disabled")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número entero válido")

    ctk.CTkButton(
        ventana, text="Buscar", command=buscar,
        font=("Segoe UI", 13), width=180, height=35, corner_radius=8
    ).pack(pady=10)

    ctk.CTkButton(
        ventana, text="Volver",
        command=lambda: volver(ventana, gestor),
        font=("Segoe UI", 13), width=180, height=35,
        fg_color="#e67e22", hover_color="#d35400", corner_radius=8
    ).pack()

def volver(ventana, gestor):
    ventana.destroy()
    from gui.materias.gui_materia_buscar import abrir_busqueda_por_campo_materia
    abrir_busqueda_por_campo_materia(gestor)
