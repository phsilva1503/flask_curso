def resumo_pedido(*args, **kwargs):
    # valida cliente
    cliente = kwargs.get('cliente')
    if not cliente:
        print('Erro: cliente não informado.')
        return

    print(f'Cliente: {cliente}\n')

    # produtos
    print('Produtos:')
    for produto in args:
        print(f'- {produto}')

    total_itens = len(args)
    print(f'\nTotal de itens: {total_itens}\n')

    # endereço
    endereco = kwargs.get('endereco', 'Não informado')
    print(f'Endereço: {endereco}')

    # entrega
    entrega = kwargs.get('entrega', False)
    print(f'Entrega: {"Sim" if entrega else "Não"}')

    # cupom
    cupom = kwargs.get('cupom')
    if cupom:
        print(f'Cupom aplicado: {cupom}')

    # desafio extra (preço)
    preco = kwargs.get('preco')
    if preco is not None:
        total = preco * total_itens
        print(f'Total do pedido: R$ {total:.2f}')

resumo_pedido(
    'Notebook',
    'Mouse',
    'Teclado',
    cliente='Pedro',
    endereco='Rua A, 123',
    entrega=True,
    cupom='DESCONTO10',
    preco=100
)