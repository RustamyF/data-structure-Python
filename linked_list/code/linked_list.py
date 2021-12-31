class ListNode :
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self, data):
        new_node=ListNode(data)
        self.head=new_node
        self.tail=new_node
    def print_list(self):
        # start from the head of linked-list
        temp=self.head
        # loop over each element until the temp.next is None
        while temp is not None:
            # at each node, print the data
            print(temp.data)
            # got to the next node
            temp=temp.next
    def insert_tail(self,data):
        # initiate the new node using the new data
        new_node = ListNode(data)
        # if there is no head, create the head node
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        # if it is not the head node, point the tail to the new node and change tail
        else:
            self.tail.next=new_node
            self.tail=new_node
    def insert_head(self,data):
        # initiate the new node using the new data
        new_node=ListNode(data)
        # if there is no head, create the head node
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        # if it is not the head node, point the new node to head and change the head to new node
        else:
            new_node.next=self.head
            self.head=new_node
    def search(self, data):
        # start from the head of linked-list
        temp=self.head
        # loop until the end of linked-list
        while temp is not None:
            # if the node values is equal to data, return True
            if temp.data==data:
                return True
            # go to the next node
            temp=temp.next
        # if the values is not there, return False
        return False
    def get(self, index):
        # check if head is None or index is below zero
        if self.head is None and index<0:
            return False
        # start from the head of linked-list
        temp=self.head
        # loop over each element until the index
        for _ in range(index):
            # check if the index is more than the length of linked_list
            if temp is None:
                return False
            temp=temp.next
        # return the node value
        return temp
    def delete(self, index):
        # check if head is None or index is below zero
        if self.head is None and index<0:
            return False
        # check if it is the head node
        if index==0:
            self.head=self.head.next
        # get the node before using the get() method
        temp=self.get(index-1)
        # check to see if it is a tail node
        if temp.next==self.tail:
            temp.next=None
            self.tail=temp
        else:
            temp.next=temp.next.next

    def update(self, index, data):
        # get the element using its index and get() method
        temp=self.get(index)
        # change its data
        temp.data=data






ll=[4,5,4,4]


my_list=linked_list(5)
my_list.insert_tail(4)
my_list.insert_head(4)
my_list.insert_tail(4)
my_list.insert_tail(6)

my_list.delete(2)

my_list.update(1,10)

my_list.print_list()
# print(my_list.search(6))
# print(my_list.get(2))

