def calcular_media(numeros):
    soma=sum(numeros)
    quantidade=len(numeros)
    media=soma/quantidade
    return media
notas=[8,7,10,8]
media_final=calcular_media(notas)
print(f"A madia é:{media_final:.2}")