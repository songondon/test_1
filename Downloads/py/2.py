class turtle:
    def __init__(self, deep):
        self.l = []
        self.deep = deep
        
    def _out(self):
        return self.l.pop(0)
        
    def _in(self,n):
        if len(self.l) == self.deep:
            _out()
        self.l.append(n)  
        
    def _len(self):
        return len(self.l)
    
    def _viev(self):
        return(self.l)
    
from collections import deque
class normal:
    def __init__(self, deep):
        self.l = deque()
        self.deep = deep
        
    def _out(self):
        return self.l.popleft()
        
    def _in(self,n):
        if len(self.l) == self.deep:
            _out()
        self.l.append(n)  
        
    def _len(self):
        return len(self.l)
    
    def _viev(self):
        return(self.l)
    
# использование списков - хорошее средство не прибегая к библеотекам, но не самое производительное
# использование методов класса deque производительней, но в классе normal не реализовывается весь потенциал встроенных библиотек в вопросе о fifo