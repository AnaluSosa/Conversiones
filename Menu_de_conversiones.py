import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# === Clase Principal ===
class crear_ventana_principal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Conversor de Unidades")
        self.crear_menu()

    def crear_menu(self):
        menu = tk.Menu(self.ventana)
        self.ventana.config(menu=menu)

        conversion_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Seleccionar Conversión", menu=conversion_menu)
        conversion_menu.add_command(label="Conversión de Longitud", command=self.abrir_longitud)
        conversion_menu.add_command(label="Conversión de Masa", command=self.abrir_masa)
        conversion_menu.add_command(label="Conversión de Tiempo", command=self.abrir_tiempo)

    def abrir_longitud(self):
        ConversorVentana("Longitud", [
            ("Metros a Kilómetros", lambda x: x / 1000),
            ("Pulgadas a Metros", lambda x: x * 0.0254)
        ])

    def abrir_masa(self):
        ConversorVentana("Masa", [
            ("Kilogramos a Gramos", lambda x: x * 1000),
            ("Libras a Kilogramos", lambda x: x * 0.453592)
        ])

    def abrir_tiempo(self):
        ConversorVentana("Tiempo", [
            ("Segundos a Minutos", lambda x: x / 60),
            ("Horas a Días", lambda x: x / 24)
        ])

# === Clase para ventanas de conversión ===
class ConversorVentana:
    def __init__(self, tipo, opciones):
        self.ventana = tk.Toplevel()
        self.ventana.title(f"Conversión de {tipo}")

        self.label_tipo = tk.Label(self.ventana, text=f"Conversión de {tipo}", font=("Arial", 14))
        self.label_tipo.pack(pady=10)

        self.combo = ttk.Combobox(self.ventana, values=[op[0] for op in opciones], state="readonly")
        self.combo.current(0)
        self.combo.pack(pady=5)

        self.entry_valor = tk.Entry(self.ventana)
        self.entry_valor.pack(pady=5)
        self.entry_valor.insert(0, "Ingrese un valor")

        self.boton_convertir = tk.Button(self.ventana, text="Convertir", command=self.convertir)
        self.boton_convertir.pack(pady=5)

        self.resultado_label = tk.Label(self.ventana, text="Resultado: ")
        self.resultado_label.pack(pady=5)

        self.opciones = opciones

    def convertir(self):
        try:
            valor = float(self.entry_valor.get())
            index = self.combo.current()
            nombre, funcion = self.opciones[index]
            resultado = funcion(valor)
            self.resultado_label.config(text=f"Resultado: {resultado:.4f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")

# === Ejecutar la aplicación ===
if __name__ == "__main__":
    ventana = tk.Tk()
    app = crear_ventana_principal(ventana)
    ventana.mainloop()