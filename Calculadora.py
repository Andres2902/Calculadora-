from tkinter import ttk, messagebox
import tkinter as tk

Ventana = tk.Tk() #crear ventana
titulo = Ventana.title("Calculadora UV") #titulo de la ventana
Ventana.geometry("300x500+200+100") #tamaño de la ventana
Ventana.configure(bg='Black') #color de la ventana

# Variable para almacenar el primer número
primer_numero = 0
# Variable para almacenar la operación
operacion = ""


#Funciones 

def suma():
    global primer_numero, operacion
    primer_numero = float(numero_entr.get()) if numero_entr.get() else 0
    operacion = "+"

    limpiar_campos()
    return

def resta():
    global primer_numero, operacion
    primer_numero = float(numero_entr.get()) if numero_entr.get() else 0
    operacion = "-"
    limpiar_campos()
    return

def multiplicacion():
    global primer_numero, operacion
    primer_numero = float(numero_entr.get()) if numero_entr.get() else 0
    operacion = "x"
    limpiar_campos()
    return

def division():
    global primer_numero, operacion
    primer_numero = float(numero_entr.get()) if numero_entr.get() else 0
    operacion = "÷"
    limpiar_campos()
    return

def raiz_cuadrada():
    global primer_numero, operacion
    primer_numero = float(numero_entr.get()) if numero_entr.get() else 0
    operacion = "√"
    limpiar_campos()
    return

def elevado_al_cuadrado():
    global primer_numero, operacion
    primer_numero = float(numero_entr.get()) if numero_entr.get() else 0
    operacion = "x²"
    limpiar_campos()
    return

def escribir_numero(numero):
    contenido_actual = numero_entr.get()
    numero_entr.delete(0, tk.END)
    numero_entr.insert(0, contenido_actual + numero)

def equal():
    global primer_numero, operacion
    try:
        segundo_numero = eval(numero_entr.get()) if numero_entr.get() else 0
        if operacion == "+":
            resultado = primer_numero + segundo_numero
        elif operacion == "-":
            resultado = primer_numero - segundo_numero
        elif operacion == "x":
            resultado = primer_numero * segundo_numero
        elif operacion == "÷":
            if segundo_numero == 0:
                raise ZeroDivisionError
            resultado = primer_numero / segundo_numero
        elif operacion == "√":
            if primer_numero < 0:
                raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
            resultado = primer_numero**0.5
        elif operacion == "x²":
            resultado = primer_numero**2
        else:
            resultado = segundo_numero

        numero_entr.delete(0, tk.END)
        if 'resultado' in locals():
            numero_entr.insert(0, resultado)


    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception:
        messagebox.showerror("Error", "Entrada inválida.")

    


    numero_entr.delete(0, tk.END)
    numero_entr.insert(0, resultado)
    return

def limpiar_campos():
    numero_entr.delete(0, tk.END)

    return

def porcentaje():
    try:
        contenido_actual = float(numero_entr.get())
        resultado = contenido_actual / 100
        numero_entr.delete(0, tk.END)
        numero_entr.insert(0, str(resultado))
    except ValueError:
        messagebox.showerror("Error", "Entrada inválida.")


#Interfaz:


numero_entr= tk.Entry(Ventana, width=10, font=("Arial", 34)) #crear una entrada de texto
numero_entr.place(x=10, y=30, width=280, height=50) #ubicacion de la entraad de texto

#Botones:

sumar_bot= tk.Button(Ventana, text="+", command=suma ,font=("Arial", 27),width=2, height=1) #crear botón, command ejecuta la funcion que va despues del igual
sumar_bot.place(x= 225 , y= 260 )

restar_bot= tk.Button(Ventana, text="-", command=resta ,font=("Arial", 27 ),width=2, height=1) #crear botón 
restar_bot.place(x= 225 , y= 340 )

multiplicar_bot= tk.Button(Ventana, text="x", command=multiplicacion ,font=("Arial", 27 ),width=2, height=1) #crear botón 
multiplicar_bot.place(x= 225 , y= 180 )

equal_bot= tk.Button(Ventana, text="=", command=equal ,font=("Arial", 27 ),width=2, height=1) #crear botón 
equal_bot.place(x= 225 , y= 420 )


dividir_bot= tk.Button(Ventana, text="÷", command=division ,font=("Arial", 27 ),width=2, height=1) #crear botón 
dividir_bot.place(x= 225 , y= 100 )

clear_bot= tk.Button(Ventana, text="C", command=limpiar_campos ,font=("Arial", 27 ),width=2, height=1) #crear botón 
clear_bot.place(x= 25 , y= 100 )

cuadrado_bot= tk.Button(Ventana, text="x²", command=elevado_al_cuadrado ,font=("Arial", 27 ),width=2, height=1) #crear botón 
cuadrado_bot.place(x= 90 , y= 100 )

raiz_bot= tk.Button(Ventana, text="√", command=raiz_cuadrada ,font=("Arial", 27 ),width=2, height=1) #crear botón 
raiz_bot.place(x= 160 , y= 100 )

punto_bot = tk.Button(Ventana, text=".", command=lambda: escribir_numero("."), font=("Arial", 27), width=2, height=1)
punto_bot.place(x=160, y=420)

porcentaje_bot = tk.Button(Ventana, text="%", command=porcentaje, font=("Arial", 27), width=2, height=1)
porcentaje_bot.place(x=25, y=420)


# Botones de números
botones = [
    ("7", 25, 180), ("8", 90, 180), ("9", 160, 180),
    ("4", 25, 260), ("5", 90, 260), ("6", 160, 260),
    ("1", 25, 340), ("2", 90, 340), ("3", 160, 340),
    ("0", 90, 420)]

for (texto, x, y) in botones:
    boton = tk.Button(Ventana, text=texto, command=lambda t=texto: escribir_numero(t), font=("Arial", 27), width=2, height=1)
    boton.place(x=x, y=y)


sumar_bot.configure(bg="orange")
restar_bot.configure(bg="orange")
multiplicar_bot.configure(bg="orange")
dividir_bot.configure(bg="orange")
equal_bot.configure(bg="green", fg="white")

Ventana.mainloop()
