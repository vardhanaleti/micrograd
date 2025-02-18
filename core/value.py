from ..micrograd.trace_graph import draw_dot

OPS = {
    "__add__": "+",
    "__mul__": "*"
}

class Value:

    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self.grad = 0
        self._children = set(_children)
        self._op = _op
        
    def __repr__(self):
        return f"Value(data={self.data}, _op={self._op}, _children={self._children})"
    
    def __add__(self, other):
        return Value(self.data + other.data, (self, other), OPS.get(self.__add__.__name__))

    def __mul__(self, other):
        return Value(self.data * other.data, (self, other), OPS.get(self.__mul__.__name__))

    
    

a = Value(2.0, label='a')
b = Value(-3.0, label='b')
c = Value(10.0, label='c')
  
print(c)
draw_dot(c)




