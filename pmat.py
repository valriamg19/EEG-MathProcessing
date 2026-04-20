<<<<<<< HEAD
=======
#Python 3.9.0
#pip install -r requirements.txt

>>>>>>> eb4e616 (Actualizacion 2 200426)
import tkinter as tk
from PIL import Image, ImageTk
import random
import os
import time
<<<<<<< HEAD
#parametros ajustables
formato_estandar = 'png'
images_path = './images-test'
images_list = os.listdir(images_path)
process_time = 15000 #ms
pauses = 4000 #ms

print(images_list)
print(f"Imagenes cargadas:{len(images_list)-1}")
images_random = random.sample(images_list, len(images_list)) #revolver contenido
=======
from pygame import mixer #req
import json

start_program = time.perf_counter()
#parametros ajustables
tiempos = {'Tiempo de inicio': start_program
           
           
           
           }
fecha = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
filename = f't{fecha}.json'.replace(':', '-')
tiempos_path = f'./tiempos/{filename}'

leng_path = f'R{fecha}.json'.replace(':', '-')
respuestas_path = f'./respuestas/{leng_path}'



problems_path = './images-math'
images_math = os.listdir(problems_path)

sound_path = os.path.abspath('01.mp3')

words_path = './images-leng'
images_leng = os.listdir(words_path)

#Matematicas
process_time = 15000 #ms 15s
pauses = 4000 #ms

#Fuerza
reaccion_time = 2000 #ms 2s
imk = 4000 #ms 4s

#lenguaje
registro = [] #vacio inicio
>>>>>>> eb4e616 (Actualizacion 2 200426)




<<<<<<< HEAD
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
=======
print(images_math)
print(f"Operaciones matematicas:{len(images_math)}")
print(f"Palabras lenguaje:{len(images_leng)}")

random_leng = random.sample(images_leng, len(images_leng))
random_math = random.sample(images_math, len(images_math)) #revolver contenido


mixer.init()


def click(event):
    print("click")

def enter(event, valor, indice):
    content = entrada.get()
    print('Entrada:', content)
    registro.append(content) #guardar en registro
    end_time = time.perf_counter()
    duracion = round(end_time - start_program, 3)
    tiempos.update({f"Tiempo respuesta {indice}": duracion})
    entrada.delete(0, tk.END) #limpiar entrada
    eliminacion(indice, valor) #comienza descanso

def finalizado(valor):
    tk.Label(root, text="Proceso finalizado", font=("Arial", 14), bg='white').pack(pady=50)
    root.after(4000, root.destroy)
    end_program = time.perf_counter()
    duracion_total = end_program - start_program
    tiempos.update({"Tiempo total del programa": duracion_total})
    print(tiempos)
    with open(tiempos_path, 'w') as f:
        json.dump(tiempos, f, indent=4)
    if valor == 3:
        with open(respuestas_path, 'w') as f:
            json.dump(registro, f, indent=4)


def sig_mat(indice, valor):
    
    if valor == 1: #Matematico
        if int(indice) < len(random_math):
            print(indice)
            filename = random_math[indice]
            #Cargar
            img = Image.open(problems_path+'\\'+filename).resize((790,200))
            foto = ImageTk.PhotoImage(img)
            imagen_label.config(image = foto)
            imagen_label.image = foto # pyright: ignore[reportAttributeAccessIssue]
            imagen_label.pack(pady=220)
            #eliminacion
            root.after(process_time, lambda: eliminacion(indice+1, valor)) #Despues del tiempo de procesamiento elimina la imagen
        else:
            print("Ya no existen mas imagenes por presentar")
            finalizado(valor)


    elif valor == 2: #Fuerza izquierda
        if int(indice) < 25:
            print(indice)
            mixer.music.load(sound_path)
            mixer.music.play()
            root.config(bg="green") #Cambio de fondo
            
            root.after(imk, lambda: eliminacion(indice+1, valor)) #imk 4000s Duracion del estimulo y despues borra
        
        else:
            print("Proceso finalizado")
            finalizado(valor)
    
    elif valor == 3: #Lenguaje
        if int(indice) <3:
            print(indice)
            filename = random_leng[indice]
            #Cargar
            img = Image.open(words_path+'\\'+filename).resize((400,400))
            foto = ImageTk.PhotoImage(img)
            imagen_label.config(image = foto)
            imagen_label.image = foto # pyright: ignore[reportAttributeAccessIssue]
            imagen_label.pack(pady=220)
            

            entrada.place(relx=0.5, rely=0.20, anchor='center') #Posicion de la entrada
            entrada.bind('<Return>', lambda event: enter(event, valor, indice+1)) #Evento de presionar Enter para guardar respuesta


            #eliminacion
            #root.after(2000, lambda: eliminacion(indice+1, valor)) #Despues del tiempo de procesamiento elimina la imagen


        else:
            print("Ya no existen mas imagenes por presentar")
            finalizado(valor)



