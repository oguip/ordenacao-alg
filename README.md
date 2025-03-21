# Relatório sobre Eficiência de Algoritmos de Ordenação

### Guilherme de Oliveira Pereira
### 10390535

## 1. Método

### Equipamento utilizado:
- **Processador:** AMD64 Ryzen 7 2700
- **Memória RAM:** 32.00 GB DDR4 3200MHz
- **Placa de Vídeo:** NVIDIA GeForce RTX 4060, 8188 MB

### Massa de dados:
- **Tamanhos dos vetores:** 1.000, 10.000 e 100.000 elementos
- **Tipos dos vetores:** Aleatório, Crescente e Decrescente

### Algoritmos utilizados:
- Bubble Sort (tradicional e otimizado)
- Selection Sort
- Insertion Sort
- MergeSort
- QuickSort

### Linguagem e Bibliotecas:
- **Linguagem:** Python
- **Bibliotecas:** NumPy, Pandas, Matplotlib

---

## 2. Resultados detalhados

### Criação dos vetores utilizando numpy

```py
vetores = {}
for tamanho in tamanhos:
    vetores[tamanho] = {}
    vetores[tamanho]['aleatório'] = np.random.randint(0, tamanho, tamanho)
    vetores[tamanho]['crescente'] = np.arange(tamanho)
    vetores[tamanho]['decrescente'] = np.arange(tamanho, 0, -1)
```

### Visualização Inicial dos Vetores:

![Vetores](/img/vetores_ordem_grafico.png)

### Implementação dos algoritmos de ordenação

```py
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubble_sort_otimizado(arr):
    n = len(arr)
    for i in range(n):
        trocado = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocado = True
        if not trocado:
            break

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i-1
        while j >=0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr)//2
        L = arr[:meio]
        R = arr[meio:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        esquerda = [x for x in arr if x < pivot]
        meio = [x for x in arr if x == pivot]
        direita = [x for x in arr if x > pivot]
        return quick_sort(esquerda) + meio + quick_sort(direita)
```

Os tempos em segundos estão registrados abaixo na tabela:

### Tabela Completa dos Resultados

|   Tamanho | Tipo        |   Bubble Sort |   Bubble Sort Otimizado |   Selection Sort |   Insertion Sort |   MergeSort |   QuickSort |
|----------:|:------------|--------------:|------------------------:|-----------------:|-----------------:|------------:|------------:|
|      1000 | aleatório   |      0.249316 |             0.270488    |         0.124209 |       0.101423   |  0.00709534 |  0.00151134 |
|      1000 | crescente   |      0.155347 |             0.000504732 |         0.117388 |       0          |  0.00614738 |  0.00151515 |
|      1000 | decrescente |      0.439005 |             0.447778    |         0.142225 |       0.217992   |  0.00473094 |  0.00151944 |
|     10000 | aleatório   |     25.9654   |            27.7966      |        12.8204   |      10.3539     |  0.0814061  |  0.0344474  |
|     10000 | crescente   |     13.323    |             0.00166535  |        11.7526   |       0.00409436 |  0.0734565  |  0.0353377  |
|     10000 | decrescente |     38.8383   |            40.554       |        11.4662   |      19.6416     |  0.0679412  |  0.0292578  |
|    100000 | aleatório   |   2685.24     |          2675.78        |      1152.54     |     967.77       |  0.907064   |  0.424003   |
|    100000 | crescente   |   1226.25     |             0.0253668   |      1126.49     |       0.0421722  |  0.804406   |  0.291706   |
|    100000 | decrescente |   3794.66     |          4008.88        |      1152.9      |    1974.53       |  0.85815    |  0.319554   |

Tempo total: 20.983 segundos - 349 minutos - 5.8 horas

### Gráficos ilustrando diferenças de desempenho (com marcação dos valores):

#### Vetor com 1.000 elementos
![Tamanho 1000](/img/grafico_tamanho_1000_marcado.png)

#### Vetor com 10.000 elementos
![Tamanho 10000](/img/grafico_tamanho_10000_marcado.png)

#### Vetor com 100.000 elementos
![Tamanho 100000](/img/grafico_tamanho_100000_marcado.png)

---

## 3. Análise Crítica sobre Eficiência

### Observações principais:
- **Bubble Sort** e **Selection Sort** demonstraram ser os métodos mais lentos, especialmente para grandes massas de dados (100.000 elementos), confirmando sua ineficiência prática.
- **Insertion Sort** apresentou bom desempenho em vetores pequenos e especialmente em vetores já parcialmente ou totalmente ordenados.
- **MergeSort** e **QuickSort** foram consistentemente os algoritmos mais eficientes em todas as condições testadas, mantendo desempenho rápido mesmo com aumento significativo do volume de dados.

---

## 4. Análise Crítica sobre Análise Assintótica vs Tempos Obtidos

- Os algoritmos com complexidade **O(n²)** (Bubble Sort, Selection Sort, Insertion Sort) apresentaram tempos exponencialmente maiores com o crescimento dos vetores, o que está alinhado diretamente com a teoria de análise assintótica. Nota-se que o QuickSort tem como pior caso **O(n²)**, porém, apenas ocorre quando o pivô escolhido seja o menor ou maior elemento do vetor.
- **MergeSort** e **QuickSort**, ambos com complexidade média **O(n log n)**, confirmaram a teoria, exibindo tempos relativamente curtos e aumento menos pronunciado conforme o crescimento da massa de dados.
- A análise experimental valida completamente a teoria de eficiência assintótica, recomendando claramente o uso de algoritmos como MergeSort e QuickSort para situações práticas com grandes conjuntos de dados.

---

## 5. Conclusão

Através dos resultados obtidos, fica evidente a importância da escolha correta do algoritmo de ordenação baseado nas características específicas da aplicação e da escala dos dados envolvidos. Para grandes volumes, a escolha ideal recai sobre algoritmos eficientes como MergeSort ou QuickSort, devido à sua escalabilidade confirmada experimentalmente e teoricamente.

