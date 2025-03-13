from logistic_data import labels, edges, sources, sinks, warehouses_sinks
import argparse
from collections import deque

parser = argparse.ArgumentParser(description="Googs logistic")
parser.add_argument("-matrix", action="store_true", help="print capacity matrix")
args = parser.parse_args()

# The function builds a matrix of capacities for the network flow problem.
def build_dynamic_capachity_matrix(labels, edges):
    length = len(labels)
    matrix = [[0 for i in range(length)] for j in range(length)]
    for edge in edges:
        matrix[labels.index(edge[0])][labels.index(edge[1])] = edge[2]
    return matrix

def label_comprassion(label):
    return label[0] + label.split()[1]

def print_matrix_with_labels(matrix, labels):
    cell_width = 5
    delimiter = f"{'_'*(cell_width*len(labels) + cell_width)}"
    print(delimiter)
    print()
    print(f"{'capacity matrix':^110}")
    print(delimiter)
    print(" " * cell_width, end="")
    for label in labels:
        print(f"{label_comprassion(label):<{cell_width}}", end="")
    print()
    for idx, row in enumerate(matrix):
        l = label_comprassion(labels[idx])
        print(f"{l:<{cell_width}}", end="")
        for value in row:
            print(f"{value:<{cell_width}}", end="")
        print()
    print(delimiter)

capacity_matrix = build_dynamic_capachity_matrix(labels, edges)

if args.matrix:
    print_matrix_with_labels(capacity_matrix, labels)

# Function for searching the increasing path (BFS)
def bfs(capacity_matrix, flow_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()
        
        for neighbor in range(len(capacity_matrix)):
            # Check if there is remaining bandwidth in the channel
            if not visited[neighbor] and capacity_matrix[current_node][neighbor] - flow_matrix[current_node][neighbor] > 0:
                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == sink:
                    return True
                queue.append(neighbor)
    
    return False

# Basic function to calculate maximum flow
def edmonds_karp(capacity_matrix, source, sink):
    num_nodes = len(capacity_matrix)
    flow_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    parent = [-1] * num_nodes
    max_flow = 0

    # As long as there is an increasing path, add a stream
    while bfs(capacity_matrix, flow_matrix, source, sink, parent):
        # Find the minimum throughput along the found path (bottleneck)
        path_flow = float('Inf')
        current_node = sink

        while current_node != source:
            previous_node = parent[current_node]
            path_flow = min(path_flow, capacity_matrix[previous_node][current_node] - flow_matrix[previous_node][current_node])
            current_node = previous_node
        
        # Update the flow along the path, taking into account the return flow
        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node
        
        # Increase the maximum flow
        max_flow += path_flow

    return max_flow

total_required_capacity_flow_by_source_map = {}
# Print the maximum flow from each source to each sink
for i_idx, source in enumerate(sources):
    total_capacity_flow_by_source = 0
    for j_idx, sink in enumerate(sinks):
        capacity_flow = edmonds_karp(capacity_matrix, labels.index(source), labels.index(sink))
        print(f"From '{source}' to '{sink}': {capacity_flow}")
        total_capacity_flow_by_source += capacity_flow
    total_required_capacity_flow_by_source_map[source] = total_capacity_flow_by_source


print(f"Total required capacity flow: {total_required_capacity_flow_by_source_map}")

total_required_capacity_flow_by_source_map = {}
for i_idx, source in enumerate(sources):
    total_capacity_flow_by_source = 0
    for j_idx, sink in enumerate(warehouses_sinks):
        capacity_flow = edmonds_karp(capacity_matrix, labels.index(source), labels.index(sink))
        print(f"From '{source}' to '{sink}': {capacity_flow}")
        total_capacity_flow_by_source += capacity_flow
    total_required_capacity_flow_by_source_map[source] = total_capacity_flow_by_source
print(f"Total awailable capacity flow: {total_required_capacity_flow_by_source_map}")