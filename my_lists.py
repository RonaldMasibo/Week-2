
my_list = []

# Appending 10,20,30,40 into the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting 15 at the second position on the list
my_list.insert(1,15)

# Extending with another list
another_list = [50,60,70]
my_list.extend(another_list)

#Removing the last element
my_list.remove(70)

# Sorting the list
my_list.sort()

# Finding & printing index of value 30
print(my_list.index(30))