import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
tk.Label (ventana, text="Hola,mundo").pack()
tk.Button (ventana, text="Cerrar", command=ventana.quit).pack()
ventana.mainloop()


print ("Hola mundo")
print("Hola mundo X2")