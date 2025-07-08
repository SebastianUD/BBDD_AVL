import customtkinter as ctk
from tkinter import messagebox

def mostrar_formulario_eliminar_materia(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Eliminar Materia")
    ventana.geometry("500x320")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Eliminar materia por código",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    entrada_codigo = ctk.CTkEntry(ventana, placeholder_text="Ingrese código de la materia", width=340)
    entrada_codigo.pack(pady=10)

    def eliminar():
        try:
            codigo = int(entrada_codigo.get())
            materia = gestor.buscar_por_codigo(codigo)

            if not materia:
                messagebox.showerror("Error", f"No se encontró la materia con código {codigo}")
                return

            confirmacion = messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar la materia: {materia.nombre}?")
            if confirmacion:
                gestor.eliminar_entidad(codigo)
                messagebox.showinfo("Eliminado", "Materia eliminada exitosamente")
                ventana.destroy()
                from gui.core.GUI_Materia import mostrar_interfaz_materias
                mostrar_interfaz_materias()

        except ValueError:
            messagebox.showerror("Error", "El código debe ser un número entero")

    ctk.CTkButton(
        ventana, text="Eliminar", command=eliminar,
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