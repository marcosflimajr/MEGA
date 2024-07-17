import itertools

# Solicitar valores para as variáveis "Inicial", "Final" e "quantidade_numeros"
Inicial = int(input("Digite o valor inicial: "))
Final = int(input("Digite o valor final: "))
quantidade_numeros = int(input("Digite a quantidade de números do sorteio: "))

# Gerar todas as combinações possíveis dentro do intervalo especificado
sequences = itertools.combinations(range(Inicial, Final + 1), quantidade_numeros)

# Inicializar contador
count = 0

# Iterar sobre as sequências e imprimir cada uma delas
for sequence in sequences:
    print(sequence)
    count += 1
    if count >= 49000:

        continuar = input("Deseja continuar gerando combinações? (S/N): ")

        if continuar.lower() != 's':
            break
        else:
            count = 0