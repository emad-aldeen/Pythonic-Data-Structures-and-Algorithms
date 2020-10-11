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


def test_get_edges_one_vertex():
    g = Graph()
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    v3 = g.add_node('Monstropolis')
    v4 = g.add_node('Metroville')
    v5 = g.add_node('Naboo')
    v6 = g.add_node('Narnia')
    g.add_nondirectional_edge(v1, v2, 110)
    g.add_nondirectional_edge(v2, v3, 50)
    g.add_nondirectional_edge(v2, v4, 12)
    g.add_nondirectional_edge(v3, v5, 43)
    g.add_nondirectional_edge(v4, v5, 23)
    g.add_nondirectional_edge(v4, v6, 14)
    g.add_nondirectional_edge(v5, v6, 21)
    
    actual = g.get_edge(['Mordor'])
    expected = (True, '$0')
    
    assert actual == expected


def test_get_edges_two_vertex():
    g = Graph()
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    v3 = g.add_node('Monstropolis')
    v4 = g.add_node('Metroville')
    v5 = g.add_node('Naboo')
    v6 = g.add_node('Narnia')
    g.add_nondirectional_edge(v1, v2, 110)
    g.add_nondirectional_edge(v2, v3, 50)
    g.add_nondirectional_edge(v2, v4, 12)
    g.add_nondirectional_edge(v3, v4, 75)
    g.add_nondirectional_edge(v3, v5, 43)
    g.add_nondirectional_edge(v4, v5, 23)
    g.add_nondirectional_edge(v4, v6, 14)
    g.add_nondirectional_edge(v5, v6, 21)
    
    actual = g.get_edge(['Monstropolis', 'Metroville'])
    expected = (True, '$75')
    
    assert actual == expected


def test_three_vertex():
    g = Graph()
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    v3 = g.add_node('Monstropolis')
    v4 = g.add_node('Metroville')
    v5 = g.add_node('Naboo')
    v6 = g.add_node('Narnia')
    g.add_nondirectional_edge(v1, v2, 110)
    g.add_nondirectional_edge(v2, v3, 50)
    g.add_nondirectional_edge(v2, v4, 12)
    g.add_nondirectional_edge(v3, v4, 75)
    g.add_nondirectional_edge(v3, v5, 43)
    g.add_nondirectional_edge(v4, v5, 23)
    g.add_nondirectional_edge(v4, v6, 14)
    g.add_nondirectional_edge(v5, v6, 21)
    
    actual = g.get_edge(['Pandora', 'Mordor', 'Monstropolis'])
    expected = (True, '$160')
    
    assert actual == expected


def test_false_get_edges():
    g = Graph()
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    v3 = g.add_node('Monstropolis')
    v4 = g.add_node('Metroville')
    v5 = g.add_node('Naboo')
    v6 = g.add_node('Narnia')
    g.add_nondirectional_edge(v1, v2, 110)
    g.add_nondirectional_edge(v2, v3, 50)
    g.add_nondirectional_edge(v2, v4, 12)
    g.add_nondirectional_edge(v3, v4, 75)
    g.add_nondirectional_edge(v3, v5, 43)
    g.add_nondirectional_edge(v4, v5, 23)
    g.add_nondirectional_edge(v4, v6, 14)
    g.add_nondirectional_edge(v5, v6, 21)
    
    actual = g.get_edge(['Naboo, Pandora'])
    expected = (False, '$0')

    assert actual == expected

def test_depth_first():
    graph = Graph()

    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')

    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(c, e)
    graph.add_edge(e, f)

    vertices_lst = graph.depth_first(a)

    assert vertices_lst == [a.value, b.value, c.value, e.value, f.value, d.value]