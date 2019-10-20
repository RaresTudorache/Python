#/class Person:

    #def __init__(self,name,job):
    #    self.name = name
   #     self.job = job
    
  #  def getEmployeeDescription(self):
 #       return self.name + "is a" + self.job

#p = Person("Freddie","Algorithm Designer")
#print(p.name)


import abc
class Queue(abc.ABC):

    @abc.abstractmethod
    def isEmpty(self):
        pass

    @abc.abstractmethod
    def push(self,x):
        pass
    
    @abc.abstractmethod
    def pop(self):
        pass

class CircBuffer_Queue(Queue):
    def __init__(self,n):
        self.size = n
        self.buffer= [()] * n
        self.head = 0
        self.tail = 0
        self.full = False

    def isEmpty(self):
        return (self.head == self.tail and
        (not self.full))
    
    def push(self,x):
        if self.full:
            raise OverflowError("The Buffer is full")
        else:
            self.buffer[self.tail] = x
            self.tail = (self.tail + 1) % self.size
            if self.head == self.tail:
                self.full = True
    def pop(self):
        if self.isEmpty():
            raise OverflowError("ai belito")
        else:
            x = self.buffer[self.head]
            self.head = (self.head - 1) %self.size
            self.full = False
            return x

q = CircBuffer_Queue(10)
print(q.isEmpty())
     

class LL_Queue(Queue):

    def __init__(self):
        self.tail = [()]
        self.head = self.tail

    def isEmpty(self):
        return self.head[0] == ()

    def push(self,x):
        self.tail[0] = (x,[()])
        self.tail = self.tail[0][1]

    def pop(self):
        if self.isEmpty():
            raise IndexError
        else:
            y = self.head[0][0]
            self.head = self.head[0][1]
            return y


#def square(value):
    #print("hello world")
#    return value*value

#print(square(2))