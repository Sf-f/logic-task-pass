#Q3/write a function that count how many the given character repeated in a given string?



str = input("Enter a string: ")

tempStr = ''
for char in str:
    if char not in tempStr:
        print(char, ', ', str.count(char))
        tempStr = tempStr+char


