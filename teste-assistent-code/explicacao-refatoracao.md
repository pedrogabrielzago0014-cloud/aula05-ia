# Prática 2 — Refatoração de Código

## Código Original (mal estruturado)

```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn

x=[23,7,45,2,67,12,89,34,56,11]
a,b,c2,d=c(x)
print("total:",a)
print("media:",b)
print("maior:",c2)
print("menor:",d)
```

---

## Código Refatorado (boas práticas)

```python
from dataclasses import dataclass
from typing import List

@dataclass
class StatisticsResult:
    total: float
    average: float
    maximum: float
    minimum: float

def calculate_statistics(numbers: List[float]) -> StatisticsResult:
    """
    Calcula estatísticas básicas de uma lista de números.
    """
    if not numbers:
        raise ValueError("A lista não pode estar vazia.")
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return StatisticsResult(total=total, average=average, maximum=maximum, minimum=minimum)

def display_statistics(result: StatisticsResult) -> None:
    print(f"Total:  {result.total}")
    print(f"Média:  {result.average:.2f}")
    print(f"Maior:  {result.maximum}")
    print(f"Menor:  {result.minimum}")

numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
result = calculate_statistics(numbers)
display_statistics(result)
```

---

## O que a IA identificou e melhorou

### 1. Nome de função sem significado (`c`)
```python
# ❌ Antes
def c(l):

# ✅ Depois
def calculate_statistics(numbers: List[float]) -> StatisticsResult:
```
`c` não comunica nada. `calculate_statistics` descreve exatamente o que a função faz.

---

### 2. Variáveis sem significado (`l`, `t`, `m`, `mx`, `mn`, `a`, `b`, `d`)
```python
# ❌ Antes
t=0 / m=t/len(l) / mx=l[0] / mn=l[0]

# ✅ Depois
total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)
minimum = min(numbers)
```
Nomes descritivos tornam o código legível sem precisar de comentários.

---

### 3. Uso de `range(len(l))` — antipadrão Python
```python
# ❌ Antes
for i in range(len(l)):
    t = t + l[i]

# ✅ Depois
total = sum(numbers)
```
Python tem funções nativas (`sum`, `max`, `min`) para isso. Mais legível e menos propenso a erros.

---

### 4. Retorno de múltiplos valores soltos (tupla sem estrutura)
```python
# ❌ Antes
return t, m, mx, mn
a, b, c2, d = c(x)   # quem chama precisa saber a ordem exata

# ✅ Depois
return StatisticsResult(total=total, average=average, maximum=maximum, minimum=minimum)
result.total / result.average  # campos nomeados, autoexplicativos
```

---

### 5. Ausência de docstring ou comentários
A função original não tinha nenhuma documentação. A versão refatorada inclui docstring com descrição, parâmetros, retorno e exceções.

---

### 6. Lista com nome genérico (`x`)
```python
# ❌ Antes
x = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

# ✅ Depois
numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
```

---

## Resumo das melhorias

| Problema | Original | Refatorado |
|----------|----------|------------|
| Nome da função | `c` | `calculate_statistics` |
| Parâmetro | `l` | `numbers` |
| Variáveis internas | `t`, `m`, `mx`, `mn` | `total`, `average`, `maximum`, `minimum` |
| Iteração | `range(len(l))` | funções nativas `sum`, `max`, `min` |
| Retorno | tupla posicional | `@dataclass StatisticsResult` |
| Documentação | ausente | docstring completa |
| Validação | nenhuma | `raise ValueError` para lista vazia |
