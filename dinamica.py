def read_instance(filename):
    with open(filename, 'r') as file:
        # Lendo capacidade da mochila e quantidade de itens
        y, W = map(int, file.readline().split())

        # Lendo os itens (valor, peso)
        items = []
        for _ in range(y):
            v, w = map(int, file.readline().split())
            items.append((v, w))

        # Lendo o vetor X
        X = list(map(int, file.readline().split()))

        return W, items, X

def knapsack_dynamic(W, items):
    n = len(items)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if items[i - 1][1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1][1]] + items[i - 1][0])
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][W]
    best_selection = [0] * n

    w = W
    for i in range(n, 0, -1):
        if max_value <= 0:
            break
        if max_value == dp[i - 1][w]:
            continue
        else:
            best_selection[i - 1] = 1
            max_value -= items[i - 1][0]
            w -= items[i - 1][1]

    return dp[n][W], best_selection


def quality_metric(x, x_opt):
  print(x,x_opt)
  return x / x_opt


# Exemplo de uso:
W, items, X = read_instance('instances_01_KP/large_scale/teste.txt')

# Executando o algoritmo de mochila com programação dinâmica
max_value_dynamic, _ = knapsack_dynamic(W, items)
print(max_value_dynamic)
print(_)
# Calculando a métrica de qualidade para o algoritmo com programação dinâmica
quality_dynamic = quality_metric(max_value_dynamic,sum(items[i][0] for i in range(len(X)) if X[i] == 1))

print("Métrica de qualidade para o algoritmo com programação dinâmica:", quality_dynamic)
