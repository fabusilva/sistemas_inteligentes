import pandas as pd
from prettytable import PrettyTable
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Repositorio\\sistemas_inteligentes\\Perceptron\\diabetes_csv.csv')

coluna_alvo = 'class'
preditoras = list(set(df.columns) - set([coluna_alvo]))
df[preditoras] = df[preditoras] / df[preditoras].max()

X = df[preditoras].values
y = df[coluna_alvo].values
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.25, random_state=40)

tamanhos_camadas_ocultas = (8, 8, 8)
ativacao = 'relu'
solver = 'adam'
max_iteracoes = 1500

taxas_aprendizagem = [0.1, 0.01, 0.001]
neuronios_camada_oculta = [3, 5, 7]

resultados = []
num_execucoes = 30
for taxa_aprendizagem in taxas_aprendizagem:
    for num_neuronios in neuronios_camada_oculta:
        mse_values = []
        matriz_confusao_values = []

        for i in range(num_execucoes):
            mlp = MLPClassifier(hidden_layer_sizes=(num_neuronios,), activation=ativacao, solver=solver, max_iter=max_iteracoes, learning_rate_init=taxa_aprendizagem)
            mlp.fit(X_treino, y_treino)

            prever_teste = mlp.predict(X_teste)

            matriz_confusao = confusion_matrix(y_teste, prever_teste)

            mse_values.append(matriz_confusao)

        resultados.append({
            'taxa_aprendizagem': taxa_aprendizagem,
            'num_neuronios': num_neuronios,
            'matriz_confusao_values': matriz_confusao_values,
            'mse_values': mse_values
        })

tabela_resultados = PrettyTable()
tabela_resultados.field_names = ["Taxa de Aprendizagem", "Neurônios na Camada Oculta", "MSE Médio"]

for resultado in resultados:
    mse_medio = sum(resultado['mse_values']) / len(resultado['mse_values'])
    tabela_resultados.add_row([resultado['taxa_aprendizagem'], resultado['num_neuronios'], mse_medio])

print("Resultados:")
print(tabela_resultados)