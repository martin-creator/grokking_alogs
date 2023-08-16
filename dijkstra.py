# Dijkstra's algorithm for shortest paths
# There are 4 steps:
# 1. Find the cheapest node. This is the node you can get to in the least amount of time.
# 2. Check whether there's a cheaper path to the neighbors of this node. If so, update their costs.
# 3. Repeat until you've done this for every node in the graph.
# 4. Calculate the final path.
# This algorithm only works with directed acyclic graphs (DAGs).
# For weighted graphs with negative weights, use Bellman-Ford algorithm.

# Implementation of Dijkstra's algorithm in Python
# We shall need a graph, costs table  and parents

from cmath import cos
from concurrent.futures import process


infinity = float("inf")

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# The costs table is used to keep track of the costs of the nodes
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# The parents table is used to keep track of the parents of the nodes
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = [] # Array to keep track of all the nodes that have already been processed

# pseudocode
# while there are nodes to process
# grab the node closest to the start
# update costs for its neighbors
# if any of the costs were updated, update the parents too
# mark the node as processed
# repeat until you've processed every node in the graph

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # Go through each node
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # If it's the lowest cost so far and hasn't been processed yet
            lowest_cost = cost # ... set it as the new lowest-cost node
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs) # Find the lowest-cost node that you haven't processed yet
while node is not None: # If you've processed all the nodes, this while loop is done
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # Go through all the neighbors of this node
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # If it's cheaper to get to this neighbor by going through this node
            costs[n] = new_cost # update the cost for this node
            parents[n] = node # This node becomes the new parent for this neighbor
    processed.append(node) # Mark the node as processed
    node = find_lowest_cost_node(costs) # Find the next node to process, and loop

print("Cost from the start to each node:")
print(costs) # Output: Cost from the start to each node: {'a': 5, 'b': 2, 'fin': 6}

# Examples of real world applications of Dijkstra's algorithm
# 1. GPS navigation systems
# 2. Network routing protocols
# 3. Biology: Used to model the spread of viruses among humans
# 4. Airline tickets: Used by airlines to determine ticket prices
# 5. Google Maps: Used to find the fastest route from point A to point B
# 6. Uber: Used to find the Uber driver closest to you
# 7. Operating systems: Used for resource allocation
# 8. Social networking: Used to model the spread of information
# 9. Internet search engines: Used to rank webpages in search results
# 10. Machine learning: Used to model the flow of traffic
# 11. Video games: Used to find paths from enemies to players
# 12. Robotics: Used to model the movement of robots
# 13. Air traffic control: Used to route planes to their destination
# 14. Manufacturing: Used to control robots in a factory
# 15. Computer chip design: Used to design computer chips
# 16. Movie studios: Used to generate movies

# commonly asked dijkstra's algorithm interview questions and answers
# 1. What is Dijkstra's algorithm?
# Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.

# 2. What is the time complexity of Dijkstra's algorithm?
# The time complexity of Dijkstra's algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph. This is because the algorithm uses a priority queue to store the distances to the vertices, and a priority queue takes O(log V) time to insert and delete elements.

# 3. What is the difference between Dijkstra's algorithm and Bellman-Ford algorithm?
# Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later. Bellman-Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph. It is slower than Dijkstra's algorithm for the same problem, but more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers.

# 4. What is the difference between Dijkstra's algorithm and A* algorithm?
# Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later. A* algorithm is an algorithm that is used in pathfinding and graph traversal. It is an extension of Dijkstra's algorithm with a heuristic function that guides the search so that it expands nodes in the most promising order.

