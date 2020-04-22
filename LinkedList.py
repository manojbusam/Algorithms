# A simple illustration of Linkedlist
# Defining Linked List 
class LinkedList:
	def __init__(self,value):
		self.value = value
		self.next = None

# Defining Objects
L1 = LinkedList(1)
L2 = LinkedList(2)
L3 = LinkedList(3)

L1.next = L2
L2.next = L3

# Retrieving values from objects
L1.value       # 1
L1.next        # L2 LinkedList object
L1.next.value  #2
