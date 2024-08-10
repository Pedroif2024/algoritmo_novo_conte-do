def minha_funcao(*args,**kwargs):
    print("argumentos posicionais:",args)
    print("argumentos nomeados:",kwargs)
    
minha_funcao(1,2,3,nome="joão",idade=25)