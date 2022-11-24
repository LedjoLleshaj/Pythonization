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

stats_to_delete = ["price","size","discount"]

for stat in stats_to_delete:
    if hasattr(bbq,stat):
        delattr(bbq,stat)
    else:
        print(f"{stat} does not exist")