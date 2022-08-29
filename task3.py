str = input("Enter a string: ")

tempStr = ''
for char in str:
    if char not in tempStr:
        print(char, ', ', str.count(char))
        tempStr = tempStr+char


