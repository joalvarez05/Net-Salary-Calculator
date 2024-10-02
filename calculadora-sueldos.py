import tkinter as tk
from tkinter import font


def calcular_sueldo_neto():
    try:
        salario_bruto = float(entry_salario_bruto.get())
        jubilacion = salario_bruto * 0.11
        obra_social = salario_bruto * 0.06
        descuentos_totales = jubilacion + obra_social
        salario_neto = salario_bruto - descuentos_totales
        result_var.set(f"Su salario Neto es: ${salario_neto:.2f}")
    except ValueError:
        result_var.set("Error: Ingresa un número válido por favor.")


ventana = tk.Tk()
ventana.title("Calculadora de Liquidación de Sueldos")

ventana.geometry("400x300")

ventana.configure(bg="#f0f0f0")

fuente = font.Font(family="Helvetica", size=12)

frame = tk.Frame(ventana, bg="#f0f0f0")
frame.pack(pady=20)

tk.Label(frame, text="Salario Bruto:", bg="#f0f0f0",
         font=fuente).grid(row=0, column=0, padx=10, pady=10)
entry_salario_bruto = tk.Entry(frame, font=fuente)
entry_salario_bruto.grid(row=0, column=1, padx=10, pady=10)

boton_calcular = tk.Button(
    frame, text="Calcular", command=calcular_sueldo_neto, font=fuente, bg="#4CAF50", fg="white")
boton_calcular.grid(row=1, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
label_result = tk.Label(frame, textvariable=result_var,
                        bg="#f0f0f0", font=fuente)
label_result.grid(row=2, column=0, columnspan=2, pady=10)

ventana.mainloop()
