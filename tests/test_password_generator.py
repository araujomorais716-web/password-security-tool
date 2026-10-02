import pytest

from src.password_generator import (
    gerar_senha_segura,
    calcular_entropia,
    classificar_entropia,
)


def test_senha_deve_ter_tamanho_solicitado():
    senha, _ = gerar_senha_segura(16)

    assert len(senha) == 16


def test_senha_deve_conter_maiuscula():
    senha, _ = gerar_senha_segura(
        16,
        usar_maiusculas=True,
        usar_minusculas=False,
        usar_numeros=False,
        usar_simbolos=False,
    )

    assert any(char.isupper() for char in senha)


def test_senha_deve_conter_numero():
    senha, _ = gerar_senha_segura(
        16,
        usar_maiusculas=False,
        usar_minusculas=False,
        usar_numeros=True,
        usar_simbolos=False,
    )

    assert any(char.isdigit() for char in senha)


def test_deve_rejeitar_senha_muito_curta():
    with pytest.raises(ValueError):
        gerar_senha_segura(8)


def test_deve_rejeitar_categorias_vazias():
    with pytest.raises(ValueError):
        gerar_senha_segura(
            16,
            False,
            False,
            False,
            False,
        )


def test_entropia_deve_ser_positiva():
    entropia = calcular_entropia(
        "Abc123!@",
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789!@",
    )

    assert entropia > 0


def test_classificacao_entropia():
    assert classificar_entropia(50) == "Fraca"
    assert classificar_entropia(70) == "Média"
    assert classificar_entropia(100) == "Forte"
    assert classificar_entropia(130) == "Muito Forte"
