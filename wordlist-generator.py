# -*- coding: utf-8 -*-
"""
Created on Jan 22 2024
@author: Felipe Laurindo
"""
# pip3 install tqdm
from tqdm import tqdm

characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
              "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
              "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
              "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7",
              "8", "9", "!", "@", "#", "$", "%", "&", "*", "_", "-", "."]

with tqdm(total=100) as bar:
    for x1 in range(len(characters)):
        for x2 in range(len(characters)):
            for x3 in range(len(characters)):
                for x4 in range(len(characters)):
                    for x5 in range(len(characters)):
                        for x6 in range(len(characters)):
                            for x7 in range(len(characters)):
                                for x8 in range(len(characters)):
                                    word = characters[x1] + characters[x2] + characters[x3] + characters[x4] + characters[x5] + characters[x6] + characters[x7] + characters[x8]
                                    print(word)
                                    bar.update(1/pow(72, 8))
                                    with open('wordlist.txt', 'a') as f:
                                        f.write(word)
                                        f.write('\n')