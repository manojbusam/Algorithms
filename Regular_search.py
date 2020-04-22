class Regular_Search:
	def regular_search(self,list,item):
		index = 0
		for i in list:
			if i == item:
				return index
			index += 1
		return None


R = Regular_Search()

R.regular_search([1,2,3,45],45) # 3