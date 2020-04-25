# find sum of items in array
d = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

    # first item index
    # 
print(str(d.values()))
sum = 0 
for i in d.values():
    if type(i) == int:
       sum += i
print(sum)
