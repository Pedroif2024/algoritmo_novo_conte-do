from time import strftime
time=0
def mostrar_relogio():
    hora_formatada = strftime('%H:%M:%S %p')
    print(hora_formatada)
    time.sleep(1)
    mostrar_relogio()

mostrar_relogio()
