languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
print(languages)
lengths = {lang:len(lang) for lang in languages}

print(lengths)


word = "Supercalifragilisticexpialidocious"

letter_counts = {letter:word.count(letter) for letter in word}