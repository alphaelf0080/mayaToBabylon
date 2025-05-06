from PySide2 import QtCore, QtGui, QtWidgets#.QFileSystemModel

def loadStyle(self):
 

    buttonStyle = "\
                     QLineEdit {\
                     height:50px;\
                     background-color:#333333;\
                     border-radius :5px;\
                     border-style:solid;\
                     border-width:3px;\
                     border-color:#5E749C;\
                     text-align:center;\
                     }\
                     QComboBox {\
                     height:50px;\
                     background-color:#333333;\
                     border-radius :5px;\
                     border-style:solid;\
                     border-width:3px;\
                     border-color:#5E749C;\
                     text-align:right;\
                     }\
                     QPushButton {\
                     background-color:#333333;\
                     border-radius:10px;\
                     border-style:solid;\
                     border-width:3px;\
                     border-color:#5E749C;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-radius:10px;\
                     border-style:solid;\
                     border-width:3px;\
                     border-color:#5E749C;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-radius:10px;\
                     border-style:solid;\
                     border-width:3px;\
                     border-color:#5E749C;\
                     }\
                     "
    buttonStyleB = "\
                     QPushButton {\
                     font-size:%spx;\
                     background-color:#778888;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#AAAA33;\
                     }\
                     "%(str(fontScale))   

    buttonStyleAdj = "\
                     QPushButton {\
                     font-size:%spx;\
                     background-color:#494949;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#AAAA33;\
                     }\
                     "%(str(fontScale))   

                     
    buttonStyleMain = "\
                     QPushButton {\
                     font-size:%spx;\
                     font-weight: bold;\
                     background-color:#33aaaa;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:2px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:2px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:2px;\
                     border-color:#AAAA33;\
                     }\
                     "%(str(fontScale))                        
                     
    buttonStyleMainLeft = "\
                     QPushButton {\
                     font-size:%spx;\
                     font-weight: bold;\
                     background-color:#33aaaa;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#AAAA33;\
                     }\
                     "%(str(fontScale))                                      
                                               
                     
                                          
                                                                                    
    buttonStyleBLeft = "\
                     QPushButton {\
                     font-size:%spx;\
                     background-color:#778888;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#AAAA33;\
                     }\
                     "%(str(fontScale))                                      
                                               
                                                            
                                                                         
                                                                                                   
    buttonStyleC = "\
                     QPushButton {\
                     background-color:#333333;\
                     color:#eeeeee;\
                     font-size:%spx;\
                     border-radius:10px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#aaaaaa;\
                     }\
                     QPushButton:hover{\
                     background-color:#aaeeaa;\
                     color:#111111;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#aaeeaa;\
                     }\
                     QPushButton:pressed{\
                     background-color:#aaeeaa;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#aaeeaa;\
                     }\
                     QPushButton:checked{\
                     background-color:#99aa99;\
                     color:#111111;\
                     border-radius:8px;\
                     border-style:solid;\
                     border-width:2px;\
                     border-color:#99cc99;\
                     }\
                     "%(str(fontScale))    

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

    buttonStyleCRight = "\
                     QPushButton {\
                     background-color:#333333;\
                     color:#777777;\
                     font-size:%spx;\
                     border-top-right-radius: 10px;\
                     border-bottom-right-radius: 10px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#aaaaaa;\
                     }\
                     QPushButton:hover{\
                     background-color:#aaeeaa;\
                     color:#777777;\
                     border-top-right-radius: 10px;\
                     border-bottom-right-radius: 10px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#aaeeaa;\
                     }\
                     QPushButton:pressed{\
                     background-color:#aaeeaa;\
                     border-top-right-radius: 10px;\
                     border-bottom-right-radius: 10px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#aaeeaa;\
                     }\
                     QPushButton:checked{\
                     background-color:#99aa99;\
                     color:#777777;\
                     border-top-right-radius: 10px;\
                     border-bottom-right-radius: 10px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#99cc99;\
                     }\
                     "%(str(fontScale))                                                                     
    buttonStyleLeft = "\
                     QPushButton {\
                     background-color:#778888;\
                     font-size: %spx;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#AAAA33;\
                     }\
                     "%(str(fontScale))                       
    buttonStyleLeftB = "\
                     QPushButton {\
                     background-color:#778888;\
                     font-size: %spx;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#AAAA33;\
                     }\
                     "%(str(fontScale))   
                     
    buttonStyleRightB = "\
                     QPushButton {\
                     background-color:#778888;\
                     font-size: %spx;\
                     border-top-right-radius:8px;\
                     border-bottom-right-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#AAAA33;\
                     }\
                     "%(str(fontScale))                                       
                                                                             
 
    buttonStyleLeftSlotGrp = "\
                     QPushButton {\
                     background-color:#778888;\
                     font-size: %spx;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#777777;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#777777;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#777777;\
                     }\
                     "%(str(fontScale))                                                                                                            
                                                                                                                                                                                                                 
    lineEditRightSlotGrp = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-top-right-radius: 8px;\
                     border-bottom-right-radius: 8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#777777;\
                     text-align:left;\
                     }\
                     QComboBox {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-top-right-radius: 8px;\
                     border-bottom-right-radius: 8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#777777;\
                     text-align:left;\
                     }\
                     "%(str(fontScale),str(fontScale))                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                 
    lineEditRight = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-top-right-radius: 8px;\
                     border-bottom-right-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#333333;\
                     text-align:left;\
                     }\
                     "%(str(fontScale))   
    lineEditRightBMiddle = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-style:solid;\
                     border-right-width:1px;\
                     border-color:#555555;\
                     text-align:left;\
                     }\
                     "%(str(fontScale))   
                     
                                            
    lineEditRightBMiddleDark = "\
                     QLineEdit {\
                     font-size:%spx;\
                     color:#aaaaaa;\
                     background-color:#333333;\
                     border-style:solid;\
                     border-right-width:1px;\
                     border-color:#555555;\
                     text-align:left;\
                     }\
                     "%(str(fontScale))                                                                                             

    lineEditRightB = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-top-right-radius: 8px;\
                     border-bottom-right-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#333333;\
                     text-align:left;\
                     }\
                     QComboBox {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-top-right-radius: 8px;\
                     border-bottom-right-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#333333;\
                     text-align:left;\
                     }\
                     "%(str(fontScale),str(fontScale))   
                                                                                                                                       
                                                                                                                     
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
                                                                                                                     
    lineEditBDark = "\
                     QLineEdit {\
                     font-size:%spx;\
                     color:#aaaaaa;\
                     background-color:#333333;\
                     text-align:center;\
                     border-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#333333;\
                     }\
                     "%(str(fontScale))   
                                                                                                                    
                                                                            
    lineEditA = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-radius :6px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:left;\
                     }\
                     "%(str(fontScale))   
                     
    errMsgA = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#888888;\
                     color:#222222;\
                     border-radius :6px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#888888;\
                     text-align:left;\
                     }\
                     "%(str(fontScale))                        
                     
                     
                     
    lineEditB = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-radius :6px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))   
                     
    lineEditC = "\
                     QLineEdit {\
                     height: 30px;\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-top-right-radius: 6px;\
                     border-bottom-right-radius: 6px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))                                                  
                                                                     
    labelA  = "\
                     QLabel {\
                     height: 30px;\
                     font-size:%spx;\
                     background-color:#777777;\
                     color:#222222;\
                     border-top-left-radius:6px;\
                     border-bottom-left-radius: 6px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#777777;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))                        

    labelTextA  = "\
                     QLabel {\
                     font-size:%spx;\
                     text-align:center;\
                     }\
                     QLineEdit {\
                     font-size:%spx;\
                     text-align:center;\
                     }\
                     "%(str(fontScale),str(fontScale)) 
    checkA  = "\
                     QCheckBox {\
                     height: 20px;\
                     font-size:%spx;\
                     text-align:center;\
                     }\
                     "%(str(fontScale)) 
    spinTextA  = "\
                     QSpinBox {\
                     height: 20px;\
                     font-size:%spx;\
                     text-align:center;\
                     }\
                     "%(str(fontScale)) 


    labelARight  = "\
                     QLabel {\
                     height: 30px;\
                     font-size:%spx;\
                     background-color:#777777;\
                     color:#222222;\
                     border-top-left-radius:6px;\
                     border-bottom-left-radius: 6px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#777777;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))              
    labelAMiddle  = "\
                     QLabel {\
                     height: 30px;\
                     font-size:%spx;\
                     background-color:#777777;\
                     color:#222222;\
                     border-style:solid;\
                     border-left-width:1px;\
                     border-right-width:1px;\
                     border-color:#777777;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))       
    lineEditCMiddle = "\
                     QLineEdit {\
                     height: 30px;\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-style:solid;\
                     border-left-width:1px;\
                     border-right-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))                                        
                     
    QGroupBoxA =  "\
                     QGroupBox {\
                     font-size:12px;\
                     font-size:%spx;\
                     background-color:#505050;\
                     border-radius :8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))               

    QGroupBoxCreateSlotBox =  "\
                     QGroupBox {\
                     font-size:12px;\
                     font-size:%spx;\
                     background-color:#303030;\
                     border-radius :8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))                         
                                          
                                                               
                                                                                                         
    treeA =  "\
                     QTreeWidget {\
                     font-size:%spx;\
                     background-color:#505050;\
                     border-radius :8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))                                                       
        
    tableA =  "\
                     QTableWidget {\
                     background-color:#333333;\
                     border-radius :8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     QTableWidget:item:hover{\
                     background-color:#883333;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#883333;\
                     }\
                     QTableWidget:pressed{\
                     background-color:#33AAA33;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#AAAA33;\
                     }\
                     QTableWidget:item {\
                     font-size:1000000px;\
                     color:rgba(255,255,255,0);\
                     background-color:#333333;\
                     border-radius :8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "          
        
                             
    
    radioBtnStyleA =  "\
             QRadioButton {\
             font-size:%spx;\
             text-align:left;\
             }\
             "%(str(fontScale))  
    optionLabelA  = "\
                     QLabel{\
                     font-size:%spx;\
                     }\
                     QLineEdit{\
                     font-size:%spx;\
                     };\
                     "%(str(fontScale),str(fontScale)) 
    optionEditA  = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#333333;\
                     color:#aaaaaa;\
                     border-radius:3px;\
                     border-style:solid;\
                     border-color:#777777;\
                     text-align:center;\
                     }\
                     QLineEdit::hover{\
                     font-size:%spx;\
                     background-color:#993333;\
                     color:#aaaaaa;\
                     border-radius:3px;\
                     border-style:solid;\
                     border-color:#777777;\
                     text-align:center;\
                     }\
                     QLineEdit:read-only {\
                     font-size:%spx;\
                     background-color:#777777;\
                     color:#333333;\
                     border-radius:3px;\
                     border-style:solid;\
                     border-color:#777777;\
                     text-align:center;\
                     }\
                     "%(str(fontScale),str(fontScale),str(fontScale))

       