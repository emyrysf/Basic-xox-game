gamespace=[[[],[],[]],
           [[],[],[]],
           [[],[],[]]]
def bosmu(list):
    if list == []:
        return True
    else:
        return False
def adder(inp, space, xo):
    space[inp//3][inp%3].append(xo)
counter=0
user=None
while True:
    for x in gamespace:
        print(x)


    if counter%2==0:
        user="X"
    elif counter%2==1:
        user="O"
    print("sıra {}de".format(user))
    a=int(input("Koordinat giriniz:"))-1
    if bosmu(gamespace[a//3][a%3]):
        adder(a,gamespace,user)
        counter+=1
    else:
        print("ora dolu başka seç")
