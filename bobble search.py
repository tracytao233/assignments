int_array = [13,26,36,47,33,876,44,3,7,8,24,76,543]
index = 0 
switched = True
while (switched == True):
	switched = False
	for index in range (0,len(int_array)-1):
		while int_array[index] > int_array[index + 1]:
			a = int_array[index]
			b = int_array[index + 1]
			int_array[index] = b
			int_array[index + 1] = a
			switched = True
		
if switched == False:
	print(int_array)


