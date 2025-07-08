import customtkinter as ctk
from tkinter import messagebox
from models.Materia import Materia

def mostrar_formulario_actualizar_materia(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Actualizar Materia")
    ventana.geometry("500x520")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Actualizar materia por código",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    entrada_codigo = ctk.CTkEntry(ventana, placeholder_text="Ingrese código de la materia", width=340)
    entrada_codigo.pack(pady=10)

    campos_frame = ctk.CTkFrame(ventana)
    campos_frame.pack(pady=10)

    entrada_nombre = ctk.CTkEntry(campos_frame, placeholder_text="Nuevo nombre", width=340)
    entrada_nombre.pack(pady=5)

    entrada_creditos = ctk.CTkEntry(campos_frame, placeholder_text="Nuevos créditos", width=340)
    entrada_creditos.pack(pady=5)

    entrada_horas = ctk.CTkEntry(campos_frame, placeholder_text="Nuevas horas/semana", width=340)
    entrada_horas.pack(pady=5)

    def actualizar():
        try:
            codigo = int(entrada_codigo.get())
            materia_actual = gestor.buscar_por_codigo(codigo)

            if not materia_actual:
                messagebox.showerror("Error", f"No se encontró la materia con código {codigo}")
                return

            nombre = entrada_nombre.get() or materia_actual.nombre
            creditos = entrada_creditos.get()
            horas = entrada_horas.get()

            creditos = int(creditos) if creditos else materia_actual.creditos
            horas = int(horas) if horas else materia_actual.horas_semana

            nueva_materia = Materia(codigo, nombre, creditos, horas)
            gestor.actualizar_entidad(codigo, nueva_materia)
            messagebox.showinfo("Éxito", "Materia actualizada correctamente")
            ventana.destroy()
            from gui.core.GUI_Materia import mostrar_interfaz_materias
            mostrar_interfaz_materias()

        except ValueError:
            messagebox.showerror("Error", "Ingrese solo valores numéricos válidos para créditos y horas")

    ctk.CTkButton(
        ventana, text="Actualizar", command=actualizar,
        font=("Segoe UI", 13), width=180, height=35, corner_radius=8
    ).pack(pady=15)

    def volver():
        ventana.destroy()
        from gui.core.GUI_Materia import mostrar_interfaz_materias
        mostrar_interfaz_materias()

    ctk.CTkButton(
        ventana, text="Volver",
        command=volver,
        font=("Segoe UI", 13), width=180, height=35,
        fg_color="#e67e22", hover_color="#d35400", corner_radius=8
    ).pack(pady=5)