def printst(string):
    return f"This is a string{string}"



def add(num1,num2):
    return num1 +num2 +3

def multiple(num3=4,num4 = 5):
    return num3*num4


print("this is modul name", __name__)




if __name__ == '__main__':
    print(printst("If Name Main"))
    printst(add(3,4))


""" agr hm if __name__ == '__main__': ko agr hm execute nii krte h to modul ke poore methods and functions execute ho jte h 
aur agr isse likh ke isske andr kuchh likh dete to only uss modul ka vii function execute hota h jo uss if __name__ == '__main__':'
 block ke andr hota
 =============================================================
 to experiment this -
 simply comment down krke dekh luga
 """







print(printst("If Name Main"))
printst(add(3,4))