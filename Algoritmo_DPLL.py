import copy
def neg(a):
    if len(a) == 1:
        l = "-" + a
    else:
        l = a[-1]
    return l


def unitPropagate(clausulas,I):
    #print(clausulas)
    #print(I)
    while listUni(clausulas):
        for clau in clausulas:
            if len(clau)==1:
                literal=clau[0]
                #print(literal)
                #aumentando diccionario
                if len(literal)==1:
                    I[literal]=1
                else:
                    I[literal[1]]=0
                #quitando clausula
                C=[x for x in clausulas if literal not in x]
                litC=complemento(literal)
                for c in C:
                    if litC in c:
                        c.remove(litC)
        clausulas=C
    return clausulas, I


# S Conjunto de clausulas , I interpretación parcial
#Algoritmo DPLL
def DPLL(s, i):
    void = []
    #print(i)
    s,i = unitPropagate(s,i)
    if void in s:#Si s tiene una clausula vacía
        return "Insatisfacible", {}
    elif len(s) == 0:#Si s es vacía
        return "Satisfacible", i
    l = "" # Literal
    for y in s:
        for x in y:
            if x not in i.keys():
                l = x
    l_comp = neg(l) # l complemento
    if l == "":
        return None
    Sp = copy.deepcopy(s)
    Sp = [n for n in Sp if l not in n]
    for q in Sp:
        if l_comp in q:
            q.remove(neg(l))
    Ip = copy.deepcopy(i)
    if l[0] == "-":
        Ip[l[1]] = 0
    else:
        Ip[l] = 1
    S1, I1 = DPLL(Sp, Ip)
    if S1 == "Satisfacible":
        return S1, I1
    else:
        Spp = copy.deepcopy(s)
        Spp = [q for q in Spp if neg(l) not in q]
        for h in Spp:
            if l in h:
                h.remove(l)
        Ipp = copy.deepcopy(i)
        if l[0] == "-":
            Ipp[l[1]] = 0
        else:
            Ipp[l] = 1
        return DPLL(Spp, Ipp)

def listUni(lista):
    for i in lista:
        if len(i)==1:
            return True
    return False

def complemento(literal):
    if len(literal)==1:
        literal="-"+literal
    else:
        literal=literal[1]
    return literal
