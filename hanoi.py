"""recursive algorithm to solve the towers of hanoi"""

def TowerOfHanoi(n, fromRod, toRod, spareRod): #create a function
    if n == 1: #avoid stack overflowing
        print(f"Move disk 1 from the {fromRod} rod to the {toRod} rod") #move the last disk
        return #exit the function
    TowerOfHanoi(n-1, fromRod, spareRod, toRod) #call the function with a rod moved
    print(f"Move disk {n} from the {fromRod} rod to the {toRod} rod") #move the disk
    TowerOfHanoi(n-1, spareRod, toRod, fromRod) #call the function with a rod moved

rods = ("left","middle","right") #initialize the possible rods
used_rods = [] #initialize the used rods

numDisks = int(input("Enter a number of disks: ")) #prompt for a number of disks; alternatively you could pass in an integer
fromRod = str(input("Enter the original rod: ")) #prompt for the original rod; alternatively you could pass in a string
toRod = str(input("Enter the rod you are moving the disks to: ")) #prompt for the target rod; alternatively you could pass in a string

used_rods.append(fromRod.lower()) #add the used rods to the list
used_rods.append(toRod.lower())
spare_rod = tuple(set(rods) - set(used_rods))[0] #find the remaining rod

TowerOfHanoi(numDisks, fromRod, toRod, spare_rod) #call the function
