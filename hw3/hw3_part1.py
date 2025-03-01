import graphviz
import random 

def create_fake_data():
    graph = graphviz.Digraph('FakeGraph')

    for i in range(2):
        node_name = f'Node_{i}'
        graph.node(node_name)

    for i in range(20):   #connnect random edges
        source_node = f'Node_{random.randint(0, 19)}'
        target_node = f'Node_{random.randint(0, 19)}'
        graph.edge(source_node, target_node)

    graph.view()



def create_bipartite_graph(num_nodes_, num_nodes_2, probability = .5):
    graph = graphviz.Digraph('RandomBipartiteGraph')

    for i in range(num_nodes_):
        node_name = f'_Node_{i}'
        graph.node(node_name, color='red')  

    for i in range(num_nodes_2):
        node_name = f'Set2_Node_{i}'
        graph.node(node_name, color='blue') 

    for i in range(num_nodes_):
        for j in range(num_nodes_2):
            source_node = f'_Node_{i}'
            target_node = f'Set2_Node_{j}'
            if random.uniform(0, 1) < probability:
                graph.edge(source_node, target_node)

    graph.view()


def create_clique_graph(num_nodes):
    graph = graphviz.Digraph('CliqueGraph')

    for i in range(num_nodes):
        node_name = f'Node_{i}'
        graph.node(node_name)

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            source_node = f'Node_{i}'
            target_node = f'Node_{j}'
            graph.edge(source_node, target_node)

    graph.view()


def create_disconnected_components_graph():
    graph = graphviz.Digraph('DisconnectedComponentsGraph')

    for i in range(1, 6):
        graph.node(f'_Node{i}', color='red')  
        if i < 5:
            graph.edge(f'_Node{i}', f'_Node{i+1}')

    for i in range(1, 4):
        graph.node(f'_Node{i}', color='blue')  
        if i < 3:
            graph.edge(f'_Node{i}', f'_Node{i+1}')

    graph.view()



def create_sparse_graph():
    graph = graphviz.Digraph('SparseGraph', engine='neato')

    graph.attr(nodesep='1', ranksep='1')

    for i in range(1, 11):
        graph.node(f'Node{i}')

    for i in range(1, 11):
        for j in range(i + 1, 11):
            if i != j and i % 2 == 0 and j % 2 == 0:  
                graph.edge(f'Node{i}', f'Node{j}')

    graph.view()


if __name__ == "__main__":
        
    # create_fake_data()
    # create_clique_graph(25)
    # create_bipartite_graph(15,15)
    # create_disconnected_components_graph()
    create_sparse_graph()
