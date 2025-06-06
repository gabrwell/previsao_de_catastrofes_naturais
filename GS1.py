import numpy as np

# Função para ler vetores do usuário
def ler_vetor(nome, tamanho):
    print(f"Digite os valores de {nome} separados por espaço ({tamanho} valores):")
    vetor = list(map(float, input().split()))
    if len(vetor) != tamanho:
        print(f"Erro: esperado {tamanho} valores.")
        return ler_vetor(nome, tamanho)
    return vetor

# Funções de alerta
def alerta_temperatura(temp):
    if temp >= 40 or temp <= 5:
        print("Alerta de temperatura crítica!")
        return 1
    return 0

def alerta_umidade(umid):
    if umid <= 20 or umid >= 95:
        print("Alerta de umidade crítica!")
        return 1
    return 0

def alerta_precipitacao(prec):
    if prec >= 80:
        print("Alerta de risco de enchente!")
        return 1
    return 0

# Análise de matriz semanal
def analisar_registros_semanais(matriz_temp):
    for i, semana in enumerate(matriz_temp):
        maior = np.max(semana)
        menor = np.min(semana)
        print(f"Semana {i+1}: Maior temperatura = {maior:.2f}°C, Menor temperatura = {menor:.2f}°C")

def prever_temperatura_simples(temperaturas):
    dias = np.arange(1, len(temperaturas) + 1)
    a = (temperaturas[-1] - temperaturas[0]) / (len(temperaturas) - 1)
    b = temperaturas[0] - a * 1
    proximo_dia = len(temperaturas) + 1
    previsao = a * proximo_dia + b
    print(f"\nPrevisão de temperatura para o próximo dia (simulada): {previsao:.2f}°C")
    return previsao


def main():
    tamanho = 5
    # Entrada de dados ambientais
    temperaturas = ler_vetor("temperaturas (°C)", tamanho)
    umidades = ler_vetor("umidades (%)", tamanho)
    precipitacoes = ler_vetor("precipitações (mm)", tamanho)

    total_alertas = 0
    print("\n--- Análise de condições críticas ---")
    for i in range(tamanho):
        total_alertas += alerta_temperatura(temperaturas[i])
        total_alertas += alerta_umidade(umidades[i])
        total_alertas += alerta_precipitacao(precipitacoes[i])



    # Matriz de registros semanais (2 semanas, 5 dias)
    print("\n--- Matriz de Temperaturas Semanais ---")
    matriz_temp = np.array([
        np.random.uniform(10, 45, tamanho),  # Semana 1
        np.random.uniform(0, 42, tamanho)    # Semana 2
    ])
    print(np.round(matriz_temp, 2))
    analisar_registros_semanais(matriz_temp)

    # Resumo final
    print("\n--- Resumo Final ---")
    print(f"Total de alertas emitidos: {total_alertas}")
    if total_alertas > 5:
        print("Risco Alto de Evento Climático Extremo")
    else:
        print("Clima sob controle")

if __name__ == "__main__":
    main()