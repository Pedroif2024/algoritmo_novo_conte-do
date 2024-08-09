y=20#VARIAVEL GLOBAL
def outra_funcao():
    global y
    y=15
    print(y)
    
outra_funcao()
print(y)