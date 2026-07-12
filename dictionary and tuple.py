d ={"sam": 25021, "tom": 53215, "pat": 89745}
print(d)
del d["sam"]
print(d)

for key in d:
    print("key:", key, "value:", d[key])

#TO ACHIEVE THE ABOVE WITH TUPLE
for k,v in d.items():
    print("key:", key, "value:", v)

