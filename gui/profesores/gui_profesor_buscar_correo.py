import customtkinter as ctk
from tkinter import messagebox

def mostrar_busqueda_por_correo(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Buscar Profesor por Correo")
    ventana.geometry("520x460")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Buscar profesor por correo (coincidencia exacta)",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    entrada_correo = ctk.CTkEntry(ventana, placeholder_text="Ej: profe@mail.com", width=360)
    entrada_correo.pack(pady=10)

    resultado = ctk.CTkTextbox(ventana, width=470, height=200, font=("Courier", 11))
    resultado.pack(pady=10)
    resultado.configure(state="disabled")

    def buscar():
        correo_buscado = entrada_correo.get().strip().lower()
        if not correo_buscado:
            messagebox.showerror("Error", "Por favor, ingrese un correo.")
            return

        profesores = gestor.arbol.inorden_lista()
        encontrados = [
            p for p in profesores if p.correo.lower() == correo_buscado
        ]

        resultado.configure(state="normal")
        resultado.delete("1.0", "end")

        if encontrados:
            resultado.insert("end", f"[ENCONTRADOS] {len(encontrados)} profesor(es) con correo = {correo_buscado}:\n")
            for p in encontrados:
                resultado.insert(
                    "end",
                    f"- Código: {p.codigo}, Nombre: {p.nombre}, Correo: {p.correo}, Vinculación: {p.vinculacion}\n"
                )
        else:
            resultado.insert("end", f"[NO ENCONTRADO] No hay profesores con correo = {correo_buscado}")
        resultado.configure(state="disabled")

    ctk.CTkButton(
        ventana, text="Buscar", command=buscar,
        font=("Segoe UI", 13), width=200, height=35
    ).pack(pady=5)

    ctk.CTkButton(
        ventana, text="Volver",
        command=lambda: volver(ventana, gestor),
        font=("Segoe UI", 13), width=200, height=35,
        fg_color="#e67e22", hover_color="#d35400"
    ).pack(pady=5)

def volver(ventana, gestor):
    ventana.destroy()
    from gui.profesores.gui_profesor_buscar import abrir_busqueda_por_campo_profesor
    abrir_busqueda_por_campo_profesor(gestor)