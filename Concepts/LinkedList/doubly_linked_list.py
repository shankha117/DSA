class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
	def __init__(self) -> None:
		self.head = None
		self.tail = None
		self.length = 0

	def prepend(self, n:Node):

		if self.head == None:
			self.tail = n
			self.head = n

		else:
			n.next = self.head
			self.head.prev = n
			self.head = n			

		self.length += 1 

	def append(self, n:Node):

		if self.head == None:
			self.tail = n
			self.head = n

		else:
			self.tail.next = n
			n.prev = self.tail
			self.tail = n 		

		self.length += 1 

	
	def printlist(self):
		toprint = self.head

		while toprint != None:
			print(f" {self.head } \n")
			toprint = toprint.next
		
		print("\n")


	def deletewithvalue(self, value:int):

		if not self.head:
			print("No Linked list found ..")
			return
		
		# if head is the node to be deleted
		if self.head.data == value:

			if not self.head.next:
				self.head = self.head.next
				self.head.prev = None
			else:
				self.head = None
				self.tail = None
			
			self.tail -= 1
			return
		
		# find the node to delete

		todelete = self.head.next

		while todelete and todelete.data != value:

			todelete = todelete.next

		if not todelete:
			print("node not found !")
			return


		# if the node is not tail node
		if todelete.next :

			todelete.prev.next = todelete.next

		# if the node is tail node
		else: 
			self.tail = todelete.prev

		
		todelete.prev.next = todelete.next

		self.tail -= 1