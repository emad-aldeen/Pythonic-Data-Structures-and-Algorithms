from data_structures_and_algorithms.data_structures.graph.graph import Graph

def test_add_node():
    gr = Graph()

    assert gr.add_node('start').value == 'start'


def test_add_edge():
    gr = Graph()
    start = gr.add_node('start')
    end = gr.add_node('end')
    gr.add_edge(start, end)

    assert gr.adjacency_list[start][0] == (end, 1)


def test_get_nodes():
    gr = Graph()
    gr.add_node('1')
    gr.add_node('2')
    gr.add_node('3')

    assert len(gr.get_nodes()) == 3


def test_get_neighbors():
    gr = Graph()
    start = gr.add_node('start')
    end = gr.add_node('end')
    gr.add_edge(start, end,4)
    neighbors = gr.get_neighbors(start)

    assert neighbors[0][0].value == 'end'
    assert neighbors[0][1] == 4


def test_size():
    gr = Graph()
    gr.add_node('ana')
    gr.add_node('3nde')
    gr.add_node('prop')
    gr.add_node('bl')
    gr.add_node('terminal')
    gr.add_node(',')
    gr.add_node('C.U..')

    assert gr.size() == 7
