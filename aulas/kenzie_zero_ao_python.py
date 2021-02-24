'''exemplo1'''
print('Olá Mundo')
print(5 + 10)
print('5'+'10')
'''#exemplo2'''
print('Olá Mundo', 10)
'''#exemplo3'''
nome = 'Xand_LIn'
idade = 20
peso = 55
print('Nome:', nome, '\nidade:', idade, '\nPeso:', peso)
'''#exemplo4'''
nome1 = input('Qual é o seu nome?: ')
idade1 = input('Sua idade?: ')
peso1 = input('Qual é seu peso?: ')
print(nome1, idade1, peso1)
'''#exemplo5'''
nome2 = input('Qual é o seu nome?: ')
print('Olá', nome2, 'Seja Bem Vindo')
resposta = input('Você esta bem?: ')
if resposta == 'não' or resposta == 'Não':
    resposta = input('Posso te ajudar e algo?: ')
    if resposta == 'não' or 'Não':
        print('Que pena acontence \nvai dormir deve melhorar')
else:
    print('Que ótimo, vai estudar')
'''#exemplo6'''
print('Dgite sua Data de Nascimento:')
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
print('Data de Nascimento: ', dia, '/', mes, '/', ano)
'''#exemplo7'''
soma = input('Digite o primeiro numero: ')
soma1 = input('Digite o segundo numero: ')
result = int(soma) + int(soma1)
print('Soma: ', result)
