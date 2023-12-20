
# Strings
first_name='warren'
last_name="ochieng"
my_fav_color=" maroon"
full_name=  first_name + '' + last_name
message=f"my name is {first_name} {last_name} and my favorite color is {my_fav_color}"

print(my_fav_color)
print(my_fav_color.count('mar'))
print(first_name.find('w'))
print(full_name)
print(message)
# print(dir(str))

# numbers
age =26
rent = 30000
rent_in_words=str(rent)
print(rent_in_words)

# Lists 
courses=['history','math','history','math']
new_courses=['philosophy','literature']
courses.append('English')
courses.insert(0,'art')
courses.extend(new_courses)
courses.pop()
print(len(courses))
print(courses)

# tuples
unchanged_list=('history','math','history','math')

# sets
new_set={'history','math','history','math'}