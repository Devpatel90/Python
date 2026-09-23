class Filemanger:
     def write(self,filename,data):
         with open (filename, "w") as f:
             f.write(data)
    
     def read(self,filename):
         with open (filename, "r") as f:
            return f.read()
             
     def append(self, filename, data):
         with open (filename, "a") as f:
             f.write(data)
         
han = Filemanger()

han.write("filehan.txt", "Hello my name is rajjj i love coding..")
print(han.read("filehan.txt"))
han.append("filehan.txt", "hello pythonnn")