"""recursive algorithm to solve the towers of hanoi"""

def TowerOfHanoi(n, fromRod, toRod, spareRod):
    if n == 1:
        print(f'Move disk 1 from the {fromRod} rod to the {toRod} rod')
        return
    TowerOfHanoi(n-1, fromRod, spareRod, toRod)
    print(f'Move disk {n} from the {fromRod} rod to the {toRod} rod')
    TowerOfHanoi(n-1, spareRod, toRod, fromRod)

rods=["left","middle","right"]
used_rods=[]

numDisks = int(input('Enter a number of disks: '))
fromRod = str(input('Enter the original rod: '))
toRod = str(input('Enter the rod you are moving the disks to: '))

used_rods.append(fromRod.lower())
used_rods.append(toRod.lower())
spare_rod = list(set(rods) - set(used_rods))[0]

TowerOfHanoi(numDisks, fromRod, toRod, spare_rod)

