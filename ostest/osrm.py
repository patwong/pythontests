import os

# os.remove("*.txt1")
# this is how to delete file:

filedir = os.listdir()  # lists all the files in the directory
print("files currently in directory\n" + str(filedir))
print("deleting all pickle files + playersnotindict.txt")
# remove pickle files
for f in filedir:
    if f.endswith(".txt1"):
        os.remove(f)
    elif f == 'playersnotindict.txt':
        os.remove(f)

print('operation complete')
filedir = os.listdir()
print("files currently in directory\n" + str(filedir))
