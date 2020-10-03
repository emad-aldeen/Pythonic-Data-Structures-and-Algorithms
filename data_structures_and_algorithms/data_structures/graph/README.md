# Graph

<br>

## Challenge:

Implement the graph, which should be represented as an adjacency list, and should include the following methods: add_node(), add_edge(), get_nodes(), get_neighbors(), size()

<br>
<br>

## Approach & Efficiency:

* add_node() time Big O(1), space Big O(1)

* get_nodes() time Big O(1), space Big O(1)

* add_edge() time Big O(1), space Big O(1)

* get_neighbors() time Big O(1), space Big O(1)

* size() time Big O(1), space Big O(1)

<br>
<hr>

## APIs:

1. add_node():

    * Adds a new vertex to the graph
    * Input: the value of that vertex
    * Output: the added vertex

2. add_edge():

    * Adds a new edge between two nodes in the graph with ability to add weight
    * Input: two vertexes to be connected by the edge
    * Both nodes should already be in the Graph

3. get_nodes():

    * Returns all of the vertexes in the graph as a collection

4. get_neighbors():

    * Returns a collection of vertexes connected to the given vertex with the weights of their connections
    * Input: Takes in a given vertex

5. size():

    * Returns the total number of nodes in the graph