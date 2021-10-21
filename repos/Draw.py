import cv2 


class Draw:
    def __init__(self):
        pass
    
    def DrawRectangle(self, image, point):
        for x in point:
            cv2.rectangle(image, (x[0], x[1]), (x[0]+x[2], x[1]+x[3]), (255, 0, 0), 1 )
    def DrawPoint(self, image, point, radius):
        for x in point:
            cv2.circle(image, (x[0]+int(x[2]/2), x[1]+int(x[3]/2)), radius, (0, 255, 0), -1)
    def putText(self, image, point, text):
        for x in point:
            cv2.putText(image, text, (x[0], x[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 0, cv2.LINE_AA)
