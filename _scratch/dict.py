d = {'key': 'value', "a number": 3, 3: "three"}
print(d)

print(type(d) == dict)

print(len(d))

print(d['key'])
del d['key']
print(d)

print(d.get(3))

d.update({'test':'test'})
print(d)

if d['test'] not in d:
    d['test']= 'test1'
    print(d)
else:
    print('not in')

for x,y in d.items():
    print('key:{} \n value:{}'.format(x,y))

print(d.pop('test'))
print(d)

print(d.popitem())
print(d)
d['a word']='the word'
print(d)
d['a word']='the penis'
print(d)

# Ausgangslage
default_settings = {'theme': 'light', 'notifications': True}
user_settings = {'theme': 'dark', 'language': 'de'}

# DER NEUE WEG (Python 3.9+)
# "Nimm die Defaults UND die User-Settings zusammen"
final_config = default_settings | user_settings

print(final_config)
# Ergebnis: {'theme': 'dark', 'notifications': True, 'language': 'de'}