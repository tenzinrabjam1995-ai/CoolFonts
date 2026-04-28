from pyfiglet import Figlet, figlet_format


fonts = {
   "1": 'bulbhead',
   "2": 'bubble',
   "3": 'barbwire',
   "4": 'avatar',
   "5": 'larry3d',
   "6": 'slscript',
   "7": 'mirror',
   "8": 'lean',
   "9": 'doh',
   "10": 'epic',
   "11": 'isometric1',
   "12": 'rectangles',
   "13": 'stellar',
   "14": 'pyramid',
   "15": 'usaflag',
   "16": 'contessa',
   "17": 'tengwar',
   "18": 'thin',
   "19": 'tinker-toy',
   "20": 'tombstone',
   "21": 'univers'
}


all_words = {}


default_example = "Example"

# Show font previews
for key, value in fonts.items():
   if key == "9":
       f = Figlet(font=value, width=200)
   else:
       f = Figlet(font=value, width=100)
   print(f"This is an example for {key}: {value}")
   print(f.renderText(default_example))

# User loop
while True:
   choice = input("Enter choice for a number corresponding font or enter exit to stop: ")
   clean_choice = choice.strip().lower()


   if clean_choice == "exit":
       break
   elif clean_choice in fonts:
       f = Figlet(font=fonts[clean_choice])
       text = input("Enter text: ")
       print(f.renderText(text))


       if choice not in all_words:
           all_words[choice] = []
       all_words[choice].append(text)
   else:
       print("Invalid choice, please try again.")
print("\nWords used:")
for numbers, strings in all_words.items():
  print(f"{numbers}:{strings}")



print("You used", len(all_words), "different font(s)")

for numbers, strings in all_words.items():
   f = Figlet(font=fonts[numbers])
   print(f"Font: {numbers}")
   print(f.renderText(strings[0]))


   # all_words.extend(strings.split())


# if all_words:
word_font_pairs = []
print(all_words)
for number, words in all_words.items():
    for w in words:
        word_font_pairs.append((w, number))

print(all_words)
print(word_font_pairs)

if word_font_pairs:
    shortest_words_list = []
    shortest_length = float('inf') #10000000000000

    longest_words_list = []
    longest_length = 0  # 10000000000000

    for word, font_num in word_font_pairs:
        if len(word) < shortest_length:
            shortest_length = len(word)
            shortest_words_list = [(word, font_num)]
        elif len(word) == shortest_length:
            shortest_words_list.append((word, font_num))

        if len(word) > longest_length:
            longest_length = len(word)
            longest_words_list = [(word, font_num)]
        elif len(word) == longest_length:
            longest_words_list.append((word, font_num))

    if len(shortest_words_list) == 1:
        print("\nThe shortest input is:")
    else:
        print("\nThe shortest inputs are:")

    for word, font_num in shortest_words_list:
        print(word)
        f = Figlet(font=fonts[font_num])
        print(f.renderText(word))

    if len(longest_words_list) == 1:
        print("\nThe longest input is:")
    else:
        print("\nThe longest inputs are:")

    for word, font_num in longest_words_list:
        print(word)
        f = Figlet(font=fonts[font_num])
        print(f.renderText(word))
else:
    print("\nNo words were entered.")