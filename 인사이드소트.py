n = int(input())
 
li = []
li = list(map(int,str(n))) 으로 변경가능
    
li.sort(reverse=True) 
 
for i in li:
    print(i,end='')