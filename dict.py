empt_dict={}
print(type(empt_dict))

a=dict(one=1,two=2,three=3)
print(a)

b={"one":1,"two":2,"three":3}
print(b)
print(a==b)


data={"name":'Ashutosh',"reg.n0":"11700740",}
print(data)
print(data["name"])
b["one"]=11
print(b)


#dic using list

d={"cs":[106,106,110],"Math":[51,119]}
print(d)
print(d.get("cs"))
#by get we can ignore key error
del b["one"]
print(b)
b.pop("three")
print(b.keys())
print(b.values())
print(b.items())
print(len(data.keys()))

('one',1) in data.items()


for value in data.values():
    print(value)


a=data.copy()
print(a)
