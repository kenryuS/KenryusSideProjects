import sys, math, random, traceback
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QDialogButtonBox
from PySide6.QtCore import QObject, QRunnable, Slot, QThreadPool, Signal
from ui_MainWindow import Ui_MainWindow as mainwin
from ui_configdialog import Ui_config as calcconf
from ui_progress import Ui_Dialog as progressdialog
from ui_result import Ui_Dialog as resultdialog

class calcthreadsig(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class calcthread(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(calcthread, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = calcthreadsig()

        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.mainui = mainwin()
        self.mainui.setupUi(self)
        self.startcalc()
        self.show()

    def startcalc(self):
        self.mainui.StartBTN.clicked.connect(self.CalcConf)

    def CalcConf(self):
        dialog = calcdialog()
        dialog.exec()

class calcdialog(QDialog):
    def __init__(self):
        super(calcdialog, self).__init__()
        self.calcui = calcconf()
        self.calcui.setupUi(self)
        self.calcui.textEdit.setPlaceholderText('Input Integer in Standard Form')
        self.calcui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.sendinfo)

    def CalcProg(self):
        dialog = calcprog()
        dialog.exec()

    def sendinfo(self):
        global calcmode
        global calcnum
        if self.calcui.radioButton.isChecked():
            calcmode = 1
        elif self.calcui.radioButton_2.isChecked():
            calcmode = 2
        elif self.calcui.radioButton_3.isChecked():
            calcmode = 3
        elif self.calcui.radioButton_4.isChecked():
            calcmode = 4
        elif self.calcui.radioButton_5.isChecked():
            calcmode = 5
        else:
            errormsg("Some Informations are missing!")
            return 1

        if self.calcui.textEdit.toPlainText() == "":
            errormsg("Some Informations are missing!")
            return 1
        else:
            calcnum = int(self.calcui.textEdit.toPlainText())
            self.CalcProg()

class calcprog(QDialog):
    def __init__(self):
        super(calcprog, self).__init__()
        self.progui = progressdialog()
        self.progui.setupUi(self)
        self.threadpool = QThreadPool()
        self.progthreads()

    def calculationcore(self, progress_callback):
        i = 1
        global resultnum
        resultnum = 0
        if calcmode == 1:
            out = 0
            while i <= calcnum:
                a = ((i**2)**-1)
                out += a
                progress_callback.emit((i/calcnum) * 100)
                i += 1
            resultnum = math.sqrt(out * 6)
        elif calcmode == 2:
            out = 1
            while i <= calcnum:
                out *= (((2*i)/((2*i)-1)))*((2*i)/((2*i)+1))
                progress_callback.emit((i/calcnum) * 100)
                i += 1
            resultnum = out * 2
        elif calcmode == 3:
            out = 0
            while i <= calcnum:
                out += ((-1)**(i-1)) * 4/((2*i)-1)
                progress_callback.emit((i/calcnum) * 100)
                i += 1
            resultnum = out
        elif calcmode == 4:
            out = 0
            while i <= calcnum:
                out += (-1)**(i-1) * (4/((2*i)*((2*i)+1)*((2*i)+2)))
                progress_callback.emit((i/calcnum) * 100)
                i += 1
            resultnum = out + 3
        elif calcmode == 5:
            x = y = z = a = out = 0
            while i <= calcnum:
                x = random.random()
                y = random.random()
                z = (x**2) + (y**2)
                if z >= float(1):
                    pass
                elif z < float(1):
                    a += 1
                progress_callback.emit((i/calcnum) * 100)
                i += 1
            resultnum = (a/calcnum) * 4
        return 0
        
    def showresult(self):
        rd = Resultdialog()
        rd.exec()
    
    def showprog(self, n):
        self.progui.progressBar.setValue(n)

    def print_output(self, s):
        print(s)

    def progthreads(self):
        calculationprogress = calcthread(self.calculationcore)
        calculationprogress.signals.result.connect(self.print_output)
        calculationprogress.signals.finished.connect(self.showresult)
        calculationprogress.signals.progress.connect(self.showprog)

        self.threadpool.start(calculationprogress)

class Resultdialog(QDialog):
    def __init__(self):
        super(Resultdialog, self).__init__()
        self.result = resultdialog()
        self.result.setupUi(self)
        self.result.textBrowser.append(str(resultnum))

def errormsg(message):
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText(message)
    button = msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())
