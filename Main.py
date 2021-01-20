import cv2
import tkinter
import tkinter.ttk
from tkinter.filedialog import askopenfilename
import faceBlur

def blurFile():
    path=askopenfilename()
    img=cv2.imread(path)
    img=faceBlur.blurFaces(img)
    cv2.imshow("Blurred Image",img)
    
def blurWebcam():
    cam=cv2.VideoCapture(0)
    while True:
        ret,img=cam.read()
        img=faceBlur.blurFaces(img)
        cv2.imshow("WebCam",img)
        if (cv2.waitKey(1) & 0xFF==ord('q')):
            break
    cam.release()
    cv2.destroyAllWindows()
    
window=tkinter.Tk()
window.title("Face blurring software")
window.minsize(300,300)

logo=tkinter.PhotoImage(file="icon.png")
window.iconphoto(False,logo)
imageLabel=tkinter.ttk.Label(window,image=logo)
imageLabel.grid()

textLabel=tkinter.ttk.Label(window,text="      Face Blurring Software\nPress A Button to Start Blurring")
textLabel.grid()

fileButton=tkinter.ttk.Button(window,text="BLUR IMAGE FILE",command=blurFile)
fileButton.grid()

webcamButton=tkinter.ttk.Button(window,text="Blur WebCam",command=blurWebcam)
webcamButton.grid()
window.mainloop()
