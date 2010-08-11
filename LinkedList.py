MSG_TypeError_LinkedNode = "Only a LinkedNode object is allowed as argument."

class LinkedNode:
	def __init__(self, data=0, next=None):
		self.__checkNext__(next)
		self._data = data
		self._next = next
	@classmethod
	def __checkNext__(cls, next):
		if not (isinstance(next, cls) or next == None):
			raise TypeError( MSG_TypeError_LinkedNode )
	def getData(self):
		return self._data
	def getNext(self):
		return self._next
	def setData(self, data):
		self._data = data
	def setNext(self, next):
		self.__checkNext__(next)
		self._next = next

class LinkedList:
	@staticmethod
