# cheq number is palindrome or not

def checkPalindrome(num):
    k=str(num)
    if k==k[::-1]:
        return True
    else:
        return False

num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
