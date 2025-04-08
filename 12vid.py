#rewatch whole video(syk syk)


# l = [ 1 , 2 ,3 , 4 , 5]
# total = 0
# for items in l:
#     total = total + items  #earlier we were using "print(sum(l))" to calculate sum of items in list
# print(f"The sum obtained is {total}")

#create a list that contain double the elements of previous list
# l = [ 1 , 2 ,3 , 4 , 5]
# el=[]
# for items in l:
#     el.append(items*2)
# print(el)

# # List comprahension (easy) , same as above
# l = [1 , 2 , 3 , 4 ]
# dl=[ num*2 for num in l ]
# print(dl)


# l = [1 , 2 , 3 , 4 ] #for finding sqareroot
# dl=[ num*num for num in l ]
# print(dl)


# l=[x for x in range(0,101)]#to create a list
# m=[n for n in l] #adding elements of l into m
# print(m)

# l = [] #this complex stuff can be carried out in simple steps
# for i in range(0,101):
#     l.append(i)
# print(l)   
# el = []
# for n in l:
#     if(n%2==0):
#         el.append(n)
# print(el)

# l=[x for x in range(0,101)]#to create a list
# print("All numbers \n",l)
# m=[n for n in l if n%2==0] #adds  only even numbers
#[expressionn for item in collection if condion] 
# print('only even number \n',m)

# l=[x for x in range(0,101)]
# print("All numbers \n",l)
# el=[num for num in l if num%2!=0] #adds  only odd numbers
# print("only odd numbers \n",el)

#for accessing only second letter
# names = ["Ajay" , "Billion" , 'chethan']
# print(names)
# sec_alp=[x[1] for x in names]
# print(sec_alp)

# Looping through dictionaries
# d={"a"  : 32 , "b" : 45 , "c":44}
# for nm in d.items():
#     print(nm) 

# d={"a"  : 32 , "b" : 45 , "c":44}  #for representing keys only
# for nm  in d.keys():
#     print(nm ) 

# d={"a"  : 32 , "b" : 45 , "c":44}  #for representing values only
# for nm  in d.values():
    # print(nm ) 

# d={"a"  : 32 , "b" : 45 , "c":44}  #for representing keys and values both
# for nm , mn in d.items():
#     print(nm , "--", mn) 

# # Creating a single dictionary from Two different list(skip this and carry next)
# a = ["a" , "b " , 'c']
# b = [12 , 13 , 14]
# c={}
# for index , a1 in enumerate(a):
#     c[a1] = b[index]
# print(c)

# a = ["a" , "b " , 'c'] #for carry same but for dynamic (changing) list
# b = [12 , 13 , 14]
# c={}
# for i in range ( 0 , len(a)):
#     c[a[i]] = b[i]
# print(c)

#dictionary comprahension
# names = ["Ajay" , "Billion" , 'chethan'] #to create a dictionary that contain key as name and vlue as length of name(key)
# dct={a:len(a) for a in names}
# print(dct)

#to create a another seprate dictionary that has value greater than 40
# s_c={"a" : 23 , "b" : 43 , "c" : 33 , "d" : 80}
# l_c={key:value for key,value in s_c.items() if value > 40}
# print(l_c)

# #STRING SPLIT
# c_h="Syk guru ninu"
# s_p=c_h.split()
# print(s_p)

# c_h="Syk-guru-ninu"
# s_p=c_h.split("-")
# print(s_p)

# #takes any input as string 
# x=[input("Enter number").split()]
# print(x) #integers are in  form of string

# x=input("Enter number").split()
# m=[int(l) for l in x]
# print(m)

# x = [int(l) for l in input("Enter number").split()]#shorter of above
# print(x)

