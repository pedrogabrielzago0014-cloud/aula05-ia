# Verificação de Número Primo em Python

## O que é um número primo?

Um número primo é aquele maior que 1 que só pode ser dividido por **1** e por **ele mesmo**, sem deixar resto. Exemplos: 2, 3, 5, 7, 11, 13, 17...

---

## Versão inicial gerada pela IA

```python
def is_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

### Explicação linha a linha

| Linha | Código | Explicação |
|-------|--------|------------|
| 1 | `def is_primo(n):` | Define a função recebendo `n` como parâmetro |
| 2 | `if n < 2:` | Números menores que 2 nunca são primos |
| 3 | `return False` | Retorna imediatamente para esses casos |
| 4 | `for i in range(2, n):` | Testa todos os possíveis divisores de 2 até n-1 |
| 5 | `if n % i == 0:` | Se o resto da divisão for 0, encontrou um divisor |
| 6 | `return False` | Encontrou divisor → não é primo |
| 7 | `return True` | Nenhum divisor encontrado → é primo |

---

## Versão otimizada (Clean Code)

```python
import math

def is_prime(number: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Args:
        number (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for divisor in range(3, math.isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False

    return True
```

### Explicação linha a linha da versão otimizada

| Linha | Código | Explicação |
|-------|--------|------------|
| 1 | `import math` | Importa o módulo `math` para usar `isqrt` (raiz quadrada inteira) |
| 3 | `def is_prime(number: int) -> bool:` | Define a função com **type hints**: recebe `int`, retorna `bool` |
| 4–10 | `"""..."""` | **Docstring**: documenta propósito, parâmetros e retorno |
| 11 | `if number < 2:` | Descarta números menores que 2 |
| 14 | `if number == 2:` | Trata o único primo par como caso especial |
| 17 | `if number % 2 == 0:` | Descarta todos os outros números pares de uma vez |
| 19 | `for divisor in range(3, math.isqrt(number) + 1, 2):` | Testa apenas ímpares até a raiz quadrada — principal otimização |
| 20 | `if number % divisor == 0:` | Verifica divisibilidade |
| 21 | `return False` | Encontrou divisor: não é primo |
| 23 | `return True` | Nenhum divisor: é primo |

---

## Por que parar na raiz quadrada?

Se `n` tem um divisor maior que √n, obrigatoriamente tem um divisor **menor** que √n. Verificar até `math.isqrt(n)` é suficiente e muito mais rápido.

> **Exemplo:** Para n = 100, √100 = 10. Não precisa testar além de 10.

---

## Comparativo: inicial vs otimizado

| Aspecto | Versão inicial | Versão otimizada |
|---------|---------------|-----------------|
| Nome da função | `is_primo` (mistura PT/EN) | `is_prime` (inglês consistente) |
| Parâmetro | `n` (genérico) | `number` (descritivo) |
| Type hints | Ausentes | `number: int -> bool` |
| Documentação | Ausente | Docstring completa |
| Complexidade | O(n) | O(√n) |
| Trata pares | Não | Sim (mais eficiente) |
