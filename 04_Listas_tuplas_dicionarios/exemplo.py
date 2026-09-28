# listas, tuplas e dicionarios

# 1. listas
# utilizadas para armazenar varios valores
nomes = ["ana", "Carlos", "João", "Maria"]
print(nomes)

# 2. acessando elementos da lista
print(nomes[0])

#podemos acessar o ultimo elemento usando o -1
print(nomes[-1])

# 3. alterando elementos

nomes[0] = "Pedro"
print(nomes)

# 4. adicionar elementos

# append() adiciona um elemento no final da lista
nome.append("Lucas")
print(nome)

# insert() adiciona um elemento em uma posição especifica
nomes.insert(1, "Maria")
print(nomes)

# 5. removendo elementos
nomes.remove("Maria")
print(nomes)

# pop() remove um elemento pelo indice
nome.pop(0)
print(nomes)

# 6. tamanho da lista
#len() informa a quantidade de elementos
print(len(nome))

#7. percorrendo uma lista
for nome in nomes:
    print(nome)

# 8.verificando se um elemento existe

if "João" in nome:
    print("João esta na lista")
else:
    print("João não esta na lista")

# 9. lista com diferentes dados
dados = ["João", 18, 1.75, true]
print(dados)

#10. lista de numeros
notas = [7.5, 8.0, 6.5, 9.0]

soma = 0

for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print(f"Média das notas: {media}")

# 11. tuplas
#tuplas são semelhantes as listas
# as tuplas nao sao alteradas

coordenada = (10, 20)
print(coordenada)

print(coordenada[0])

# 12. dicionarios

#dicionarios armazenam informações de formatos chave: valor

aluno = {
    "nome": "Carlos",
    "idade": 17,
    "Nota": 8.5
}
print(aluno)

# 13 acessando valores do dicionario

print(aluno["nome"])
print(aluno["idade"])
print(aluno["Nota"])

# 14 alterando valores

aluno["Nota"] = 9.0
print(aluno)

# 15 adicionando novos dados

aluno["curso"] = "informatica"
print(aluno)

# 16 removendo dados

del aluno["curso"]
print(aluno)

# 17 percorrendo um dicionario
for chave in aluno:
    print(chave)

# podemos acessar chave e valor ao mesmo tempo
for chave, valor in aluno.itens():
 print(f"{chave}: {valor}")

# 18 verificando chaves
if "nome" in aluno:
    print("a chave nome existe")

# 19 dicionario com lista

aluno = {
    "nome": "Maria",
    "notas": [8.9, 7.5, 9.0]
}










