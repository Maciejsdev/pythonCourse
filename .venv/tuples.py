posts_ids = (151, 245, 762, 167)  # not mutable, doesn't support item deletion
# del posts_ids[0] won't work

print(posts_ids[0])

users = ({
             'user_id': 1,
             'user_name': 'John'
         },
         {
             'user_id': 2,
             'user_name': 'Alice'
         })
print(users)
print(users[1]['user_name'])
users[1]['user_name'] = 'Cris'  # Mutable objects in tuples can be changed
print(users)
print(users[1]['user_name'])

# Conversion to list

ids = (151, 245)
print(f"Ids tuple: {ids}")
ids_list = list(ids)
ids_list.append(355)
print(f"List: {ids_list}")

new_ids_tuple = tuple(ids_list)
print(f"Tuple: {new_ids_tuple}")

# practice

screen_res = (1920, 1080)
print(f"ScreenRes: {screen_res}")
print(f"ScreenRes id: {id(screen_res)}")
print(screen_res.count(1080))

screen_res_list = list(screen_res)
screen_res_list[0] = 1440
print(screen_res_list)

screen_res = tuple(screen_res_list)
print(screen_res)
print(f"ScreenRes id: {id(screen_res)}")

screen_info = (True, 'Samsung', 150)

screen_data = screen_res + screen_info
print(f"ScreenData: {screen_data}")
