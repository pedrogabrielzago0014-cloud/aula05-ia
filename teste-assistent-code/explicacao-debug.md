# Prática 3 — Debug com IA

## Código original com erros

```python
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input(Preço do item 1? ))          # ERRO 1

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))  # ERRO 2
desconto = subtotal * (desconto_cupom / 100)

total = subtotal + imposto - desconto

linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(" Item 2:        R$ {total_item2:.2f}")    # ERRO 3
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")   # ERRO 4

print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)
```

---

## Erros identificados pela IA

### ❌ Erro 1 — SyntaxError: string sem aspas no `input`

```python
# ❌ Errado
item1 = float(input(Preço do item 1? ))

# ✅ Correto
item1 = float(input("Preço do item 1? "))
```

**Causa:** O texto `Preço do item 1?` passado para `input()` não está entre aspas. O Python interpreta isso como se fosse uma expressão/variável, não uma string, causando `SyntaxError`.  
**Tipo:** `SyntaxError`

---

### ❌ Erro 2 — TypeError: `input()` retorna `str`, operação matemática falha

```python
# ❌ Errado — retorna string, não número
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)   # TypeError: can't divide str by int

# ✅ Correto — converte para float
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

**Causa:** `input()` sempre retorna uma `str`. Sem conversão (`float()`), a divisão `desconto_cupom / 100` lança `TypeError` porque Python não divide string por número.  
**Tipo:** `TypeError` em tempo de execução

---

### ❌ Erro 3 — f-string sem o prefixo `f`

```python
# ❌ Errado — imprime o texto literal, não o valor da variável
print(" Item 2:        R$ {total_item2:.2f}")

# ✅ Correto
print(f" Item 2:        R$ {total_item2:.2f}")
```

**Causa:** Sem o prefixo `f`, Python não interpola a variável `{total_item2:.2f}` — imprime a chave como texto literal: `R$ {total_item2:.2f}`.  
**Tipo:** Erro de lógica (não levanta exceção, mas exibe resultado errado)

---

### ❌ Erro 4 — IndentationError: `print` sem indentação dentro do `if`

```python
# ❌ Errado — print na coluna 0, fora do bloco if
if desconto_cupom > 0:
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

# ✅ Correto — print indentado dentro do if
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Causa:** Em Python, a indentação **define** os blocos de código. Um `print` sem indentação após `if` causa `IndentationError` pois o bloco do `if` fica vazio.  
**Tipo:** `IndentationError`

---

## Resumo dos erros

| # | Erro | Tipo | Causa |
|---|------|------|-------|
| 1 | `input(Preço do item 1? )` | `SyntaxError` | String sem aspas |
| 2 | `input(...)` sem `float()` | `TypeError` | `str` usada em operação matemática |
| 3 | `print("... {variavel}")` | Erro lógico | f-string sem prefixo `f` |
| 4 | `print` sem indentação no `if` | `IndentationError` | Bloco do `if` vazio |

---

## Lição aprendida

- **SyntaxError** e **IndentationError** são detectados antes de executar — o Python se recusa a rodar.
- **TypeError** aparece apenas em tempo de execução, quando o dado errado é usado.
- Erros **lógicos** (f-string sem `f`) são os mais perigosos: o código roda sem erros, mas exibe resultado incorreto.
