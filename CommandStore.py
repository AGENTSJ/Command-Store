


from tkinter import *


temp=""
txt=Tk()
txt.geometry("600x650")
txt.title('Command Storage')
txt.config(bg="#FFA833")
def insertlinux():
    f=open("codes2.txt",'a')
    xh=entry1.get()
    hx=entry2.get()
    f.write("\n"+xh.upper()+":\t"+hx+"\n")
    f.close()
    entry1.delete(0,END)
    entry2.delete(0,END)

def insertcmd():
    f=open("codes.txt",'a')
    xh=entry1.get()
    hx=entry2.get()
    f.write("\n"+xh.upper()+":"+hx+"\n")
    f.close()
    entry1.delete(0,END)
    entry2.delete(0,END)
    

def readlinux():
    f=open("codes2.txt",'rt')
    b=f.read()
    end=len(b)
    start=b.index("$$linux$$")
    f.close()
    g=b[start:end]
    textop.config(state='normal')
    textop.insert('end',g)
    textop.config(state='disabled')
    global temp
    temp=b
    


def readcmd():
    f=open("codes.txt",'rt')
    b=f.read()
    end=len(b)
    start=b.index("$$cmd$$")
    g=b[start:end]
    f.close()
    textop.config(state='normal')
    textop.insert('end',g)
    textop.config(state='disabled')
    global temp
    temp=b
    


def clear():
    textop.config(state='normal')
    textop.delete(1.0,END)
    textop.config(state='disabled')



def search():
    clear()
    key=entry3.get()
    if key in temp:
        value=temp[temp.index(key.upper()):len(temp)]
        textop.config(state='normal')
        textop.insert(1.0,"search results.....top......")
        textop.insert('end',"\n")
        textop.insert('end',"\n")
        textop.insert('end',"\n")
        textop.insert('end',value)
        textop.config(state='disabled')
    

    
    


textop=Text(txt,height=20,width=40)
textop.grid(row=0,column=3)



frame = LabelFrame(txt,bg='black',padx=10,pady=10)
frame.grid(row =0, column=0)

label1=Label(txt,text="Label")
label1.grid(row=1 ,column =2)

label2=Label(txt,text="Command")
label2.grid(row= 2,column =2)

entry1=Entry(txt,width=40)
entry1.grid(row=1 ,column=3 ,columnspan=3,padx=0,pady=10)

entry2=Entry(txt,width=40)
entry2.grid(row=2 ,column=3 ,columnspan=3,padx=0,pady=10)

entry3=Entry(txt,width=40)
entry3.grid(row=3 ,column=3 ,columnspan=3,padx=0,pady=10)

label3=Label(txt,text="keyword")
label3.grid(row= 3,column =2)


label2=Label(txt,text="Command")
label2.grid(row= 2,column =2)

linuxadd=Button(frame,text="Add Linux",padx=25,pady=25,bg="#FFA833",command=insertlinux).grid(row=0 ,column =0,padx=10,pady=10)

linuxread=Button(frame,text="Read Linux",padx=25,pady=25,bg="#FFA833",command=readlinux).grid(row=1 ,column =0,padx=10,pady=10)

cmdadd=Button(frame,text="Add Cmd",padx=25,pady=25,bg="#FFA833",command=insertcmd).grid(row=2 ,column =0,padx=10,pady=10)

cmdread=Button(frame,text="Read Cmd",padx=25,pady=25,bg="#FFA833",command=readcmd).grid(row=3 ,column =0,padx=10,pady=10)

searchr=Button(txt,text="search",padx=10,pady=10,bg='black',fg='white',command=search).grid(row=4 ,column =3,padx=10,pady=10)

cleart=Button(txt,text="clear",padx=10,pady=10,bg='black',fg='white',command=clear).grid(row=5 ,column =3,padx=10,pady=10)

print(temp)

mainloop()
