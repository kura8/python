import sys

def printing1(str1, str2, str3):
    print(str1)
    print(str2)
    print(str3)

def printing2(str1='aaa', str2='bbb', str3='ccc'):
    print(str1)
    print(str2)
    print(str3)

# printing1(sys.argv[1],sys.argv[2],sys.argv[3])
if __name__ == "__main__":
    printing2(str2='b')
