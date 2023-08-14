# Breadth First Search Algorithm
# This algorithm is used to find the shortest path between two nodes in a graph.
# A graph is a collection of nodes that are connected to each other by edges.
# Examples of graphs are social networks, molecular structures, and the World Wide Web.
# Real world uses of graphs include finding the shortest path between two points on a map, finding the cheapest way to get from one city to another, and finding the best way to schedule flights.
# Examples of applications that use graphs are Google Maps, Facebook, and LinkedIn.
# A directed graph is a graph where the edges have a direction.
# A directed graph is also known as a digraph.
# Undirected graphs are graphs where the edges do not have a direction.
# Examples of directed graphs are Facebook and Twitter.
# Facebook is a directed graph because if you are friends with someone, they are not necessarily friends with you.
# Twitter is a directed graph because if you follow someone, they are not necessarily following you.
# Examples of undirected graphs are LinkedIn and Instagram.
# LinkedIn is an undirected graph because if you are connected to someone, they are also connected to you.
# Instagram is an undirected graph because if you follow someone, they are also following you.
# A weighted graph is a graph where the edges have a weight.
# Examples of weighted graphs are Google Maps and Waze.
# An unweighted graph is a graph where the edges do not have a weight.
# Examples of unweighted graphs are Facebook and Twitter.
# A cyclic graph is a graph where there is a path from one node back to itself.
# Examples of cyclic graphs are Facebook and Twitter.
# An acyclic graph is a graph where there is no path from one node back to itself.
# Examples of acyclic graphs are LinkedIn and Instagram.

# The time complexity of breadth first search is O(V + E) where V is the number of vertices and E is the number of edges.
# The space complexity of breadth first search is O(V).
# Vertices are the nodes of the graph.
# Edges are the connections between the nodes.
# The best case time complexity of breadth first search is O(1) when the start node is the same as the target node.
# The worst case time complexity of breadth first search is O(V + E) when the target node is the last node in the graph or is not in the graph.
# The two main steps of breadth first search are:
# 1. Add the start node to the queue.
# 2. While the queue is not empty, remove the first node from the queue and add its neighbors to the queue.
# Breadth first search answers the question: Is there a path from node A to node B? and if so, what is the shortest path from node A to node B?

# Bread first search uses a queue to store the nodes that need to be visited.
# This is because the nodes are visited in the order that they were added to the queue.
# The first node that is added to the queue is the first node that is visited.
# The queue is a first in first out data structure.
# The queue supports two operations: enqueue and dequeue.
# Enqueue adds an item to the end of the queue.
# Dequeue removes an item from the front of the queue.
# There is no random access in a queue.

# Implementation of breadth first search in Python

# Import the deque class from the collections module
from collections import deque
from re import search

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm' # Check whether the person's name ends with 'm'. If it does, they're a mango seller

def search(name):
    search_queue = deque() # Create a queue
    search_queue += graph[name] # Add all of your neighbors to the search queue
    searched = [] # This array is how you keep track of which people you've searched before.
    while search_queue: # While the queue isn't empty
        person = search_queue.popleft() # Grab the first person off the queue
        if not person in searched: # Only search this person if you haven't already searched them
            if person_is_seller(person): # Check whether the person is a mango seller
                print(person + " is a mango seller!") # Yes, they're a mango seller
                return True
            else:
                search_queue += graph[person]
                # No, they aren't. Add all of this person's friends to the search queue
                searched.append(person) # Marks this person as searched
    return False # If you reached here, no one in the queue was a mango seller

print(search("you")) # Output: thom is a mango seller! True

