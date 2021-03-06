#find all path to reached specific position (only going right and down)
#r,d is starting position
#fr,fd is finding position
def pathfinder(matrix,fr,fd,r=0,d=0,path=""):
    if r==len(matrix[0]) or d==len(matrix): return
    if r==fr and d==fd:
        print(path)
        return
    path+="R"
    pathfinder(matrix,fr,fd,r+1,d,path)
    path=path[:-1]
    path+="D"
    pathfinder(matrix,fr,fd,r,d+1,path)
    path = path[:-1]

matrix = [  ["start",2,  3],
            [   4  ,   5 ,"find"],
            [7,8,9]]

pathfinder(matrix,fr=2,fd=1)