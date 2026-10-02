import math
import secrets
import string
from typing import Tuple


def gerar_senha_segura(
    tamanho: int = 16,
    usar_maiusculas: bool = True,
    usar_minusculas: bool = True,
    usar_numeros: bool = True,
    usar_simbolos: bool = True,
) -> Tuple[str, str]:

    if not isinstance(tamanho, int):
        raise TypeError("O tamanho deve ser um número inteiro.")

    if tamanho < 12:
        raise ValueError("A senha deve ter pelo menos 12 caracteres.")

    categorias = []

    if usar_maiusculas:
        categorias.append(string.ascii_uppercase)

    if usar_minusculas:
        categorias.append(string.ascii_lowercase)

    if usar_numeros:
        categorias.append(string.digits)

    if usar_simbolos:
        categorias.append(string.punctuation)

    if not categorias:
        raise ValueError(
            "Pelo menos uma categoria de caracteres deve ser selecionada."
        )

    if tamanho < len(categorias):
        raise ValueError(
            f"O tamanho deve ser pelo menos {len(categorias)} "
            "para utilizar todas as categorias selecionadas."
        )

    senha = []

    # Garante pelo menos um caractere de cada categoria selecionada.
    for categoria in categorias:
        senha.append(secrets.choice(categoria))

    conjunto_caracteres = "".join(categorias)

    # Completa o restante da senha.
    for _ in range(tamanho - len(senha)):
        senha.append(secrets.choice(conjunto_caracteres))

    # Embaralhamento utilizando uma fonte segura de aleatoriedade.
    secrets.SystemRandom().shuffle(senha)

    return "".join(senha), conjunto_caracteres


def calcular_entropia(senha: str, conjunto_caracteres: str) -> float:
    """
    Calcula uma estimativa da entropia da senha.

    Fórmula:
        E = L * log2(N)

    Onde:
        L = tamanho da senha
        N = tamanho do conjunto de caracteres utilizado
    """

    if not senha:
        raise ValueError("A senha não pode estar vazia.")

    if not conjunto_caracteres:
        raise ValueError("O conjunto de caracteres não pode estar vazio.")

    return len(senha) * math.log2(len(conjunto_caracteres))


def classificar_entropia(entropia: float) -> str:
    if entropia < 64:
        return "Fraca"

    if entropia < 80:
        return "Média"

    if entropia < 120:
        return "Forte"

    return "Muito Forte"
