def selection_sort(arrayTosort):
	a = arrayTosort
	for i in range(len(a)):
		idxMin = i
		for j in range(i+1, len(a)):
			if a[j] < a[idxMin]:
				idxMin = j
		a[i],a[idxMin] = a[idxMin], a[i]
	return a


def binary_search(arrTosearch, value):
	left = 0
	right = len(arrTosearch)
	while left <= right:
		mid = (left + right)//2
		if value == arrTosearch[mid]:
			print ("Element " + str(value) +" have index = "+ str(mid))
			break
		elif value > arrTosearch[mid]:
			left = mid + 1
		elif value < arrTosearch[mid]:
			right = mid - 1



def insertion_sort(list):
	for index in range(1, len(list)):
		value = list[index]
		i = index - 1
		while i >= 0:
			if value < list[i]:
				list[i+1] = list[i]
				list[i] = value
				i = i -1
			else:
				break
	return list

def bubble_sort(li):
	n = 1 
	while n < len(li):
		for i in range(len(li)-n):
			if li[i] > li[i+1]:
				li[i],li[i+1] = li[i+1],li[i]
		n += 1



			

import sys
from random import randint

a = [3, 7 , 9, 4, 66, 10, 33, 0, 1]
try:
	k = int(sys.argv[1])
except:
	k = 10
a = [randint(1, 100) for x in range(k)]
bubble_sort(a)
print(a)
#print (insertion_sort(a))
