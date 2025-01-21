# Utiliza divisão e conquista para reduzir o número de comparações.
def maxmin3(arr, esq, dir):
    if esq == dir:
        return arr[esq], arr[esq], 0  # Apenas um elemento

    if dir == esq + 1:  # Apenas dois elementos
        if arr[esq] > arr[dir]:
            return arr[esq], arr[dir], 1
        else:
            return arr[dir], arr[esq], 1

    meio = (esq + dir) // 2
    max1, min1, comp1 = maxmin3(arr, esq, meio)
    max2, min2, comp2 = maxmin3(arr, meio + 1, dir)

    maximo = max(max1, max2)
    minimo = min(min1, min2)
    comparacoes = comp1 + comp2 + 2

    return maximo, minimo, comparacoes

# Exemplo de uso:
arr = [3, 1, 5, 2, 4]
print(maxmin3(arr, 0, len(arr)-1))  # (5, 1, número de comparações)
