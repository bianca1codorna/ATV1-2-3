
#ATV1

nome = input('Me diga seu nome')
print (f' È um prazer te conhecer',nome)


#ATV2

nome = input('Digite seu nome:')
dia = input('Digite o dia do seu aniversário: ')
mes = input('Digite o mês do seu aniversário: ')
ano = input('Digite o ano do seu aniversário: ')

print(f'Olá,',nome,'! Sua data de aniversário é' ,dia,'/',mes,'/',ano)

#ATV3

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c

print("\n**************************\n")

if a == 0:
    print("O valor de a, deve ser diferente de 0")
elif delta < 0:
    print("Sem raízes reais")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("x1: {}, x2: {}".format(x1, x2))
