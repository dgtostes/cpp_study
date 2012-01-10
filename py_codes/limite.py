import sys

def limite(var, x, func, inter):
    f = func
    inicio = x - inter
    fim = x + inter
    mod_x = modulo(x)
    modulo_inicio = modulo(inicio)
    modulo_fim = modulo(fim)
    incremento = modulo(mod_x-modulo_inicio)/float(var)
    dic_testes = gera_dic_teste(incremento, x, var)
    numero_elementos_dic = len(dic_testes)
    print numero_elementos_dic
    i = numero_elementos_dic - 1
    while i >=0:
        print f(dic_testes[i][1])-f(dic_testes[i][0])
        i = i - 1
    

def gera_dic_teste(incremento, target, numero_de_testes):
    target = target
    dic = {}
    for i in range(0, numero_de_testes):
        dic[i] = (target-incremento*i, target+incremento*i)

    return dic
      
    
def modulo(x):
    if x >=0:
        return x
    else:
        return x*-1


def projecao(inicial, juros, dep_mensal, anos):
    total = inicial
    for i in range(0, anos*12):
        total = total + total*juros
        total = total + dep_mensal

    return total


if __name__ == "__main__":
    x =float(sys.argv[1])
    func = eval(sys.argv[2])
    #limite(30, 9, lambda x:x*x, 0.0001)
    limite(30, x, func, 0.0001)
#    print 

    #lista = gera_lista_teste(0.01,-2,0)
    #print lista
    #print len(lista)
#    print gera_dic_teste(0.1, 9, 30)
##    dep = 300
##    while dep < 1000:
##        print 'dep - %s --> total: %.2f' % (dep,projecao(7000, 0.005, dep, 20))
##        dep = dep + 50
##    dep = 300
##    while True:
##        if projecao(7000, 0.006, dep, 20) >= 1000000:
##            print dep
##            break
##        else:
##            dep = dep + 50
