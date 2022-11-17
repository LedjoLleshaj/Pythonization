agents = {
    "Mulder",
    "Scully",
    "Doggett",
    "Reyes",
}
print(agents)
agents.remove("Doggett")
print(agents)
agents.discard("Rey") # if the item is not in the set, discard does nothing
print(agents)