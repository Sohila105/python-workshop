text = (input("enter a word: ")).lower()
print(f"Total characters (with spaces): {len(text)}")

count = len([x for x in text if x !=" "])
count_2 = text.replace(' ','')
print(f"Total characters (without spaces): {count}")

word = text.split()
print(f"number of words: {len(word)}")

char_count = {}
for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1 
print("Character frequency:", char_count)

most_common = max(char_count, key=char_count.get)
print(f"Most common character: {most_common} (appears {char_count[most_common]} times)")


if list(text) == list(reversed(text)):
    print("Is palindrome: yes")
else:
    print("Is palindrome: no")


reversed = text[::-1]
print(f"Reversed: {reversed}")