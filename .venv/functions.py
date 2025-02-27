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


def sum_nums(*args):  # merging arguments into tuple
    print(args)
    print(type(args))

    print(args[0])
    return sum(args)


print(sum_nums(2, 3, 7, 4))


def sort_nums(*args):
    return sorted(args)


sorted_nums = sort_nums(10, 3, 15, 246, 23, 4521, 213)

print(sorted_nums)
print("==============KEYWORD ARGUMENTS================")


def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info


info = get_posts_info(posts_qty=5, name='Bob')
print(info)

print("=================MERGING ARGUMENTS TO THE DICT==================")


def get_posts_info(**person):
    print(person)
    print(type(person))
    info = (
        f"{person['name']} wrote"
        f"{person['posts_qty']} posts"
    )
    return info


new_info = get_posts_info(name='Mark', posts_qty=25)

print("===============Practice=================")


def comments_info(comments_qty, day):
    print(f"{comments_qty} comments were posted on {day}")


comments_info(comments_qty=50, day='Monday')
