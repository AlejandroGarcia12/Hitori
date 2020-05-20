import random
import Tableaux
import FNC
import copy
import Algoritmo_DPLL
from tkinter import *

app = Tk()
app.title("HITORI")
app.config(bg="light blue")

app2 = Tk()
app2.title("Solucion")
app2.config(bg="light blue")
nf=4
nc=4
no=10
letrasProposicionales = [chr(x) for x in range(256, 1000)]
def codifica(f, c, Nf, Nc):
    # Funcion que codifica la fila f y columna c

    assert((f >= 0) and (f <= Nf - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nf) - 1  + "\nSe recibio " + str(f)
    assert((c >= 0) and (c <= Nc)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1)  + "\nSe recibio " + str(c)

    n = Nc * f + c
    # print(u'Número a codificar:', n)
    return n



def decodifica(n, Nf, Nc):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla

    assert((n >= 0) and (n <= Nf * Nc - 1)), 'Codigo incorrecto! Debe estar entre 0 y' + str(Nf * Nc - 1) + "\nSe recibio " + str(n)

    f = int(n / Nc)
    c = n % Nc
    return f, c



def codifica3(f, c, o, nf, nc, no):
    # Funcion que codifica tres argumentos
    assert((f >= 0) and (f <= nf - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nf - 1) + "\nSe recibio " + str(f)
    assert((c >= 0) and (c <= nc - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1) + "\nSe recibio " + str(c)
    assert((o >= 0) and (o <= no)), 'Tercer argumento incorrecto! Debe ser un numero entre 0 y ' + str(No - 1)  + "\nSe recibio " + str(o)
    v1 = codifica(f, c, nf, nc)
    v2 = codifica(v1, o, nf * nc, no)
    return v2



def decodifica3(x, nf, nc, no):
    # Funcion que codifica un caracter en su respectiva fila f, columna c y objeto o
    v1, o = decodifica(x, nf * nc, no)
    f, c = decodifica(v1, nf, nc)
    return f, c, o


def dic_creator():
    dic={}
    props=[]
    for i in range(nf):
        for j in range(nc):
            num=random.randint(1, 9)
            x=codifica3(i, j, num, nf, nc, no)
            x=chr(x+256)
            props.append(x)
            dic[x]=1
    return dic




def tapada(f, c):
	color3 = "black"
	label_5 = Label(app2,width= "13",height = "5" , bg= color3, text= "t" ,pady="1", padx="2")
	label_5.grid(row = f , column = c)




def visualizar(dic):
    nums=[]
    #print(dic)
    if len(dic.keys())==0:
        return -1
    for j in dic.keys():
        aux=[]
        f,c,num =decodifica3(ord(j)-256, nf, nc, no)
        aux.append(f)
        aux.append(c)
        aux.append(num)
        #print("aux: ",aux)
        nums.append(aux)
    #print(nums)
    cont=0
    #print("numeros: ",nums)
    for i in range(4):
            color1=["white", "gray","white", "gray"]
            color2=["gray", "white","gray", "white"]
            a=nums[cont]
            numa=a[2]
            cont+=1
            b=nums[cont]
            numb=b[2]
            cont+=1
            c=nums[cont]
            numc=c[2]
            cont+=1
            d=nums[cont]
            numd=d[2]
            cont+=1
            #print(cont)
            
            if numa==0:
                tapada(a[0],a[1])
            else:
                if a[0]%2==0:
                    label_1 = Label(app2,width= "13",height = "5" , bg= color1[a[1]] , text= str(numa),pady="1", padx="2")
                else:
                    label_1 = Label(app2,width= "13",height = "5" , bg= color2[a[1]] , text= str(numa),pady="1", padx="2")
                label_1.grid(row =a[0] , column = a[1])
            if numb==0:
                tapada(b[0], b[1])
            else:
                if b[0]%2==0:
                    label_2 = Label(app2,width= "13",height = "5" , bg= color1[b[1]], text= str(numb) ,pady="1", padx="2")
                else:
                    label_2 = Label(app2,width= "13",height = "5" , bg= color2[b[1]], text= str(numb) ,pady="1", padx="2")
                label_2.grid(row = b[0] , column = b[1])
            if numc==0:
                tapada(c[0], c[1])
            else:    
                if c[0]%2==0:
                    label_3 = Label(app2,width= "13",height = "5" , bg= color1[c[1]], text= str(numc),pady="1", padx="2" )
                else:
                    label_3 = Label(app2,width= "13",height = "5" , bg= color2[c[1]], text= str(numc),pady="1", padx="2" )
                label_3.grid(row = c[0] , column = c[1])
            if numd==0:
                tapada(d[0], d[1])
            else:
                if d[0]%2==0:
                    label_4 = Label(app2,width= "13",height = "5" , bg= color1[d[1]], text= str(numd),pady="1", padx="2")
                else:
                    label_4 = Label(app2,width= "13",height = "5" , bg= color2[d[1]], text= str(numd),pady="1", padx="2")
                label_4.grid(row = d[0] , column = d[1])
        
        
        
        
def empezar():
    dic=dic_creator()
    #print(dic)
    nums=[]
    temp2=[]
    for j in dic.keys():
        f,c,num =decodifica3(ord(j)-256, nf, nc, no)
        nums.append(num)
    #print(nums)
    #print("props: ", dic.keys())
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
    regla0= Crear_regla0(dic)
    regla00= Crear_regla00()
    regla1= Crear_regla1(dic)
    regla2= Crear_regla2()
    regla3= Crear_regla3()
    regla = regla0+regla1+regla2+regla3+"Y"+"Y"+"Y"
    regla = regla00
    #print("regla: ", regla)
    print("Resolviendo")
    regla = Tableaux.StringtoTree(regla)
    print(".")
    regla2 = Tableaux.Inorder1(regla)
    regla = Tableaux.Inorder(regla)
    print(regla)
    print(".")
    regla = FNC.Tseitin(regla,letrasProposicionales)
    print("tseitin: ",regla)
    print(".")
    regla = FNC.formaClausal(regla)
    print(".")
    k={}
    print(".")
    s,newdic = Algoritmo_DPLL.DPLL(regla, k)
    print("listo!")
    print("s:",s)
    #print("diccionario: ",newdic)
    auxdic={}
    for key in newdic.keys():
        if key in letrasProposicionales and newdic[key]==1:
            temp=decodifica3(ord(key)-256, nf, nc, no)
            auxdic[key]=newdic[key]
            print("(f,c,num): ", temp)
    #print("regla algoritmo: ",auxdic) 
    print("vizualizando")
    visualizar(auxdic)
       

def Crear_regla00():
    inicial_regla=True
    for c in range(nc-3):
        for f in range(nf-2):
            for o in range(no-8):
                objetos=[x for x in range(10) if x!=o]
                inicial_clau=True
                for oi in objetos:
                    if inicial_clau:
                        clau=chr(codifica3(f, c, oi, nf, nc, no)+256)
                        inicial_clau=False
                    else:
                        clau+=chr(codifica3(f, c, oi, nf, nc, no)+256)+"O"  
                if inicial_regla:
                    regla=chr(codifica3(f, c, o, nf, nc, no)+256)+clau+"-"+"="
                    inicial_regla=False
                else:
                    regla+=chr(codifica3(f, c, o, nf, nc, no)+256)+clau+"-"+"="+"Y"
    return regla

def Crear_regla0an(dic):
    inicial_regla=True
    for c in range(nc):
        for f in range(nf):
            for o in range(no):
                if chr(codifica3(f, c, o, nf, nc, no)+256) in dic.keys():
                    if inicial_regla:
                        regla=chr(codifica3(f, c, o, nf, nc, no)+256)+chr(codifica3(f, c, 0, nf, nc, no)+256)+"O"+chr(codifica3(f, c, o, nf, nc, no)+256)+"-"+chr(codifica3(f, c, 0, nf, nc, no)+256)+"-"+"O"+"Y"
                        inicial_regla=False
                    else:
                        regla+=chr(codifica3(f, c, o, nf, nc, no)+256)+chr(codifica3(f, c, 0, nf, nc, no)+256)+"O"+chr(codifica3(f, c, o, nf, nc, no)+256)+"-"+chr(codifica3(f, c, 0, nf, nc, no)+256)+"-"+"O"+"Y"+"Y"
    
    return regla

def Crear_regla0(dic):
    inicial_regla=True
    for c in range(nc):
        for f in range(nf):
            for o in range(no):
                if chr(codifica3(f, c, o, nf, nc, no)+256) in dic.keys():
                    if inicial_regla:
                        regla=chr(codifica3(f, c, o, nf, nc, no)+256)+chr(codifica3(f, c, 0, nf, nc, no)+256)+"-"+"="
                        inicial_regla=False
                    else:
                        regla+=chr(codifica3(f, c, o, nf, nc, no)+256)+chr(codifica3(f, c, 0, nf, nc, no)+256)+"-"+"="+"Y"
    
    return regla 


#REGLA 1
#Eliminar casilla si en su fila o columna se encuentra un número repetido

def Crear_regla1an(dic):
    fila=[x for x in range(nf)]
    colum=[x for x in range(nc)]
    inicial_regla=True
    
    for f in fila:
        for c in colum:
            for o in range(1,10):
                letra=chr(codifica3(f, c, o, nf, nc, no)+256)
                if letra in dic.keys():
                    inicial_clau=True
                    otrasF=[x for x in fila if x!=f]
                    otrasC=[x for x in colum if x!=c]
                    for j in len(otrasC)-1:
                        if inicial_clau:
                            clau=chr(codifica3(f, otrasC[j], o, nf, nc, no)+256)+chr(codifica3(f, otrasC[j+1], o, nf, nc, no)+256)+"O"
                            inicial_clau=False
                        else:
                            clau+=chr(codifica3(f, j, o, nf, nc, no)+256)+"-"+"Y"
                    
                    for k in otrasF:
                        if inicial_clau:
                            clau=chr(codifica3(k, c, o, nf, nc, no)+256)+"-"
                            inicial_clau=False
                        else:
                            clau+=chr(codifica3(k, c, o, nf, nc, no)+256)+"-"+"Y"
                    if inicial_regla:
                        regla=clau+chr(codifica3(f, c, o, nf, nc, no)+256)+"="
                        inicial_regla=False
                    else:
                        regla+=clau+chr(codifica3(f, c, o, nf, nc, no)+256)+"="+"Y"
    return regla

def Crear_regla1(dic):
    fila=[x for x in range(nf)]
    colum=[x for x in range(nc)]
    inicial_regla=True
    
    for f in fila:
        for c in colum:
            for o in range(1,10):
                letra=chr(codifica3(f, c, o, nf, nc, no)+256)
                if letra in dic.keys():
                    inicial_clau=True
                    otrasF=[x for x in fila if x!=f]
                    otrasC=[x for x in colum if x!=c]
                    for j in otrasC:
                        if inicial_clau:
                            clau=chr(codifica3(f, j, o, nf, nc, no)+256)+"-"
                            inicial_clau=False
                        else:
                            clau+=chr(codifica3(f, j, o, nf, nc, no)+256)+"-"+"Y"
                    
                    for k in otrasF:
                        if inicial_clau:
                            clau=chr(codifica3(k, c, o, nf, nc, no)+256)+"-"
                            inicial_clau=False
                        else:
                            clau+=chr(codifica3(k, c, o, nf, nc, no)+256)+"-"+"Y"
                    if inicial_regla:
                        regla=clau+chr(codifica3(f, c, o, nf, nc, no)+256)+"="
                        inicial_regla=False
                    else:
                        regla+=clau+chr(codifica3(f, c, o, nf, nc, no)+256)+"="+"Y"
    return regla



                        
def Crear_regla2():
    fc=[1,2,3,0]
    inicial_regla=True
    for c in range(nc):
        for f in range(nf):
            inicial_clau=True
            adjaF=[x for x in fc if (x==f+1) or (x==f-1)]
            adjaC=[x for x in fc if (x==c+1) or (x==c-1)]
            for af in adjaF:
                if inicial_clau:
                    clau=chr(codifica3(af, c, 0, nf, nc, no)+256)+"-"
                    inicial_clau=False
                else:
                    clau+=chr(codifica3(af, c, 0, nf, nc, no)+256)+"-"+"Y"
            #print(clau)
            for ac in adjaC:
                if inicial_clau:
                    clau=chr(codifica3(f, ac, 0, nf, nc, no)+256)+"-"
                    inicial_clau=False
                else:
                    clau+=chr(codifica3(f, ac, 0, nf, nc, no)+256)+"-"+"Y"
            if inicial_regla:
                regla=clau+chr(codifica3(f, c, 0, nf, nc, no)+256)+">"
                inicial_regla=False
            else:
                regla+=clau+chr(codifica3(f, c, 0, nf, nc, no)+256)+">"+"Y"
    return regla



#Regla 3
#Las que no estan tapadas queden conectadas ortogonalmente
def Crear_regla3():
    #esquinas
    esq=""
    literal1 = codifica3(0,1,0,nf,nc,no)
    literal1=chr(literal1+256)
    literal2 = codifica3(1,0,0,nf,nc,no)
    literal2=chr(literal2+256)
    esq=literal1+literal2+"Y"+"-"
    literal1 = codifica3(0,2,0,nf,nc,no)
    literal1=chr(literal1+256)
    literal2 = codifica3(1,3,0,nf,nc,no)
    literal2=chr(literal2+256)
    esq=literal1+literal2+"Y"+"-"+esq+"Y"
    literal1 = codifica3(2,0,0,nf,nc,no)
    literal1=chr(literal1+256)
    literal2 = codifica3(3,1,0,nf,nc,no)
    literal2=chr(literal2+256)
    esq=literal1+literal2+"Y"+"-"+esq+"Y"
    literal1 = codifica3(2,3,0,nf,nc,no)
    literal1=chr(literal1+256)
    literal2 = codifica3(3,2,0,nf,nc,no)
    literal2=chr(literal2+256)
    esq=literal1+literal2+"Y"+"-"+esq+"Y"
    #Diagonales
    d1=""
    d2=""
    d3=""
    d4=""
    d5=""
    d6=""
    iniciald1=True
    iniciald2=True
    iniciald3=True
    for j in range(3):
        for i in range(3):
            literal1=codifica3(j,i,0,nf,nc,no)
            literal1=chr(literal1+256)
            literal2 = codifica3(j+1,i+1,0,nf,nc,no)
            literal2=chr(literal2+256)
            if j==0:
                if iniciald1:
                    d1=literal1+literal2+"Y"
                    iniciald1=False
                else:
                    d1=literal1+literal2+"Y"+d1+"O"
            elif j==1:
                if iniciald2:
                    d2=literal1+literal2+"Y"
                    iniciald2=False
                else:
                    d2=literal1+literal2+"Y"+d1+"O"
            elif j==2:
                if iniciald3:
                    d3=literal1+literal2+"Y"
                    iniciald3=False
                else:
                    d3=literal1+literal2+"Y"+d1+"O"
            literal1=codifica3(j+1,i,0,nf,nc,no)
            literal1=chr(literal1+256)
            literal2 = codifica3(j,i+1,0,nf,nc,no)
            literal2=chr(literal2+256)
            if j==0:
                if iniciald1:
                    d1=literal1+literal2+"Y"
                    iniciald1=False
                else:
                    d1=literal1+literal2+"Y"+d1+"O"
            elif j==1:
                if iniciald2:
                    d2=literal1+literal2+"Y"
                    iniciald2=False
                else:
                    d2=literal1+literal2+"Y"+d1+"O"
            elif j==2:
                if iniciald3:
                    d3=literal1+literal2+"Y"
                    iniciald3=False
                else:
                    d3=literal1+literal2+"Y"+d1+"O"
    iniciald1=True
    iniciald2=True
    iniciald3=True
    for j in range(3):
        for i in range(3):
            literal1=codifica3(i,j,0,nf,nc,no)
            literal1=chr(literal1+256)
            literal2 = codifica3(i+1,j+1,0,nf,nc,no)
            literal2=chr(literal2+256)
            if j==0:
                if iniciald1:
                    d4=literal1+literal2+"Y"
                    iniciald1=False
                else:
                    d4=literal1+literal2+"Y"+d1+"O"
            elif j==1:
                if iniciald2:
                    d5=literal1+literal2+"Y"
                    iniciald2=False
                else:
                    d5=literal1+literal2+"Y"+d1+"O"
            elif j==2:
                if iniciald3:
                    d6=literal1+literal2+"Y"
                    iniciald3=False
                else:
                    d6=literal1+literal2+"Y"+d1+"O"
            literal1=codifica3(i,j+1,0,nf,nc,no)
            literal1=chr(literal1+256)
            literal2 = codifica3(i+1,j,0,nf,nc,no)
            literal2=chr(literal2+256)
            if j==0:
                if iniciald1:
                    d4=literal1+literal2+"Y"
                    iniciald1=False
                else:
                    d4=literal1+literal2+"Y"+d1+"O"
            elif j==1:
                if iniciald2:
                    d5=literal1+literal2+"Y"
                    iniciald2=False
                else:
                    d5=literal1+literal2+"Y"+d1+"O"
            elif j==2:
                if iniciald3:
                    d6=literal1+literal2+"Y"
                    iniciald3=False
                else:
                    d6=literal1+literal2+"Y"+d1+"O"
    d=d6+"-"+d5+"-"+d4+"-"+"O"+"O"+d3+"-"+d2+"-"+d1+"-"+"O"+"O"+"Y"
    regla=d+esq+"Y"
    return regla


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
