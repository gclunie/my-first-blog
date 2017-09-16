print("Hello Django Girls!")
if 3 > 2:
    print("It Works!")
if 5 > 2:
    print("5 is indeed greater than 2")
else:
    print("5 is not greater than 2")
    
name = "Grace"
if name == "Grace":
    print("Hey Grace")
elif name == "Ellen":
    print("Hey Ellen")
else:
    print("Hey anonymous!")
# this is a comment 
def hi ():
    print("Hi There!")
    print ("How are you?")

hi()

def hi(name):
    if name == "Grace":
        print("Hi Grace")
    elif name == "Ellen":
        print("Hi Ellen")
    else:
        print("Hi annoymous")
hi("Ellen")

def hi(name):
    print("Hi " + name +"!")
hi("Rachel")



girls = ["Grace", "Savannah", "Kate", "Sophia"]
for name in girls:
    hi(name)
    print("Next Girl")
    
