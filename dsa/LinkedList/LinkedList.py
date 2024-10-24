
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList : 
    def __init__(self):
        # default 0 length linked list
        self.head = None
        # size of the linked list
        self.n = 0

    def getLastNode(self):

        # check if the head is None

        if self.head is None:
            return self.head
        
        pointer = self.head

        
        while pointer.next is not None :
            #print(pointer.value,end = "->")
            pointer = pointer.next
        return pointer



    def append(self,value):
        # create a new node 
        new_node = Node(value)

        # traverse to the last node
        lastNode = self.getLastNode()

        # check if the last Node is Null

        if lastNode is None:
            self.head = new_node

        else:
            lastNode.next = new_node
        self.n +=1
    def traversal(self):

        if self.head is None :
            print("Null")
        
        pointer = self.head
        while pointer is not None:
            print(pointer.value,end="->")
            pointer = pointer.next
        print("\n")

    def getNodeAt(self,pos):
        # returns the pointer before pos
        # check the position limits 

        if 0<= pos< self.n:
            pointer = self.head
            while pos>0:
                pointer = pointer.next
                pos-=1
            return pointer
        else :
        
            # raise an error
            print("out of range index error")


            
        

    
    def insert_at(self,pos,val):
        new_node = Node(val)

        if pos == 0 :
            new_node.next = self.head
            self.head = new_node
            self.n +=1
        

        current_node = self.getNodeAt(pos-1)
        print(f"Node value at {pos}: {current_node.value}")
        
        if current_node is None :
            self.head = new_node
        else : 
            new_node.next = current_node.next
            current_node.next = new_node
        

obj = LinkedList()

obj.append(3)
obj.append(4)
obj.append(5)
obj.append(10)
print(obj.n)
obj.traversal()
obj.insert_at(2,15)
obj.traversal()
obj.insert_at(0,23)
obj.traversal()