class LinkedList:
	def __init__(self,value):
		self.value = value
		self.next = None

L1 = LinkedList(1)
L2 = LinkedList(2)
L3 = LinkedList(3)

L1.next = L2

L2.next = L3

L1.value       # 1
L1.next        # L2 LinkedList object
L1.next.value  #2