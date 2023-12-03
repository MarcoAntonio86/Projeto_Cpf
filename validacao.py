import os
os.system('cls')


cpf = []
numero = 0
list_cpf = []


def valida_cpf(cpf):
    while len(cpf) < 11:
        numero = input('Informe um número: ')
        
        
        if numero.isdigit():
            numero = int(numero)
            cpf.append(numero)
            print(cpf)
        else:
            print('Valor inválido. Por favor, informe um número inteiro.')

def algoritimo1(cpf):
    base = 10
    num10 = 0
    i = 0

    while i < 9:
        num = cpf[i] * base
        num10 += num
        base -= 1
        i += 1

    digito = num10 % 11

    if digito >= 2 or digito <= 9:
        num10 = 11 - digito
    else:
        num10 = 0
    return num10

def algoritimo2(cpf):
    base = 11
    num11 = 0
    i = 0

    while i < 9:
        num = cpf[i] * base
        num11 += num
        base -= 1
        i += 1

    num10 = algoritimo1(cpf)
    num = num10 * 2
    num11 += num

    digito = num11 % 11

    if digito >= 2 or digito <= 9:
        num11 = 11 - digito
    else:
        num11 = 0
    return num11
      
def validacao(cpf):
    num10 = algoritimo1(cpf)
    num11 = algoritimo2(cpf)

    if num10 == cpf[9] and num11 == cpf[10]:
        return True
    else:
        return False


list_cpf = []  

while True:
    cpf = []  
    valida_cpf(cpf)
    if validacao(cpf):
        list_cpf.append(cpf)  
        print('Cpf válido')
    else:
        print('Cpf inválido')
    pergunta = input('Deseja continuar? S/N: ') .strip().upper()
    if pergunta == 'N':
        break

print(list_cpf)



