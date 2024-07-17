from itertools import product

# Sequências fornecidas
seq1 = [


[6, 12, 23, 34, 39, 50],


]

seq2 = [


[6, 12, 23, 34, 39, 50],

]
# Lista para armazenar os pares de sequências encontrados
found_pairs = []

# Encontrando sequências com no mínimo 4 números iguais
for seq1_item, seq2_item in product(seq1, seq2):
    common_numbers = set(seq1_item) & set(seq2_item)
    if len(common_numbers) >= 4:
        pair = (seq1_item, seq2_item)
        if pair not in found_pairs:
            found_pairs.append(pair)
            print("Sequência 1:", seq1_item)
            print("Sequência 2:", seq2_item)
            print("Números em comum:", common_numbers)
            print()

# Verificando se todos os casos foram encontrados
if len(found_pairs) == len(seq1) * len(seq2):
    print("Todos os casos foram encontrados.")
else:
    print("Alguns casos ainda não foram encontrados.")