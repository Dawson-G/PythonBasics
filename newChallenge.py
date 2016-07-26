a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
b = [17,18,19,20,21,22,23,24,25,26,27,28,29]

def newChallenge(a,b):
    x = a+b;
    
    for k in x:
        if k % 2 == 0 or k == 1:
            print "yeah evens"
        else:
            print "yeah odds"
            
newChallenge(a,b)