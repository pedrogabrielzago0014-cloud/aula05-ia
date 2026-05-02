import math


def is_prime(number: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número é primo se for maior que 1 e divisível
    apenas por 1 e por ele mesmo.

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


def main():
    test_numbers = [1, 2, 3, 4, 5, 17, 18, 97, 100]

    for number in test_numbers:
        result = "primo" if is_prime(number) else "não primo"
        print(f"{number} → {result}")


if __name__ == "__main__":
    main()
