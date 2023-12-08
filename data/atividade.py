import numpy as np
import json
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, mean_squared_error, confusion_matrix
from prettytable import PrettyTable

with open('diabetes_json.json') as f:
    dados = json.load(f)

for entrada in dados:
    entrada["class"] = 1 if entrada["class"] == "tested_positive" else 0


X = np.array([list(d.values())[:-1] for d in dados])
y = np.array([d['class'] for d in dados])

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

with open('validation_report.json') as f:
    dados_validacao = json.load(f)
    
tabela_validacao = dados_validacao[0]["tables"][0]

normalizador = StandardScaler()

X_treino_normalizado = normalizador.fit_transform(X_treino)
X_teste_normalizado = normalizador.transform(X_teste)

taxas_aprendizado = [0.1, 0.01, 0.001]
tamanhos_camada_escondida = [3, 5, 7]

resultados_tabela = PrettyTable()
resultados_tabela.field_names = ["Taxa de Aprendizado", "Neuronios na Camada Escondida","Acuracia Media", "Erro Quadratico Medio Medio", "Matriz de Confusao Media"]

for aprendizado in taxas_aprendizado:
    for tamanho_camada in tamanhos_camada_escondida:
        lista_acuracia = []
        lista_erro_quadratico_medio = []
        matrizes_confusao = []
        for _ in range(30):
            mlp = MLPClassifier(hidden_layer_sizes=(tamanho_camada,), learning_rate_init=aprendizado, max_iter=1000, random_state=42)
            mlp.fit(X_treino_normalizado, y_treino)
            y_predito = mlp.predict(X_teste_normalizado)
            acuracia = accuracy_score(y_teste, y_predito)
            lista_acuracia.append(acuracia)
            erro_quadratico_medio = mean_squared_error(y_teste, y_predito)
            lista_erro_quadratico_medio.append(erro_quadratico_medio)
            resultado_matriz_confusao = confusion_matrix(y_teste, y_predito)
            matrizes_confusao.append(resultado_matriz_confusao)
        acuracia_media = np.mean(lista_acuracia)
        erro_quadratico_medio_medio = np.mean(lista_erro_quadratico_medio)
        matriz_confusao_media = np.mean(matrizes_confusao, axis=0)
        if tamanho_camada in [3, 5, 7]:
            resultados_tabela.add_row([taxas_aprendizado, tamanho_camada, acuracia_media, erro_quadratico_medio_medio, matriz_confusao_media])

print("Resultados:")
print(resultados_tabela)