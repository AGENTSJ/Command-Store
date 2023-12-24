inp=str(input("terminal name:\n"))
act=str(input("insert or read:\n"))
tname="$$"+inp.lower()+"$$"
c=" "
flag=1
def readlinux():
    f=open("codes2.txt",'rt')
    b=f.read()
    end=len(b)
    start=b.index(tname)
    print(b[start:end])
    f.close()
    keyword(b)


def insertlinux():
    f=open("codes2.txt",'a')
    xh=str(input("give the label"))
    hx=str(input("give the commands"))
    f.write("\n"+xh.upper()+":\t"+hx+"\n")
    f.close()


def readcmd():
    f=open("codes.txt",'rt')
    b=f.read()
    end=len(b)
    start=b.index(tname)
    print(b[start:end])
    f.close()
    keyword(b)


def insertcmd():
    f=open("codes.txt",'a')
    xh=str(input("give the label"))
    hx=str(input("give the commands"))
    f.write("\n"+xh.upper()+":"+hx+"\n")
    f.close()


def keyword(cv):
    key=str(input("did not find it try giving a key word"))
    if key.upper() in cv:
        ght=cv.index(key.upper())
        print("...........top .................")
        print(cv[ght:ght+100])
        print("................................")
    else:
        print("not found")
        

#functions ends

while(flag==1):
    if inp.lower()=="linux" and act.lower()=="insert" :
        insertlinux()
    if inp.lower()=="linux" and act.lower()=="read" :
        readlinux()
    if inp.lower()=="cmd" and act.lower()=="insert" :
        insertcmd()
    if inp.lower()=="cmd" and act.lower()=="read" :
        readcmd()
        

    x=int(input("1 to continue 0 to exit"))
    if x==0:
        break
    if x==1:
        inp=str(input("terminal name:\n"))
        act=str(input("insert or read"))
        tname="$$"+inp.lower()+"$$"
    