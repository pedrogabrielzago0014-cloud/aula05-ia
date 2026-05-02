"""
Módulo para análise estatística básica de uma lista de números.
Calcula total, média, maior e menor valor.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class StatisticsResult:
    """Armazena os resultados da análise estatística."""
    total: float
    average: float
    maximum: float
    minimum: float


def calculate_statistics(numbers: List[float]) -> StatisticsResult:
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numbers (List[float]): Lista de valores numéricos.

    Returns:
        StatisticsResult: Objeto com total, média, máximo e mínimo.

    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not numbers:
        raise ValueError("A lista não pode estar vazia.")

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return StatisticsResult(
        total=total,
        average=average,
        maximum=maximum,
        minimum=minimum
    )


def display_statistics(result: StatisticsResult) -> None:
    """Exibe os resultados estatísticos de forma legível."""
    print(f"Total:  {result.total}")
    print(f"Média:  {result.average:.2f}")
    print(f"Maior:  {result.maximum}")
    print(f"Menor:  {result.minimum}")


def main():
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    result = calculate_statistics(numbers)
    display_statistics(result)


if __name__ == "__main__":
    main()
