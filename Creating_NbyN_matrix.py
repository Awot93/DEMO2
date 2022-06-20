rows = int(input("Plsease enter the number of rows in the matrix: "))
columns = int(input("Please enter the number of column in the matrix: "))

list2 = []

for i in range(rows):
    list1 = []
    for j in range(columns):
        value = int(input("Value: "))
        list1.append(value)
    list2.append(list1)
print(list2)