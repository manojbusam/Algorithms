class Selection_Sort:

	def findSmallestIndex(self,arr):

		smallest = arr[0]

		smallest_index = 0

		for i in range(len(arr)):

			if arr[i] < smallest:

				smallest = arr[i]

				smallest_index = i

		return smallest_index

	def selection_sort(self,arr):

		newArray = []

		for i in range(len(arr)):

			smallest_index = self.findSmallestIndex(arr)

			newArray.append(arr.pop(smallest_index))

		return newArray


S = Selection_Sort()

S.selection_sort([1,9,8,4,5,8,2])   #[1, 2, 4, 5, 8, 8, 9]