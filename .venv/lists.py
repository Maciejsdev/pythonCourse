my_list = [10, 'abc', True, 255, False]

my_list.pop(2)
print(my_list)
my_list.reverse()

another_list = ['foo',-200]
my_list=my_list + another_list
print(my_list)


first_list = ['foo', 'bar', 'baz']
second_list = [123, 456, 789]
merged_list = first_list.__add__(second_list)
print(merged_list)