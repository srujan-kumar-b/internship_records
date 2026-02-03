###LISTS AND TUPLES###

numbers=[10,20,30,40]

coordinates = (5,10)
print(numbers)
print(coordinates)


#####SLICING#####
data=[100,700,400,500,300,600,200,800,900]
print(data[2:4])
print(data[-1])
print(data[:3])   
print(data[2:])
print(data[:])
print(data[-1:-3])
print(data[-3:-1:2])
print(data[1:8:3])

data.append(1000)
print("After appending 1000:", data)
data.pop()
print("pop up data:", data)
data.sort()
print("Sorted data:", data)
data.reverse()
print("Reversed data:", data)

