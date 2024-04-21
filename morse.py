# Text-based (command line) program that takes any String input and converts it into Morse Code.
# https://en.wikipedia.org/wiki/Morse_code
# morse csv table https://introcs.cs.princeton.edu/python/44st/morse.csv
import pandas
word = input("Enter word for morse code: ").upper()
m_table = pandas.read_csv("morse.csv")
letters_list = m_table["letter"].to_list()
codes_list = m_table["code"].to_list()
mc = ""
for l in word:
    if l == " ":
        mc += "/"
    elif l in letters_list:
        index = letters_list.index(l)
        mc += (codes_list[index]) + "/" # "/" for letters separation
    else:
        mc += "?" # spaces or non-letter symbols between words marked with question mark
print(mc)