texto = input()
    
limite = 140
    
tamanho = len(texto)

status = "TWEET" if tamanho <= limite else "MUTE"

print (status)
print (tamanho)