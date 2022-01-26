s = 'The quick brown fox jumps over the lazy dog'
reversed = 'The quick brown fox jumps over the lazy dog'
reversed = reversed.split(' ')
reversed.reverse()
reversed_s = ' '.join(reversed)


unwanted = [
    "the",
    "and",
    "on",
    "and",
    "over"
]
unwanted = [x.lower() for x in unwanted]

new_s = []

for word in reversed:
    if word.lower() in unwanted:
        continue
    else:
        new_s.append(word)

print(' '.join(new_s))
