from PySide2 import QtCore, QtGui, QtWidgets#.QFileSystemModel


def buildDock(self,dockName,x,y,w,h,fontScale):
    
    #print "buildDock"
    #print (self)
    #print (dockName)

    dockGrpStyle =  "\
                     QGroupBox {\
                     font-size:12px;\
                     font-size:%spx;\
                     background-color:#202020;\
                     border-radius :4px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))    


    lineEditRightBDark = "\
                     QLineEdit {\
                     font-size:%spx;\
                     color:#aaaaaa;\
                     background-color:#333333;\
                     border-top-right-radius: 8px;\
                     border-bottom-right-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#333333;\
                     text-align:left;\
                     }\
                     "%(str(fontScale))   
                                            


    dockWidget = QtWidgets.QDockWidget(self.tr(dockName),self)
    dockWidget.setObjectName(dockName)
    dockWidget.setMinimumWidth(w)
    dockWidget.setMinimumHeight(h)



    dockGrp = QtWidgets.QGroupBox(dockWidget)
    dockGrp.setGeometry(QtCore.QRect(x, y, w-10, h-30))
    dockGrp.setObjectName("dockGrp")
    dockGrp.setTitle(QtWidgets.QApplication.translate("MainWindow", "", None, -1))   
    dockGrp.setStyleSheet(dockGrpStyle)     
    dockGrp.setVisible(True)

    return dockGrp

   # self.qEditFrameL = QtWidgets.QLineEdit(self.dockGrp)
   # self.qEditFrameL.setGeometry(QtCore.QRect(90, 10, 60, 30))
   # self.qEditFrameL.setObjectName("qEditFrameL")
   # self.qEditFrameL.setAlignment(QtCore.Qt.AlignCenter)
    #self.qEditFrameL.setText('1')
   # self.qEditFrameL.setStyleSheet(lineEditRightBDark)     
    
    

    #self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockWidgetImages)

    #self.previewImageDock = QtWidgets.QDockWidget(self.tr("image preview"),self)
    #self.previewImageDock.setObjectName("previewImageDock")
   # self.previewImageDock.setMinimumWidth(290)
    #self.previewImageDock.setMinimumHeight(300)
    
    
  #  self.workSpaceInfoDock = QtWidgets.QDockWidget(self.tr("project Info"),self)
  #  self.workSpaceInfoDock.setObjectName("workSpaceInfoDock")
  #  self.workSpaceInfoDock.setMinimumWidth(550)
 #   self.workSpaceInfoDock.setMinimumHeight(300)
    #self.workSpaceInfoDock.setMaximumHeight(200)
    

def buildEditWithLabelBtn(parent,lineEditName,x,y,w,h,fontScale,labelTextInput,btnText):
                                                                                                  
    lineEditRightBDark = "\
                     QLineEdit {\
                     font-size:%spx;\
                     color:#aaaaaa;\
                     background-color:#333333;\
                     border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-top-left-radius: 2px;\
                     border-bottom-left-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#333333;\
                     text-align:right;\
                     }\
                     "%(str(fontScale))   

    labelWidth = len(labelTextInput) *fontScale
    labelTextStyle =  "\
                        QLabel {\
                        font-size:%spx;\
                        color:#aaaaaa;\
                        background-color: rgba(255, 255, 255, 0);\
                        border-top-right-radius: 2px;\
                        border-bottom-right-radius: 2px;\
                        border-top-left-radius: 2px;\
                        border-bottom-left-radius: 2px;\
                        border-style:solid;\
                        border-width:0px;\
                        text-align:center;\
                        border-color:#333333;\
                        }\
                        "%(str(fontScale))   

    buttonStyle = "\
                     QPushButton {\
                     background-color:#778888;\
                     font-size: %spx;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                     border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                    border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                     border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#AAAA33;\
                     }\
                     "%(str(fontScale))   
                     

                        

    labelText = QtWidgets.QLabel(parent)
    labelText.setGeometry(QtCore.QRect(x, y ,labelWidth, h))
    labelText.setText(QtWidgets.QApplication.translate("MainWindow",labelTextInput, None, -1))

    #labelText.setPixmap(QtGui.QPixmap())
   # labelText.setScaledContents(True)
    labelText.setObjectName("labelText")

    labelText.setStyleSheet(labelTextStyle)


    inpuLineEdit = QtWidgets.QLineEdit(parent)
    inpuLineEdit.setGeometry(QtCore.QRect(x, y+h+5, w, h))
    inpuLineEdit.setObjectName(lineEditName)
    inpuLineEdit.setAlignment(QtCore.Qt.AlignCenter)
    inpuLineEdit.setText(QtWidgets.QApplication.translate("MainWindow",'', None, -1))
    inpuLineEdit.setStyleSheet(lineEditRightBDark)    

    btnWidth = len(btnText)*(fontScale/2)
    inputBtn = QtWidgets.QPushButton(parent)
    inputBtn.setGeometry(QtCore.QRect(x + w ,  y+h+5, btnWidth,h))
    inputBtn.setObjectName("inputBtn")
    inputBtn.setText(QtWidgets.QApplication.translate("MainWindow",btnText, None, -1))
    #self.trimBeforeFrameBtn.clicked.connect(self.trimBeforeFrame)
    inputBtn.setStyleSheet(buttonStyle)     



    
    return [labelText,inputBtn,inpuLineEdit]


