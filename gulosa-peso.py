import time

def read_instance(filename):
    with open(filename, 'r') as file:
        # Lendo capacidade da mochila e quantidade de itens
        y, W = map(int, file.readline().split())
        print("capacidade da mochila:", W)
        print("quantidade de itens:", y)

        # Lendo os itens (valor, peso)
        items = []
        for _ in range(y):
            v, w = map(int, file.readline().split())
            items.append((v, w))

        print("item:", items)    

        # Lendo o vetor X
        X = list(map(int, file.readline().split()))
        print("vetor X: ",X)
        return W, items, X


def knapsack_greedy(W, items):
# Ordenar os itens por peso em ordem crescente
  sorted_items = sorted(items, key=lambda x: x[1])
  
  current_weight = 0
  current_value = 0
  selection = [0] * len(items)
  
  for i in range(len(sorted_items)):
      if current_weight + sorted_items[i][1] <= W:
          selection[i] = 1
          current_weight += sorted_items[i][1]
          current_value += sorted_items[i][0]
  
  return current_value, selection

def quality_metric(x, x_opt):
    print(x);
    print(x_opt);
    return x / x_opt

# Exemplo de uso:
W, items, X = read_instance('instances_01_KP/large_scale/teste.txt')
#knapPI_1_100_1000_1

# Medindo o tempo de execução
start_time = time.time()
# Executando o algoritmo de mochila booleano
max_value_boolean, _ = knapsack_greedy(W, items)
# Calculando o tempo de execução
tempo_total = time.time() - start_time
print("Tempo de execução:", tempo_total, "segundos")

# Calculando a métrica de qualidade para o algoritmo booleano
quality_boolean = quality_metric(max_value_boolean, sum(items[i][0] for i in range(len(X)) if X[i] == 1))

print("Items:", max_value_boolean, _)

print("Métrica de qualidade para o algoritmo booleano:", quality_boolean)

