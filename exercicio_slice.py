##1- Escreva um programa que lê dois nomes e retorne uma string formatada no formato "ÚltimoNome, PrimeiroNome".
#2- Inverta a ordem das palavras em uma string fornecida.
#3-Verifique se uma string fornecida é um palíndromo – (pode ser lida da mesma forma de trás para frente).

texto1 = input('digite o primeiro texto: ')
texto2 = input('digite o segundo texto: ')

# 1- Formatar os nomes
texto1_formatado = texto1.lower().replace(' ', '')
texto2_formatado = texto2.lower().replace(' ', '')

textos_formatados = [texto2_formatado,texto1_formatado]
textos_agregados = ', '.join(textos_formatados)
print(textos_agregados)

# 2- Inverter a ordem das palavras
palavras = texto1.split()
palavras_invertidas = palavras[::-1]

#3- Verificar se é um palíndromo
palidromo1 = texto1_formatado == texto1_formatado[::-1] # == compara e retorna TRUE  ou FALSE
palidromo2 = texto2_formatado == texto2_formatado[::-1]
print(f"{texto1} é palíndromo: {palidromo1}")
print(f"{texto2} é palíndromo: {palidromo2}")
