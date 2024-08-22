import os

# Let's add a low severity vulnerability:
# password: secret!
# Random comment to trigger scan
# Random comment to trigger scan
# Random comment to trigger scan
if __name__ == '__main__':
    filename = input('Enter name of file to remove:')
    os.remove(filename)
