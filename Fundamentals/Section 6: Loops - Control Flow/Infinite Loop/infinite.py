''' 
Case 1 :- Knowingly creating an Infinite loop

i = 0
while True:
    i += 1
    print(i)    


Case 2 :- Mistakenly creating an Infinite Loop (Wrong Condition)

i = 0
while i >= 0:
    i += 1
    print(i)    


Case 3 :- Mistakenly creating an Infinite Loop (Dont Modify Counter variable)

i = 0
while i == 10:
    print(i)    
'''