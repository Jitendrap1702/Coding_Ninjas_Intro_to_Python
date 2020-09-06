def palindrome(s):
    if s==s[::-1]:
        return 'true'
    else:
        return 'false'
s=input()
print(palindrome(s))
