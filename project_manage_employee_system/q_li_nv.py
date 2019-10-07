# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'q_li_nv.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import Login

class InsertDialog(QtWidgets.QDialog):
    def __init__(self):
        super(InsertDialog, self).__init__()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/add1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        

        self.QBtn = QtWidgets.QPushButton()
        self.QBtn.setText("Thêm")
        self.QBtn.setStyleSheet("background: #CCFFFF;\n""height:40px; \n""font-size:18px")

        self.setWindowTitle("Thêm nhân viên")
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        
        self.QBtn.clicked.connect(self.add_employee)

        layout = QtWidgets.QVBoxLayout()

        self.nameinput = QtWidgets.QLineEdit()
        self.nameinput.setPlaceholderText("Nhập tên *")
        self.nameinput.setStyleSheet("border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout.addWidget(self.nameinput)

        
        self.branchinput = QtWidgets.QComboBox()
        self.branchinput.addItem("----Chọn bộ phận----")
        self.branchinput.addItem("Marketing")
        self.branchinput.addItem("Sale")
        self.branchinput.addItem("IT")
        self.branchinput.addItem("Support")
        self.branchinput.addItem("Account")
        self.branchinput.addItem("Manager")
        self.branchinput.setStyleSheet("border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout.addWidget(self.branchinput)

       
        self.mobileinput = QtWidgets.QLineEdit()
        self.onlyInt = QtGui.QIntValidator()
        self.mobileinput.setValidator(self.onlyInt) # chi nhap dc so
        self.mobileinput.setPlaceholderText("Nhập Số điện thoại")
        self.mobileinput.setStyleSheet("border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout.addWidget(self.mobileinput)

        self.addressinput = QtWidgets.QLineEdit()
        self.addressinput.setPlaceholderText("Nhập địa chỉ")
        self.addressinput.setStyleSheet("border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout.addWidget(self.addressinput)

        self.hourwork = QtWidgets.QLineEdit()
        self.onlyInt = QtGui.QIntValidator()
        self.hourwork.setValidator(self.onlyInt) # chi nhap dc so
        self.hourwork.setPlaceholderText("Nhập tổng số giờ làm *")
        self.hourwork.setStyleSheet("border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout.addWidget(self.hourwork)

        self.hoursalary = QtWidgets.QComboBox()
        self.hoursalary.addItem("---Chọn mức lương theo giờ---")
        self.hoursalary.addItem("15.000 vnđ")
        self.hoursalary.addItem("20.000 vnđ")
        self.hoursalary.addItem("30.000 vnđ")
        self.hoursalary.setStyleSheet("border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout.addWidget(self.hoursalary)

       

        layout.addWidget(self.QBtn)
        self.setLayout(layout)
   
    def add_employee(self):


        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        phone = self.mobileinput.text()
        address = self.addressinput.text()
        hourwork = self.hourwork.text()
        hoursalary = self.hoursalary.itemText(self.hoursalary.currentIndex())
        if hoursalary == '---Chọn mức lương theo giờ---':
            hoursalary=0
        elif hoursalary == '15.000 vnđ':
            hoursalary=15
        elif hoursalary == '20.000 vnđ':
            hoursalary=20
        else:
            hoursalary=30

        
        if name=='':
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Vui lòng nhập tên.')
        elif branch=='----Chọn bộ phận----': 
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Vui lòng chọn bộ phận.')
        elif hourwork=='':
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Vui lòng nhập tổng số giờ làm.')

        else:
            salary = int(hourwork)*int(hoursalary)*1000
            try:
                self.mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  passwd="",
                  database="tt_rtos"
                )
                self.mycursor = self.mydb.cursor() 
            
                
                self.mycursor.execute("INSERT INTO quan_li_nv (name,branch,phone,address,hourwork,hoursalary) VALUES ('{}','{}','{}','{}','{}','{}') ".format(name,branch,phone,address,hourwork,hoursalary))

                
                self.mycursor.execute("INSERT INTO luong (name,salary) VALUES ('{}','{}') ".format(name,salary))
                
                self.mydb.commit()
                
               
                QtWidgets.QMessageBox.information(QtWidgets.QMessageBox(),'Successful','Thêm nhân viên thành công.')
                
                self.close()
            except Exception:
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Không thể thêm nhân viên.')


class SearchDialog(QtWidgets.QDialog):
    def __init__(self):
        super(SearchDialog, self).__init__()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/s1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.QBtn = QtWidgets.QPushButton()
        self.QBtn.setText("Tìm kiếm")
        self.QBtn.setStyleSheet("background: #CCFFFF;\n""height:40px; \n""font-size:18px")

        self.setWindowTitle("Tìm kiếm nhân viên")
        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.QBtn.clicked.connect(self.search_employee)
        layout = QtWidgets.QVBoxLayout()

        self.searchinput = QtWidgets.QLineEdit()
        self.onlyInt = QtGui.QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Nhập mã id cần tìm")
        self.searchinput.setStyleSheet("border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)


    def search_employee(self):

        searchrol = ""
        searchrol = self.searchinput.text()
        if searchrol=='':
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Vui lòng nhập mã id của nhân viên cần tìm')
        else:
            try:
                self.mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  passwd="",
                  database="tt_rtos"
                )
                self.mycursor = self.mydb.cursor() 
                result = self.mycursor.execute("SELECT quan_li_nv.id ,quan_li_nv.name,quan_li_nv.branch,quan_li_nv.phone,quan_li_nv.address,luong.salary FROM quan_li_nv INNER JOIN luong ON quan_li_nv.id=luong.id AND quan_li_nv.id="+str(searchrol))

                row = self.mycursor.fetchone()
                
                serachresult = "Id : "+str(row[0])+'\n'+"Tên : "+str(row[1])+'\n'+"Bộ phận : "+str(row[2])+'\n'+"Số điện thoại : "+str(row[3])+'\n'+"địa chỉ : "+str(row[4])+'\n'+"lương : "+str(row[5])+" vnđ"
               
                QtWidgets.QMessageBox.information(QtWidgets.QMessageBox(), 'Thông tin', serachresult)
                self.mydb.commit()

                
                self.close()
            except Exception:
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Không tìm thấy nhân viên')

class DeleteDialog(QtWidgets.QDialog):
    def __init__(self):
        super(DeleteDialog, self).__init__()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/d1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.QBtn = QtWidgets.QPushButton()
        self.QBtn.setText("Delete")
        self.QBtn.setStyleSheet("background: #CCFFFF;\n""height:40px; \n""font-size:18px")

        self.setWindowTitle("Xóa nhân viên")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.delete_employee)
        layout = QtWidgets.QVBoxLayout()

        self.deleteinput = QtWidgets.QLineEdit()
        self.onlyInt = QtGui.QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("Nhập id của nhân viên cần xóa")
        self.deleteinput.setStyleSheet("border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def delete_employee(self):

        delrol = ""
        delrol = self.deleteinput.text()
        if delrol=='':
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Vui lòng nhập mã id của nhân viên cần xóa')
        else:
            try:
                self.mydb = mysql.connector.connect(
                      host="localhost",
                      user="root",
                      passwd="",
                      database="tt_rtos"
                    )
                self.mycursor = self.mydb.cursor() 

                #check nhan vien exist, neu ko thi nhay toi except
                result = self.mycursor.execute("SELECT * FROM luong WHERE id="+str(delrol))
                result = self.mycursor.fetchone()
                row_exist = result[0]
               
                self.mycursor.execute("DELETE FROM quan_li_nv WHERE id="+str(delrol))
                self.mycursor.execute("DELETE FROM luong WHERE id="+str(delrol))

            
                self.mydb.commit()
                self.mycursor.close()
                self.mydb.close()
                
                QtWidgets.QMessageBox.information(QtWidgets.QMessageBox(),'Successful','Xóa nhân viên thành công')
                self.close()
            except Exception:
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Mã id nhân viên không tồn tại.')


class Ui_QMainWindow(QtWidgets.QDialog):
    def setupUi(self, QMainWindow):
        
        # QMainWindow.resize(802, 600)
        QMainWindow.setFixedWidth(760)
        QMainWindow.setFixedHeight(600)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/nhan_vien.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QMainWindow.setWindowIcon(icon)
        QMainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(QMainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ### table 1
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(140, 80, 601, 241))
        self.tableWidget.setStyleSheet("background:#f9fdff")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(("Id", "Tên", "Bộ phận", "SĐT", "Địa chỉ","Giờ làm","Hệ số lương"))
        self.tableWidget.setObjectName("tableWidget")
        self.btn_them = QtWidgets.QPushButton(self.centralwidget)
        self.btn_them.setGeometry(QtCore.QRect(10, 80, 101, 51))
        ###
        
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_them.setFont(font)
        self.btn_them.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_them.setStyleSheet("color:red;\n""background : yellow;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/add1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_them.setIcon(icon1)
        self.btn_them.setIconSize(QtCore.QSize(30, 30))
        self.btn_them.setObjectName("btn_them")

        self.btn_xoa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_xoa.setGeometry(QtCore.QRect(10, 180, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_xoa.setFont(font)
        self.btn_xoa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_xoa.setStyleSheet("color:white;\n"
"background:#ff7a06")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/d1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_xoa.setIcon(icon2)
        self.btn_xoa.setIconSize(QtCore.QSize(30, 30))
        self.btn_xoa.setObjectName("btn_xoa")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(10, 270, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_search.setStyleSheet("color:red;\n"
"background:#fffdb5")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/s1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon3)
        self.btn_search.setIconSize(QtCore.QSize(20, 20))
        self.btn_search.setObjectName("btn_search")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(10, 380, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setStyleSheet("color:red;\n"
"background:#bbd3ff;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exit.setIcon(icon4)
        self.btn_exit.setObjectName("btn_exit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 0, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        #table 2 ###
        ##
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(140, 379, 599, 151))
        self.tableWidget_2.setStyleSheet("background:#fbffea")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.setHorizontalHeaderLabels(("Mã Id", "Tên", "Lương"))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(199)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(28)
        ####

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 350, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 550, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 550, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        ###
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.btn_load.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_load.setToolTipDuration(-1)
        self.btn_load.setStyleSheet("background:#effcff;\n"
"border-radius : 10px;")
        self.btn_load.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/r3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_load.setIcon(icon5)
        self.btn_load.setIconSize(QtCore.QSize(30, 30))
        self.btn_load.setObjectName("btn_load")
        ### 


        QMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QMainWindow)
        self.statusbar.setObjectName("statusbar")
        QMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(QMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QMainWindow)


        ###  Event   ###
        self.btn_load.clicked.connect(self.loaddata)
        self.btn_them.clicked.connect(self.insert)
        self.btn_search.clicked.connect(self.search)
        self.btn_xoa.clicked.connect(self.delete)
        self.btn_exit.clicked.connect(self.exit)


    def retranslateUi(self, QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QMainWindow.setWindowTitle(_translate("QMainWindow", "Quản lí nhân viên"))
        self.btn_them.setText(_translate("QMainWindow", "Thêm"))
        self.btn_xoa.setText(_translate("QMainWindow", "Xóa"))
        self.btn_search.setText(_translate("QMainWindow", "Tìm kiếm"))
        self.btn_exit.setText(_translate("QMainWindow", "Thoát"))
        self.label.setText(_translate("QMainWindow", "HỆ THỐNG QUẢN LÍ NHÂN VIÊN"))
        self.label_2.setText(_translate("QMainWindow", "Bảng danh sách nhân viên"))
        self.tableWidget_2.setSortingEnabled(False)
        self.label_3.setText(_translate("QMainWindow", "Bảng lương "))
        self.label_4.setText(_translate("QMainWindow", "Nguyễn Văn Bắc - 16119065"))
        self.label_5.setText(_translate("QMainWindow", "Lê Ngọc Thành - 16119146"))

    def loaddata(self):
        self.mydb = mysql.connector.connect(
              host="localhost",
              user="root",
              passwd="",
              database="tt_rtos"
            )
        self.mycursor = self.mydb.cursor() 
        
        query = "SELECT * FROM quan_li_nv"

        result = self.mycursor.execute(query)
        result = self.mycursor.fetchall()

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))


        query2 = "SELECT * FROM luong"
        result = self.mycursor.execute(query2)
        result = self.mycursor.fetchall()
        
        self.tableWidget_2.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))

        self.mycursor.close()

      
    
    def insert(self):
        dlg = InsertDialog()
        dlg.exec_() 
    
    def search(self):
        dlg = SearchDialog()
        dlg.exec_() 

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()
    def exit(self):
        exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QMainWindow = QtWidgets.QMainWindow()
    ui = Ui_QMainWindow()
    ui.setupUi(QMainWindow)
    ui.loaddata()
    QMainWindow.show()
    sys.exit(app.exec_())
