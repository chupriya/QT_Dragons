import networkx as nx
import plotly.graph_objects as go
import numpy as np

def plot_entanglement_graph(ent_matrix):
    n = len(ent_matrix)

    G = nx.Graph()

    for i in range(n):
        G.add_node(i)

    for i in range(n):
        for j in range(i+1, n):
            if ent_matrix[i][j] > 0:
                G.add_edge(i, j, weight=ent_matrix[i][j])

    pos = nx.spring_layout(G, dim=3)

    edge_x, edge_y, edge_z = [], [], []

    for edge in G.edges():
        x0, y0, z0 = pos[edge[0]]
        x1, y1, z1 = pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]
        edge_z += [z0, z1, None]

    edge_trace = go.Scatter3d(
        x=edge_x, y=edge_y, z=edge_z,
        mode='lines',
        line=dict(width=4),
    )

    node_x, node_y, node_z = [], [], []

    for node in G.nodes():
        x, y, z = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_z.append(z)

    node_trace = go.Scatter3d(
        x=node_x, y=node_y, z=node_z,
        mode='markers+text',
        text=[f"Q{n}" for n in G.nodes()],
        marker=dict(size=8)
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.show()