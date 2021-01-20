import face_recognition
import cv2

def blurFaces(img):
    kwidth=21
    kheight=21
    faces=face_recognition.face_locations(img)#top right bottom left
    
    for face in faces:
        croppedImg=img[face[0]:face[2],face[3]:face[1]]
        blurImg=cv2.blur(croppedImg,(kwidth,kheight))
        img[face[0]:face[2],face[3]:face[1]]=blurImg
        
    return img

#conda activate py37
#python -m idlelib
