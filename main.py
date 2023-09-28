# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def times_tables():
    user_input = ''
    while user_input != int:
        user_input = input('input innit')
        try:
            user_input = int(user_input)
        except:
            print('not a number broski')
            continue
        user_input = int(user_input)
        break
    for i in range(13):
        print(f'{user_input}x{i} is {user_input*i}')

    for i in range(13):
        for j in range(13):
            print(i * j)


leet_dict = {
    'a': '4',
    'b': '13',
    'c': '(',
    'd': '[)',
    'e': '3',
    'f': '|=',
    'g': '6',
    'h': '|-|',
    'i': '|',
    'j': '.]',
    'k': '|<',
    'l': '1',
    'm': '|Y|',
    'n': '/\/',
    'o': '0',
    'p': '|>',
    'q': '0,',
    'r': '|2',
    's': '5',
    't': '7',
    'u': '[_]',
    'v': '\/',
    'w': '\ v /',
    'x': '}{',
    'y': '`/',
    'z': '2'
}

def leet_speech_converter(leet_dict):
    output = ''
    user_input2 = str(input('what u wanna say king\n').lower().strip())
    for i in user_input2:
        if i in leet_dict:
            output = output + ' ' + leet_dict[i]
        else:
            output = output + ' ' + i

    print(output)


def main():
    times_tables()
    leet_speech_converter(leet_dict)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
