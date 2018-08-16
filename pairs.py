a = '{'
b = '('
c = '['
a1 = '}'
b1 = ')'
c1 = ']'
string = ['{','(','(','[',']','[',']','[',']','{','}','[',']','(','{','(',')','}',')','(','[','[','[',']',']',']','[','{','}',']',')',')',')','}']
d = 1
for i in range(len(string)):
    if string[i] == a:
        if string[d] == a1:
            string.remove(string[i])
            string.remove(string[d])
 
    elif string[i] == b:
        if string[d] == b1:
            string.remove(string[i])
            string.remove(string[d])
            d += 1
            i += 1
    elif string[i] == c:
         if string[d] == c1:
            string.remove(string[i])
            string.remove(string[d])
            d += 1
            i += 1
    elif string[i] == a1:
         if string[d] == a:
            string.remove(string[i])
            string.remove(string[d])
            d += 1
            i += 1
    elif string[i] == b1:
         if string[d] == b:
            string.remove(string[i])
            string.remove(string[d])
            d += 1
            i += 1
    elif string[i] == c1:
           if string[d] == c:
            string.remove(string[i])
            string.remove(string[d])
            d += 1
            i += 1
print(string)
