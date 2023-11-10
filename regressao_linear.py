print("*******************************************************************************")
print("****BEM VINDO AO NOSSO CÓDIGO, VAMOS REALIZAR A REGRESSÃO LINEAR PARA VOCÊ!****")
print("*******************************************************************************")

# Interação pra pedir o valor de "M".
m = int(input("Qual o valor de m? "))


# Variáveis da fórmula em forma de lista para receber todos os valores.
x = []
y = []
x_y = []
x_2 = []


# Os loops de acordo com o valor de "M" informado pelo usuário para inserir os valores das variáveis.
for i in range(m):
    x_valor = int(input("Insira os valores de x! "))
    x.append(int(x_valor))


print(x)
questao_x = str(input("Estes são os valores de acordo com a sua lista?(Responda com SIM ou Não!"))
questao_x = questao_x.strip().upper()

if questao_x == "SIM":
    for i in range(m):
        y_valor = int(input("Insira os valores de y! "))
        y.append(int(y_valor))

    print(y)

    questao_y = str(input("Estes são os valores de acordo com a sua lista?(Responda com SIM ou Não!"))
    questao_y = questao_y.strip().upper()

    if questao_y == "SIM":
        for i, j in zip(x, y):
            x_y_valor = i * j
            x_y.append(x_y_valor)

        for i, j in zip(x, x):
            x_2_valor = i * j
            x_2.append(x_2_valor)
    else:
        print("Desculpa, por favor rodar o código novamente e tente outra vez!")

else:
    print("Desculpa, por favor rodar o código novamente e tente outra vez!")


# Soma das variáveis.
soma_x = sum(x)
soma_y = sum(y)
soma_x_y = sum(x_y)
soma_x_2 = sum(x_2)


a = (((soma_x) * (soma_x_y) - (soma_x_2) * (soma_y)) / ((soma_x * soma_x) - m * (soma_x_2)))

b = (((soma_x) * (soma_y) - m * (soma_x_y)) / ((soma_x * soma_y) - m * (soma_x_2)))

print("Φ(x) = a + bx")
print(f"O resultado é: Φ(x) = {a} + {b}x")
