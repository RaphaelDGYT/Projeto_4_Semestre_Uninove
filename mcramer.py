# Introdução ao código
print("*******************************************************************************")
print("****BEM VINDO AO NOSSO CÓDIGO, VAMOS REALIZAR O MÉTODO DE CRAMER PARA VOCÊ!****")
print("*******************************************************************************")


# Solicitando ao usuário para inserir os coeficientes do sistema
print("Digite a equação a seguir sem acrescentar as letras (Ex: 3x = 3).")
x1, x2, x3 = map(int, input("Digite os coeficientes de x1, x2, x3 (separados por espaços): ").split())
y1, y2, y3 = map(int, input("Digite os coeficientes de y1, y2, y3 (separados por espaços): ").split())
z1, z2, z3 = map(int, input("Digite os coeficientes de z1, z2, z3 (separados por espaços): ").split())
d1, d2, d3 = map(int, input("Digite os coeficientes depois do sinal de igual (separados por espaços): ").split())

# Mostrando a equação ao usuário
print(f"{x1}x, {y1}y, {z1}z = {d1}")
print(f"{x2}x, {y2}y, {z2}z = {d2}")
print(f"{x3}x, {y3}y, {z3}z = {d3}")


# Variável para verificar se a equação é a mesma de acordo com o do usuário
questao = str(input("Esta é a equação que procurava? (Responda com SIM ou NÃO) "))

# Cálculos dos determinantes
Det_Geral = ((x1 * y2 * z3) + (y1 * z2 * x3) + (z1 * x2 * y3)) - ((z1 * y2 * x3) + (x1 * z2 * y3) + (y1 * x2 * z3))
Det_X = ((d1 * y2 * z3) + (y1 * z2 * d3) + (z1 * d2 * y3)) - ((z1 * y2 * d3) + (d1 * z2 * y3) + (y1 * d2 * z3))
Det_Y = ((x1 * d2 * z3) + (d1 * z2 * x3) + (z1 * x2 * d3)) - ((z1 * d2 * x3) + (x1 * z2 * d3) + (d1 * x2 * z3))
Det_Z = ((x1 * y2 * d3) + (y1 * d2 * x3) + (d1 * x2 * y3)) - ((d1 * y2 * x3) + (x1 * d2 * y3) + (y1 * x2 * d3))

# Cáculos dos valores de x, y e z
x = Det_X / Det_Geral
y = Det_Y / Det_Geral
z = Det_Z / Det_Geral

# Condição para verificar se o usuário deseja continuar com a resolução ou se deseja parar o código
if questao == "SIM":
    print("Determinante Geral: ", Det_Geral)
    print("Soluções usando Cramer:")
    print(f"x = {x:.1f}")
    print(f"y = {y:.1f}")
    print(f"z = {z:.1f}")
else:
    print("Desculpa, por favor rodar o código novamente e tente outra vez!")
