# text to work with
text = (f'Today I went to the zoo. \
I saw a(n) {adjective}{noun} jumping up and down in its tree.  \
He {verb_past_tense} {adverb} through the large tunnel that led to its {adjective} {noun}. \
I got some peanuts and passed  them through the cage to a gigantic gray {noun}towering above my head. \
Feeding that animal made  me hungry. I went to get a {adjective} scoop  of ice cream. It filled my stomach. \
Afterwards I had to {verb} {adverb} to catch our bus.  \
When I got home I {verb_past_tense} my  mom for a {adjective} day at the zoo.')

# Dictionary that stores a number of times part of speach presented in text.
parts_of_speech_count = {
  'adjective' : 4,
  'adverb' : 2,
  'noun' : 3,
  'verb' : 1,
  'verb_past_tense' : 2
}

# Dictionary with lists where user input is stored.
parts_of_speech_and_words = {
  'adjective' : []],
  'adverb' : [],
  'noun' : [],
  'verb' : [],
  'verb_past_tense' : []
}

# Calculate total count of parts of speech.
# To determine the number of times user has to input.
parts_of_speech_count_list = list(parts_of_speech_count.values()
i = 0
for int in parts_of_speach_count:
  int += i
parts_of_speech_total = int

# Prompt user for input.
# Store the input in parts_of_speech_and_words.
i = 0
while i < parts_of_speech_total:
  for k, v in parts_of_speech_count.items():
    b = 0
    while len(parts_of_speech_and_words[1]) < b:  
      word = input(f'Please enter {part}: ')
  
