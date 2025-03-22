
from PyQt5.QtWidgets import *
import cv2 as cv
import numpy as np
import winsound
import sys
   
class Panorama(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle('파노라마 영상')
        self.setGeometry(200,200,1000,150)
        
        collectButton=QPushButton('영상 수집',self)
        self.showButton=QPushButton('영상 보기',self) 
        self.stitchButton=QPushButton('봉합',self) 
        self.saveButton=QPushButton('저장',self)
        quitButton=QPushButton('나가기',self)
        self.label=QLabel('환영합니다!',self)
        #
        self.paintButton=QPushButton('페인팅',self)
        self.cutButton=QPushButton('오림',self)
        self.incButton=QPushButton('+',self)
        self.decButton=QPushButton('-',self)
        
        collectButton.setGeometry(10,25,100,30)
        self.showButton.setGeometry(110,25,100,30) 
        self.stitchButton.setGeometry(210,25,100,30) 
        self.saveButton.setGeometry(710,25,100,30)
        quitButton.setGeometry(850,25,100,30) 
        self.label.setGeometry(10,80,500,50)
        #
        self.paintButton.setGeometry(310,25,100,30)
        self.cutButton.setGeometry(410,25,100,30)
        self.incButton.setGeometry(510,25,50,30)
        self.decButton.setGeometry(610,25,50,30)

        self.showButton.setEnabled(False) 
        self.stitchButton.setEnabled(False) 
        self.saveButton.setEnabled(False)
        #
        self.paintButton.setEnabled(False)
        self.cutButton.setEnabled(False)
        self.incButton.setEnabled(False)
        self.decButton.setEnabled(False)
        
        collectButton.clicked.connect(self.collectFunction)
        self.showButton.clicked.connect(self.showFunction)       
        self.stitchButton.clicked.connect(self.stitchFunction) 
        self.saveButton.clicked.connect(self.saveFunction)   
        quitButton.clicked.connect(self.quitFunction)      
        #
        self.paintButton.clicked.connect(self.paintFunction) 
        self.cutButton.clicked.connect(self.cutFunction)    
        self.incButton.clicked.connect(self.incFunction)              
        self.decButton.clicked.connect(self.decFunction)  


        self.BrushSiz=10			# 페인팅 붓의 크기
        
    def collectFunction(self):
        self.showButton.setEnabled(False) 
        self.stitchButton.setEnabled(False) 
        self.saveButton.setEnabled(False)
        self.label.setText('c를 여러 번 눌러 수집하고 끝나면 q를 눌러 비디오를 끕니다.')
        
        self.cap=cv.VideoCapture(0,cv.CAP_DSHOW) 
        if not self.cap.isOpened(): sys.exit('카메라 연결 실패')
        
        self.imgs=[]   
        while True:
            ret,frame=self.cap.read()  
            if not ret: break
            
            cv.imshow('video display', frame)
            
            key=cv.waitKey(1) 
            if key==ord('c'):            
                self.imgs.append(frame)	# 영상 저장
            elif key==ord('q'):
                self.cap.release() 
                cv.destroyWindow('video display')                
                break 
        
        if len(self.imgs)>=2:		# 수집한 영상이 2장 이상이면
            self.showButton.setEnabled(True) 
            self.stitchButton.setEnabled(True) 
            self.saveButton.setEnabled(True)        
                    
    def showFunction(self):
        self.label.setText('수집된 영상은 '+str(len(self.imgs))+'장 입니다.')
        stack=cv.resize(self.imgs[0],dsize=(0,0),fx=0.25,fy=0.25)
        for i in range(1,len(self.imgs)):
            stack=np.hstack((stack,cv.resize(self.imgs[i],dsize=(0,0),fx=0.25,fy=0.25))) 
        cv.imshow('Image collection',stack)        
        
    def stitchFunction(self):
        stitcher=cv.Stitcher_create()
        status,self.img_stitched=stitcher.stitch(self.imgs)
        if status==cv.STITCHER_OK:
            cv.imshow('Image stitched panorama',self.img_stitched)     
        else:
            winsound.Beep(1000,500)            
            self.label.setText('파노라마 제작에 실패했습니다. 다시 시도하세요.')    
        #
        self.paintButton.setEnabled(True)
        self.cutButton.setEnabled(True)
        self.incButton.setEnabled(True)
        self.decButton.setEnabled(True)
                
        self.mask=np.zeros((self.img_stitched.shape[0],self.img_stitched.shape[1]),np.uint8) 
        self.mask[:,:][:,:]=cv.GC_PR_BGD	# 모든 화소를 배경일 것 같음으로 초기화

                      
    def paintFunction(self):
        cv.setMouseCallback('Image stitched panorama',self.painting) # paint in stitched image
        
    def painting(self,event,x,y,flags,param):
        if event==cv.EVENT_LBUTTONDOWN:   
            cv.rectangle(self.img_stitched,(x,y),(x+self.BrushSiz,y+self.BrushSiz),(0,0,255),-1)    # fill rectangle with red
            cv.rectangle(self.mask,(x,y),(x+self.BrushSiz,y+self.BrushSiz),cv.GC_BGD,-1)
            
        elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
            cv.rectangle(self.img_stitched,(x,y),(x+self.BrushSiz,y+self.BrushSiz),(0,0,255),-1)
            cv.rectangle(self.mask,(x,y),(x+self.BrushSiz,y+self.BrushSiz),cv.GC_BGD,-1)
            
        cv.imshow('Image stitched panorama',self.img_stitched)        
        
    def cutFunction(self):
        background=foreground=np.zeros((1,65),np.float64) 
        foreground=np.zeros((1,65),np.float64) 
        cv.grabCut(self.img_stitched,self.mask,None,background,foreground,5,cv.GC_EVAL_FREEZE_MODEL)
        mask2=np.where((self.mask==2)|(self.mask==0),0,1).astype('uint8')
        self.grabImg=self.img_stitched*mask2[:,:,np.newaxis]
        cv.imshow('Scissoring',self.grabImg) 
        
    def incFunction(self):
        self.BrushSiz=min(20,self.BrushSiz+1) 
        print('Increase BrushSize: ',self.BrushSiz)
        
    def decFunction(self):
        self.BrushSiz=max(1,self.BrushSiz-1) 
        print('Decrease BrushSize: ',self.BrushSiz)

    

    def saveFunction(self):
        fname=QFileDialog.getSaveFileName(self,'파일 저장','./')
        cv.imwrite(fname[0],self.img_stitched)
        
    def quitFunction(self): 
        self.cap.release() 
        cv.destroyAllWindows()  
        self.close()

app=QApplication(sys.argv) 
win=Panorama() 
win.show()
app.exec_()

