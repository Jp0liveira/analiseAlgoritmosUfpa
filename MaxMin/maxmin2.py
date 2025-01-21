# Analisa os números em pares, reduzindo o número de comparações.
def maxmin2(arr):
    if len(arr) % 2 == 0:
        minimo = min(arr[0], arr[1])
        maximo = max(arr[0], arr[1])
        inicio = 2
    else:
        minimo = maximo = arr[0]
        inicio = 1

    comparacoes = 1 if len(arr) % 2 == 0 else 0

    for i in range(inicio, len(arr) - 1, 2):
        maior = max(arr[i], arr[i+1])
        menor = min(arr[i], arr[i+1])
        maximo = max(maximo, maior)
        minimo = min(minimo, menor)
        comparacoes += 3  # Duas comparações no par + 1 para atualizar max/min

    return maximo, minimo, comparacoes

# Exemplo de uso:
arr = [3, 1, 5, 2, 4]
print(maxmin2(arr))  # (5, 1, número de comparações)
