#A Program to print random vocals of japanese alphabets to improve my alphabet writing capacity
import time
print("Welcome this is a program to print phonetics of japanese alphabets")  #Just an intro of what the program is about
input("When ready press press 'ENTER' to continue") #the start button
jap_hirkat = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'shi', 'su', 'se', 'so', 'ta', 'ti', 'tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'fu', 'he', "ho", "ma", "mi", "mu", "me", "mo", "ya", "yu", "yo", "ra", "ri", "ru", "re", "ro", "wa", "wo", "n"]
jap_dakuon = ['ga', 'gi', 'gu', 'ge', 'go', 'za', 'ji', 'zu', 'ze', 'zo', 'da', 'ji (variant)', 'zu (variant)', 'de', 'do', 'ba', 'bi', 'bu', 'be', 'bo', 'pa', 'pi', 'pu', 'pe', 'po']
jap_combo = ['kya', 'kyu', 'kyo', 'gya', 'gyu', 'gyo', 'sha', 'shu', 'sho', 'jya', 'jyu','jyo', 'cha', 'chu', 'cho', 'nya', 'nyu', 'nyo', 'hya', 'hyu', 'hyo', 'bya', 'byu', 'byo', 'pya', 'pyu', 'pyo', 'mya', 'myu', 'myo', 'rya', 'ryu', 'ryo']
jap_small = ['つ/ツ + k', 'つ/ツ + s', 'つ/ツ + t', 'つ/ツ + p']
jap_longvowels = ['aa', 'ii', 'uu', 'ee', 'oo', 'ei(only in hiragana)', 'ou(only in hiragana)']

def draw(n):
    a = 0  # 'a' denotes the first letter of the list
    for a in range(0, len(n), ):   # this loop prints the lists' elements
        print(n[a])
        backopt = input()       # importantly this input is the function which stops the program until a random key is pressed
        if (backopt == "back"): #secret function not known to user
            options()
        time.sleep(2)
        if a == len(n)-1:
            print("End of list\n")

def options():
    print("Press 1 to print the basic 'HIRAGANA/KATAKNA' phonetics")
    print("Press 2 to print 'DAKUON' phonetics")
    print("Press 3 to print 'COMBO' phonetics")
    print("Press 4 to print 'SMALL つ/ツ' phonetics")
    print("Press 5 to print 'LONG VOWELS' phonetics")
    print("Press 6 to 'PRINT EVERYTHING'")
    print("Press 7 to 'EXIT'")
    option = int(input())
    match option:
        case 1:
            draw(jap_hirkat)
            options()
        case 2:
            draw(jap_dakuon)
            options()
        case 3:
            draw(jap_combo)
            options()
        case 4:
            draw(jap_small)
            options()
        case 5:
            draw(jap_longvowels)
            options()
        case 6:
            draw(jap_hirkat)
            draw(jap_dakuon)
            draw(jap_small)
            draw(jap_combo)
            draw(jap_longvowels)
            options()
        case 7:
            pass

options()