def buildEditWithLabelBtn_stand(parent,lineEditName,x,y,w,w_lineE,h,fontScale,lineE_inputText,btnText,btnColor):
                                                                                                  
    lineEditRightBDark = "\
                     QLineEdit {\
                     font-size:%spx;\
                     color:#aaaaaa;\
                     background-color:#333333;\
                     border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-top-left-radius: 2px;\
                     border-bottom-left-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#333333;\
                     text-align:right;\
                     }\
                     "%(str(fontScale))   


    buttonStyle = "\
                     QPushButton {\
                     background-color:%s;\
                     font-size: %spx;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                     border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                    border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                     border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#AAAA33;\
                     }\
                     "%(btnColor,str(fontScale))   
                     

                        

    #labelText = QtWidgets.QLabel(parent)
    #labelText.setGeometry(QtCore.QRect(x, y ,labelWidth, h))
    #labelText.setText(QtWidgets.QApplication.translate("MainWindow",labelTextInput, None, -1))

    #labelText.setPixmap(QtGui.QPixmap())
   # labelText.setScaledContents(True)
    #labelText.setObjectName("labelText")

    #labelText.setStyleSheet(labelTextStyle)
    #btnWidth = len(btnText)*(fontScale/2)
    inputBtn = QtWidgets.QPushButton(parent)
    inputBtn.setGeometry(QtCore.QRect(x ,  y, w, h))
    inputBtn.setObjectName("inputBtn")
    inputBtn.setText(QtWidgets.QApplication.translate("MainWindow",btnText, None, -1))
    #self.trimBeforeFrameBtn.clicked.connect(self.trimBeforeFrame)
    inputBtn.setStyleSheet(buttonStyle)     

    inpuLineEdit = QtWidgets.QLineEdit(parent)
    inpuLineEdit.setGeometry(QtCore.QRect(x + w +5, y, w_lineE, h))
    inpuLineEdit.setObjectName(lineEditName)
    inpuLineEdit.setAlignment(QtCore.Qt.AlignCenter)
    inpuLineEdit.setText(QtWidgets.QApplication.translate("MainWindow",lineE_inputText, None, -1))
    inpuLineEdit.setStyleSheet(lineEditRightBDark)    




    
    return [inputBtn,inpuLineEdit]


