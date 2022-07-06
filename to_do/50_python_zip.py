names = ["Alice", "Bob", "Mark", "Frank", "Anna"]
person_id = [14324, 78392, 94721, 40293, 58294]

print(zip(names, person_id))           # <zip object at 0x7f88586ddf80>
print(list(zip(names, person_id)))     # [('Alice', 14324), ('Bob', 78392), ('Mark', 94721), ...]
print(dict(zip(names, person_id)))     # {'Alice': 14324, 'Bob': 78392, 'Mark': 94721, ...}

zipped = zip("ABC", [1, 2, 3])
print(list(zipped))
print(dict(zipped))
