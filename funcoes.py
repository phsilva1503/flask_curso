'''
def hello():
    print("Hello, World!")

for i in range(10):
    hello()
'''
#função calcula a media de um conjunto de avaliações fornecidas pelo usuário
def calcular_media():
    numero_avaliacoes = int(input("Digite o número de avaliações: "))
    total = 0

    for i in range(numero_avaliacoes):
        nota = float(input(f'Digite a nota da avaliação '))
        total += nota

        if numero_avaliacoes > 0:
            media = total / numero_avaliacoes
            
        
    return media

resultado = calcular_media()
print(f'O resultado da média é: {resultado}')
