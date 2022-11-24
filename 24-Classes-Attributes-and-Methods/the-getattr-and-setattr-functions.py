# they will be used when we dont know the attribute we want to read/write

stats = {
    "name": "BBQ chicken",
    "price": 10.99,
    "size": "large",
    "ingredients": ["chicken", "bbq sauce", "cheese"]
}

class Pizza():
    def __init__(self,stats):
        for key,value in stats.items():
            setattr(self,key,value)

    

bbq = Pizza(stats)
print(bbq.name)
print(bbq.price)
print(bbq.size)
print(bbq.ingredients)

for attr in ["price","name","diameter","discount"]:
    print(getattr(bbq,attr,"Not found"))