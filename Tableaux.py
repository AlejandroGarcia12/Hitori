from random import choice

##############################################################################
# Variables globales
##############################################################################
nf=4
nc=4
no=10
# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(256, 1000)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

def decodifica(n, Nf, Nc):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla

    assert((n >= 0) and (n <= Nf * Nc - 1)), 'Codigo incorrecto! Debe estar entre 0 y' + str(Nf * Nc - 1) + "\nSe recibio " + str(n)

    f = int(n / Nc)
    c = n % Nc
    return f, c

def decodifica3(x, nf, nc, no):
    # Funcion que codifica un caracter en su respectiva fila f, columna c y objeto o
    v1, o = decodifica(x, nf * nc, no)
    f, c = decodifica(v1, nf, nc)
    return f, c, o

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"
def Inorder1(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
        
		return str(decodifica3(ord(f.label)-256, nf, nc, no) )
	elif f.label == '-':
		return f.label + Inorder1(f.right)
	else:
		return "(" + Inorder1(f.left) + f.label + Inorder1(f.right) + ")"

def StringtoTree(A):
	global letrasProposicionales
	treelist=[]
	for i in A:
		if i in letrasProposicionales:
			treelist.append(Tree(i,None, None))
		elif i=="-":
			faux=Tree(i,None,treelist[-1])
			treelist.pop(-1)
			treelist.append(faux)
		elif i in ["O","Y",">","="]:
			faux=Tree(i,treelist[-1],treelist[-2])
			treelist.pop(-1)
			treelist.pop(-1)
			treelist.append(faux)
	return treelist[0]

##############################################################################
# Definición de funciones de tableaux
##############################################################################

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"

def par_complementario(l):
	# Esta función determina si una lista de solo literales
	# contiene un par complementario
	# Input: l, una lista de literales
	# Output: True/False
    for i in l:
        if i.label == "-":
            if i.right.label in ["-","Y","O",">"]:
                continue
            else:
                for j in l:
                    if i.right.label == j.label:
                        return True
    return False

def es_literal(f):
	# Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
	# Output: True/False
    if f.right == None:
        return True
    elif f.label == "-" and f.right.label not in [">","-","Y","O"]:
        return es_literal(f.right)
    elif f.left != None:
        return False
    else: return False

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
	for i in l:
		#revisa si la formula i de la lista l es literal
		if es_literal(i):
			continue
		# si i no es literal, la retorna y termina la funcion
		else:
			return i
	# Cuando i no es literal para todo i en l, retorna None
	return None


def clasifica_y_extiende(hoja, f):

	global listaHojas

	tipo = ""
	#===TIPO_ALFA===#
	if (f.label == '-') and (f.right.label == '-'):
		tipo = "ALFA1"

	elif (f.label == 'Y'):
		tipo = "ALFA2"

	elif (f.label == '-') and (f.right.label == 'O'):
		tipo = "ALFA3"

	elif (f.label == '-') and (f.right.label == '>'):
		tipo = "ALFA4"

	#===TIPO_BETA===#
	elif (f.label == '-') and (f.right.label == 'Y'):
		tipo = "BETA1"

	elif (f.label == 'O'):
		tipo = "BETA2"

	elif (f.label == '>'):
		tipo = "BETA3"

	#===CONVERSIÓN===#
	# Alfa
	if (tipo == "ALFA1"):
		A1 = f.right.right

		hoja.remove(f)

		hoja.append(A1)
		# print("ALFA1", (Inorder(i) for i in hoja))

	elif (tipo == "ALFA2"):
		A1 = f.left
		A2 = f.right

		hoja.remove(f)

		hoja.append(A1)
		hoja.append(A2)
		# print("ALFA2", (Inorder(i) for i in hoja))

	elif (tipo == "ALFA3"):
		nA1 = Tree("-", None, f.right.left)
		nA2 = Tree("-", None, f.right.right)

		hoja.remove(f)

		hoja.append(nA1)
		hoja.append(nA2)
		# print("ALFA3", (Inorder(i) for i in hoja))

	elif (tipo == "ALFA4"):
		A1 = f.right.left
		nA2 = Tree("-", None, f.right.right)

		hoja.remove(f)

		hoja.append(A1)
		hoja.append(nA2)

	# Beta
	elif (tipo == "BETA1"):
		nB1 = Tree("-", None, f.right.left)
		nB2 = Tree("-", None, f.right.right)

		hoja.remove(f)
		h_aux = [f for f in hoja]

		hoja.append(nB1)
		h_aux.append(nB2)

		listaHojas.append(h_aux)

	elif (tipo == "BETA2"):
		B1 = f.left
		B2 = f.right

		hoja.remove(f)
		h_aux = [f for f in hoja]

		hoja.append(B1)
		h_aux.append(B2)

		listaHojas.append(h_aux)

	elif (tipo == "BETA3"):
		nB1 = Tree("-", None, f.left)
		B2 = f.right

		hoja.remove(f)
		h_aux = [f for f in hoja]

		hoja.append(nB1)
		h_aux.append(B2)

		listaHojas.append(h_aux)

def Tableaux(f):
	# Algoritmo de creacion de tableau a partir de lista_hojas

	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f
	global listaHojas
	global listaInterpsVerdaderas # acá se incluiran las hojas con 0

	A = StringtoTree(f)
	print("la fórmula ingresada es: ", Inorder(A))

	listaHojas = [[A]]

	while (len(listaHojas)>0):
		hoja = listaHojas[0]
		f = no_literales(hoja)
		# f == none si hoja solo contiene literales
		if f == None:
			# si hoja contiene un par complementario es removida de listaHojas
			if par_complementario(hoja):
				listaHojas.remove(hoja)
			# si hoja no contiene ningun par complementario, la añadimos a
			# listaInterpsVerdaderas y la removemos de listaHojas
			else:
				listaInterpsVerdaderas.append(hoja)
				listaHojas.remove(hoja)
		else:
			clasifica_y_extiende(hoja, f)

	return listaInterpsVerdaderas

if __name__ == '__main__':
	A = "sr>-qpO-Y--"
	A1= StringtoTree(A)
	print(Inorder(A1))
	B = "q-p-YqpOY"
	B1= StringtoTree(B)
	print(Inorder(B1))
	C =  "p-pY-"
	C1= StringtoTree(C)
	print(Inorder(C1))
	D = "sr>-qpO-Y--q-p-YqpOY-Ysr>-qpO-Y--q-p-YqpOY-YO-"
	D1= StringtoTree(D)
	print(Inorder(D1))
	AD = "sr>-qpO-Y--->sr>-qpO-Y--q-p-YqpOY-Ysr>-qpO-Y--q-p-YqpOY-YO-"
	AD1= StringtoTree(AD)
	print(Inorder(AD1))