def eliminacion(indice, valor): #descanso
    
    if valor == 1:
        imagen_label.pack_forget()# Eliminacion
        end_time = time.perf_counter()
        duracion = round(end_time - start_program, 3)
        tiempos.update({f"Tiempo respuesta {indice}": duracion})
        root.after(pauses, lambda: sig_mat(indice, valor)) #Vuelve a iniciar la funcion para mostrar nueva imagen
    
    elif valor == 2:
        descanso = (random.randint(2, 7) * 1000) + reaccion_time #ms 2-7s
        print(f"Descanso de {int(descanso/1000)}s")
        root.config(bg="white") #Cambio de fondo
        end_time = time.perf_counter()
        duracion = round(end_time - start_program, 3)
        tiempos.update({f"Tiempo respuesta {indice}": duracion})

        root.after(descanso, lambda: sig_mat(indice, valor)) #Vuelve a iniciar la funcion para mostrar nueva imagen

    if valor == 3:
        leng_delay = random.randint(2,5) * 1000 #ms 2-5s
        entrada.place_forget()
        imagen_label.pack_forget()# Eliminacion
        end_time = time.perf_counter()
        duracion = round(end_time - start_program, 3)
        tiempos.update({f"Tiempo respuesta {indice}": duracion})
        root.after(leng_delay, lambda: sig_mat(indice, valor)) #Vuelve a iniciar la funcion para mostrar nueva imagen
    

               
def iniciar_proceso(valor):
   
    boton_math.pack_forget()
    botonfder.pack_forget()
    botonfizq.pack_forget()
    botonlen.pack_forget()

    if valor == 1:
        etiqueta_proceso = tk.Label(root, text=f"Proceso inicializado. Espera {int(pauses/1000)}s", font=("Arial", 14))
        etiqueta_proceso.pack(pady=50)


        root.after(pauses, lambda: etiqueta_proceso.pack_forget())
        
        root.after(pauses, lambda: sig_mat(0, valor)) #valor inicial de arranque

    elif valor == 2:
        etiqueta_proceso = tk.Label(root, text=f"Proceso inicializado. Espera {int(reaccion_time/1000)}s", font=("Arial", 14))
        etiqueta_proceso.pack(pady=50)

        root.after(reaccion_time, lambda: etiqueta_proceso.pack_forget())
        root.after(reaccion_time, lambda:sig_mat(0, valor))

    elif valor == 3:
        etiqueta_proceso = tk.Label(root, text=f"Proceso inicializado. Espera {int(reaccion_time/1000)}s", font=("Arial", 14))
        etiqueta_proceso.pack(pady=50)

        root.after(2000, lambda: etiqueta_proceso.pack_forget())
        root.after(2000, lambda:sig_mat(0, valor))
        

    
#configracion de la ventana
root = tk.Tk()
root.title("Interfaz de pruebas")
root.config(bg="white")
root.geometry("400x200")

entrada = tk.Entry(
    root, 
    font = ('Arial', 12),
    justify= 'center',
    width=30)

boton_math = tk.Button(
    root, 
    text="Matemático", 
    command=lambda: iniciar_proceso(1), 
    bg="green", 
    fg="white", 
    padx=10, 
    pady=4,

)
botonfizq = tk.Button(
    root, 
    text="Fuerza IZQ", 
    command=lambda: iniciar_proceso(2), 
    bg="blue", 
    fg="white", 
    padx=10, 
    pady=4,

)
botonfder = tk.Button(
    root, 
    text="Fuerza DER", 
    command=lambda: iniciar_proceso(2), 
    bg="blue", 
    fg="white", 
    padx=10, 
    pady=4,

)
botonlen = tk.Button(
    root, 
    text="Lenguaje", 
    command=lambda: iniciar_proceso(3), 
    bg="green", 
    fg="white", 
    padx=10, 
    pady=4,
)


boton_math.pack(pady=20, anchor="s") #Agregar boton
botonfizq.pack(pady=40, anchor="s") #Agregar boton
botonfder.pack(pady=60, anchor="s") #Agregar boton
botonlen.pack(pady=80, anchor="s") #Agregar boton

>>>>>>> eb4e616 (Actualizacion 2 200426)
imagen_label = tk.Label(root)
root.mainloop()