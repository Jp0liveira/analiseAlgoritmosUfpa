# Outra abordagem recursiva que compara diretamente os elementos e reduz chamadas desnecessárias.
def maxmin4(arr, n):
    if n == 1:
        return arr[0], arr[0], 0

    max_ant, min_ant, comparacoes = maxmin4(arr, n - 1)

    maximo = max(max_ant, arr[n - 1])
    minimo = min(min_ant, arr[n - 1])
    comparacoes += 2

    return maximo, minimo, comparacoes

# Exemplo de uso:
arr = [3, 1, 5, 2, 4]
print(maxmin4(arr, len(arr)))  # (5, 1, número de comparações)
