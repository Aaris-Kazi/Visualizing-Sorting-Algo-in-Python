import cv2 as c
import numpy as np
import time

def sorty(a, p):
    img = np.zeros((512,512,4),np.uint8)
    n = len(a)
    for i in range(1, n):
        j = i
        while j > 0 and a[j] < a[j-1]:
            
            c.line(img, (20,155+p[j-1]), (200+a[j-1], 155+p[j-1]), (0,0 ,0),5)
            
            t = a[j]
            a[j] = a[j-1]
            a[j-1] = t
            c.line(img, (20,155+p[j-1]), (200+a[j-1], 155+p[j-1]), (255,0 ,255),5)
            c.line(img, (20,155+p[j]), (200+a[j], 155+p[j]), (0,0 ,0),5)
            c.line(img, (20,155+p[j]), (200+a[j], 155+p[j]), (255,0 ,255),5)
            
            
            c.imshow('Animation Window', img)
            
            k = c.waitKey(1000)
            if k == 270:
                break
            j -= 1
               
            
        
    c.destroyAllWindows()

def ask():
    a = []
    p = []
    t= 5
    c = int(input('How many lines do you want:-'))
    for i in range(0, c) :
        x = int(input('Enter the Value:- '))
        a.append(x)
        p.append(t)
        t += 20
    return a, p

def main():
    a, p = ask()
    sorty(a, p)

if __name__ == "__main__":
    main()
    ## Copyrights Reserves to Aaris Kazi for the Visualising the Algorithm