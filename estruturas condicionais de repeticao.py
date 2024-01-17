MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
IDADE_LIMITE = 65

idade = int(input( " Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print( " Pode tirar habilitação.")

elif idade == IDADE_ESPECIAL:
    print( " Voce pode realizar as aulas teóricas, mas não pode tira a habilitação ainda.")

elif idade >= IDADE_LIMITE:
    print( " Voce precisa realizar o exame de vista para tira a habilitação .")

else:
    print ( " Voce não tem idade para tirar habilitação ainda.")


