def height_to_meters(feet, inches):
    return (feet * 12 + inches )* 0.0254

print(height_to_meters(5, 11))

stats = {
    'feet': 5,
    'inches': 11
}

#what if we want to pass the dictionary as an argument to the function?
#we can use the unpacking operator ** to unpack the dictionary

print(height_to_meters(**stats))