def buildEditWithLabelA(parent,lineEditName,x,y,w,h,fontScale,labelTextInput):
                                                                                                  
    lineEditRightBDark = "\
                     QLineEdit {\
                     font-size:%spx;\
                     color:#aaaaaa;\
                     background-color:#333333;\
                     border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-top-left-radius: 2px;\
                     border-bottom-left-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#333333;\
                     text-align:right;\
                     }\
                     "%(str(fontScale))   

    labelWidth = len(labelTextInput) *fontScale
    labelTextStyle =  "\
                        QLabel {\
                        font-size:%spx;\
                        color:#aaaaaa;\
                        background-color: rgba(255, 255, 255, 0);\
                        border-top-right-radius: 2px;\
                        border-bottom-right-radius: 2px;\
                        border-top-left-radius: 2px;\
                        border-bottom-left-radius: 2px;\
                        border-style:solid;\
                        border-width:0px;\
                        text-align:center;\
                        border-color:#333333;\
                        }\
                        "%(str(fontScale))   

    buttonStyle = "\
                     QPushButton {\
                     background-color:#778888;\
                     font-size: %spx;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                     border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                    border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                     border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#AAAA33;\
                     }\
                     "%(str(fontScale))   
                     

                        

    labelText = QtWidgets.QLabel(parent)
    labelText.setGeometry(QtCore.QRect(x, y ,labelWidth, h))
    labelText.setText(QtWidgets.QApplication.translate("MainWindow",labelTextInput, None, -1))

    #labelText.setPixmap(QtGui.QPixmap())
   # labelText.setScaledContents(True)
    labelText.setObjectName("labelText")

    labelText.setStyleSheet(labelTextStyle)


    inpuLineEdit = QtWidgets.QLineEdit(parent)
    inpuLineEdit.setGeometry(QtCore.QRect(x, y+h+5, w, h))
    inpuLineEdit.setObjectName(lineEditName)
    inpuLineEdit.setAlignment(QtCore.Qt.AlignCenter)
    inpuLineEdit.setText(QtWidgets.QApplication.translate("MainWindow",'', None, -1))
    inpuLineEdit.setStyleSheet(lineEditRightBDark)    




    
    return [labelText,inpuLineEdit]


def buildItemTable(parent,tableName,x,y,w,h,fontScale):  ### label and input , the same line
                                                                                                  
    tableA =  "\
                     QTableWidget {\
                     background-color:#333333;\
                     border-radius :2px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     QTableWidget:item:hover{\
                     background-color:#883333;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#883333;\
                     }\
                     QTableWidget:pressed{\
                     background-color:#33AAA33;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#AAAA33;\
                     }\
                     QTableWidget:item {\
                     font-size:1000000px;\
                     color:rgba(255,255,255,0);\
                     background-color:#333333;\
                     border-radius :2px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "          
        
    itemTable = QtWidgets.QTableWidget(parent)
    itemTable.clear()
    itemTable.setGeometry(QtCore.QRect(x, y,w, h))
    itemTable.setObjectName(tableName)
    itemTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    itemTable.horizontalHeader().setVisible(False)
    itemTable.verticalHeader().setVisible(False)
    itemTable.setStyleSheet(tableA)

    return itemTable

def buildInfoTable(parent,tableName,x,y,w,h,fontScale):
    infoTableStyle =  "\
                 QTableWidget {\
                 font-size:12px;\
                 background-color:#333333;\
                 border-radius :2px;\
                 border-style:solid;\
                 border-width:1px;\
                 border-color:#666666;\
                 text-align:center;\
                 }\
                 "     
        
        
    infoTable = QtWidgets.QTableWidget(parent)
    infoTable.setGeometry(QtCore.QRect(x, y,w,h))

    infoTable.setObjectName("infoTable")

    infoTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    infoTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    infoTable.horizontalHeader().setVisible(False)
    infoTable.verticalHeader().setVisible(False)

    infoTable.setStyleSheet(infoTableStyle)

    return infoTable

def buildOneBtnA(parent,x,y,w,h,fontScale,btnColor,textColor,btnText):
    buttonStyleA = "\
                     QPushButton {\
                     background-color:%s;\
                     font-size: %spx;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                     border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                    border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-top-left-radius:2px;\
                     border-bottom-left-radius: 2px;\
                     border-top-right-radius: 2px;\
                     border-bottom-right-radius: 2px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#AAAA33;\
                     }\
                     "%(btnColor,str(fontScale))   

    #btnWidth = len(btnText)*(fontScale/2)
    btnA = QtWidgets.QPushButton(parent)
    btnA.setGeometry(QtCore.QRect(x , y, w, h))
    btnA.setObjectName("btnA")
    btnA.setText(QtWidgets.QApplication.translate("MainWindow",btnText, None, -1))
    #self.trimBeforeFrameBtn.clicked.connect(self.trimBeforeFrame)
    btnA.setStyleSheet(buttonStyleA)   
    return btnA


