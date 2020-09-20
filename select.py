import cv2 as c
import numpy as np
import time

def sorty(a, p):
    img = np.zeros((512,512,4),np.uint8)
    n = len(a)
    for i in range(n):
        min_id = i
        for j in range(i+1, n):
            
            if a[min_id] > a[j] :
                min_id = j
                
                c.line(img, (20,155+p[i]), (200+a[i], 155+p[i]), (0,0 ,0),5)
                
                t = a[i]
                a[i] = a[min_id]
                a[min_id] = t
                c.line(img, (20,155+p[i]), (200+a[i], 155+p[i]), (255,0 ,255),5)
                c.line(img, (20,155+p[min_id]), (200+a[min_id], 155+p[min_id]), (0,0 ,0),5)
                c.line(img, (20,155+p[min_id]), (200+a[min_id], 155+p[min_id]), (255,0 ,255),5)
                
                
                c.imshow('Animation Window', img)
                k = c.waitKey(1000)
                if k == 270:
                    break
                
                swap = True
        if swap == False:
            break
        
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