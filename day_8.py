# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())

phonebook={}
for i in range(n):
    str=input()
    str=str.split() #splits the name and number into 2 list.
    phonebook[str[0]]=str[1]

while True:
    try:
        search= input()
        if(search in phonebook):
            print(search+"="+phonebook[search])
            
        else:
            print("Not found")
            
    except Exception:
        break