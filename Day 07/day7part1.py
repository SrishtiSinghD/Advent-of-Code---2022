class Folder:
    def __init__(self,name,parent):
        self.files = []
        self.folders = []
        self.name = name
        self.size = 0
        self.parent = parent

    def addFile(self,content):
        self.files.append(content)

    def addFolders(self,content):
        self.folders.append(content)

    def printContent(self):
        print(self.name)
        print("Files: ")
        for f in self.files:
            f.printContent()
        if len(self.folders) != 0:
            print("Folders: ")
            for folder in self.folders:
                folder.printContent()

    def move(self,name):
        for x in self.folders:
            if x.name == name:
                return x

    def printFolderNames(self):
        for folder in self.folders:
            print(folder.name)

    def printFileNames(self):
        for f in self.files:
            print(f.name)

class File:
    def __init__(self,name,size):
        self.size = size
        self.name = name

    def getSize(self):
        return self.size

    def printContent(self):
        print(self.name, "-->",self.size)

fileobj = open("Day 07\inputday7.txt","r")

reader = fileobj.readlines()

root = Folder("/",None)
line_no=1
current=root
while line_no < len(reader):
    line = reader[line_no].strip("\n").split()

    if line[0] == '$':
        if line[1] == "cd":
            # do something
            if line[2] == "..":
                current = current.parent
            else:
                current = current.move(line[2])
            line_no+=1
        if line[1] == "ls":
            line_no+=1
            line = reader[line_no].strip("\n").split()

            while line[0] != "$":
                # do something
                if line[0] == "dir":
                    current.addFolders(Folder(line[1],current))
                else:
                    current.addFile(File(line[1],int(line[0])))
                
                line_no+=1
                if(line_no) >= len(reader):
                    break
                line = reader[line_no].strip("\n").split()
            
# root.printFolderNames()
# root.printFileNames()

def calculateSize(node):
    for f in node.files:
        node.size+=f.size
    if len(node.folders) == 0:
        return node.size
    for folder in node.folders:
        calculateSize(folder)
        node.size+=folder.size  

calculateSize(root) 
print(root.size) 
total = 0   
def traverse(node):
    global total
    if node.size <= 100000:
        total+=node.size
    if len(node.folders) == 0:
        return 
    for folder in node.folders:
        traverse(folder)

traverse(root)
print(total)