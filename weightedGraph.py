import networkx as nx
import matplotlib.pyplot as plt

class WeightedGraph:
    def __init__(self):
        # self.graph ={}
        self.graph = nx.Graph()

    def add_edge(self, from_node, to_node, weight):
        self.graph.add_edge(from_node, to_node,weight=weight)

    def shortest_path(self, start, end):
        try:
            path = nx.shortest_path(self.graph, source=start, target=end, weight="weight")
            total_distance = nx.shortest_path_length(self.graph, source=start,target=end, weight="weight")
            return path, total_distance
        except nx.NetworkXNoPath:
            return None, None

    def draw_graph(self):
        pos = nx.spring_layout(self.graph)  
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_size=500, node_color='lightblue')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.show()

if __name__ == "__main__":
    weighted_graph = WeightedGraph()
    weighted_graph.add_edge("Ntcheu","Dedza",74)
    weighted_graph.add_edge("Dedza","Salima",96)
    weighted_graph.add_edge("Dedza","Lilongwe",92)
    weighted_graph.add_edge("Salima","Dowa",67)
    weighted_graph.add_edge("Salima","Nkhotakota",112)
    weighted_graph.add_edge("Lilongwe","Dowa",55)
    weighted_graph.add_edge("Lilongwe","Mchinji",109)
    weighted_graph.add_edge("Nkhotakota","Ntchisi",66)
    weighted_graph.add_edge("Mchinji","Kasungu",141)
    weighted_graph.add_edge("Kasungu","Dowa",117)
    weighted_graph.add_edge("Kasungu","Ntchisi",66)
    weighted_graph.add_edge("Ntchisi","Dowa",38)
    
    start_node = "Dedza"
    end_node = "Salima"
    

    path, distance  = weighted_graph.shortest_path(start_node, end_node)

    if path:
        print(f"Shortest Path from {start_node} to {end_node}: {distance}")
    else:
        print(f"No path found from {start_node} to {end_node}")

    weighted_graph.draw_graph()