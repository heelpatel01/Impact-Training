''' An automobile company manufactures both a two wheeler (TW) and a four wheeler (FW). A company manager wants to make the production of both types of vehicle according to the given data below: 1st data, Total number of vehicle (two-wheeler + four-wheeler)=v 2nd data, Total number of wheels = W The task is to find how many two-wheelers as well as four-wheelers need to manufacture as per the given data.'''
v=int(input("Number of vehicles"))
w=int(input("Bumber of wheels"))
tw = ((4 * v) - w) / 2
fw=(v-tw)
print(f'TW: {tw} FW: {fw}')