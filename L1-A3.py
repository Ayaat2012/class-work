def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:] #adding new values in a dict
    return result

students = [[1, 'Naomi carter', 'III'], [2, 'Rya McCoy', 'I'], [3, 'Evelyn Parker', 'IV'], [4, 'Brian Howell', 'VI'], [5, 'Zachary Simon', 'VII']]

print("\nOriginal list of lists:")
print(students)
print("\nConverted lists to a dictionary:")
print(test(students))