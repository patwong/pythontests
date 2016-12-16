# import z1
import z2

def main1():
    new_z = z2.zclass()
    print ("znum1: " + str(new_z.znum1))
    new_z.pdict['name'] = "john smith"
    print (new_z.pdict)
    print (new_z.pdict['name'])

main1()
