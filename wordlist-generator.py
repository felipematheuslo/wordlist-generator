"""
WPA Key--
The shared secret key for WPA Personal security.
Enter a string of at least 8 characters to a maximum of 63 characters.
Acceptable characters include upper and lower case alphabetic letters,
the numeric digits, and special symbols such as @ and #.
"""

characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
              "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
              "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
              "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7",
              "8", "9", "!", "@", "#", "$", "%", "&", "*", "_", "-", "."]

for x7 in range(len(characters)):
    for x8 in range(len(characters)):
        word = characters[x7] + characters[x8]
        with open('wordlist.txt', 'a') as f:
            f.write(word)
            f.write('\n')