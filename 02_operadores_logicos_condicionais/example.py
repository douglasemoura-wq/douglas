# estrutura condicionais

nota = 6

nota  >= 7;
    print("Aprovado")
if nota >= 7:
    print("Recuperado")
elif nota >= 5:
    print("Reprovado")
else:
    print("Reprovado")

# 2. Condições com operados logicos]
# and -> todas as condições devem ser verdadeiras
#or -> Pelo menos uma condição verdadeira
# nor -> inverte o resultado

idade = 20
ingresso = true

if idade >= 18 and ingresso:
    print("Entrada permitida")
else:
    print("Entrada não permitida")

# 3. Estrutura de repetição
contador = 1
while contador < 5:
    print(contador)
    contador += 1

# 4. estrutua de repetição for

for numero in range(1,6):
    print(numero)

# 5. percorrendo uma lista
nomes = ["Ana","Carlos","João","Maria"]
for nome in nomes:
    print(nome)

# 6. break
# 0 breack intemrromp  completamente a repetição
#0 pass nao execulta nenuma ação
#0 continue itemrrompe apenas a repetição atual

for numero in range(1,11):
    print(numero)

    if numero == 7:
        #break
        #pass
    continue

    print(numero)

    # 7. condição dentro de repetição

for numero in range(1,11):
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")

























