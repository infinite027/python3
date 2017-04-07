raw = input('Input numbers, seperate with ","\n')
numbers = raw.split(",")
print(numbers)
numbers=list(map(int,numbers))
for i in range(len(numbers)):
  for number in range(len(numbers)-1):
    if numbers[number]>numbers[number+1]:
      print(numbers[number])
      print(numbers[number+1])
      print(numbers[number]>numbers[number+1])
      numbers[number],numbers[number+1]=numbers[number+1],numbers[number]
      print(numbers)
print(numbers)


listA = [-1,-99,23,44,-33,44,-6,435,-433,56]
listA.sort()
print(listA)
for i in range(len(listA)):
  for j in range(len(listA)-1):
    if listA[j]>listA[j+1]:
      temp=listA[j]
      listA[j]=listA[j+1]
      listA[j+1]=temp
print(listA)
