sentence = input("Enter text: ").lower()
words = sentence.split()
filler_words = ["the", "is", "a", "an", "and", "to", "in" ]
filtered_words = []

for word in words:
    if word not in filler_words:
        filtered_words.append(word)

word_count = {}

for word in filtered_words:
    if word in word_count:
        word_count[word] +=1 
    else:
        word_count[word] =1 

longest_word = " "

for word in filtered_words:
    if len(word) > len(longest_word):
        longest_word = word

print("\n Clean words: ")
print(filtered_words)

print("Word count: ")
print(word_count)

print("Longest word: ")
print(longest_word)
