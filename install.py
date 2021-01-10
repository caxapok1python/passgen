import os


def windows():
    print("Windows install")
    os.system('python3 -m pip install -r req.txt')


def linux():
    print("Linux/Unix install")
    os.system('python3 -m pip install -r req.txt')


if __name__ == '__main__':
    if os.name == 'nt':
        windows()
    else:
        linux()
