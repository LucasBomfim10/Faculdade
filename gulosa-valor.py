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


def knapsack_greedy_ratio(W, items):
  # Calcular a relação benefício/custo para cada item
  item_ratios = [(i[0] / i[1], i[0], i[1]) for i in items]
  print(item_ratios)
  
  # Ordenar os itens por sua relação benefício/custo em ordem decrescente
  sorted_items = sorted(item_ratios, key=lambda x: x[0], reverse=True)
  
  current_weight = 0
  current_value = 0
  selection = [0] * len(items)
  
  for ratio, value, weight in sorted_items:
      if current_weight + weight <= W:
          for i in range(len(items)):
              if items[i] == (value, weight):
                  selection[i] = 1
                  current_weight += weight
                  current_value += value
                  break
  
  return current_value, selection

def quality_metric(x, x_opt):
    print(x,x_opt)
    return x / x_opt

# Exemplo de uso:
W, items, X = read_instance('instances_01_KP/large_scale/teste.txt')
#knapPI_1_100_1000_1

# Medindo o tempo de execução
start_time = time.time()
# Executando o algoritmo de mochila booleano
max_value_boolean, _ = knapsack_greedy_ratio(W, items)
# Calculando o tempo de execução
tempo_total = time.time() - start_time
print("Tempo de execução:", tempo_total, "segundos")

# Calculando a métrica de qualidade para o algoritmo booleano
quality_boolean = quality_metric(max_value_boolean, sum(items[i][0] for i in range(len(X)) if X[i] == 1))

print("Items:", max_value_boolean, _)

print("Métrica de qualidade para o algoritmo booleano:", quality_boolean)

print

