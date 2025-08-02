lst = ['Apple', 'Guava', 'Mango', 'Blueberry', 'Kiwi']

print("Length of list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Pawmagranet')
print("Updated list after appending:", lst)

lst.remove('Guava')
print("Updated list after removing:", lst)

lst.sort()
print("Sorted list:", lst)

lst.pop(1)
print("Updated list after popping:", lst)

lst.reverse()
print("Reversed list:", lst)


lst = lst*2
print("Multiplication of list:", lst)

lst = lst[2:5]
print("Sliced list:", lst)


lst.clear()
print("cleared list:", lst)