# Relatorio do projeto

O projeto foi desenvolvido empregando a biblioteca scikit-learn (sklearn) para implementar uma Rede Neural Multilayer Perceptron, focalizando o conjunto de dados relacionado ao diabetes. O pré-processamento dos dados ocorre da seguinte maneira: a leitura dos dados é realizada a partir de um arquivo JSON denominado 'diabetes_json.json'. As classes dos dados, originalmente em formato de string, são convertidas em valores binários (1 ou 0) com base nas condições 'tested_positive' ou 'tested_negative'. A divisão dos dados em conjuntos de treino e teste é efetuada utilizando a função train_test_split do sklearn.

O scikit-learn (sklearn) é empregado da seguinte maneira: o classificador de Perceptron Multicamadas é utilizado para treinar a rede neural. Parâmetros como taxa de aprendizado, número de neurônios na camada escondida e número máximo de iterações são configurados. Além disso, os dados são normalizados através do StandardScaler para otimizar o desempenho do modelo.

O código implementa um loop aninhado para avaliar diferentes combinações de taxas de aprendizado e tamanhos de camada escondida. Uma tabela de resultados é gerada utilizando a biblioteca PrettyTable, exibindo métricas como acurácia média, erro quadrático médio médio e matriz de confusão média para cada conjunto específico de hiperparâmetros.
