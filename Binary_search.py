class Binary_Search:

	def binary_search(self,list,item):

		low = 0

		high = len(list) - 1

		while low <= high:

			mid = (low + high)//2

			guess = list[mid]

			if guess == item :
				return mid
			elif guess < mid:
				high = mid - 1
			else:
				low = mid + 1
		return None



b = Binary_Search()

b.binary_search([1,2,3],3) #2

 b.binary_search([1,2,3],4) #None