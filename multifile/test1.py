# import a1
from main1 import d1 as d1

def tf1():
    print("this is tf1")
    if 'bob' in d1:
        print ("bob is" + d1['bob'])
    else:
        print ("no bob")
