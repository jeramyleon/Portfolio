friends = ['Kevin', 'Jamil', 'Porter', 'Alex', 'Gabe']
print(friends[1]) # accessing single element
print(friends[1:]) # accessing from index 1 and on
print(friends[1:3]) # accessing index 1 and up to index 3, not including 3
friends[1] = 'Kanye'
lucky_numbers = [1, 2, 3, 4, 5]
friends.extend(lucky_numbers)
friends.append('Daniel')
friends.insert(1, 'Kanye')
friends.remove('Gabe')
friends.pop()
print(friends.index('Kevin'))
print(friends.index('Kanye'))
print(friends.count('Kanye'))

friends = ['Kevin', 'Jamil', 'Porter', 'Alex', 'Gabe']
friends.sort()
friends.reverse()
friends2 = friends.copy()



