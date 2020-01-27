# arrays
lucky_numbers = [99, 25, 2, 77, 62, 64]

lucky_numbers.sort()

print(lucky_numbers)

lucky_numbers.reverse();

print(lucky_numbers)

friends = ["Rick", "Debjit", "Shubhayu","Shubhayu", "Somnath", "Saptarshi"]

print(friends.sort())

print(friends.count("Shubhayu"))

print(friends.pop())

print(friends.index("Shubhayu"))

friends.append("Surojit")

friends.insert(1, "Sajid")

# friends.extend(lucky_numbers)

print(friends)

# When left to right first position is 0

print(friends[1])

# When right to left first position is -1

print(friends[-3])

# Get all elements after index 1
print(friends[1:])

# Get all elements between indexes 1 and 3
print(friends[1:3])

# friends.clear();

print(friends)

friends2 = friends.copy()

print(friends2)










