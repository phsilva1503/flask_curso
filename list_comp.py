# list comprehension


filmes_assistidos = ['Matrix', 'O Senhor dos Anéis', 'Star Wars', 'Harry Potter']


#filmes que possuem letra e
filmesComE = [filme for filme in filmes_assistidos if 'e' in filme.lower()]
print(filmesComE)

#encontrar filme pelo nome

while True:
    nome_filme = input('Digite o nome do filme que deseja encontrar: ').strip().lower()

    if nome_filme =='listar':
        print('Filmes assistidos:')
        for filme in filmes_assistidos:
            print(f' - {filme}')
        continue
        
        
    if nome_filme == 'sair':
        print('Encerrando o programa.')
        break

    filme_encontrado = [filme for filme in filmes_assistidos if nome_filme in filme.lower()]

    if filme_encontrado:
        print(f'Filme encontrado: {filme_encontrado[0]}')

    else:
        print('Filme não encontrado.')

        opção = input('deseja adiconar esse filme a lista ? (s/n)').strip().lower()
        
        if opção =='s':
            if nome_filme not in filmes_assistidos:
                filmes_assistidos.append(nome_filme)
                print(f'filme "{nome_filme}" adicionado a lista')
            
        else:
            print('filme ja na lista.')

else:
    print ('não adicionado')





