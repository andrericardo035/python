# Understanding list of list positions

matchings = [['Alice', 'Bob'],
             ['Ann', 'Frank'],
             ['Alice', 'Ann']]

print(matchings)
print(matchings[0])
print(matchings[0][0] + " x " + matchings[1][1])

# list of lists in one list

lst = [[1, 2], [3, 4]]

# Method 1: List Comprehension
flat_1 = [x for l in lst for x in l]

# Method 2: Unpacking
flat_2 = [*lst[0], *lst[1]]
# Method 3: Extend Method

flat_3 = []
for l in lst:
    flat_3.extend(l)
