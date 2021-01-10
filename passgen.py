import string
import random
from colorama import *
init()

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
PUNCTUATION = "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
SEP = '-' * 25

PRESETS = {
    1: {
        'length': 8,
        'lowercase': 4,
        'uppercase': 2,
        'digits': 2,
        'punctuation': 0
    },
    2: {
        'length': 10,
        'lowercase': 5,
        'uppercase': 2,
        'digits': 2,
        'punctuation': 1
        },
    3: {
        'length': 12,
        'lowercase': 5,
        'uppercase': 3,
        'digits': 2,
        'punctuation': 2
        },
    4: {
        'length': 15,
        'lowercase': 6,
        'uppercase': 3,
        'digits': 3,
        'punctuation': 3
        },
    5: {
        'length': 18,
        'lowercase': 7,
        'uppercase': 4,
        'digits': 4,
        'punctuation': 3
        }
}


def get_settings():
    while True:
        mode = int(input(f"Enter mode\n"
                         f"\t0: Custom\n"
                         f"\t1-{len(PRESETS.keys())}: Presets\n"
                         f">>>"))
        print(SEP)
        if mode == 0:
            lowercase = int(input("Lowercase count :> "))
            uppercase = int(input("Uppercase count :> "))
            digits = int(input("Digits count :> "))
            punctuation = int(input("Punctuation count :> "))
            pritn(SEP)
            return {
                'lowercase': lowercase,
                'uppercase': uppercase,
                'digits': digits,
                'punctuation': punctuation
            }
        elif mode in PRESETS.keys():
            print(f"{Fore.GREEN}[+]{Fore.RESET} You have selected {mode} preset")
            preset = PRESETS[mode]
            print(f"{Fore.YELLOW}[!]{Fore.RESET} {mode} preset is:\n"
                  f"\t>Length: {preset['length']}\n"
                  f"\t>Uppercase: {preset['uppercase']}\n"
                  f"\t>Lowercase: {preset['lowercase']}\n"
                  f"\t>Digits: {preset['digits']}\n"
                  f"\t>Punctuation: {preset['punctuation']}")
            print(SEP)
            return PRESETS[mode]
        else:
            print(f"{Fore.RED}[#]{Fore.YELLOW} !!!WRONG MODE!!!{Fore.RESET}")
            print(Fore.RESET + SEP)


def main():
    settings = get_settings()
    lowercase = set(''.join(random.sample(LOWERCASE, settings['lowercase'])))
    uppercase = set(''.join(random.sample(UPPERCASE, settings['uppercase'])))
    digits = set(''.join(random.sample(DIGITS, settings['digits'])))
    punctuation = set(''.join(random.sample(PUNCTUATION, settings['punctuation'])))
    all_symbols = lowercase | uppercase | digits | punctuation
    all_symbols = list(all_symbols)
    password = ''
    for i in range(len(all_symbols)):
        taken = random.choice(all_symbols)
        all_symbols.remove(taken)
        password += taken
    print(f"{Fore.GREEN}[+]{Fore.RESET} Password: {password}\n{SEP}")


if __name__ == '__main__':
    while True:
        main()
        status = input("We will repeat(Yes(y)/No(n))")
        if status.lower() == 'no' or status.lower() == 'n':
            break
