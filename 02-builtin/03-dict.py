# -*- encoding: utf-8 -*-

# definition
contacts = {
    "Dad": "20214432",
    "Mom": "44329981",
    "Boss": "110"
}

print(contacts["Boss"])
print("Boss" in contacts)

# try look up a missing key
# print(contacts["Wife"])

# handle missing key way 1:

try:
    print(contacts['Wife'])
except KeyError:
    print('not exist')


# handle missing key way 2:
if 'Wife' in contacts:
    print(contacts['Wife'])
else:
    print('not exist')


# handle missing key way 3:
print(contacts.get('Wife', 'not exist'))

print(list(contacts.keys()))
print(list(contacts.values()))
print(list(contacts.items()))

for k in contacts:
    print(k)

for k, v in contacts.items():
    print(k, '->', v)
