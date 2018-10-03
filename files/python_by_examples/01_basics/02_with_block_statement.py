# this is a with statement
# https://preshing.com/20110920/the-python-with-statement-by-example/

with open('/tmp/output.txt', 'w') as f:
    f.write('Hi there!')

# here's another example:
from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
print(story_words)
print(type(story_words))
