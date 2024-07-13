import pandas as pd
import networkx as nx
import re
from networkx.algorithms.community import greedy_modularity_communities

# Cargar los datos
df_10_04 = pd.read_csv('./data/tweets_20191004.csv', encoding='iso-8859-3', encoding_errors='replace', sep=';')
df_10_19 = pd.read_csv('./data/tweets_20191019.csv', encoding='iso-8859-3', encoding_errors='replace', sep=';')
df_11_03 = pd.read_csv('./data/tweets_20191103.csv', encoding='iso-8859-3', encoding_errors='replace', sep=';')

# Función para extraer menciones de un texto de tweet
def extraer_menciones(texto):
    menciones = re.findall(r'@\w+', texto)
    return menciones

# Función para crear y exportar la red a GEXF con detección de comunidades
def crear_y_exportar_gexf(df, fecha):
    G = nx.DiGraph()

    # Añadir aristas basadas en menciones
    for index, row in df.iterrows():
        user = row['user_id']
        menciones = extraer_menciones(row['text'])
        for mencion in menciones:
            G.add_edge(user, mencion)

    # Filtrar nodos con pocas conexiones
    G = G.subgraph([node for node, degree in dict(G.degree()).items() if degree > 1])

    # Detección de comunidades
    communities = greedy_modularity_communities(G)
    community_map = {}
    for i, community in enumerate(communities):
        for node in community:
            community_map[node] = i
    
    nx.set_node_attributes(G, community_map, 'community')

    # Asignar colores a los nodos según la comunidad
    colors = [community_map[node] for node in G.nodes()]
    nx.set_node_attributes(G, {node: colors[i] for i, node in enumerate(G.nodes())}, 'color')

    # Guardar el grafo en formato GEXF
    nx.write_gexf(G, f'network_{fecha}.gexf')
    print(f'Archivo GEXF guardado: network_{fecha}.gexf')

# Crear y exportar redes para cada DataFrame
crear_y_exportar_gexf(df_10_04, '20191004')
crear_y_exportar_gexf(df_10_19, '20191019')
crear_y_exportar_gexf(df_11_03, '20191103')
