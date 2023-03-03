import json

x = {
  "name": "Ayazhan",
  "age": 18,
  "married": True,
  "divorced": False,
  "children": ("Ann","Gilbert"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, sort_keys=True))