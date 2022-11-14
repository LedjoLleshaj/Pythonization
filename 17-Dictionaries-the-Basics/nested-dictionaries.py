tv_shows = {
    "The Simpsons": {
        "seasons": 30,
        "episodes": ["Bart the Genius", "Homer the Heretic", "Lisa the Iconoclast"],
        "original_run": "1989-2019",
    },
    "Friends": {
        "seasons": 10,
        "episodes": ["The One with the Sonogram at the End", "The One with the Thumb", "The One with George Stephanopoulos"],
        "original_run": "1994-2004",
    },
    "The Office": {
        "seasons": 9,
        "episodes": ["The Dundies", "The Injury", "The Secret"],
        "original_run": "2005-2013",
    },
}

print(tv_shows)

# how to access the value of the key "seasons" in the dictionary "The Simpsons"
print(tv_shows["The Simpsons"]["seasons"])

print(tv_shows["The Office"]["episodes"][2])