import sys,math,copy
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
CELL_SIZE=60
WINDOW_WIDTH=500
WINDOW_HEIGHT=400
NUMBER_OF_CELLS=100

class Example(QtGui.QWidget):
    cur_field = [[0 for col in range(NUMBER_OF_CELLS)] for row in range(NUMBER_OF_CELLS)]

    next_field = [[0 for col in range(NUMBER_OF_CELLS)] for row in range(NUMBER_OF_CELLS)]
    
    timer = QtCore.QTimer()
    step_number = 0
    def init(self):
        for i in range(NUMBER_OF_CELLS):
            for j in range(NUMBER_OF_CELLS):
                self.cur_field[i][j] = 0
    def __init__(self):
        super(Example, self).__init__()
        self.init()
        self.initUI()

    def getAmountOfNeighbs(self,x,y):
        neighbors = 0

        for diffX in range(-1, 2):
          for diffY in range(-1, 2):
            nX = x + diffX
            nY = y + diffY
            if nX >= 0 and nY >= 0 and nX < NUMBER_OF_CELLS and nY < NUMBER_OF_CELLS:
                if self.cur_field[nX][nY]==1 and not (diffX == diffY == 0):
                    neighbors += 1

        # if neighbors>0: print x,y,neighbors

        return neighbors

        
    def generate_new(self):
        self.next_field = copy.deepcopy(self.cur_field)
        self.step_number+=1
        #print "Gen #**************",self.step_number
        for i in range(NUMBER_OF_CELLS-1):
            for j in range(NUMBER_OF_CELLS-1):
                cell = self.cur_field[i][j]
                neighbors=self.getAmountOfNeighbs(i,j)
                if cell == 1 and (neighbors < 2 or neighbors > 3):
                    self.next_field[i][j] = 0
                if cell == 0 and neighbors == 3:
                    self.next_field[i][j] = 1
        self.cur_field=copy.deepcopy(self.next_field)
        self.repaint()

    def initUI(self):      

        self.setGeometry(300, 300, WINDOW_WIDTH,WINDOW_HEIGHT)
        self.setWindowTitle('Olol')

        self.btnStart = QtGui.QPushButton('Next',self)
        self.btnStart.clicked.connect(self.generate_new)


        self.btnExit = QtGui.QPushButton('Exit',self)
        self.btnExit.move(100,0)    #So both buttons don't overlap
        self.btnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.setMouseTracking(True)

        self.lblCellUnderMouse = QtGui.QLabel('0,0',self)
        self.lblCellUnderMouse.move(200,0)
        self.lblCellUnderMouse.setFixedWidth(300)
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawGrid(qp)
        qp.end()

        
    def drawGrid(self, qp): 
        for i in range(NUMBER_OF_CELLS-1):
            for j in range(NUMBER_OF_CELLS-1):
                if self.cur_field[i][j] == 1:
                    qp.setBrush(QtGui.QColor(0, 0, 200))
                    qp.drawRect(15*i,15*j,60,60)
                elif self.cur_field[i][j] == 0:
                    qp.setBrush(QtGui.QColor(255, 255, 255))
                    qp.drawRect(15*i,15*j,60,60)

    def mousePressEvent(self,event):
        sender = self.sender
        # if sender
        x = event.x()
        y = event.y()
        cell_x = int(math.ceil(x/15))
        cell_y = int(math.ceil(y/15))
        #print cell_x,cell_y
        if self.cur_field[cell_x][cell_y] == 1:
            self.cur_field[cell_x][cell_y] = 0
        else:
            self.cur_field[cell_x][cell_y] = 1
        self.repaint()
    def mouseMoveEvent(self,event):
        sender = self.sender
        x = event.x()
        y = event.y()
        cell_x = str(int(math.ceil(x/15)))
        cell_y = str(int(math.ceil(y/15)))


        cell_text = cell_x+":"+cell_y
        self.lblCellUnderMouse.setText(cell_text)

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()