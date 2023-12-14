# Relatorio
O objetivo deste trabalho é desenvolver e analisar um classificador utilizando o algoritmo Perceptron de Múltiplas Camadas (MLP) para prever a classe de um conjunto de dados relacionados à diabetes.

Foi utilizado a biblioteca Pandas para carregar o conjunto de dados relacionado à diabetes('diabetes_csv.csv').
As variáveis preditoras foram normalizadas para garantir que todas as características do conjunto de dados estivessem na mesma escala. um conjunto de dados em que as variáveis preditoras são normalizadas, contribui para um treinamento mais eficaz do modelo de Perceptron de Múltiplas Camadas (MLP). Essa etapa é crucial para garantir que o modelo seja capaz de aprender padrões de todas as variáveis de forma equilibrada.
A normalização ocoore na seguinte linha de código:

`df[preditoras] = df[preditoras] / df[preditoras].max()`

`df[preditoras]`: seleciona todas as colunas de variáveis preditoras no DataFrame.

`df[preditoras].max()`: calcula o valor máximo para cada coluna de variável preditora.

O conjunto de dados foi dividido em conjuntos de treino e teste (75% treino, 25% teste) usando a função `train_test_split` da biblioteca scikit-learn. `train_test_split` Divide o conjunto de dados em dois subconjuntos independentes: um para treinamento do modelo e outro para avaliação, assim garantindo uma avaliação mais segura do código.

Para a Configuração do Modelo MLP foi utilizado: 
* Um modelo MLP com três camadas ocultas, cada uma contendo 8 neurônios.
* Número máximo de iterações: 1500.
* Função de ativação: 'relu'.
* Solver: 'adam'.

As funções de ativação 'relu' e o otimizador 'adam' foram escolhidos pois apresentam desempenho eficazes em problemas de classificação e treinamento de redes neurais.

Foi realizado experimentos variando a taxa de aprendizagem e o número de neurônios na camada oculta.
Para cada combinação, executamos o treinamento e avaliamos o modelo 30 vezes, registrando as matrizes de confusão resultantes.

### Resultados:


A variação da taxa de aprendizagem não demonstrou uma influência significativa no desempenho do modelo, conforme evidenciado pela similaridade nos MSEs médios para diferentes taxas. Aumentar o número de neurônios na camada oculta parece ter impacto positivo no desempenho do modelo, refletido na redução dos valores de MSE médio.