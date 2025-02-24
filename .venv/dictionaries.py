my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2
}

other_motorbike = {
    'engine_vol': 1.2,
    'brand': 'Ducati',
    'price': 25000,
}

print(my_motorbike == other_motorbike)
print(id(my_motorbike) == id(other_motorbike))
print(my_motorbike)

print(my_motorbike['price'])
my_motorbike['is_new'] = True
del my_motorbike['price']
print(my_motorbike)

key_name = 'brand'
my_motorbike[key_name] = 'BMW'
print(my_motorbike)

my_bike = {
    'brand': 'Custom',
    'price': 2000,
}

print(my_bike['brand'])
print(my_bike['price'])

my_bike['max_speed'] = 50

print(my_bike)
print(my_bike.items())
print(my_bike.keys())

print(my_bike.get('color'))  # no error when key is not in dict
print(my_bike.get('color', 'no color attribute'))  # returns 2nd param if absent

my_list = [['a', 10], ['b', 20]]

print(dict(my_list))

#Task

my_dict = {}

user_first_key = input('Enter first key: ')
user_first_value = input('Enter first value: ')
my_dict[user_first_key] = user_first_value
user_second_key = input('Enter second key: ')
user_second_value = input('Enter second value: ')
my_dict[user_second_key] = user_second_value
user_third_key = input('Enter third key: ')
user_third_value = input('Enter third value: ')
my_dict[user_third_key] = user_third_value

print(my_dict)
