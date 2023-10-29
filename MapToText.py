# MAP PNF to TEXT by Alejandro V.
import cv2

img = cv2.imread("map.png")
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

imgCorners = cv2.imread("map.png")
imgCorners = cv2.cvtColor(imgCorners, cv2.COLOR_RGB2BGR)

h,w,c = img.shape

class Pixel:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

def getColor(img, x, y):
    if -1 >= x or x >= h or -1 >= y or y >= w:
        return "0,0,0"
    else:
        return "%d,%d,%d" % (img[x,y,0],img[x,y,1],img[x,y,2])

def checkColor(color):
    if  color == "0,0,0":
        return '0'
    elif color == "255,255,255":
        return '1'
    elif color == "0,255,33":
        return '1'
    elif color == "255,0,0":
        return '1'
    elif color == "0,38,255":
        return '2'

def OrderPath( path):
    for p in path:
        if p.c == "0,255,33":
            startP = p
        elif p.c == "255,0,0":
            endP = p

    orderedPath = []
    orderedPath.append(startP)
    path.remove(startP)

    while len(path) > 0:
        lastTile = orderedPath[len(orderedPath) - 1]
        for p in path:
            if p.x == lastTile.x + 1 and p.y == lastTile.y or p.x == lastTile.x - 1 and p.y == lastTile.y or p.x == lastTile.x and p.y == lastTile.y + 1 or p.x == lastTile.x and p.y == lastTile.y - 1:
                orderedPath.append(p)
                path.remove(p)

    BVal = 255
    inc = 255 / len(orderedPath)

    for i in range(len(orderedPath)):
        img[orderedPath[i].y][orderedPath[i].x] = (255,0,BVal)
        BVal = BVal - inc
    
    return orderedPath

if __name__ == "__main__":
    
    open("Map.txt", "w").close()
    with open('Map.txt', 'a') as file:
        for y in range(h):
            line = ""
            for x in range(w):
                color = getColor(img, y, x)
                
                if x == 0:
                    line = line + str(checkColor(color))
                elif x < w:
                    line = line + "," + str(checkColor(color))
                else:
                    line = line + str(checkColor(color))
            if (x == w - 1):
                line = line + ',0'
            if(y < h - 1):
                file.write(line + '\n')
            else:
                file.write(line)
    
    open("MapCorners.txt", "w").close()
    with open('MapCorners.txt', 'a') as file:
        path = []

        for y in range(h):
            for x in range(w):
                color = getColor(img, y, x)
                if checkColor(color) == "1":
                    path.append(Pixel(x, y, color))
        
        orderedPath = OrderPath(path)
        corners = []
        
        for p in orderedPath:
            if (checkColor(p.c) == checkColor(getColor(imgCorners, p.y-1, p.x)) and checkColor(p.c) == checkColor(getColor(imgCorners, p.y+1, p.x)) or checkColor(p.c) == checkColor(getColor(imgCorners, p.y, p.x-1)) and checkColor(p.c) == checkColor(getColor(imgCorners, p.y, p.x+1))):
                pass
            else:
                corners.append(p)
        
        for c in corners:
            imgCorners[c.y][c.x] = (255,0,220)
            if (c == corners[len(corners) - 1]):
                file.write("%d,%d" % (c.x, c.y))
                
            else:
                file.write("%d,%d" % (c.x, c.y) + '\n')

    img = cv2.resize(img, (0,0), fx=20, fy=20, interpolation=0)
    cv2.imshow("Map Path Gradien", img)
    imgCorners = cv2.resize(imgCorners, (0,0), fx=20, fy=20, interpolation=0)
    cv2.imshow("Map Corners", imgCorners)
    cv2.waitKey(0)
    cv2.destroyAllWindows()