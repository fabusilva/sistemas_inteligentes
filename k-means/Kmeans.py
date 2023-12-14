from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

dados = np.array([
    [1, 1.9, 7.3],
    [2, 3.4, 7.5],
    [3, 2.5, 6.8],
    [4, 1.5, 6.5],
    [5, 3.5, 6.4],
    [6, 2.2, 5.8],
    [7, 3.4, 5.2],
    [8, 3.6, 4],
    [9, 5, 3.2],
    [10, 4.5, 2.4],
    [11, 6, 2.6],
    [12, 1.9, 3],
    [13, 1, 2.7],
    [14, 1.9, 2.4],
    [15, 0.8, 2],
    [16, 1.6, 1.8],
    [17, 1, 1]
])

n_clusters = 3

kmeans = KMeans(n_clusters=n_clusters)

kmeans.fit(dados)

rotulos = kmeans.labels_

dados_clusterizados = np.column_stack((dados, rotulos))

cores = ['red', 'blue', 'green']
for i in range(n_clusters):
    pontos_cluster = dados_clusterizados[dados_clusterizados[:, -1] == i]
    print(f'Cluster {i}')
    print(pontos_cluster)
    print('________________________')
    plt.scatter(pontos_cluster[:, 1], pontos_cluster[:, 2], c=cores[i], label=f'Cluster {i + 1}')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.legend()

plt.show()
