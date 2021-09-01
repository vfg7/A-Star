import math

#present the graph as matrix
#path: Dij denotes distance from i to j and Dij = Dji implies that you can move back and forth from one point to another
#straight-line distance: another graph, written the same way

def mirrorMatrix(dim):
    #let's make an easy square matrix with 0s in the main diagonal and -1s everywhere else
    M = []
    for x in range(dim):
        A =[]
        for y in range(dim):
            if x == y:
                A.append(0)
            else:
                A.append(-1)

        M.append(A)

    # print(M)
    return M

def insertCell(d =[], M=[]):
    # receives an array d containg a set of coordinates and the distance in the [x, y, distance] format
    #the program then fills the matrix with the distance between x and y in both M[x][y] and M[y][x] since this is bidirectional graph by design
    # -1 to correct the index (i'm assuming queries will be in the 1-X format and not in the usual programming format of 0-X)
    M[d[0]-1][d[1]-1] = d[2]
    M[d[1]-1][d[0]-1] = d[2]

def mapFill(d=[], M=[]):
    # receives an array of straight-line distances from a point to the another
    # the program then fills the matrix with the distance between in both M[x][y] and M[y][x] since this is bidirectional graph by design
    for a in range(len(M)):
        for b in range(len(M)):
            if M[a][b] == -1:
                M[a][b] = d[0]
                M[b][a] = d[0]
                d.pop(0)

#a somewhat greedy searching algorithm, breadth-first, minimum paths in a weighted graph. Inspired by classic dijkstra
#so lets code the decision-making in this crossroad: should we stay or should we go? And if we are going, how long's the trip?

def Star(start, finish, path=[], distance=[], carry=[]):
    #step keeps the start, the next point, the distance between these two points and the distance between the next point and the goal
    step =[-1,-1,-1,-1]
    startup = start-1 #make it easier
    step[0] = start

    for x in range(len(path[startup])):
        keepgoing = True #boolean to keep it going for as long it needs

        for y in range(len(carry)):
            if x == (carry[y][0]-1):
                keepgoing = False

        if keepgoing:
            if path[startup][x] > 0:
            # if not path[startup][x] == -1:
                #take the first one

                if step[1] == -1:
                    # print(path[startup])
                    # print("update one:", startup, " and ", x)
                    step[1] = x+1
                    step[2] = path[startup][x] #distance between stations
                    step[3] = distance[x][finish-1] #distance between this target and final destination
                else:
                    #try to optimize it
                    # print(path[startup])
                    # print("check and check again: ", startup, " and ", x)
                    # print((step[2]+step[3]), " > or < ",(path[startup][x] + distance[x][finish-1]))
                    #check A*
                    if (step[2]+step[3]) > (path[startup][x] + distance[x][finish-1]):
                        # print("update")
                        step[1] = x+1
                        step[2] = path[startup][x]
                        step[3] = distance[x][finish - 1]

    # print(step)
    if step[-1] == -1:
        # print("mark end of line")
        step[1] = carry[-1][0]
        # mark invalid paths, not to be returned

    carry.append(step)
    # print("so far: ",carry)
    if step[1] == finish:
        return
    else:
        Star(step[1], finish, path, distance, carry)

#and, finally, convert a pathmaker to a travel time estimate
def timestimate(speed, optPath=[]):

    #pop redundancies
    adaptativeCheck = 0
    while not adaptativeCheck == len(optPath):
        if optPath[adaptativeCheck][-1] == -1:
            if len(optPath) == 1:
                #checking for exceptions: an 'impossible' result
                return
            else:
                #popping returns out of the path matrix thus optimizing the path
                optPath.pop(adaptativeCheck)
                optPath.pop(adaptativeCheck-1)
                print("optimized, final path", optPath)
                adaptativeCheck = adaptativeCheck-2
                # print(adaptativeCheck," < >", len(optPath))

        adaptativeCheck = adaptativeCheck+1

    #now do your magic: count the time!
    fullength = 0
    station2station = len(optPath)-1 #number of line changes
    for x in range(len(optPath)):
        fullength += optPath[x][2]

    fullength = 60*fullength/speed
    fullength += 4*station2station

    print("* you hear a beep and a charming voice in french says: *\n","Bienvenue dans le metro de Paris! Temps estimé pour ton voyage est de: ",fullength," minutes")
    print("Ou de", math.floor(fullength/60),"heurs et ", round(fullength%60),"minutes! Bon Voyage!\n")

#let's go

PathMap = mirrorMatrix(14) #paths
DistanceMap = mirrorMatrix(14) #straight-line distances

#input data!
pathways = [[1, 2, 10], [2, 3, 8.5], [2, 9, 10], [2, 10, 3.5], [3, 4, 6.3], [3, 9, 9.4], [3, 13, 18.7], [4, 5, 13], [4, 8, 15.3], [4, 13, 12.8], [5, 6, 3], [5, 7, 2.4], [5, 8, 30], [8, 9, 9.6], [8, 12, 6.4], [9, 11, 12.2], [13, 14, 5.1]]
distances = [10, 18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1, 16.7, 27.3, 27.6, 29.8, 8.5, 14.8, 26.6, 29.1, 26.1, 17.3, 10, 3.5, 15.5, 20.9, 19.1, 21.8, 6.3, 18.2, 20.6, 17.6, 13.6, 9.4, 10.3, 19.5, 19.1, 12.1, 16.6, 12, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4, 3, 2.4, 19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9, 3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2, 20, 23, 27.3, 34.2, 25.7, 12.4, 15.6, 8.2, 20.3, 16.1, 6.4, 22.7, 27.6, 13.5, 11.2, 10.9, 21.2, 26.6, 17.6, 24.2, 18.7, 21.2, 14.2, 31.5, 35.5, 28.8, 33.6, 5.1]

for x in range(len(pathways)):
    # print(path[x])
    insertCell(pathways[x], PathMap)

# print(PathMap)

mapFill(distances, DistanceMap)
# print(DistanceMap)

#example1
answer = []
Star(6, 13, PathMap, DistanceMap, answer)
print("exemplo 1: ",answer)

timestimate(30, answer)

#example2
answer = []
Star(11, 13, PathMap, DistanceMap, answer)
print("exemplo 2: ",answer)

timestimate(30, answer)