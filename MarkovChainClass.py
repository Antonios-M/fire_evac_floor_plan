import math
import random
import random
import numpy as np # type: ignore
import itertools
import pandas as pd
from typing import Dict, List, Tuple, Union
import networkx as nx
import networkx as nx
import matplotlib.pyplot as plt
import pygad
import numpy as np
import pickle
## page 2084
Decomposition_graph_node_mapping ={ 
    
    ## Decomposition graph mapping from nodes to activity names
        1: 'Pre-event activity, typically sleeping',
        2: 'Investigate / Misinterpret',
        3: 'Encounter Smoke or Fire',
        4: 'Dress',
        5: 'Enter room of fire origin',
        6: 'Close door',
        7: 'Fight fire',
        8: 'Encounter difficulties in smoke',
        9: 'Evasive',
        10: 'Search for person in smoke',
        11: 'Feel concern',
        12: 'Wait for person to return',
        13: 'Phone fire brigade',
        14: 'Rescue Attempt',
        15: 'Exit (start evacuation route)'
    }
    
Decomposition_graph_node_colour_mapping ={

    ## Decomposition graph mapping to colours
    1: '#A2AD59',
    2: '#FF5400',
    3: '#FF5400',
    4: '#A2AD59',
    5: '#FF5400',
    6: '#FF5400',
    7: '#FF5400',
    8: '#FF5400',
    9: '#FF5400',
    10: '#FF5400',
    11: '#A2AD59',
    12: '#FF5400',
    13: '#FF5400',
    14: '#A2AD59',
    15: '#04A777'
}

Decomposition_graph_edges = [

    ## Graph weights from original decomposition graph
    (1,2, 9.84),
    (1,3, 1.94),
    (2,3, 8.88),
    (2,5, 3.13),
    (2,9, 1.72),
    (2,10, 1.34),
    (3,3, 2.12),
    (3,6, 0.89),
    (3,7, 0.1),
    (3,13,1.34),
    (4,2, 1.79),
    (5,3,2.24),
    (5,8, 1.34),
    (6,9, 0.45),
    (7,7, 3.58),
    (7,8,1.79),
    (8,8, 2.12),
    (8,9 , 3.90),
    (9, 15, 14.3),
    (10,15, 10),
    (11,12, 0.89),
    (12,12, 0.89),
    (12,2, 2.68),
    (13,15, 10),
    (14,8, 1.79),
]

Decomposition_graph_initial_node_weights = {

    ## weights (seconds taken by each task) use to initiate genetic algorthm
    1: 90,
    2: 90,
    3: 90,
    4: 90,
    5: 90,
    6: 90,
    7: 90,
    8: 90,
    9: 90,
    10: 90,
    11: 90,
    12: 90,
    13: 90,
    14: 90,
    15: 90,
}


## start actions of pre-evacuation decomposition graph
Start_nodes = [1,4,11,14]

## end action of pre_evacuation decomposition graph (start evacuation)
End_node = 15

## desired mean / expected pre-evacuation time (seconds)
Expected_preEvac_time = 318

