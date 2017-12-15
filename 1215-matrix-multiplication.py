import numpy

matrix = [[0.6, 0.4],
		  [0.3, 0.7]]

arr = input("input 2 number (separated by a space): ").split()
arr = [int(arr[0]), int(arr[1])]
for i in range(10):
	arr = numpy.dot(arr, matrix)
	arr = [round(arr[0]), round(arr[1])]
	print("#"+str(i+1), arr[0], arr[1])
