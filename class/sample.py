class SimpleData:
    
    def __init__(self):
        self.a = 100
        self.b = 200

    
    def sum(self):
        return self.a + self.b
    
    def set(self, a, b):
        self.a = a
        self.b = b

class SimpleData2:
    val = 'bbb'

    def __init__(self, arg):
        print('this is SimpleData2')
        self.val = arg

class child(SimpleData2):
    child_val = 'CHILD'    
    def __init__(self):
        print('this is child')

data1 = SimpleData()
data2 = SimpleData()
data2.set(1,2)
print(data1.sum())
print(data2.sum())

data3 = SimpleData2('ccc')
print(SimpleData2.val)
print(data3.val)

print(child.val)
print(child.child_val)

call_child = child()
call_child