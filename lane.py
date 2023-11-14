import cv2
import numpy as np
#import motors as mot
def findCenter(p1,p2):
    center = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
    return center
def minmax_centerPoints(tergetList,pos):
    if len(tergetList) > 0:
        maximum = max(tergetList, key = lambda i: i[pos])
        minimum = min(tergetList, key = lambda i: i[pos])
        return [maximum,minimum]
    else:
        return None
global  count
def detectedlane1(imageFrame):
    center1= 0
    center2 = 0
    width,height = 320,240
    pts1 = [[0,240],[320,240],[290,30],[30,30]]
    pts2 = [[0, height], [width, height],
                       [width,0], [0,0]]
    target = np.float32(pts1)
    destination = np.float32(pts2)
    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(target, destination)
    result = cv2.warpPerspective(frame, matrix, (width,height))
    cv2.imshow('Result', result)
   # cv2.line(imageFrame, (pts1[0][0],pts1[0][1]), (pts1[1][0],pts1[1][1]), (0, 255, 0), 1)
    #cv2.line(imageFrame, (pts1[1][0],pts1[1][1]), (pts1[2][0],pts1[2][1]), (0, 255, 0), 1)
    #cv2.line(imageFrame, (pts1[2][0],pts1[2][1]), (pts1[3][0],pts1[3][1]), (0, 255, 0), 1)
    #cv2.line(imageFrame, (pts1[3][0], pts1[3][1]), (pts1[0][0], pts1[0][1]), (0, 255, 0), 1)
   # cv2.imshow('Main Image Window', imageFrame)    
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    threshold = cv2.inRange(gray, 80, 200)      # THRESHOLD IMAGE OF GRAY IMAGE
    edges = cv2.Canny(gray, 1, 100, apertureSize=3)
    mergedImage = cv2.add(threshold,edges)
    cv2.imshow('merged', mergedImage)
    #cv2.line(result, (pts2[0][0], pts2[0][1]), (pts2[1][0], pts2[1][1]), (0, 255, 0), 2)
    #cv2.line(result, (pts2[1][0], pts2[1][1]), (pts2[2][0], pts2[2][1]), (0, 255, 0), 2)
    #cv2.line(result, (pts2[2][0], pts2[2][1]), (pts2[3][0], pts2[3][1]), (0, 255, 0), 2)
    #cv2.line(result, (pts2[3][0], pts2[3][1]), (pts2[0][0], pts2[0][1]), (0, 255, 0), 2)
    firstSquareCenters1 = findCenter((pts2[1][0], pts2[1][1]), (pts2[2][0], pts2[2][1]))
    firstSquareCenters2 = findCenter((pts2[3][0], pts2[3][1]), (pts2[0][0], pts2[0][1]))
  #  print("Centers:", firstSquareCenters1,firstSquareCenters2)
    #cv2.circle (frame, (firstSquareCenters1,firstSquareCenters1),5,(0,0,255),cv2.FILLED)
    cv2.line(result, firstSquareCenters1, firstSquareCenters2, (0, 255, 0), 1)
    mainFrameCenter = findCenter(firstSquareCenters1,firstSquareCenters2)
    lines = cv2.HoughLinesP(mergedImage,1,np.pi/180,10,minLineLength=120,maxLineGap=250)
    centerPoints = []
    left = []
    right = []
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            if 0<=x1 <=width and 0<= x2 <=width :
                center = findCenter((x1,y1),(x2,y2))
                if center[0] < (width//2):
                    center1 = center
                    left.append((x1, y1))
                    left.append((x2,y2))
                else:
                    center2 = center
                    right.append((x1, y1))
                    right.append((x2,y2))
                if center1 !=0 and center2 !=0:
                    centroid1 = findCenter(center1,center2)
                    centerPoints.append(centroid1)       
        centers = minmax_centerPoints(centerPoints,1)
        laneCenters = 0
        mainCenterPosition = 0        
        if centers is not None:
            laneframeCenter = findCenter(centers[0],centers[1])
            #print(mainFrameCenter,laneframeCenter)          
            mainCenterPosition = mainFrameCenter[0] - laneframeCenter[0]            
            cv2.line(result, centers[0], centers[1], [0, 255, 0], 2)
            laneCenters = centers
           # print(centers)
        return [laneCenters,result,mainCenterPosition]
frame_counter = 0
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,320) # set the width to 320 p
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240) # set the height to 240 p
    count = 0
    speed = 0
    maincenter = 0
    while(cap.isOpened()):
        frame_counter = frame_counter+1
        print(frame_counter)
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            laneimage1 = detectedlane1(frame)
            if laneimage1 is not None:
                maincenter = laneimage1[2]
                cv2.putText(laneimage1[1],"Pos="+str(maincenter),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
                cv2.imshow('FinalWindow',laneimage1[1])
                #print("Position-> "+str(maincenter))
        else:
            cv2.imshow('FinalWindow', frame)
            resizeWindow('FinalWindow',570, 480)
        if maincenter <= 6 and maincenter > -6:
            #mot.frontmiddle()
            speed = 25
        elif maincenter > 6 and frame_counter%10 ==0:
            #mot.frontleft()
            speed = 25
            print("Right")
        elif(frame_counter%10 ==0):
            print("Forward")
            #mot.forward(speed)
        elif maincenter < -6 and frame_counter%10 ==0:
            #mot.frontright()
            speed = 25
            print("left")       
        #mot.forward(speed)  
       # cv2.imshow('Frame', frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    mot.stop()