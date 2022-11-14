sports_team_roster = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski", "Julian Edelman"],
    "New York Giants": ["Eli Manning", "Odell Beckham Jr.", "Victor Cruz"],
    "Dallas Cowboys": ["Tony Romo", "Dez Bryant", "Jason Witten"]
}

print(sports_team_roster["New England Patriots"]) # ['Tom Brady', 'Rob Gronkowski', 'Julian Edelman']
sports_team_roster["Teuta Durres"] = ["Ermir Lenjani", "Ermir Lenjani", "Ermir Lenjani"]
print(sports_team_roster) 

video_game_options = {}
# video_game_options = dict()
# we can add a key-value pair to an empty dictionary
# be adding the key inside square brackets and assigning it a value
video_game_options["subtitles"] = True
video_game_options["difficulty"] = "Easy"
video_game_options["music"] = "Off"

print(video_game_options) # {'subtitles': True, 'difficulty': 'Easy', 'music': 'Off'}

# we can also modify the value of a key-value pair
video_game_options["subtitles"] = False

words = ["danger", "danger", "high voltage"]

def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1 # increment the value of the key
        else:
            counts[word] = 1 # if the word is not in the dictionary, we add it
    return counts

print(count_words(words)) # {'danger': 2, 'high voltage': 1}