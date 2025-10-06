import re

with open('input.txt', 'r') as file:
    text = file.readline()[:-1]

def decode_length(text):
    match = re.search('\\((\\d+)x(\\d+)\\)', text)
    if match is None:
        return len(text)
    size = int(match.group(1))
    repeats = int(match.group(2))
    if size > len(text) - match.end():
        print('error: matches size')
    newtext = text[match.end():match.end()+size] * repeats
    posttext = text[match.end()+size:]
    return match.start() + decode_length(newtext) + decode_length(posttext)
    

print(decode_length(text))