class behaviour_in_fire_markov_chain:
    """ Data taken from the Decomposition Graph of human behaviour during domestic fire emergencies"""
    """ class outputs decomposition graph and graphviz, and training dataset for regression (adjust sampling as needed, now its random)"""
    def __init__(self, number_of_samples, colour_mapping = Decomposition_graph_node_colour_mapping, graph_edges = Decomposition_graph_edges, node_attributes = list(Decomposition_graph_initial_node_weights.values()), start_nodes = Start_nodes, end_node = End_node) -> None:

        ## class input variables
        self.colour_mapping = colour_mapping
        self.graph_edges = graph_edges
        self.node_attributes = {i + 1: x for i, x in enumerate(node_attributes)}
        self.start_nodes = start_nodes
        self.end_node = end_node
        self.number_of_samples = number_of_samples

        ## class return variables
        self.graph = self.__get_probability_graph()
        self.mean_time = self.__get_mean_time()
            
    def __get_probability_graph(self):

        edges = self.graph_edges
        node_weights = self.node_attributes
    

        # Create a directed graph
        G = nx.DiGraph()

        # Add edges with weights
        G.add_weighted_edges_from(edges)

        # Dictionary to store outgoing edge weights for each node
        outgoing_weights = {}
        
        # Set node attributes (weights)
        nx.set_node_attributes(G, node_weights, name='weight')

        # Iterate over nodes
        for node in G.nodes():
            outgoing_weights[node] = {}

            # Iterate over outgoing edges
            for successor in G.successors(node):
                weight = G[node][successor]['weight']
                outgoing_weights[node][successor] = weight

        def find_probabilities(p):
            """ Normalises values as probabilities from 0 to 1 so that the sum of the probabilities is 1"""

            will_happen_prob = sum(p)
            new_prob = [round((prob / will_happen_prob), 3) for prob in p]
            return new_prob


        for node in list(outgoing_weights.keys()):
            values = outgoing_weights[node].values()
            probabilities = find_probabilities(values)

            for neighbour_i, neighbour_node in enumerate(list(outgoing_weights[node].keys())):
                G[node][neighbour_node]['weight'] = probabilities[neighbour_i]

        return G

    def show_graph_with_weights(self):

        graph = self.graph

        ## Initialize plot figsize
        plt.figure(figsize=(8,8))

        pos = {i: (i, i % 5) for i in range(1, 16)}
        pos_node_labels = {i: (i, (i % 5 + 0.24)) for i in range(1, 16)}

        # Draw the nodes
        nx.draw(graph, pos, with_labels=True, node_color=[Decomposition_graph_node_colour_mapping[node] for node in graph.nodes()], node_size=2000)

        # Draw the edges with weights
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edges(graph, pos, width=0.5, edge_color='#D6D1CD')  # Set alpha value for transparency
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        nx.draw_networkx_labels(graph, pos_node_labels, labels= self.node_attributes, bbox=dict(facecolor='#9CBFA7', edgecolor='#C5C3C6', boxstyle='round,pad=0.1', alpha=0.7))
        # Draw self-edges with weights
        for node in graph.nodes():
            if graph.has_edge(node, node):
                x, y = pos[node]
                plt.text(x, y + 0.05, s=graph[node][node]['weight'], bbox=dict(facecolor='grey', alpha=0.4), horizontalalignment='right')

        legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#A2AD59', markersize=10, label='Start Node'),
                        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#04A777', markersize=10, label='Activity Node'),
                        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FF5400', markersize=10, label='End Node')]
        plt.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5), fontsize='large')

        # Show plot
        plt.show()
    
    def simulate_markov_chain(self, start_node, n):
            graph = self.graph
            end_node = self.end_node

            expected_sum = 0
            for _ in range(n):
                current_node = start_node
                sum_weights = 0
                while current_node != end_node:

                    ## successors are the list of neighbours of the current node
                    successors = list(graph.successors(current_node))

                    ## check if node has neighbours
                    if not successors:
                        break

                    ## choose next step based on probabilities, given as markov chain edge weights
                    next_node = random.choices(successors, [graph[current_node][successor]['weight'] for successor in successors])[0]
                    time_to_add = list(graph.nodes(data=True))[current_node - 1][1]['weight']

                    sum_weights += time_to_add

                    current_node = next_node
                expected_sum += sum_weights

            return expected_sum / n
        
    def __get_mean_time(self):
        n = self.number_of_samples
        start_nodes = self.start_nodes
        expected_route_times = []

        for start_node in start_nodes:
            pre_evac_time = self.simulate_markov_chain(start_node, n)
            expected_route_times.append(pre_evac_time)

        return sum(expected_route_times) / len(expected_route_times)

## copied from pre_evacuation_time_prediction.ipynb
optimal_node_attributes = [95.34, 54.55, 111.35, 45.61, 33.35, 90.93, 25.52, 38.42, 106.8, 26.93, 83.25, 19.55, 86.18, 106.19, 0]