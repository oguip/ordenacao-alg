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

[Veja aqui a tabela completa](sandbox:/mnt/data/tabela_resultados.md)

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

