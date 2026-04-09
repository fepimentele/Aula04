# Estrutura IF

# idade = int(input('Insira a idade:'))

# if idade >= 18:
#     print('Você é adulto')
# else: 
#     print('Você não é adulto')

# ----------------------------------
    
pontos = int(input('Informe os pontos:'))

if pontos >= 100:
    print('Excelente!')
elif pontos >= 50:
    print('Bom desempenho')
elif pontos >= 25:
    print('Satisfatório!')
else:
    print('Pratique mais...')

    # --------------------------------

    # Operadores AND e OR 

usuario = input('Nome:')
senha = input('Senha:')

if usuario == "admin" or senha == "1234":
    print('Login realizado com sucesso')
else:
    print('Usuário ou senha incorretos.')

# --------------------------------------

# Exemplo IFs encadeados
    
nota = 8.9
if nota >= 9:
    print('A')
elif nota >= 7:
    print('B')
elif nota >= 5:
    print('c')
elif nota >= 3:
    print('D')
else:
    print('E')

# Exemplo de IFs não encadeados
    



# IFs aninhados
nota = float(input('Insira a nota:'))
frequencia = float(input('Informe a fequência:'))

if nota >= 7:
    # Aprovado por nota, mas precisa checar a frequência

    if frequencia >= 75:
        print('Aluno aprovado por Nota e frequência')
    else:
        print('Reprovado por frequência baixa')
else: 
    print('Reprovado por nota baixa.')

   


