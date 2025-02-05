from morse import morse

while (True):
    print('''This is program that converts words into Morse code
    -   long signal
    .   short signal
    /   letter separator
    //  word separator''')
    word = input("Enter word for morse code: ")
    m_code = morse(word)
    print(m_code)
    next = input("Will you continue or quit?\n1 - new words for morse code or\nany other key - quit program: ")
    if next == "1":
        continue
    else:
        break

