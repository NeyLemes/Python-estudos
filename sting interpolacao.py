nome = "claudinei"
idade = "36"
profissao = "programacao"
linguagem = "python"


dados = {"nome": "claudinei", "idade": "36", "profissao": "programacao", "linguagem": "python", "saldo": "45.435"}

print("Ola, me chamo %s. Eu tenho %s anos de idade, trabalho com %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
# metodo antigo com format %

print("Ola, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}." .format (nome, idade, profissao, linguagem))
# metodo antigo com format

print("Ola, me chamo {0}. Eu tenho {1} anos de idade, trabalho com {2} e estou matriculado no curso de {3}." .format (nome, idade, profissao, linguagem))
# metodo antigo com format e indicando a posição das strings

print("Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}." .format (nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}." .format (**dados))

print(f"Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}." )
# metodo f string

PI = 3.14159
saldo = 45.435

print( f"Valor de PI: {PI:.2f}")# .2f define o mumero de casas decimais após o ponto
print( f"Valor de PI: {PI:10.2f}")# 10.2f define o numero de casa decimais após o ponto e insere os espaços antes do numero

print( f"Seu saldo é: {saldo:10.2f}")