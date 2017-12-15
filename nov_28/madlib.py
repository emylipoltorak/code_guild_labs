def mad_lib():
    adjectives = input("Give me 3 adjectives, separated by commas: ").split(', ')
    plural_nouns = input("Give me 3 plural nouns, separated by commas: ").split(', ')
    nouns = input("Give me 4 nouns, separated by commas: ").split(', ')
    adverb = input("Give me an adverb: ")
    past_tense_verb = input("Give me a past tense verb: ")

    story = "{adjective1} {plural_noun1} is a {noun1} {noun2} where one {noun3} prompts others for a list of {plural_noun2} to substitute for {plural_noun3} in a story, before reading the – often {adjective2} or {adjective3} – story aloud. The game is {adverb} {past_tense_verb} as a {noun4} game."
    story = story.format(adjective1=adjectives[0], adjective2 = adjectives[1], adjective3 = adjectives[2], plural_noun1 = plural_nouns[0], plural_noun2 = plural_nouns[1], plural_noun3 = plural_nouns[2], noun1 = nouns[0], noun2 = nouns[1], noun3 = nouns[2], noun4 = nouns[3], adverb = adverb, past_tense_verb = past_tense_verb)
    print(story)

mad_lib()

play_again = input("Would you like to play again? y/n: ")

while play_again == "y":
    mad_lib()
    play_again = input("Would you like to play again? y/n: ")
else:
    print("Ok. Goodbye!")
