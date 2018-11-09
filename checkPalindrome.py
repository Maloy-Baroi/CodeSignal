def checkPalindrome(inputString):

    test=list(inputString)
    reverse_test=[]
    for i in reversed(test):
        reverse_test.append(i)
    x="".join(test)
    y="".join(reverse_test)
    if x==y:
        return True
    else:
        return False
