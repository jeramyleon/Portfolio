dict = {'Name': 'Jeramy', 'Age': 22, 'Class': 'First'}
print(dict['Name'])
print(dict['Age'])

dict['Age'] = '23'
dict['School'] = 'BMCC'
print(dict['Age'])
print(dict['School'])

del dict['Name']
dict.clear()
del dict

hash_table = {
    'Name': 'Jeramy',
    'Age':  '22',
    'School': 'BMCC'
}
print(hash_table['Name'])
print(hash_table['Age'])
print(hash_table['School'])

del hash_table['Name']
hash_table.clear()
del hash_table
print(hash_table['Name'])
print(hash_table['Age'])
print(hash_table['School'])
