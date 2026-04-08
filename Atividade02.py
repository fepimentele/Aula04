valor_compra = float(input('Informe o valor da compra:'))

if valor_compra > 250:
    desconto = valor_compra * 0.16
    valor_total = valor_compra - desconto

    print(f'O valor total da compra foi de:{valor_compra - desconto}')
else: 
    print(f'Sem desconto. {valor_compra}')

forma_de_pagamento = input('Qual será a forma de pagamento?')

if valor_compra > 250 and forma_de_pagamento == "à vista": 
    print('Desconto aplicado com sucesso!')
else:
    print('Desconto não aplicado.')