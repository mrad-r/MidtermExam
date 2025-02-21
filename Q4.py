def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("7489617719749244646336564429479177169847"))