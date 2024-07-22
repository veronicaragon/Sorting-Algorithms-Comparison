# Aragon, Veronica      80752302

def insertion_sort(arr):
  for i in range(1,len(arr)):
    j=i

    while j > 0 and arr[j]< arr[j-1]:
      temp = arr[j]
      arr[j] = arr[j-1]
      arr[j-1] = temp
      j -= 1

def partition(arr,start_index,end_index):
  midpoint = start_index+(end_index-start_index)//2
  pivot = arr[midpoint]

  low = start_index
  high = end_index

  done = False
  while not done:
    while arr[low] < pivot:
      low += 1
    while pivot < arr[high]:
      high -= 1
    if low >= high:
      done = True
    else:
      temp = arr[low]
      arr[low] = arr[high]
      arr[high] = temp
      low += 1
      high -= 1
  return high

def quick_sort(arr,start_index,end_index):
  if end_index <= start_index:
    return
  high = partition(arr,start_index,end_index)
  quick_sort(arr,start_index,high)
  quick_sort(arr,high + 1,end_index)

def bubble_sort(arr):
   n = len(arr)
   for i in range(n):
      for j in range(0,n-i-1):
         if arr[j] > arr[j+1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

def mix_sort(arr):
    mid = len(arr) // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    insertion_sort(arr1)
    bubble_sort(arr2)
    return arr1 + arr2

# Test Code
arr = [10, 2, 78, 4, 45, 32, 7, 11]

print("\nTesting Insertion Sort:")
print('UNSORTED:', arr)
insertion_sort(arr)
print('SORTED:', arr)

arr = [10, 2, 78, 4, 45, 32, 7, 11]

print("\nTesting Quick Sort:")
print('UNSORTED:', arr)
quick_sort(arr,0, len(arr)-1)
print('SORTED:', arr)

arr = [10, 2, 78, 4, 45, 32, 7, 11]

print("\nTesting Mixed Sort:")
print('Original:', arr)
arr = mix_sort(arr)
print('Final:', arr)