'''
The text is given in a single line. For each word of the text count the number of its occurrences before it.
'''
text = 'one two one two three two four three'
word_list = text.split()
counts = {}
for word in word_list:
  if word in counts:
    print(counts[word], end=' ')
    counts[word] +=1
  else:
    print(0, end=' ')
    counts[word] = 1
