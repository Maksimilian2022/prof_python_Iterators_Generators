nested_list = [['a', 'b', 'c'],
			   ['d', 'e', 'f', 'h', False],
			   [1, 2, None]]

class Number1:
	def __init__(self, new_list, step2=-1, step=0):
		self.new_list = new_list
		self.step2 = step2
		self.step = step
		self.i = len(self.new_list)
		return

	def __iter__(self):
		self.step1 = self.step
		return self

	def __next__(self):
		if self.step2 == len(self.new_list[self.step1]) - 1:
			self.step1 += 1
			self.step2 = -1
		if self.step1 >= len(self.new_list):
			raise StopIteration
		if self.step2 <= len(self.new_list[self.step1]):
			self.step2 += 1
			return self.new_list[self.step1][self.step2]






def nested_list_generate():
	step1 = 0
	step2 = -1
	while step2 < len(nested_list[step1]) - 1:
		step2 += 1
		yield nested_list[step1][step2]
		if step2 == len(nested_list[step1]) - 1:
			step1 += 1
			step2 = -1
			if step1 > len(nested_list) - 1:
				break




nested_list2 = [['a', 'b', 'c', ['g', 7, [9, ['gg']]]],
			   ['d', 'e', 'f', 'h', False],
			   [1, 2, None]]



def nested_list_generate2():
	step1 = 0
	while step1 < len(nested_list2):
		list_for_nested_elements = nested_list2[step1]
		step1 += 1
		i = -1
		list1 = []
		b = 0
		while i <= b:
			for element1 in list_for_nested_elements:
				list1.append(element1)
			list_for_nested_elements.clear()
			for element2 in list1:
				if type(element2) != list:
					list_for_nested_elements.append(element2)
				else:
					b += 1
					for element3 in element2:
						list_for_nested_elements.append(element3)
			list1.clear()
			i += 1
			if i > b:
				for element4 in list_for_nested_elements:
					break_counter = 0
					yield element4
					break_counter += 1
					if break_counter == len(list_for_nested_elements):
						break
print(nested_list_generate2())
