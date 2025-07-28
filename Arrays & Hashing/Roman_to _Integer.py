#ROMAN TO INTEGER
#LEETCODE link: https://leetcode.com/problems/roman-to-integer/description/

def Roman(str):
    dct = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    integer = 0
    for x in range(len(str)):
        if x < len(str)-1 and dct[str[x]] < dct[str[x+1]]:
            integer -= dct[str[x]]
        else:
            integer += dct[str[x]]
    return integer

print(Roman("MCMLXXXIV"))
