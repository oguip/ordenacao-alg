import numpy as np
import time
import pandas as pd

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

def medir_tempo(sort_func, arr):
    inicio = time.time()
    sort_func(arr.copy())
    fim = time.time()
    return fim - inicio


tamanhos = [1000, 10000, 100000]
tipos_vetores = ['aleatório', 'crescente', 'decrescente']
metodos = {
    'Bubble Sort': bubble_sort,
    'Bubble Sort Otimizado': bubble_sort_otimizado,
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'MergeSort': merge_sort,
    'QuickSort': quick_sort
}

vetores = {}
for tamanho in tamanhos:
    vetores[tamanho] = {}
    vetores[tamanho]['aleatório'] = np.random.randint(0, tamanho, tamanho)
    vetores[tamanho]['crescente'] = np.arange(tamanho)
    vetores[tamanho]['decrescente'] = np.arange(tamanho, 0, -1)

np.savez('vetores_teste.npz', **{f'{t}_{tipo}': vetores[t][tipo] for t in tamanhos for tipo in tipos_vetores})
print("Vetores salvos no arquivo 'vetores_teste.npz'")

dados = []
for tamanho in tamanhos:
    for tipo in tipos_vetores:
        vetor = vetores[tamanho][tipo]
        for nome_metodo, funcao in metodos.items():
            print(f'Iniciando: Tamanho={tamanho}, Tipo={tipo}, Método={nome_metodo}')
            tempo_gasto = medir_tempo(funcao, vetor)
            print(f'Finalizado: Tamanho={tamanho}, Tipo={tipo}, Método={nome_metodo}, Tempo={tempo_gasto}')
            dados.append({
                'Tamanho': tamanho,
                'Tipo': tipo,
                'Método': nome_metodo,
                'Tempo': tempo_gasto
            })

resultado = pd.DataFrame(dados)
resultado.to_csv('resultados_ordenacao.csv', index=False)
print("Arquivo CSV com os resultados salvo como 'resultados_ordenacao.csv'")