import random
import networkx as nx
from community import community_louvain
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def draw_graph(G, pos, partition, nodes):
    
    # Color the nodes according to their partition
    cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
    nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=nodes,
                           cmap=cmap, node_color=list(partition.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.show()

def generate_network_graph(n):
    '''
    This function will generate a random weighted network associated to the user specifed
    number of nodes. 
    '''
    # Initialize Dictionary with Nodes
    graph_dict = {node:[] for node in range(n)}
    nodes = list(range(n))
    
    # Generate Edges
    for n, edge_list in graph_dict.items():
        edge_count = random.randint(min(nodes), int(max(nodes) / 2))
        samples_list = random.sample(nodes, edge_count)
        graph_dict[n] = samples_list
    
    # Create Networkx multi-edge graph
    G = nx.MultiGraph(graph_dict)
    return G


def louvain_algorithm(nodes):
    G = generate_network_graph(nodes)

    # Visualize initial graph
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=nodes)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.title("Initial Random Multi-Graph")
    plt.show()

    # Compute the best partition
    partition = community_louvain.best_partition(G)
    print("Modularity for MultiGraph case: " + str(community_louvain.modularity(partition, G)))
    # Draw the Graph
    plt.title("Random Multi-Graph after Louvain Algorithm")
    draw_graph(G,pos,partition,nodes)
 
    # Karate Club graph from Networkx libraru
    # Visualize initial graph
    G = nx.karate_club_graph()
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=nodes)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.title("Initial Karate Graph")
    plt.show()

    # Compute the best partition
    partition = community_louvain.best_partition(G)
    print("Modularity for Karate Club case: " + str(community_louvain.modularity(partition, G)))
    # Draw the Graph
    plt.title("Karate Graph after Louvain Algorithm")
    draw_graph(G,pos, partition,nodes)

if __name__ == '__main__':
    nodes = 0 # Number of Nodes
    while nodes <= 0:
        nodes = int(input("Give number of desired Nodes of the Graph: "))
    louvain_algorithm(nodes)
