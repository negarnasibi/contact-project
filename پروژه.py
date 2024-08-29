contact={}
def new():
    name=input("enter name : ")
    number=int(input("enter number :"))     
    contact[name]=number
    print (contact)
    
# enter name
# enter number 
# add contact

def delete ():
    name=input("enter name : ")
    del contact[name]
    print("done")
    print(contact)
    
# enter name
# enter number 
# add contact

def change():
    name=input("enter name new :")
    number=int(input("enter number new :"))
    contact[name]=number
    print("done")
    print(contact)

# enter name
# enter number new


def show():
    print(contact)

# print contact

while True:
    x=input("choice:")
    if x=="out":
        print ("good by")
        break
    elif x=="new":
        new()

    elif x=="delete":
        delete()

    elif x=="change":
        change()
        
    elif x=="show":
        show()

    else :
        print ("un valid!")
        