def buildAttrInfoTable(parent,tableName,x,y,w,h,fontScale,rowHeight,colW1,colW2,rowCount):
    '''
    attrInfoTableStyle =  "\
                 QTableWidget {\
                 font-size:12px;\
                 background-color:#333333;\
                 border-radius :2px;\
                 border-style:solid;\
                 border-width:1px;\
                 border-color:#666666;\
                 text-align:center;\
                 }\
                 "     
    '''
    attrInfoTableStyle =  "\
                     QTableWidget {\
                     background-color:#333333;\
                     font-size:%spx;\
                     border-radius :2px;\
                     border-style:solid;\
                     border-width:0.5px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     QTableWidget:item:hover{\
                     background-color:#883333;\
                     border-style:solid;\
                     border-width:0.5px;\
                     border-color:#883333;\
                     }\
                     QTableWidget:pressed{\
                     background-color:#33AAA33;\
                     border-style:solid;\
                     border-width:0.5px;\
                     border-color:#AAAA33;\
                     }\
                     "%(str(fontScale))   
                     
    attrInfoTable = QtWidgets.QTableWidget(parent)
    attrInfoTable.setGeometry(QtCore.QRect(x, y,w,h))

    attrInfoTable.setObjectName("attrInfoTable")

    attrInfoTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
    attrInfoTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    attrInfoTable.horizontalHeader().setVisible(False)
    attrInfoTable.verticalHeader().setVisible(False)

    attrInfoTable.setStyleSheet(attrInfoTableStyle)
        
    attrInfoTable.setColumnCount(2)
    attrInfoTable.setRowCount(rowCount)
    attrInfoTable.setColumnWidth(0, colW1)
    attrInfoTable.setColumnWidth(1, colW2)
    for i in range(0,rowCount):
        attrInfoTable.setRowHeight(i, rowHeight)



                         
    attrInfoTable.setItem(0,0,QtWidgets.QTableWidgetItem())
    attrInfoTable.item(0, 0).setText(QtWidgets.QApplication.translate("MainWindow",'attributeName', None,-1))
    attrInfoTable.item(0, 0).setToolTip(QtWidgets.QApplication.translate("MainWindow","attributeName", None,-1))

    attrInfoTable.setItem(1,0,QtWidgets.QTableWidgetItem())
    attrInfoTable.item(1, 0).setText(QtWidgets.QApplication.translate("MainWindow",'materialId', None,-1))
    attrInfoTable.item(1, 0).setToolTip(QtWidgets.QApplication.translate("MainWindow","materialId", None,-1))
   
 
    attrInfoTable.setItem(2,0,QtWidgets.QTableWidgetItem())
    attrInfoTable.item(2, 0).setText(QtWidgets.QApplication.translate("MainWindow",'isEnabled', None,-1))
    attrInfoTable.item(2, 0).setToolTip(QtWidgets.QApplication.translate("MainWindow","isEnabled", None,-1))
   
    attrInfoTable.setItem(3,0,QtWidgets.QTableWidgetItem())
    attrInfoTable.item(3, 0).setText(QtWidgets.QApplication.translate("MainWindow",'isVisible', None,-1))
    attrInfoTable.item(3, 0).setToolTip(QtWidgets.QApplication.translate("MainWindow","isVisible", None,-1))
   
 
 
 
 
 
 
    return attrInfoTable


def buildRadioCheck():
    self.drawLineCheck = QtWidgets.QRadioButton(styleDynaGrp)
    self.drawLineCheck.setGeometry(QtCore.QRect(20, 40, 70, 20))
    self.drawLineCheck.setChecked(True)
    self.drawLineCheck.setObjectName("drawLineCheck")
    self.drawLineCheck.setText(QtWidgets.QApplication.translate("MainWindow", "draw line", None, -1))
    self.drawLineCheck.setStyleSheet(radioBtnStyleA)     


def buildCheckBoxA(parent,x,y,w,h,fontScale,checkDescText):
    checkStyle = "\
                     QCheckBox {\
                     height: 20px;\
                     font-size:%spx;\
                     text-align:center;\
                     }\
                     "%(str(fontScale)) 

    checkBox = QtWidgets.QCheckBox(parent)
    checkBox.setGeometry(QtCore.QRect(x, y, w, h))
    checkBox.setObjectName("checkBox")
    #checkBox.setCheckable(True)
    checkBox.setChecked(True)  
    checkBox.setText(QtWidgets.QApplication.translate("MainWindow",checkDescText, None, -1))
    checkBox.setStyleSheet(checkStyle)   

    return checkBox


