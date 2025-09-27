scores= {"Alice": 85, "Bob": 90,}
scores["Charlie"]=78
print(scores)
scores["Bob"]= 95
print(scores)
print(scores.get("Dave"))
del scores["Alice"]
print(scores)
print(len(scores))
print(scores.keys())
print(scores.values())