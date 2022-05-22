
logo = ''' ¶¶¶¶´´´´´¶¶¶´´´´´¶
¶¶¶´¶¶¶¶¶´¶´¶¶¶¶¶´¶
¶¶´¶¶¶¶¶¶¶´¶¶¶¶¶¶¶´¶
¶¶´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´¶
¶¶¶´¶¶¶¶¶¶¶¶¶¶¶¶¶´¶ 
¶¶¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶
¶¶¶¶¶¶´¶¶¶¶¶¶¶´¶ 
¶¶¶¶¶¶¶¶´¶¶¶´¶
¶¶¶¶¶¶¶¶¶´¶´¶
¶¶¶¶¶¶¶¶¶¶´¶ 
¶¶¶¶¶¶¶¶¶¶´¶
¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶__________¶¶ 
¶¶¶¶¶_______________¶¶¶
¶¶¶____________________¶
¶¶______¶¶______________¶
¶______¶¶¶¶______________¶
¶______¶¶¶¶____¶¶¶¶______¶
¶_______¶¶_______________¶
¶________________________¶
¶_____¶¶__________¶¶_____¶
¶¶_____¶¶________¶¶_____¶
¶¶¶______¶¶¶¶¶¶¶¶¶_____¶
¶¶¶¶¶________________¶¶
¶¶¶¶¶¶¶¶___________¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
'''
print(logo)
# name as raw input
name1 = input("Tera naam bol be?\n")
name2 = input("Item ka name bata bhootni ke?\n")
# changing casing of alphabets
premi = name1.lower()
premika = name2.lower()

# calculation of digits
digit1 = 0
digit2 = 0
first = 'true'
sec = 'love'
for i in first:
    digit1 += premi.count(i)+premika.count(i)
for j in sec:
    digit2 += premi.count(j)+premika.count(j)


final=digit1*10+digit2
print(f"Your Score is {final}")
if final>=90:
    print("\U0001F48B")
    print("\U0001F48B")
    print("\U0001F48B")
    print("Nikal Padi")
    print("\U0001F48B")
    print("\U0001F48B")
    print("\U0001F48B")
elif(70<=final<90):
    print("\U0001F648")    
    print("\U0001F648")    
    print("\U0001F648")
    print("Kch ho sakta hain.")    
    print("\U0001F648")    
    print("\U0001F648")    
    print("\U0001F648")
elif(50<=final<70):
    print("\U0001F61F")        
    print("\U0001F61F")        
    print("\U0001F61F")
    print("Muskuraiye...aap Friend Zone me ho")        
    print("\U0001F61F")        
    print("\U0001F61F")        
    print("\U0001F61F")
else:
    print("\U0001F92C")            
    print("\U0001F92C")            
    print("\U0001F92C")
    print("Mar jaa Bs**k")            
    print("\U0001F92C")            
    print("\U0001F92C")            
    print("\U0001F92C")            