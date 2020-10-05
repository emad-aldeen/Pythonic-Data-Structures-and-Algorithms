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


def test_breadth_first():
    graph = Graph()

    # add all nodes
    apple = graph.add_node('apple')
    banana = graph.add_node('banana')
    cantelope = graph.add_node('cantelope')
    dates = graph.add_node('dates')
    eggplant = graph.add_node('eggplant')
    figs = graph.add_node('figs')

    # add all edges
    graph.add_edge(apple, banana, 1)

    graph.add_edge(banana, apple, 2)
    graph.add_edge(banana, cantelope, 3)
    graph.add_edge(banana, figs, 4)

    graph.add_edge(cantelope, banana, 5)
    graph.add_edge(cantelope, figs, 6)
    graph.add_edge(cantelope, dates, 7)

    graph.add_edge(figs, banana, 8)
    graph.add_edge(figs, cantelope, 9)
    graph.add_edge(figs, dates, 10)
    graph.add_edge(figs, eggplant, 20)

    graph.add_edge(dates, cantelope, 30)
    graph.add_edge(dates, figs, 40)
    graph.add_edge(dates, eggplant, 50)

    graph.add_edge(eggplant, figs, 60)
    graph.add_edge(eggplant, dates, 70)

    assert graph.breadth_first(apple) == {apple, dates, eggplant, cantelope, figs, banana}