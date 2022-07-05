#A Program to print random vocals of japanese alphabets to improve my alphabet writing capacity
import os
import sys
print("Welcome this is a program to print phonetics of japanese alphabets")  #Just an intro of what the program is about
input("When ready press press 'ENTER' to continue") #the start button
jap_hirkat = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'shi', 'su', 'se', 'so', 'ta', 'ti', 'tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'fu', 'he', "ho", "ma", "mi", "mu", "me", "mo", "ya", "yu", "yo", "ra", "ri", "ru", "re", "ro", "wa", "wo", "n"]
jap_dakuon = ['ga', 'gi', 'gu', 'ge', 'go', 'za', 'ji', 'zu', 'ze', 'zo', 'da', 'ji (variant)', 'zu (variant)', 'de', 'do', 'ba', 'bi', 'bu', 'be', 'bo', 'pa', 'pi', 'pu', 'pe', 'po']
jap_combo = ['kya', 'kyu', 'kyo', 'gya', 'gyu', 'gyo', 'sha', 'shu', 'sho', 'jya', 'jyu','jyo', 'cha', 'chu', 'cho', 'nya', 'nyu', 'nyo', 'hya', 'hyu', 'hyo', 'bya', 'byu', 'byo', 'pya', 'pyu', 'pyo', 'mya', 'myu', 'myo', 'rya', 'ryu', 'ryo']
jap_small = ['つ/ツ + k', 'つ/ツ + s', 'つ/ツ + t', 'つ/ツ + p']
jap_longvowels = ['aa', 'ii', 'uu', 'ee', 'oo', 'ei(only in hiragana)', 'ou(only in hiragana)']
whole_list = (jap_hirkat, jap_dakuon, jap_combo, jap_small, jap_longvowels)
whole_listcount = len(jap_hirkat + jap_dakuon + jap_combo + jap_small + jap_longvowels)
# the above line is the list of japanese phonetics(all)
def options():
    print("Press 1 to print the basic 'HIRAGANA/KATAKNA' phonetics")
    print("Press 2 to print 'DAKUON' phonetics")
    print("Press 3 to print 'COMBO' phonetics")
    print("Press 4 to print 'SMALL つ/ツ' phonetics")
    print("Press 5 to print 'LONG VOWELS' phonetics")
    print("Press 6 to 'PRINT EVERYTHING'")
    print("Press 7 to 'EXIT'")
    option = int(input())
options()

if option == 1:
    print("You chose basic Hiragana/Katakana phonetics")
    a = 0  # 'a' denotes the first letter of the list
    while a <= len(jap_hirkat):   # this loop prints the lists' elements
        print(jap_hirkat[a])
        backopt = input()       # importantly this input is the function which stops the program until a random key is pressed
        if (backopt == "back"):
            options()
        a += 1
        if a == len(jap_hirkat):
            print("End of list")

elif option == 2:    #code block to print the dakuon letters, the same method is used for all five blocks
    print("You chose Dakuon phonetics")
    b = 0
    while b <= len(jap_dakuon):
        print(jap_dakuon[b])
        input()
        b += 1
        if b == len(jap_dakuon):
            print("End of List")

elif option == 3:
    print("You chose Combo phonetics")
    c = 0
    while c <= len(jap_combo):
        print(jap_combo[c])
        input()
        c += 1
        if c == len(jap_combo):
            print("End of List")

elif option == 4:
    print("You chose Small つ/ツ phonetics")
    d = 0
    while d <= len(jap_small):
        print(jap_small[d])
        input()
        d += 1

elif option == 5:
    print("You chose Long Vowels' phonetics")
    e = 0
    while e <= len(japanese_longvowels):
        print(japanese_longvowels[e])
        input()
        e += 1

elif option == 6:
    print("Are you sure? There are", whole_listcount, "characters. Press enter to continue")
    f = 0
    k = 0
    input()
    while f <= len(whole_list):
        print(whole_list[f])
        input()
        f += 1

elif option == 7:
    print("You chose to 'EXIT', See you later")
    input()
    exit()

else:
    print("Invalid input ばか, restart the program.")
    input()
    exit()
options()
