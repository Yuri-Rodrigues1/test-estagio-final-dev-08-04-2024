def calculandoDesconto(consumoMedio, tipoTarifa):
    if tipoTarifa == 'Residencial':
        if consumoMedio < 10000:
            return 0.18
        elif 10000 <= consumoMedio <= 20000:
            return 0.22
        else:
            return 0.25
    elif tipoTarifa == 'Comercial':
        if consumoMedio < 10000:
            return 0.16
        elif consumoMedio <= 20000:
            return 0.18
        else:
            return 0.22
    elif tipoTarifa == 'Industrial':
        if consumoMedio < 10000:
            return 0.12
        elif 10000 <= consumoMedio <= 20000:
            return 0.15
        else:
            return 0.18
    else:
        return 0.0
    
def calculandoCobertura(consumoMedio):
    if consumoMedio < 10000:
        return 0.9
    elif 10000 <= consumoMedio <= 20000:
        return 0.95
    else:
        return 0.99

def calculator(consumo, tarifa, tipoTarifa):
    consumoMedio = sum(consumo) / len(consumo)
    
    desconto = calculandoDesconto(consumoMedio, tipoTarifa)
    cobertura = calculandoCobertura(consumoMedio)
    economiaMensal = consumoMedio * desconto * tarifa * cobertura
    economiaAnual = economiaMensal * 12  # Corrigido: incluído cobertura no cálculo da economia mensal

    return (
        round(economiaAnual, 2),
        round(economiaMensal, 2),
        desconto,
        cobertura,
    ) 
if __name__ == "__main__":
    print("Testing...")

    assert calculator([1518, 1071, 968], 0.95871974, "Industrial") == (
        1473.19,
        122.77,
        0.12,
        0.9,
    )

    assert calculator([1000, 1054, 1100], 1.12307169, "Residencial") == (
        2295.32,
        191.28,
        0.18,
        0.9,
    )

    assert calculator([973, 629, 726], 1.04820025, "Comercial") == (
        1405.56,
        117.13,
        0.16,
        0.9,
    )

    assert calculator([15000, 14000, 16000], 0.95871974, "Industrial") == (
        24591.16,
        2049.26,
        0.15,
        0.95,
    )

    assert calculator([12000, 11000, 11400], 1.12307169, "Residencial") == (
        32297.74,
        2691.48,
        0.22,
        0.95,
    )

    assert calculator([17500, 16000, 16400], 1.04820025, "Comercial") == (
        35776.75,
        2981.40,
        0.18,
        0.95,
    )

    assert calculator([30000, 29000, 29500], 0.95871974, "Industrial") == (
        60478.73,
        5039.89,
        0.18,
        0.99,
    )

    assert calculator([22000, 21000, 21400], 1.12307169, "Residencial") == (
        71602.56,
        5966.88,
        0.25,
        0.99,
    )

    assert calculator([25500, 23000, 21400], 1.04820025, "Comercial") == (
        63832.12,
        5319.34,
        0.22,
        0.99,
    )

    print("Everything passed")
