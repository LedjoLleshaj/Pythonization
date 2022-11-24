class Counter:
    instances = 0
    def __init__(self):
        Counter.instances += 1

    @classmethod
    def create_two(cls):
        two_counters = [cls(), cls()]
        print(f"New number of instances: {cls.instances}")
        return two_counters

print(Counter.instances) 
c1 = Counter()
print(Counter.instances)

c2, c3 = Counter.create_two()
print(Counter.instances)
