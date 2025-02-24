# sets
# sets has only unique elements

posts_ids = {125, 442, 387, 224, 125, 442}
print(posts_ids)  # returns only unique one {224, 442, 387, 125}
print(len(posts_ids))  # python wont tell us that there are duplicates but remove them so it will return 4 instead of 6

# Sets don't have indexes, and you can't assign mutable objects such as lists, dictionaries, or other sets to them.

my_set = {10, 5, 5, 100, 10, 20, 50, 125}

print(my_set)
print(type(my_set))
print(isinstance(my_set, set))

my_second_set = {15, 10, 5, 0, 20, 25, 100}

print(my_set.intersection(my_second_set))

photo_s = {'1920x1080', '800x600'}
other_s = {'800x600', '1024x768'}

all_sizes = photo_s.union(other_s)
print(f"(All sizes: {all_sizes})")

common_s = photo_s.intersection(other_s)
print(f"(Common sizes: {common_s})")

nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}
res = nums.issubset(other_nums)
print(f"Is subset? : {res}")
res_superset = other_nums.issuperset(nums)
print(f"Is superset? : {res_superset}")

my_new_set = {10,2,10,5,7}
print(my_new_set)

my_new_set.add(8)
print(my_new_set)
my_new_set.remove(5) # key error 200 if absent element
print(my_new_set)
my_new_set.discard(200) # no error if element is absent
my_other_set = {34,1,10,5}

print(my_new_set.intersection(my_other_set))
print(my_new_set & my_other_set)

print(my_new_set | my_other_set)

set_copy = my_other_set.copy()

set_copy.add(200)
print(set_copy)
print(my_other_set)

set_a = {'a','c','d'}
set_b = {'l','m','c'}

print(set_a.symmetric_difference(set_b))

print((set_a | set_b) - (set_a & set_b))

# TASK

task_set = {1,3,5,7,9}
task_set.add(11)
task_another_set = {1,5,9,25,112,332,115,590,1000}
task_new_set = task_set & task_another_set
task_new_list = list(task_new_set)
print(task_new_list)