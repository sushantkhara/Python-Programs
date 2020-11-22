with open('data.txt','a+') as new:
    new.seek(0)
    content=new.read()
    new.seek(0)
    new.write(content)
    new.write(content)

with open("data.txt") as new:
    new.seek(0)
    contents=new.read() 
    print(contents)