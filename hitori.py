import random
from tkinter import *

app = Tk()
app.title("HITORI")
app.config(bg="light blue")
nf=4
nc=4
def codifica(f, c, Nf, Nc):
    # Funcion que codifica la fila f y columna c
    n = Nc * (f - 1) + c
    # print(u'Número a codificar:', n)
    return n+256
    
def codifica3(f, c, o, Nf, Nc, No):
    # Funcion que codifica la fila f, columna c, y objeto o
    v1 = codifica(f + 1, c + 1, Nf, Nc)
    v2 = codifica(v1, o, Nf * Nc, No)
    return v2

def decodifica(x, Nf, Nc):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla
    n = x
    n = n - 1
    f = int(n / Nc) + 1
    c = n % Nc + 1
    return f, c

def decodifica3(x, Nf, Nc, No):
    # Funcion que codifica un caracter en su respectiva fila f, columna c y objeto o
    v1, o = decodifica(x, Nf * Nc, No)
    f, c = decodifica(v1, Nf, Nc)
    return f, c, o    
    
def dic_creator():
    dic={}
    props=[]
    for i in range(nf):
        for j in range(nc):
            num=random.randint(1, 9)
            x=codifica3(num, i, j, nf, nc, 9)
            x=chr(x+255)
            props.append(x)
            dic[x]=1
    return dic
        
def empezar():
    dic=dic_creator()
    nums=[]
    for j in dic.keys():
        v1,n=decodifica(ord(j)-255, nf*nc, 9)
        f,c=decodifica(v1, nf, nc)
        num=(f,c,n)
        nums.append(num)
    print(nums)
    cont=0    
    for i in range(4):
        color1=["white", "gray","white", "gray"]
        color2=["gray", "white","gray", "white"]
        a=nums[cont]
        cont+=1
        b=nums[cont]
        cont+=1
        c=nums[cont]
        cont+=1
        d=nums[cont]
        cont+=1
        
        
        label_1 = Label(app,width= "13",height = "5" , bg= color1[i] , text= str(a),pady="1", padx="2")
        label_2 = Label(app,width= "13",height = "5" , bg= color2[i], text= str(b) ,pady="1", padx="2")
        label_3 = Label(app,width= "13",height = "5" , bg= color1[i], text= str(c),pady="1", padx="2" )
        label_4 = Label(app,width= "13",height = "5" , bg= color2[i], text= str(d),pady="1", padx="2")
        
        label_1.grid(row = i , column = 0)
        label_2.grid(row = i , column = 1)
        label_3.grid(row = i , column = 2)
        label_4.grid(row = i , column = 3)

"""
def rule1(dic):
    fila=[]
    colm=[]
    nums=[]
    keys=[]
    fals_dic={}
    cont=0
    dif=1
    fals=[]
    for j in dic.keys():
        j=decode(j, int(cont/4), cont%4, dif)
        dif+=1
        nums.append(j)
        cont=cont+1
    cont=0
    for i in range(4):
        fila.append(nums[cont])
        fila.append(nums[cont+1])
        fila.append(nums[cont+2])
        fila.append(nums[cont+3])
        cont+=4
    for i in range(4):
        colm.append(nums[i])
        colm.append(nums[i+4])
        colm.append(nums[i+8])
        colm.append(nums[i+12])        
    indx=0
    for k in range(4):
        cont=3
        for i in range(4):
            for j in range(cont):
                if fila[i]==fila[j+i+1]:
                    fals.append(indx)
                    break
            cont=cont-1
            indx+=1
        for h in range(4):
            fila.pop(0)
    indx=0
    for k in range(4):
        cont=3
        indx=k
        for i in range(4):
            for j in range(cont):
                if colm[i]==colm[j+i+1]:
                    fals.append(indx)
                    break
            cont=cont-1
            indx+=4
        for h in range(4):
            colm.pop(0)
    for i in dic.keys():
        keys.append(i)
    for i in fals:
        fals_dic[keys[i]]=1
    return fals_dic
"""  
        

#Barra de menú
bm = Menu(app)
mnuJuego = Menu(bm)
mnuJuego.add_command(label="Nuevo" , command = empezar)
mnuJuego.add_separator()
mnuJuego.add_command(label="Solución")
mnuayuda = Menu(bm)
mnuayuda.add_command(label= "Acerca del juego")
bm.add_cascade(label="Juego",menu=mnuJuego)
bm.add_cascade(label="Ayuda",menu=mnuayuda)
app.config(menu=bm)

#ejecucion
    
empezar()

app.mainloop()