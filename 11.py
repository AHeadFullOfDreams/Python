
    




def main():
    
    
    string = input()
    new=''
    for s in string:
        num=ord(s)
        if num >= 97 and num <= 122:
            num = 97 + ((num - 97) + 13) % 26
            new=new+chr(num)
        elif num >=65 and num <= 90:
            num = 65 + ((num -65) +13) % 26
            new=new+chr(num)
        else:
            new=new+chr(num)
    
    print(new)
   

if __name__ == '__main__':
    main()
