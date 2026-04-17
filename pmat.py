import tkinter as tk
from PIL import Image, ImageTk
import random
import os
import time
#parametros ajustables
formato_estandar = 'png'
images_path = './images-test'
images_list = os.listdir(images_path)
process_time = 15000 #ms
pauses = 4000 #ms

print(images_list)
print(f"Imagenes cargadas:{len(images_list)-1}")
images_random = random.sample(images_list, len(images_list)) #revolver contenido




def mostrar_siguiente(indice):

    if int(indice) < len(images_random):
        filename = images_random[indice]
        #Cargar
        img = Image.open(images_path+'\\'+filename).resize((790,200))
        foto = ImageTk.PhotoImage(img)
        imagen_label.config(image = foto)
        imagen_label.image = foto
        imagen_label.pack(pady=220)
        #eliminacion
        root.after(process_time, lambda: eliminacion(indice+1))
    else:
        print("Ya no existen mas imagenes por presentar")
        imagen_label.config(text="Proceso finalizado")
        imagen_label.pack()
        root.after(4000)
        exit()


def eliminacion(indice):
    imagen_label.pack_forget()


    root.after(pauses, lambda: mostrar_siguiente(indice + 1))


               
def iniciar_proceso():
   
    boton_inicio.pack_forget()

    etiqueta_proceso = tk.Label(root, text="Proceso inicializado. Espera 4s", font=("Arial", 14))
    etiqueta_proceso.pack(pady=50)

    root.after(4000, lambda: etiqueta_proceso.pack_forget())
    root.after(4000, lambda: mostrar_siguiente(0))
    

root = tk.Tk()
root.title("Procesamiento matemático")
root.geometry("400x200")


boton_inicio = tk.Button(
    root, 
    text="Iniciar", 
    command=iniciar_proceso, 
    bg="green", 
    fg="white", 
    padx=10, 
    pady=4
)


boton_inicio.pack(pady=20, anchor="s") #Agregar boton
imagen_label = tk.Label(root)
root.mainloop()