import sys,math,copy,time
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
from UI_MainWindow import Ui_MainWindow
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtOpenGL

CELL_SIZE=10
WINDOW_WIDTH=500
WINDOW_HEIGHT=500
NUMBER_OF_CELLS=100
cur_field = [[0 for col in range(NUMBER_OF_CELLS)] for row in range(NUMBER_OF_CELLS)]

next_field = [[0 for col in range(NUMBER_OF_CELLS)] for row in range(NUMBER_OF_CELLS)]
boxes = [[0 for col in range(NUMBER_OF_CELLS)] for row in range(NUMBER_OF_CELLS)]

class MyQGraphicsItem(QGraphicsRectItem):
    _i= 0
    _j=0
    _cell=0
    def changeCell(self):
        if self._cell == 1:
            cur_field[self._i][self._j] = 0
            self._cell = 0
        else:
            cur_field[self._i][self._j] = 1
            self._cell = 1

    def mousePressEvent(self,event):
        self.changeCell()

        print self._i,self._j,self._cell
        ui.drawGrid()
class MyStopWatch():
    _time = 0.0
    _startTime = 0.0

    def start(self):
        self._startTime= time.clock()

    def stop(self):
        self._time = time.clock() - self._startTime

    def getTime(self):
        return self._time


class Ui_MainWindow(QtGui.QMainWindow,Ui_MainWindow):
    timer = QtCore.QTimer()
    step_number = 0
    timer_speed = 0.00001
    time =0.0
    stopwatch = MyStopWatch()
    def __init__(self,parent=None):
        super(Ui_MainWindow,self).__init__(parent)

        self.setupUi(self)
        
        self.initUI()
        self.timer.timeout.connect(self.generate_new)    

    def startNew(self):
        global next_field,cur_field,NUMBER_OF_CELLS

        cur_field = [[0 for col in range(NUMBER_OF_CELLS)] for row in range(NUMBER_OF_CELLS)]

        next_field = [[0 for col in range(NUMBER_OF_CELLS)] for row in range(NUMBER_OF_CELLS)]
        boxes = [[0 for col in range(NUMBER_OF_CELLS)] for row in range(NUMBER_OF_CELLS)]
        self.lbl_Fps=0
        self.lbl_NumOfGen=0
        self.step_number=0
        self.time=0
        self.initUI()

    def getAmountOfNeighbs(self,x,y):
        neighbors = 0
        global next_field,cur_field,NUMBER_OF_CELLS
        for diffX in range(-1, 2):
          for diffY in range(-1, 2):
            nX = x + diffX
            nY = y + diffY
            if nX >= 0 and nY >= 0 and nX < NUMBER_OF_CELLS and nY < NUMBER_OF_CELLS:
                if cur_field[nX][nY]==1 and not (diffX == diffY == 0):
                    neighbors += 1

        if neighbors>0: print x,y,neighbors

        return neighbors

        
    def generate_new(self):
        self.stopwatch.start()
        global next_field,cur_field,NUMBER_OF_CELL

        next_field = copy.deepcopy(cur_field)
        self.step_number+=1

        self.lbl_NumOfGen.setText(str(self.step_number))

        for i in range(NUMBER_OF_CELLS-1):
            for j in range(NUMBER_OF_CELLS-1):
                cell = cur_field[i][j]
                neighbors=self.getAmountOfNeighbs(i,j)
                if cell == 1 and (neighbors < 2 or neighbors > 3):
                    next_field[i][j] = 0
                if cell == 0 and neighbors == 3:
                    next_field[i][j] = 1
        cur_field=copy.deepcopy(next_field)

        self.drawGrid()

        #Stops FPS stopwatch
        self.stopwatch.stop()

        #Last_Frame holds fps value
        last_frame=self.stopwatch.getTime()
        self.lbl_Fps.setText(str(last_frame))

    def initUI(self):       
        global boxes,cur_field,NUMBER_OF_CELLS
        self.graphicsScene = QtGui.QGraphicsScene()
        self.graphicsView.setScene(self.graphicsScene)

        #Changes the size of the scene
        self.graphicsScene.setSceneRect(0,0,400,300)
        
        #Applies OpenGl layer for faster rendering
        self.graphicsView.setViewport(QtOpenGL.QGLWidget())

        self.btn_NextGen.clicked.connect(self.generate_new)

        self.connect(self.btn_Exit,SIGNAL("clicked()"),app.quit)
        self.btn_AutoGen.clicked.connect(self.toogleAutoGen)
        self.btn_New.clicked.connect(self.startNew)
        self.setMouseTracking(True)

        for i in range(NUMBER_OF_CELLS):
            for j  in range(NUMBER_OF_CELLS):
                boxes[i][j] = MyQGraphicsItem(CELL_SIZE*i,CELL_SIZE*j,CELL_SIZE,CELL_SIZE)
                boxes[i][j]._i = i
                boxes[i][j]._j=j
                cur_field[i][j]=0
                boxes[i][j]._cell=0
                self.graphicsScene.addItem(boxes[i][j])

        self.graphicsView.setAlignment(Qt.Alignment(Qt.AlignLeft))
        self.graphicsView.setSceneRect(self.graphicsScene.itemsBoundingRect())
        self.scaleView(0.50,0.5)
        self.drawGrid()
    def toogleAutoGen(self):
        if self.timer.isActive()==True:
            self.timer.stop()
        else:
            self.timer.start(self.timer_speed)

    def scaleView(self,x,y):
        self.graphicsView.scale(x,y)
        self.drawGrid

        
    def drawGrid(self): 
        global boxes,cur_field,NUMBER_OF_CELLS


        box_width = self.graphicsScene.width()/NUMBER_OF_CELLS
        box_height = self.graphicsScene.height()/NUMBER_OF_CELLS

        #QBrushes for checked or unchecked cells
        checked = QtGui.QBrush(QtGui.QColor(0,0,0))
        unchecked = QtGui.QBrush(QtGui.QColor(0,0,255))

        for i in range(NUMBER_OF_CELLS):
            for j  in range(NUMBER_OF_CELLS):
                if cur_field[i][j] == 1:
                    boxes[i][j].setBrush(checked)
                else:
                    boxes[i][j].setBrush(unchecked)

        #TODO: Make it scale when number of cells are changed

        #TODO:Make it center on the middle element
        # self.graphicsView.centerOn(self.graphicsScene.itemAt(NUMBER_OF_CELLS/2,NUMBER_OF_CELLS/2))




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()

    app.exec_()