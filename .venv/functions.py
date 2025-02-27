def my_test_fn(a, b):
    a = a + 1
    c = a + b
    return c


res = my_test_fn(2, 3)
print(res)


def increase_person_age(person):  # We should not return external variable so better make a copy of it.
    person_copy = person.copy()
    person_copy['age'] += 1
    person_copy['name'] = 'New Bob'
    return person_copy


person_one = {
    'name': 'Bob',
    'age': 21
}

new_person = increase_person_age(person_one)
print(person_one)
print(new_person)


def print_fruits_info(person_name,
                      fruits):  # Mutable objects like fruits list will be modified, but not mutable like strings won't
    fruits_copy = fruits.copy()
    person_name = 'New Maciej'
    fruits_copy.pop()
    for fruit in fruits_copy:
        print(f'{person_name} likes {fruit}')


my_name = 'Maciej'
favorite_fruits = ['apple', 'orange', 'banana']

print_fruits_info(my_name, favorite_fruits)
print(favorite_fruits)


def my_second_fn(first, second=True):
    print(first)
    print(second)


my_second_fn('abc', 'optional')


def merge_list_to_dict(list_one, list_two):
    dictionary = dict(zip(list_one, list_two))
    return dictionary


list_of_keys = ['a', 'b', 'c']
list_of_values = [1, 2, 3]

dict = merge_list_to_dict(list_of_keys, list_of_values)
print(dict)
