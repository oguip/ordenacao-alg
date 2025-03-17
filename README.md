# Relatório sobre Eficiência de Algoritmos de Ordenação

## 1. Método

### Equipamento utilizado:
- **Processador:** AMD64 Family 23 Model 8 Stepping 2, AuthenticAMD
- **Memória RAM:** 31.93 GB
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
- **Bibliotecas:** NumPy, Pandas, GPUtil, psutil, platform, Matplotlib

---

## 2. Resultados detalhados

Os tempos completos estão registrados abaixo na tabela:

### Tabela Completa dos Resultados

|   Tamanho | Tipo        |   Bubble Sort |   Bubble Sort Otimizado |   Insertion Sort |   MergeSort |   QuickSort |   Selection Sort |
|----------:|:------------|--------------:|------------------------:|-----------------:|------------:|------------:|-----------------:|
|      1000 | aleatório   |      0.249316 |             0.270488    |       0.101423   |  0.00709534 |  0.00151134 |         0.124209 |
|      1000 | crescente   |      0.155347 |             0.000504732 |       0          |  0.00614738 |  0.00151515 |         0.117388 |
|      1000 | decrescente |      0.439005 |             0.447778    |       0.217992   |  0.00473094 |  0.00151944 |         0.142225 |
|     10000 | aleatório   |     25.9654   |            27.7966      |      10.3539     |  0.0814061  |  0.0344474  |        12.8204   |
|     10000 | crescente   |     13.323    |             0.00166535  |       0.00409436 |  0.0734565  |  0.0353377  |        11.7526   |
|     10000 | decrescente |     38.8383   |            40.554       |      19.6416     |  0.0679412  |  0.0292578  |        11.4662   |
|    100000 | aleatório   |   2685.24     |          2675.78        |     967.77       |  0.907064   |  0.424003   |      1152.54     |
|    100000 | crescente   |   1226.25     |             0.0253668   |       0.0421722  |  0.804406   |  0.291706   |      1126.49     |
|    100000 | decrescente |   3794.66     |          4008.88        |    1974.53       |  0.85815    |  0.319554   |      1152.9      |

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

- Os algoritmos com complexidade **O(n²)** (Bubble Sort, Selection Sort, Insertion Sort) apresentaram tempos exponencialmente maiores com o crescimento dos vetores, o que está alinhado diretamente com a teoria de análise assintótica.
- **MergeSort** e **QuickSort**, ambos com complexidade média **O(n log n)**, confirmaram a teoria, exibindo tempos relativamente curtos e aumento menos pronunciado conforme o crescimento da massa de dados.
- A análise experimental valida completamente a teoria de eficiência assintótica, recomendando claramente o uso de algoritmos como MergeSort e QuickSort para situações práticas com grandes conjuntos de dados.

---

## 5. Conclusão

Através dos resultados obtidos, fica evidente a importância da escolha correta do algoritmo de ordenação baseado nas características específicas da aplicação e da escala dos dados envolvidos. Para grandes volumes, a escolha ideal recai sobre algoritmos eficientes como MergeSort ou QuickSort, devido à sua escalabilidade confirmada experimentalmente e teoricamente.

