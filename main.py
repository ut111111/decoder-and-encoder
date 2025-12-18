import random






#basic coder and decoder 

#.1 Consist of three functions 
#1) Encode
#2) Decode
#3) User_loop
#4) random words for code





def rand_words():
      alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
      'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
      'y', 'z']
      x=random.choices(alphabets,k=3)
      return ("".join(x))




def user_loop():
    
    while True:
     
     x=input("User_1:")
     for i in x:
        if i in "/?!@#$%^&*|":
           raise ValueError 

     y=int(input("press 1 to Encode\npress 2 to exit"))
     if y==1:
         print(encode(x))  
     
     elif y==2:
        return False
     
     elif y not in range(1,2):
        print("Restarting....")
        print(user_loop())

     z=int(input("press 1 to decode \n press 2 to quit"))
     if z==1:
        print(decode(encode(x)))

     elif z==2:
        return False
     
     else:
        print("Restarting....")
        print(user_loop())
        
   


def encode(n):
    y=n.split(" ")
    z=[]
    for letter in y:
       if len(letter)>2:
           str_1=rand_words()+letter[1:]+letter[0]+rand_words()
           z.append(str_1)
            
       elif 0<=len(letter)<=2:
           str_2=(letter[1]+letter[0])
           z.append(str_2)
    return (" ".join(z))
           

def decode(m):
    y=m.split(" ")
    z=[]
    for letter in y:
        if len(letter)>8:
         str_dec1=letter[len(letter)-4]+letter[3:len(letter)-4]
         z.append(str_dec1)

        elif 0<=len(letter)<=2:
           str_dec2=letter[1]+letter[0]
           z.append(str_dec2)
    
    return (" ".join(z))
    
   
      

user_loop   ()





