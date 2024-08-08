import random

lista_numeros_magicos = [1,2,3,4,5,6,7,8,9,10]
numero_magico = random.choice(lista_numeros_magicos)
entrada_usuario = int(input('Adivina el numero magico\n'))

if numero_magico != entrada_usuario:
    print(f'Perdiste, el numero magico es {numero_magico}')
else:
    print('Has ganado la loteria!')
