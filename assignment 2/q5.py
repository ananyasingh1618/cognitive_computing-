dict = {"name": "Kelly", "age": "25", "salary": 8000, "city": "New york"}
if 'city' in dict:
    dict['location'] = dict.pop('city')
print("Updated dictionary:", dict)
