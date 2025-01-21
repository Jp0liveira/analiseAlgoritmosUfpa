# Percorre o array uma única vez, armazenando o mínimo e o máximo encontrados até o momento.
def maxmin1(arr):
    minimo = maximo = arr[0]
    comparacoes = 0

    for num in arr[1:]:
        if num > maximo:
            maximo = num
        elif num < minimo:
            minimo = num
        comparacoes += 2  # Cada iteração faz até 2 comparações

    return maximo, minimo, comparacoes

# Exemplo de uso:
arr = [3, 1, 5, 2, 4]
print(maxmin1(arr))  # (5, 1, número de comparações)
