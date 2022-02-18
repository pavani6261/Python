def greeting():
    return "Good Morning"

# greeting()

def cuboid_volume(l):
    return (l*l*l)
length = [2,3,4,1]
for i in range(len(length)):
    print ("The volume of cuboid:",cuboid_volume(length[i]))

