# 📊 Calculadora Financeira Simples
# Autor: Thaylor Batista

def juros_simples(capital, taxa, tempo):
    """Cálculo de Juros Simples"""
    return capital * (taxa / 100) * tempo

def juros_compostos(capital, taxa, tempo):
    """Cálculo de Juros Compostos"""
    return capital * ((1 + taxa / 100) ** tempo - 1)

def conversao_dolar(valor, taxa_cambio=5.20):
    """Conversão de Dólar para Real (taxa fixa)"""
    return valor * taxa_cambio

def menu():
    print("\n📊 CALCULADORA FINANCEIRA 📊")
    print("1 - Juros Simples")
    print("2 - Juros Compostos")
    print("3 - Conversão Dólar -> Real")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        capital = float(input("Digite o capital inicial (R$): "))
        taxa = float(input("Digite a taxa de juros (%): "))
        tempo = int(input("Digite o tempo (em meses): "))
        resultado = juros_simples(capital, taxa, tempo)
        print(f"✅ Juros Simples: R$ {resultado:.2f}")

    elif opcao == "2":
        capital = float(input("Digite o capital inicial (R$): "))
        taxa = float(input("Digite a taxa de juros (%): "))
        tempo = int(input("Digite o tempo (em meses): "))
        resultado = juros_compostos(capital, taxa, tempo)
        print(f"✅ Juros Compostos: R$ {resultado:.2f}")

    elif opcao == "3":
        valor = float(input("Digite o valor em dólares (US$): "))
        resultado = conversao_dolar(valor)
        print(f"✅ Valor em Reais: R$ {resultado:.2f}")

    elif opcao == "0":
        print("👋 Saindo da calculadora... até logo!")
        break

    else:
        print("❌ Opção inválida! Tente novamente.")
