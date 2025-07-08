import customtkinter as ctk
from tkinter import messagebox
from models.Estudiante import Estudiante

def abrir_formulario_actualizar(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Actualizar Estudiante")
    ventana.geometry("520x580")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(ventana, text="Actualizar estudiante", font=("Segoe UI", 18, "bold"), text_color="white").pack(pady=20)

    entrada_codigo = ctk.CTkEntry(ventana, placeholder_text="Código del estudiante a actualizar", width=350)
    entrada_codigo.pack(pady=10)

    campos = {}
    for campo in ["Nombre", "Correo", "Facultad", "Carrera"]:
        ctk.CTkLabel(ventana, text=campo, font=("Segoe UI", 12), text_color="white").pack()
        entrada = ctk.CTkEntry(ventana, width=350)
        entrada.pack(pady=5)
        campos[campo.lower()] = entrada

    def actualizar():
        try:
            codigo = int(entrada_codigo.get().strip())
        except ValueError:
            messagebox.showerror("Error", "El código debe ser un número entero válido.")
            return

        estudiante = gestor.buscar_por_codigo(codigo)
        if not estudiante:
            messagebox.showerror("No encontrado", f"No existe estudiante con código {codigo}.")
            return

        nombre = campos["nombre"].get().strip() or estudiante.nombre
        correo = campos["correo"].get().strip() or estudiante.correo
        facultad = campos["facultad"].get().strip() or estudiante.facultad
        carrera = campos["carrera"].get().strip() or estudiante.carrera

        if not all([nombre, correo, facultad, carrera]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if "@" not in correo or "." not in correo:
            messagebox.showerror("Error", "Correo no válido.")
            return

        actualizado = Estudiante(codigo, nombre, correo, facultad, carrera)
        gestor.actualizar_entidad(codigo, actualizado)

        messagebox.showinfo("Éxito", f"Estudiante con código {codigo} actualizado correctamente.")
        # Limpiar campos después de actualizar
        entrada_codigo.delete(0, ctk.END)
        for entry in campos.values():
            entry.delete(0, ctk.END)

    def volver():
        ventana.destroy()
        from gui.core.GUI_Estudiante import mostrar_interfaz_estudiantes
        mostrar_interfaz_estudiantes()

    ctk.CTkButton(
        ventana,
        text="Actualizar",
        command=actualizar,
        font=("Segoe UI", 13),
        width=150,
        height=35,
        corner_radius=8
    ).pack(pady=15)

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
    ).pack(pady=10)

def volver(ventana):
    ventana.destroy()
    from gui.core.GUI_Estudiante import mostrar_interfaz_estudiantes
    mostrar_interfaz_estudiantes()