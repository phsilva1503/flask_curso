#*args

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    print(f'Os números fornecidos foram: {args}')
    print(f'A soma dos números é: {total}')


soma(1, 2, 3, 4, 5)


#kwargs
#presentação de curos
def apresentacao(**kwargs):
    print('Apresentação do curso:')
    for chave, valor in kwargs.items():
        print(f'{chave.capitalize()}: {valor}')


apresentacao(nome='Python para Iniciantes', instrutor='Pedro', duracao='4 semanas')
apresentacao(nome='Curso de Flask', instrutor='Maria', duracao='6 semanas', nivel='Intermediário')

