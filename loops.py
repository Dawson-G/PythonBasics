#loops

abc = [25,32,16,15,14]

dez = [85,82,19,23,18]

ef = ["Aimee", "Grace", "Caleb"]


for x in abc:
    print x
    
    
for x in ef:
    if x == "Aimee":
        print "Hai"
    else:
        print "Hello"
        
for x in dez:
    if x == 19:
        print "I hate 19"
    elif x == 85:
        print "better then 19!"
    else:
        print "better then before"
        
for x in range(1,10):
    print x