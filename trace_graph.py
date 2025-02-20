from graphviz import Digraph
from core.value import Value


def trace(root):
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._children:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges



def draw_dot(root):

    assert randir in ['LR', 'TB']
    dot = Digraph(format='svg', graph_attr={'rankdir': randir})
    nodes, edges = trace(root)
    for n in nodes:
        dot.node(name=str(id(n)), label = "{ data %.4f | grad %.4f }" % (n.data, n.grad), shape='record')
        if n._op:
            dot.node(name=str(id(n)) + n._op, label=n._op)
            dot.edge(str(id(n)) + n._op, str(id(n)))
    
    for n1, n2 in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)
    
    return dot
        

x = Value(1.0)
y = (x * 2 + 1)
draw_dot(y)