def buildCheckBtnA(parent,x,y,w,h,fontScale,btnText):
    buttonStyleCMiddle = "\
                    QPushButton {\
                    background-color:#333333;\
                    color:#777777;\
                    font-size:%spx;\
                    border-radius:0px;\
                    border-style:solid;\
                    border-right-width:1px;\
                    border-color:#555555;\
                    }\
                    QPushButton:hover{\
                    background-color:#aaeeaa;\
                    color:#777777;\
                    border-radius:0px;\
                    border-style:solid;\
                    border-right-width:1px;\
                    border-color:#555555;\
                    }\
                    QPushButton:pressed{\
                    background-color:#aaeeaa;\
                    border-radius:0px;\
                    border-style:solid;\
                    border-right-width:1px;\
                    border-color:#555555;\
                    }\
                    QPushButton:checked{\
                    background-color:#99aa99;\
                    color:#777777;\
                    border-radius:0px;\
                    border-style:solid;\
                    border-right-width:1px;\
                    border-color:#555555;\
                    }\
                     "%(str(fontScale))          
    checkBtnA = QtWidgets.QPushButton(parent)
    checkBtnA.setGeometry(QtCore.QRect(x, y, w, h))
    checkBtnA.setObjectName("checkBtnA")
    checkBtnA.setCheckable(True)
    checkBtnA.setChecked(False)  
    checkBtnA.setText(QtWidgets.QApplication.translate("MainWindow", btnText, None, -1))
    #self.fillet_n1_btn.clicked.connect(self.optionalSelect)
    checkBtnA.setStyleSheet(buttonStyleCMiddle)     


def buildTableCheckBtnItemA(w,h,fontScale,btnText,btnBGColor,btnHoverColor,btnCheckColor):
    #print w,h,fontScale,btnText
    checkBtnItemAStyle = "\
                    QPushButton {\
                    background-color:%s;\
                    color:#777777;\
                    font-size:%spx;\
                    border-radius:0px;\
                    border-style:solid;\
                    border-right-width:1px;\
                    border-color:#555555;\
                    }\
                    QPushButton:hover{\
                    background-color:#aaeeaa;\
                    color:#777777;\
                    border-radius:0px;\
                    border-style:solid;\
                    border-right-width:1px;\
                    border-color:%s;\
                    }\
                    QPushButton:pressed{\
                    background-color:#aaeeaa;\
                    border-radius:0px;\
                    border-style:solid;\
                    border-right-width:1px;\
                    border-color:#555555;\
                    }\
                    QPushButton:checked{\
                    background-color:%s;\
                    color:#777777;\
                    border-radius:0px;\
                    border-style:solid;\
                    border-right-width:1px;\
                    border-color:#555555;\
                    }\
                     "%(btnBGColor,str(fontScale),btnHoverColor,btnCheckColor)      
    checkBtnItemA = QtWidgets.QPushButton()
    checkBtnItemA.setGeometry(QtCore.QRect(0, 0, w, h))
    checkBtnItemA.setObjectName("checkBtnItemA")
    checkBtnItemA.setCheckable(True)
    checkBtnItemA.setChecked(False)  
    checkBtnItemA.setText(QtWidgets.QApplication.translate("MainWindow", btnText, None, -1))
    checkBtnItemA.setStyleSheet(checkBtnItemAStyle)   
   # print w,h,fontScale,btnText

    return checkBtnItemA

def buildLabelA(parent,x,y,w,h,fontScale,labelText,bgColor,fontColor,):


    labelA  = "\
                     QLabel {\
                     height: 30px;\
                     font-size:%spx;\
                     background-color:%s;\
                     color:%s;\
                     border-top-left-radius:0px;\
                     border-bottom-left-radius:0px;\
                     border-top-right-radius:0px;\
                     border-bottom-right-radius: 0px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#777777;\
                     text-align:center;\
                     }\
                     "%(str(fontScale),bgColor,fontColor)    

    labelTextA = QtWidgets.QLabel(parent)
    labelTextA.setGeometry(QtCore.QRect(x, y, w, h))
    labelTextA.setObjectName("labelTextA")
    labelTextA.setText(QtWidgets.QApplication.translate("MainWindow", labelText, None, -1))

    labelTextA.setStyleSheet(labelA)
    return labelTextA