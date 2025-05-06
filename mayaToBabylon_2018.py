import sys
import maya.OpenMaya as OpenMaya

try:
    sys.path.append("//mcd-one/database/assets/scripts/python2.7_alpha/22") 
   # sys.path.append("//mcd-one/database/assets/scripts/python2.7_alpha/glTools/tools")
    #sys.path.append("C:/alphaOnly/python_tool/babylonMaya") 
    
except:
    pass

import babylonMayaUI #as bbUI
#try:
reload(babylonMayaUI)
#except:
#    pass
    
import babylonUI_style
reload(babylonUI_style)
                           
  
  
                                                                                                                         
from PySide2 import QtCore, QtGui, QtWidgets#.QFileSystemModel
import maya.cmds as cmds
import maya.OpenMaya as om
import maya.OpenMayaUI as mui
import shiboken2
import random
import getpass

import datetime
import time

from time import gmtime,strftime

#from PySide2.QtCore import QString
import os,math,json,shutil
import subprocess



import babylonMayaUI #as bbUI
#try:
reload(babylonMayaUI)

import babylonUI_style
reload(babylonUI_style)
                           
  
  


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "BabyLonMayeTOol", None, -1))

       # print ('1',MainWindow)


class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)

        self.infoDock = babylonMayaUI.buildDock(self,'infoDock',5,20,1200,1100,14)
        
       # self.attributeDock = babylonMayaUI.buildDock(self,'attributeDock',800,20,400,1100,14)

        ### build get babylon file grp
        #self.fileNameLineEditGrp =  babylonMayaUI.buildEditWithLabelBtn(self.infoDock,'fileNameLineEdit',10,10,400,20,14,'babylon file :','get file')
        self.getBBFileBtnGrp =  babylonMayaUI.buildEditWithLabelBtn_stand(self.infoDock,'fileNameLineEdit',10,10,150,800,25,14,'get babylon file name','Get Babylon File','#669966')

        ### build export babylon file grp
        #buildEditWithLabelBtn_stand(parent,lineEditName,x,y,w,w_lineE,h,fontScale,lineE_inputText,btnText,btnColor)
        self.bbExportFileBtnGrp =  babylonMayaUI.buildEditWithLabelBtn_stand(self.infoDock,'fileNameLineEdit',10,1010,150,800,25,14,'export babylon file name','Export File','#996666')
        self.exportBabylonDataBtn = self.bbExportFileBtnGrp[0]
        self.exportBabylonFileName = self.bbExportFileBtnGrp[1]
        self.setExportDirBtn = babylonMayaUI.buildOneBtnA(self.infoDock,970,1010,100,25,14,'#669966','#ff6666','set')
        self.setExportDirBtn.clicked.connect(self.setExportDirFn)  

        
      
        self.getBabylonFileBtn =self.getBBFileBtnGrp[0] 
       # self.getBabyLonFileNameInputBox = self.getBBFileBtnGrp[1] 
        self.babylonFileInputBox =  self.getBBFileBtnGrp[1] 
        
        
        ### toolBtn
        self.addMeshAttrBtn = babylonMayaUI.buildOneBtnA(self.infoDock,10,170,200,25,14,'#666666','#666666','add all meshs attributes')
        self.delMeshAttrBtn = babylonMayaUI.buildOneBtnA(self.infoDock,250,170,200,25,14,'#996666','#ff6666','del all meshs attributes')
        self.testABtn = babylonMayaUI.buildOneBtnA(self.infoDock,600,170,100,25,14,'#999966','#ff6666','test A')

        self.testABtn.clicked.connect(self.testFun)  


        self.addMeshAttrBtn.clicked.connect(self.addMeshBabylonAttr)  
        self.delMeshAttrBtn.clicked.connect(self.delMeshBabylonAttr)  
        self.exportBabylonDataBtn.clicked.connect(self.exportBabylonFile)  

       # self.getBabylonFileBtn.clicked.connect(self.clickSelBabylonFileBtn)  

        
        ### build get mesh count grp
        self.meshInfoGrp =  babylonMayaUI.buildEditWithLabelA(self.infoDock,'meshCountEdit',10,60,100,20,14,'mesh Count :')
        self.meshCountEditInput =  self.meshInfoGrp[1]
 
        ### build get material count grp
        self.materialInfoGrp =  babylonMayaUI.buildEditWithLabelA(self.infoDock,'materialCountEdit',10,110,100,20,14,'material Count :')
        self.materialCountEditInput = self.materialInfoGrp[1]
       
       
        ### build get Fps grp
        self.fpsInfoGrp =  babylonMayaUI.buildEditWithLabelA(self.infoDock,'fpsEdit',200,60,100,20,14,'FPS :')
        self.fpsEditInput =  self.fpsInfoGrp[1]
        
        frameRate =  cmds.currentUnit( query=True, t=True )
        if frameRate == 'film' :
            self.fps = 24.0
        elif  frameRate == 'ntsc' :
            self.fps = 30.0
        elif  frameRate == 'ntscf' :
            self.fps = 60.0    
       
        self.fpsEditInput.setText(str(self.fps)) 
       
       
        self.startFrameInfoGrp =  babylonMayaUI.buildEditWithLabelA(self.infoDock,'fpsEdit',350,60,100,20,14,'start Frame :')
        self.startFrameInput =  self.startFrameInfoGrp[1]
        self.startFrameInput.setText('0.0')
       
        self.endFrameInfoGrp =  babylonMayaUI.buildEditWithLabelA(self.infoDock,'fpsEdit',500,60,100,20,14,'end Frame :')
        self.endFrameInput =  self.endFrameInfoGrp[1]
        self.endFrameInput.setText('75.0')    
       
            
        ### build mesh/material table
       # buildLabelA(parent,x,y,w,h,fontScale,labelText):
        self.meshTableHeaderLabelA = babylonMayaUI.buildLabelA(self.infoDock,30,230,100,20,12,'mesh','#222222','#eeeeee')
        self.meshTableHeaderLabelB = babylonMayaUI.buildLabelA(self.infoDock,210,230,100,20,12,'material','#222222','#eeeeee')
        self.meshTableHeaderLabelC = babylonMayaUI.buildLabelA(self.infoDock,390,230,100,20,12,'texture','#222222','#eeeeee')
        
        self.meshTableHeaderLabelD = babylonMayaUI.buildLabelA(self.infoDock,575,230,300,20,12,'copy diffuse to pass','#222222','#eeeeee')
        
        self.meshTableHeaderLabelD = babylonMayaUI.buildLabelA(self.infoDock,720,230,50,20,12,'from','#222222','#eeeeee')
        self.meshTableHeaderLabelE = babylonMayaUI.buildLabelA(self.infoDock,770,230,50,20,12,'Loop','#222222','#eeeeee')
        self.meshTableHeaderLabelF = babylonMayaUI.buildLabelA(self.infoDock,820,230,50,20,12,'to','#222222','#eeeeee')

        #self.meshTableHeaderCheckE = babylonMayaUI.buildLabelA(self.infoDock,380,230,100,20,12,'texture','#222222','#eeeeee')
        #self.meshTableHeaderCheckF = babylonMayaUI.buildLabelA(self.infoDock,380,230,100,20,12,'texture','#222222','#eeeeee')

        self.meshItemTable = babylonMayaUI.buildInfoTable(self.infoDock,'tableName',10,250,900,750,14)

        self.meshItemTable.itemClicked.connect(self.meshInfo)  


        ### build  attribute info table
        self.itemAttrInfoTable = babylonMayaUI.buildAttrInfoTable(self.infoDock,'tableName',920,250,300,750,12,20,150,130,50)




        ### build optionCheck def buildCheckBoxA(parent,x,y,w,h,fontScale,checkDescText):

        self.delProducerCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,830,60,300,30,14,'delete Producer')
        self.delLightCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,830,80,300,30,14,'delete Light')
        self.delGravityCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,830,100,300,30,14,'delete Gravity')
        self.delSoundsCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,830,120,300,30,14,'delete Sounds')
        self.delMetadataCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,830,140,300,30,14,'delete Metadata')


        ### build optionCheck for transform ani
        self.bakeTransformAnimationCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,1000,60,300,30,14,'bake transform')
        self.bakeTransformAnimationCheckBox.setChecked(False)  
        self.exportSelectObjCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,1000,80,300,30,14,'export select object')
        self.exportSelectObjCheckBox.setChecked(False)  

        ### connect by sign

        self.getBabylonFileBtn.clicked.connect(self.clickSelBabylonFileBtn)  

        ### error message
        self.errorMsgLabel = babylonMayaUI.buildLabelA(self.infoDock,10,1040,1060,22,14,'','#aaaaaa','#111111')
        #self.errorMsgLabel.setText('aaaaaaaaaaaaaaaaaaa')
        ### initial data
        self.meshAttrDataList = [
                ##{'ln':'bb_name','dataType':'string','keyable':False,'dafaultValue':''},
                ##{'ln':'bb_id','dataType':'string','keyable':False,'dafaultValue':''},
                ##{'ln':'bb_materialId','dataType':'string','keyable':False,'dafaultValue':''},
                {'ln':'bb_mesh_isEnabled','dataType':'enum','keyable':True,'dafaultValue':'true','options':"true:false"},
                {'ln':'bb_mesh_isVisible','dataType':'enum','keyable':True,'dafaultValue':'true','options':"true:false"},
                {'ln':'bb_mesh_hasVertexAlpha','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_mesh_receiveShadows','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_mesh_infiniteDistance','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_mesh_billboardMode','dataType':'mode','keyable':True,'dafaultValue':'0','options':"0:1:2:3:4:5:6:7:8:9:10:11:12"},
                {'ln':'bb_mesh_visibility','dataType':'float','keyable':True,'dafaultValue':1.0},
              ##  {'ln':'bb_mesh_instances','dataType':'string','keyable':False,'dafaultValue':''},
              ##  {'ln':'bb_mesh_skeletonId','dataType':'float','keyable':False,'dafaultValue':-1},
              ##  {'ln':'bb_mesh_numBoneInfluencers','dataType':'float','keyable':False,'dafaultValue':4},
                {'ln':'bb_mesh_applyFog','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
              ##  {'ln':'bb_mesh_actions','dataType':'string','keyable':False,'dafaultValue':''},
                {'ln':'bb_mesh_checkCollisions','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_mesh_pickable','dataType':'enum','keyable':True,'dafaultValue':'true','options':"true:false"},
                {'ln':'bb_mesh_showBoundingBox','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_mesh_showSubMeshesBoundingBox','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
               ## {'ln':'bb_mesh_alphaIndex','dataType':'float','keyable':True,'dafaultValue':1000.0},
              ##  {'ln':'bb_mesh_parentId','dataType':'string','keyable':False,'dafaultValue':''},
              ##  {'ln':'bb_mesh_animations','dataType':'string','keyable':False,'dafaultValue':''},
                {'ln':'bb_mesh_autoAnimate','dataType':'enum','keyable':True,'dafaultValue':'true','options':"true:false"},
                {'ln':'bb_mesh_autoAnimateFrom','dataType':'float','keyable':True,'dafaultValue':0.0},
                {'ln':'bb_mesh_autoAnimateTo','dataType':'float','keyable':True,'dafaultValue':200.0},
                {'ln':'bb_mesh_autoAnimateLoop','dataType':'enum','keyable':True,'dafaultValue':'true','options':"true:false"},
               ## {'ln':'bb_mesh_metadata','dataType':'string','keyable':False,'dafaultValue':''},    
                {'ln':'bb_Material_alphaMode','dataType':'mode','keyable':True,'dafaultValue':'combine','options':"none:Add:Combine:Subtract:Multipy:Maximized:One one: Pre-multiplied"},
                {'ln':'bb_Material_alpha','dataType':'float','keyable':True,'dafaultValue':1.0},
                {'ln':'bb_Material_useLightmapAsShadowmap','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_Material_useSpecularOverAlpha','dataType':'enum','keyable':True,'dafaultValue':'true','options':"true:false"},
                {'ln':'bb_Material_disableLighting','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_Material_useEmissiveAsIllumination','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_Material_linkEmissiveWithDiffuse','dataType':'enum','keyable':True,'dafaultValue':'true','options':"true:false"},
                {'ln':'bb_Material_twoSidedLighting','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_Material_useGlossinessFromSpecularMapAlpha','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_Material_alphaCutOff','dataType':'float','keyable':True,'dafaultValue':0.5},
                {'ln':'bb_Material_maxSimultaneousLights','dataType':'float','keyable':True,'dafaultValue':4},
                {'ln':'bb_Material_backFaceCulling','dataType':'enum','keyable':True,'dafaultValue':'true','options':"true:false"},
                {'ln':'bb_Material_wireframe','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},

      
      
            ]
        #print self.meshAttrDataList
        self.currentMeshList = []
        self.currentMaterialList = []
      
    def testFun(self):
        print ("test test test")
        #self.updateMaterialUVFromMaya()
        self.updateMeshTranslateFromMaya()
        
    def exportBabylonFileB(self):

        exportFileName = self.exportBabylonFileName.text()
        
        #print exportFileName



    def setExportDirFn(self):

        basicFilter = "*.babylon"
        openBabylonFile = cmds.fileDialog2(caption="get babylon file",fileFilter=basicFilter, dialogStyle=2,fm=0)[0]
        #self.getBabyLonFileNameInputBox 
       # self.babylonFileInputBox.setText(openBabylonFile)
       # exportBabylonFileName = openBabylonFile.split('.babylon')[0] +'_mod.babylon'
        self.exportBabylonFileName.setText(openBabylonFile)



        
        # = self.exportBabylonFileName.text()


    def exportBabylonFile(self):
        print 'exportBabylonFile'
 
        exportFileName =  self.exportBabylonFileName.text()



        self.getTextureData()
        self.getAllMeshAnimationData()
        
        
        
        self.delCheckedInfo()
        self.copyPassToSelPass()
        
        #print self.babylonFile
        writeData = json.dumps(self.babylonFile, sort_keys=True , indent =4) 
        #writeData = json.dumps(exportData) 
        with open(exportFileName, 'w') as the_file:
            the_file.write(writeData)  
            
        
            
    def delCheckedInfo(self):
        print ('delCheckedInfo')
           
                  
        if self.delProducerCheckBox.isChecked() == True:
            #del self.babylonFile['producer']
            try:
                self.babylonFile.pop("producer")
            except:
                pass
           # self.babylonFile['producer'] = []
        if self.delLightCheckBox.isChecked() == True:
            #del self.babylonFile['lights']
            try:
                self.babylonFile.pop("lights")
            except:
                pass
           # self.babylonFile['lights'] = []

        if self.delGravityCheckBox.isChecked() == True:
           # del self.babylonFile['gravity']
            try:
                self.babylonFile.pop("gravity")
            except:
                pass
           # self.babylonFile['gravity'] = []

        if self.delSoundsCheckBox.isChecked() == True:
            #del self.babylonFile['sounds']
            try:
                self.babylonFile.pop("sounds")
            except:
                pass
            #self.babylonFile['sounds'] = []

        if self.delMetadataCheckBox.isChecked() == True:
            #del self.babylonFile['metadata']
            try:
                self.babylonFile.pop("metadata")
            except:
                pass
            #self.babylonFile['sounds'] = []

        
        
     
    def copyPassToSelPass(self): 
        print ('copyPassToSelPass')
        #self.meshItemTable.item(3,1).text()
        rowCount =  self.meshItemTable.rowCount()
        babylonMeshData = self.babylonFile['meshes']

       # print rowCount 
        for i in range(0,rowCount):
            if self.meshItemTable.cellWidget(i,4).isChecked() == True:
                selMeshName = self.meshItemTable.cellWidget(i,4).toolTip()
                currentMeshData = filter(lambda x:x['name'] == selMeshName,babylonMeshData)[0]
                materialID = currentMeshData['materialId']
                materialData =  filter(lambda x:x['id'] == materialID,self.babylonFile['materials'])[0]
                materialData['opacityTexture'] = materialData['diffuseTexture']
               # print 'copy diffuse to opacity',materialData
            if self.meshItemTable.cellWidget(i,5).isChecked() == True:
                selMeshName = self.meshItemTable.cellWidget(i,5).toolTip()
                currentMeshData = filter(lambda x:x['name'] == selMeshName,babylonMeshData)[0]
                materialID = currentMeshData['materialId']
                materialData =  filter(lambda x:x['id'] == materialID,self.babylonFile['materials'])[0]
                materialData['ambientTexture'] = materialData['diffuseTexture']

                #print 'copy diffuse to ambiment',materialData
            if self.meshItemTable.cellWidget(i,6).isChecked() == True:
                
                selMeshName = self.meshItemTable.cellWidget(i,6).toolTip()
                currentMeshData = filter(lambda x:x['name'] == selMeshName,babylonMeshData)[0]
                materialID = currentMeshData['materialId']
                materialData =  filter(lambda x:x['id'] == materialID,self.babylonFile['materials'])[0]
                materialData['emissiveTexture'] = materialData['diffuseTexture']

               # print 'copy diffuse to emissive',materialData


    def getTextureData(self):
        print ('fixTextureData')
        babylonMeshData = self.babylonFile['meshes']
        
        #print  '11111111111111111111111111111111111111',self.currentMeshList
        for mesh in self.currentMeshList:
            currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
            meshName = cmds.ls(mesh,dag=2,typ='mesh')[0]
            shadingGrps = cmds.listConnections(meshName ,type='shadingEngine')[0]
            shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
            fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0] 
            attachmentName = cmds.getAttr("%s.fileTextureName" %fileNode).split('/')[-1]#.split('.')[0]
            
            materialID = currentMeshData['materialId']
            materialData =  filter(lambda x:x['id'] == materialID,self.babylonFile['materials'])[0]
           # print 'materialData',materialData
           # print 'attachmentName',attachmentName
            
            #### fix material texture file
            materialData['diffuseTexture']['name'] = attachmentName

           # materialData = 
     
            
    def getAllMeshAnimationData(self):  ###  function, get all meshes animation data
        self.getAlphaGainMod()  ### call alpha gain as visibility
        self.updateMaterialValueFromMaya()
        self.updateMaterialUVFromMaya()
       # self.updateMeshTranslateFromMaya()
        
  
    
  

        
        
        
        
        
    def getAlphaGainMod(self):   ### function get alphaGain , visibility animation
       # print 'currentMeshList_______________1111111111111111111111',self.currentMeshList
        print 'getAlphaGainMod'
        babylonMeshData = self.babylonFile['meshes']
        for mesh in self.currentMeshList:
            currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
            try:
                currentMeshAniData = currentMeshData['animations']
              #  
              #  print 'aaaaaaaaaaaaaaaa'
            except:
                currentMeshAniData.append({'animations':[]})
              #  print 'bbbbbbbbbbbbbbb'

                
           # print '12341232144123213213213',mesh,currentMeshAniData

        #cmds.getAttr('DB_E_N_CrackBlack.bb_visibility',t = 15)
      #  for meshData in self.babylonFile['meshes']:
            #print meshData['name']
           # meshData['animations']
            #meshName = meshData['name']
            # '11111111111111111111111111111111111111111111111111'
            ###remove visibility Animation dict
            try:
                currentMeshVisibilityAniData = filter(lambda x:x['name'] ==  "visibility animation" , currentMeshAniData)[0]  ### get mesh visibility ani data
                currentMeshAniData.remove(currentMeshVisibilityAniData)
                currentMeshAniData.append(
                                {
                                    "name": "visibility animation",
                                    "property": "visibility",
                                    "dataType": 0,
                                    "enableBlending": False,
                                    "blendingSpeed": 0.01,
                                    "loopBehavior": 1,
                                    "framePerSecond": int(self.fps),
                                    "keys":["%s"%mesh]
                                    
                                }  
                    
                            )
              #  print "77777777777777777777777"
            except:
                currentMeshAniData.append(
                                {
                                    "name": "visibility animation",
                                    "property": "visibility",
                                    "dataType": 0,
                                    "enableBlending": False,
                                    "blendingSpeed": 0.01,
                                    "loopBehavior": 1,
                                    "framePerSecond": int(self.fps),
                                    "keys":[]
                                    
                                }  
                    
                            )
                
                
                
                
               # print "99999999999999999999999"
                pass
                
            ### add visibility Animaiton Dict to BB babylonMeshData
            
            #try:
            
           # except:
            #    pass
                
            
            
            try:
                
                
                currentMeshVisibilityAniData = filter(lambda x:x['name'] ==  "visibility animation" , currentMeshAniData)[0]  ### get mesh visibility ani data
              #  print '22222222222222222222222',currentMeshVisibilityAniData
                #try:
                keyFrameList_selBb_vis = cmds.keyframe(mesh,query=True, at= 'bb_mesh_visibility')
                   # print cmds.keyframe('DB_S_N_battlefieldObject',query=True, at= 'bb_mesh_visibility')
                #print 'aaaaasdasdsdasdsdsdsd',keyFrameList_selBb_vis
               # except:
                    
                  #  keyFrameList_selBb_vis = []
               # print '3333333333333333333333333333',mesh,keyFrameList_selBb_vis
               
                if keyFrameList_selBb_vis == None:
                   # print 'gggggggggggggggggggggggggggggggggggg' 
                    
                    keyValue = float('%.3f'%(cmds.getAttr('%s.bb_mesh_visibility'%mesh,t = 1)))
                    initianVisFrameValue = [{"frame":1.0,"values": [keyValue]}]
                    currentMeshVisibilityAniData['keys'] = initianVisFrameValue
                    
                    
                if len(keyFrameList_selBb_vis) > 0:
                    keyValue_visAniList =[]
                    for f in keyFrameList_selBb_vis:
                        keyValue = float('%.3f'%(cmds.getAttr('%s.bb_mesh_visibility'%mesh,t = f)))
                      #  print '4444444444444444444444444444',mesh,f,keyValue
                        keyValue_visAniList.append({"frame":f,"values": [keyValue]})    
                        
                    sortedkeyValue_visAniList = list(sorted(keyValue_visAniList, key = lambda x: int(x['frame'])))
                   # print '55555555555555555',mesh,sortedkeyValue_visAniList

                    currentMeshVisibilityAniData['keys'] = sortedkeyValue_visAniList
                   # print '666666666',mesh,currentMeshVisibilityAniData
                #elif keyFrameList_selBb_vis == None:
              #  else:
                 #   print 'gggggggggggggggggggggggggggggggggggg'
                  #  keyValue = float('%.3f'%(cmds.getAttr('%s.bb_mesh_visibility'%mesh,t = 1)))
                   # initianVisFrameValue = [{"frame":1.0,"values": [keyValue]}]
                  #  currentMeshVisibilityAniData['keys'] = initianVisFrameValue

              #  else:
               #     keyValue = float('%.3f'%(cmds.getAttr('%s.bb_mesh_visibility'%mesh,t = 1)))
                #    initianVisFrameValue = [{"frame":1.0,"values": [keyValue]}]
                #    currentMeshVisibilityAniData['keys'] = initianVisFrameValue

            except:
                pass
                    
            
            
    def updateMaterialUVFromMaya(self):
        babylonMeshData = self.babylonFile['meshes']
        materialsData =  self.babylonFile['materials']
        materialAnimationAttrList = [{'uOffset':'offsetU'},{'vOffset':'offsetV'},{'uScale':'repeatU'},{'vScale':'repeatV'},{'wAng':'rotateFrame'}]
        angelAttrList = ['wAng']
        
        
        
        
        
        for mesh in self.currentMeshList:
            currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
            currentMeshAniData = currentMeshData['animations']
            materialID = currentMeshData['materialId']
            materialData =  filter(lambda x:x['id'] == materialID,self.babylonFile['materials'])[0]
            materialDiffuseAnimAtionData = materialData['diffuseTexture']['animations']
            meshShapeName = cmds.ls(mesh,dag=2,typ='mesh')[0]
            shadingGrps = cmds.listConnections(meshShapeName ,type='shadingEngine')[0]
            shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
            fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0]
            placementNode = cmds.listConnections('%s.offset'%fileNode,type='place2dTexture')[0] 
           # print 'materialDiffuseAnimAtionData',materialDiffuseAnimAtionData
            ###remove Select Animation list from bb
            try:
                for i in range(0,len(materialAnimationAttrList)):
                    bbAttrName = materialAnimationAttrList[i].keys()[0]
                    
                  #  print 'bbAttrName',bbAttrName
                    try:
                       # materialDiffuseAnimAtionData = filter(lambda x:x['property'] != bbAttrName,materialDiffuseAnimAtionData)[0] 
                       # print 'materialDiffuseAnimAtionData',materialDiffuseAnimAtionData
                        
                        material_ani_Attr = filter(lambda x:x['property'] ==bbAttrName , materialDiffuseAnimAtionData)[0]
                        materialDiffuseAnimAtionData.remove(material_ani_Attr)
                    except:
                        pass
                    materialData['diffuseTexture']['animations'] = materialDiffuseAnimAtionData
            except:
                pass
            
            ###add select animation to bb    
            try:
                for i in range(0,len(materialAnimationAttrList)):
                    bbAttrName = materialAnimationAttrList[i].keys()[0]
                    mayaAttrName = materialAnimationAttrList[i][bbAttrName]
                    if bbAttrName == 'wAng':
                        attr_startFrameValue = cmds.getAttr('%s.%s'%(placementNode,mayaAttrName),t=1)
                        initSelAttrValueFromMayaObj = (((attr_startFrameValue%360))*math.pi)/180.0
                                
                    else:
                        initSelAttrValueFromMayaObj = cmds.getAttr('%s.%s'%(placementNode,mayaAttrName) ,t = 1)
                        material_Ani_Attr= {
                                "blendingSpeed": 0.01, 
                                "dataType": 0, 
                                "enableBlending": False, 
                                "framePerSecond": int(self.fps), 
                                "keys":[
                                        {
                                        "frame": 1.0, 
                                        "values": [
                                            float('%.3f'%initSelAttrValueFromMayaObj)
                                        ]
                                        }                                 
                                        ],  
                                "loopBehavior": 1, 
                                "name": "%s animation"%bbAttrName, 
                                "property": "%s"%bbAttrName
                                        } 
                        materialData['diffuseTexture']['animations'].append(material_Ani_Attr)
            except:
                pass
                
                
                
            ### get attribute value from maya and add dict to bb
           # try:
            for i in range(0,len(materialAnimationAttrList)):
                bbAttrName = materialAnimationAttrList[i].keys()[0]
                mayaAttrName = materialAnimationAttrList[i][bbAttrName]
                attr_DataList = []

                try:
                    selAttrKeyFrameListFromMayaObj = cmds.keyframe(placementNode,at = mayaAttrName,q=True)  
                   # print '11111111111111111111111',mayaAttrName,selAttrKeyFrameListFromMayaObj
                    if len(selAttrKeyFrameListFromMayaObj) >0:
                        for f in selAttrKeyFrameListFromMayaObj:
                            attr_SelFrameValue = cmds.getAttr('%s.%s'%(placementNode,mayaAttrName),t=f)
                           # print 'bbAttrName' ,bbAttrName
                            if bbAttrName == 'wAng' :
                                
                                angleValueTrans = (((attr_SelFrameValue%360))*math.pi)/180.0
                                
                                attr_DataList.append({"frame":f,"values":[float('%.3f'%angleValueTrans)]})

                            else:
                                
                                attr_DataList.append({"frame":f,"values":[float('%.3f'%attr_SelFrameValue)]})
                            
                        selMaterial_ani_Attr = filter(lambda x:x['property'] == bbAttrName,materialData['diffuseTexture']['animations'])[0]
                        selMaterial_ani_Attr['keys'] = attr_DataList

                 
                    
                except:
                    pass
              
                
                    
                
                
                   # bbAttrName = attr.keys[]
                   # material_ani_offestU = filter(lambda x:x['property'] == 'uOffset',materialDiffuseAnimAtionData)[0]
            
           # materialDiffuseAnimAtionData = 
            
           # print 'materialDiffuseAnimAtionData',materialDiffuseAnimAtionData
           
     

    def updateMeshTranslateFromMaya(self):
        print ('updateMeshTranslateFromMaya')
        

        frameStart = self.startFrameInput.text()
        frameEnd = self.endFrameInput.text()
 
        meshCountInBB = len(self.currentMeshList)
        babylonMeshData = self.babylonFile['meshes']


     
        ##check if object freeze in bb
        for mesh in self.currentMeshList:
           # print mesh
            x0 = cmds.getAttr('%s.translateX'%mesh,t=0)
            y0 = cmds.getAttr('%s.translateY'%mesh,t=0)
            z0 = cmds.getAttr('%s.translateZ'%mesh,t=0)
            rx0 = cmds.getAttr('%s.rotateX'%mesh,t=0)
            ry0 = cmds.getAttr('%s.rotateY'%mesh,t=0)
            rz0 = cmds.getAttr('%s.rotateZ'%mesh,t=0)
            sx0 = cmds.getAttr('%s.scaleX'%mesh,t=0)
            sy0 = cmds.getAttr('%s.scaleY'%mesh,t=0)
            sz0 = cmds.getAttr('%s.scaleZ'%mesh,t=0)
         #   print x0,y0,z0 ,rx0,ry0,rz0,sx0,sy0,sz0
            if [x0,y0,z0 ,rx0,ry0,rz0,sx0,sy0,sz0] == [0.0 ,0.0 ,0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0]:
                pass
               # print x0,y0,z0 ,rx0,ry0,rz0,sx0,sy0,sz0
            else:
                self.errorMsgLabel.setText('meshes in BB not freeze')

   
        
        
        
        ###remove Select mesh Animation list from bb
        #transformAttrList = [{'position':'translate'},{'scaling':'scale'},{'rotationQuaternion':'rotate'}]
        transformAttrList = [{'position':'translate'},{'scaling':'scale'}]

        try:
           # print '333333333333333333333333333333333333',self.currentMeshList
            for mesh in self.currentMeshList:
                currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
                currentMeshAniData = currentMeshData['animations']

                
                for i in  range(0,len(transformAttrList)):
                    bbTransAttrName = transformAttrList[i].keys()[0]

                    try:
                        mesh_ani_AttrList = filter(lambda x:x['property'] ==bbTransAttrName , currentMeshAniData)[0]
                       # print '111111111111111111111111111111111111111111',mesh_ani_AttrList
                        currentMeshAniData.remove(mesh_ani_AttrList)
                    
                    except:
                        pass
                        
                   # print '111111111111122222222222222222222222222222222',mesh,bbTransAttrName,mest_ani_AttrList

                '''
                    print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',i,bbTransAttrName,mest_ani_AttrList
                
                    
                   # print 'mest_ani_AttrList',bbTransAttrName,mest_ani_AttrList

                '''
                ###modify all mesh animaiton from to
                #cmds.keyframe(mesh,q=True)
   



        except:
           # print "no sel transform anim dict"
            self.errorMsgLabel.setText( 'no transform animation for mesh in bb')
           # pass
            
            
            
        ###add animation Dict to bb
        
        for mesh in self.currentMeshList:
            currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
            currentMeshAniData = currentMeshData['animations']
            currentMeshData['metadata'] = {}
            try:
                allKeyFrameSelMeshFromMaya = list(dict.fromkeys(cmds.keyframe(mesh,q=True)))
                meshKeyFrom = 0
                meshKeyTo = allKeyFrameSelMeshFromMaya[-1]
                currentMeshData['autoAnimateFrom'] = 1
                currentMeshData['autoAnimateTo'] = meshKeyTo
            except:
                pass
    
        
            for i in  range(0,len(transformAttrList)):
                bbTransAttrName = transformAttrList[i].keys()[0]
                mayaAttrName =  transformAttrList[i][bbTransAttrName]
                print 'mayaAttrName',mayaAttrName
                        
                mesh_ani_AttrList =  {
                                        "name": "%s animation"%bbTransAttrName,
                                        "property": "%s"%bbTransAttrName,
                                        "dataType": 1,
                                        "enableBlending": False,
                                        "blendingSpeed": 0.01,
                                        "loopBehavior": 1,
                                        "framePerSecond": int(self.fps), 
                                        "keys": []
                                        }        
                currentMeshAniData.append(mesh_ani_AttrList)   
                
                
          

                 
        '''           
        try:
            for mesh in self.currentMeshList:
                currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
                
                currentMeshAniData = currentMeshData['animations']
                

                for i in  range(0,len(transformAttrList)):
                    bbTransAttrName = transformAttrList[i].keys()[0]
                   # print '1111111111111111111111111111111111111111111111' ,bbTransAttrName   

                    mest_ani_AttrList =  {
                                    "name": "%s animation"%bbTransAttrName,
                                    "property": "%s"%bbTransAttrName,
                                    "dataType": 1,
                                    "enableBlending": False,
                                    "blendingSpeed": 0.01,
                                    "loopBehavior": 1,
                                    "framePerSecond": int(self.fps), 
                                    "keys": []
                                    }
                   
                    currentMeshAniData .append(mest_ani_AttrList)
                   # allKeyFrameSelMeshFromMaya = list(dict.fromkeys(cmds.keyframe(mesh,q=True)))
                    #meshKeyFrom = 1
                   # meshKeyTo = allKeyFrameSelMeshFromMaya[-1]
                   # currentMeshData['autoAnimateFrom'] = 1
                   # currentMeshData['autoAnimateTo'] = meshKeyTo

                   #print 'allKeyFrameSelMeshFromMaya',allKeyFrameSelMeshFromMaya
                  #  print '222222222222222222222222' ,currentMeshAniData   

            #self.errorMsgLabel.setText( 'updateMeshTranslateFromMaya error 06')         
        except:
            self.errorMsgLabel.setText( 'updateMeshTranslateFromMaya error 02 ,add animation Dict to bb')

            #pass
        
        ###add animation value from maya attr to bb mesh animation dict
        '''   
        
      #  for mesh in self.currentMeshList:
        #    cmds.currentTime( 0, edit=True )

        #    currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
        #    currentMeshAniData = currentMeshData['animations']
         #   print '00000000000000000000000000000',mesh
        
        try:
            for mesh in self.currentMeshList:
              #  print '00000000000000000000000000000',mesh

                cmds.currentTime( 0, edit=True )

                currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
                currentMeshAniData = currentMeshData['animations']
                
                
                for i in  range(0,len(transformAttrList)):
                    bbTransAttrName = transformAttrList[i].keys()[0]
                   # print '11111111111111111111111111111111',bbTransAttrName
                    mayaAttrName = transformAttrList[i][bbTransAttrName]
                   # print '22222222222222222222222222222222',mayaAttrName

                    #selAttrKeyFrameListTemp =cmds.keyframe(mesh,at = mayaAttrName,q=True)  
                    try:
                        selAttrKeyFrameList = list(dict.fromkeys(cmds.keyframe(mesh,at = mayaAttrName,q=True)))
                    except:
                        selAttrKeyFrameList = []
                   # print '333333333333333333333333333333333',mesh,bbTransAttrName,mayaAttrName,len(selAttrKeyFrameList)
                    
                    
                    if len(selAttrKeyFrameList) > 0:
                        attrValueList = []
                        for f in selAttrKeyFrameList:
                           # print '2222222222222222222222222222222222222222222222',mesh,bbTransAttrName,mayaAttrName,f,selAttrKeyFrameList,currentFrameAttrValue
                            if bbTransAttrName == "position":
                                currentFrameAttrValue = cmds.getAttr('%s.%s'%(mesh,mayaAttrName),t = f)[0]

                                attrValueList.append({
                                    "frame":f,
                                    "values":[float('%.3f'%currentFrameAttrValue[0]),float('%.3f'%currentFrameAttrValue[1]),-float('%.3f'%currentFrameAttrValue[2])]
                                    })
                                    
                               # print "333333333333333333333333333333333",attrValueList
                            if bbTransAttrName == "scaling":
                                currentFrameAttrValue = cmds.getAttr('%s.%s'%(mesh,mayaAttrName),t = f)[0]

                                attrValueList.append({
                                    "frame":f,
                                    "values":[float('%.3f'%currentFrameAttrValue[0]),float('%.3f'%currentFrameAttrValue[1]),float('%.3f'%currentFrameAttrValue[2])]
                                    })
                               # print "4444444444444444444444444444",attrValueList

                            if bbTransAttrName == "rotationQuaternion":
                                
                                rq = self.getQuatRotation(mesh,f)
                                
                                attrValueList.append({
                                    "frame":f,
                                    "values":[-float('%.3f'%rq[0]),-float('%.3f'%rq[1]),float('%.3f'%rq[2]),float('%.3f'%rq[3])]
                                    })
                            #    pass 
                    
                    if len(selAttrKeyFrameList) == 0: 
                       # print "21212121212"
                        attrValueList = []
                        if bbTransAttrName == "position":
                            currentFrameAttrValue = cmds.getAttr('%s.%s'%(mesh,mayaAttrName),t = 1)[0]

                            attrValueList.append({
                                        "frame":0.0,
                                        "values":[float('%.3f'%currentFrameAttrValue[0]),float('%.3f'%currentFrameAttrValue[1]),-float('%.3f'%currentFrameAttrValue[2])]
                                        })   
                                        
                           # print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",currentFrameAttrValue,attrValueList

                        elif bbTransAttrName == "scaling":
                            currentFrameAttrValue = cmds.getAttr('%s.%s'%(mesh,mayaAttrName),t = 1)[0]

                            attrValueList.append({
                                "frame":0.0,
                                "values":[float('%.3f'%currentFrameAttrValue[0]),float('%.3f'%currentFrameAttrValue[1]),float('%.3f'%currentFrameAttrValue[2])]
                                })               
                           
                           # print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",currentFrameAttrValue,attrValueList
             
                        elif bbTransAttrName == "rotationQuaternion":
                          #  print "cccccccccccccccccccccccccccccccccccccccccccc"
                            rq = self.getQuatRotation(mesh,0)
                            
                            attrValueList.append({
                                "frame":0.0,
                                "values":[-float('%.3f'%rq[0]),-float('%.3f'%rq[1]),float('%.3f'%rq[2]),float('%.3f'%rq[3])]
                                })                
                                    
                        
                    else:
                        self.errorMsgLabel.setText( 'updateMeshTranslateFromMaya error 04 ,no keys for select mesh attribute')
                        
                    mesh_ani_AttrList = filter(lambda x:x['property'] ==bbTransAttrName , currentMeshAniData)[0]
                  #  print '77777777777777777777',mesh_ani_AttrList

                    sortedAttrValueList = list(sorted(attrValueList, key = lambda x: int(x['frame'])))
                    mesh_ani_AttrList['keys'] = sortedAttrValueList
                  #  print '88888888888888888888888',sortedAttrValueList

                    
        except:
            self.errorMsgLabel.setText( 'updateMeshTranslateFromMaya error 03 ,add animation value from maya attr to bb mesh animation dict')
        
       # cmds.getAttr('DB_E_N_FreezePlan_A.rotate')

        
        
        
        
        


    def updateMeshTranslateFromMayaB(self):
        print "updateMeshTranslateFromMaya"
        babylonMeshData = self.babylonFile['meshes']
        materialsData =  self.babylonFile['materials']
        #print len(self.currentMeshList)
        for mesh in self.currentMeshList:

            #print mesh
            meshDataSel = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
            meshAniData = meshDataSel['animations']
            try:
                meshPositionAniData = filter(lambda x:x['name'] == "position animation",meshAniData)[0]
            except:
                meshPositionAniData = {}
            try:
                meshScaleAniData = filter(lambda x:x['name'] == "scaling animation",meshAniData)[0]
                
            except:
                meshScaleAniData = {}
            try:
                meshRotationAniData = filter(lambda x:x['name'] == "rotationQuaternion animation",meshAniData)[0]
                try:
                    
                    rotationKeyFrameList = sorted(list(dict.fromkeys(cmds.keyframe(mesh,at = 'rotate' ,q=True))))
                    minFrame = int(rotationKeyFrameList[0])
                    maxFrame = int(rotationKeyFrameList[-1]) +1
                    cmds.currentTime( 0, edit=True )    
                    rotationQuatData = [] 
                   # print minFrame,maxFrame
                    #self.getQuatRotation(mesh,1)
                    for i in range(minFrame,maxFrame):
                       # print i
                        rq = self.getQuatRotation(mesh,i)
                       # print rq
                        #rotationQuatData.append({str(i):['%.3f'%rq[0],'%.3f'%rq[1],'%.3f'%rq[2],'%.3f'%rq[3]]})      
                     
                        rotationQuatData.append({"frame":i,"values":[-float('%.3f'%rq[0]),-float('%.3f'%rq[1]),float('%.3f'%rq[2]),float('%.3f'%rq[3])]})      
                    meshRotationAniData['keys'] = rotationQuatData
                  #  print 'rotationQuatData',rotationQuatData
                  #  print 'rotationKeyFrameList',rotationKeyFrameList
                except:
                    keyValue_RSList = []
                    rqS = self.getQuatRotation(mesh,int(self.startFrameInput.text()))
                    rqS_value =[-float('%.3f'%rqS[0]),-float('%.3f'%rqS[1]),float('%.3f'%rqS[2]),float('%.3f'%rqS[3])]    
                    rqE = self.getQuatRotation(mesh,int(self.endFrameInput.text()))
                    rqE_value =[-float('%.3f'%rqE[0]),-float('%.3f'%rqE[1]),float('%.3f'%rqE[2]),float('%.3f'%rqE[3])]    
                    keyValue_RSList.append({"frame":float(self.startFrameInput.text()),"values": rqS_value})
                    keyValue_RSList.append({"frame":float(self.endFrameInput.text()),"values":rqE_value})


                    meshRotationAniData = {
                        "blendingSpeed": 0.01, 
                        "dataType": 2, 
                        "enableBlending": False, 
                        "framePerSecond": int(self.fps), 
                        "keys": keyValue_RSList, 
                        "loopBehavior": 1, 
                        "name": "rotationQuaternion animation", 
                        "property": "rotationQuaternion"                            
                    }

            except:
                
                keyValue_RSList = []
                rqS = self.getQuatRotation(mesh,self.startFrameInput.text())
                rqS_value =[-float('%.3f'%rqS[0]),-float('%.3f'%rqS[1]),float('%.3f'%rqS[2]),float('%.3f'%rqS[3])]    
                rqE = self.getQuatRotation(mesh,int(self.endFrameInput.text()))
                rqE_value =[-float('%.3f'%rqE[0]),-float('%.3f'%rqE[1]),float('%.3f'%rqE[2]),float('%.3f'%rqE[3])]    
                keyValue_RSList.append({"frame":float(self.startFrameInput.text()),"values": rqS_value})
                keyValue_RSList.append({"frame":float(self.endFrameInput.text()),"values":rqE_value})


                meshRotationAniData = {
                    "blendingSpeed": 0.01, 
                    "dataType": 2, 
                    "enableBlending": False, 
                    "framePerSecond": int(self.fps), 
                    "keys": keyValue_RSList, 
                    "loopBehavior": 1, 
                    "name": "rotationQuaternion animation", 
                    "property": "rotationQuaternion"                            
                }
                
               # meshRotationAniData = {}
              #  pass
                
           # print 'meshPositionAniData',meshPositionAniData
           # print 'meshScaleAniData',meshScaleAniData
           # print 'rotationQuatData',rotationQuatData
            #print 'meshRotationAniData',meshRotationAniData

        
        #for i in range(1,30):
        #    rq = getQuatRotation('A',i)
        #    rotationQuatData.append({str(i):['%.3f'%rq[0],'%.3f'%rq[1],'%.3f'%rq[2],'%.3f'%rq[3]]})    
                   
                    
           # meshName = cmds.ls(mesh,dag=2,typ='mesh')[0]
        
    def getQuatRotation(self,mesh,f):
     #   print 'getQuatRotation',mesh,f
        frame = float(f)
        cmds.currentTime( frame, edit=True )
        #make  a object of type MObject
        obj=OpenMaya.MObject()
        

        #make a object of type MSelectionList
        selList=OpenMaya.MSelectionList()

        #add something to it
        #you could retrieve this form function or the user selection
        selList.add(mesh)

        #fill in the MObject
        selList.getDependNode(0,obj)
       # print 'a2222222222222222222222222'

        
        
        try:
            
            if (obj.hasFn(OpenMaya.MFn.kTransform)):
              #then we can add it to transfrom Fn
              #Fn is basically the collection of functions for given objects
                xform=OpenMaya.MFnTransform(obj)
                  #now the api requires pointer types
                x = OpenMaya.MScriptUtil().asDoublePtr()
                z = OpenMaya.MScriptUtil().asDoublePtr()

                y = OpenMaya.MScriptUtil().asDoublePtr()
                w = OpenMaya.MScriptUtil().asDoublePtr()
             #   print x,y,z,w
                #we are ready to ask the values
                xform.getRotationQuaternion(x,y,z,w)
                #convert them back to normal python floats
                x = OpenMaya.MScriptUtil().getDouble(x)
                y = OpenMaya.MScriptUtil().getDouble(y)
                z = OpenMaya.MScriptUtil().getDouble(z)
                w = OpenMaya.MScriptUtil().getDouble(w)
        except:
            print "not transform"
            x = 0
            y = 0
            z = 0
            w = 0
            
        return [x,y,z,w]
        
  

            
    def updateMaterialValueFromMaya(self):  #### updata self.babylonFile from maya mesh
        #print ('updateMaterialValueFromMaya')
        #self.currentMeshList 
        #self.currentMaterialList
        babylonMeshData = self.babylonFile['meshes']
        materialsData =  self.babylonFile['materials']
        for mesh in self.currentMeshList :
            meshDataSel = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
            materialId = meshDataSel['materialId']
            materialDataSel = filter(lambda x:x['id'] == materialId,materialsData)[0]    
        
            for i in self.meshAttrDataList:
                longName = i['ln']
                dataType = i['dataType']

                attrMode = longName.split('_')[1]
                babylonAttrName = longName.split('_')[2]
                #print attrMode
                if attrMode == 'mesh':
                    currentBBMeshAttrValueFromMaya = cmds.getAttr('%s.%s'%(mesh,longName))

                    if dataType == 'enum':
                        if int(currentBBMeshAttrValueFromMaya) == 0:
                            mataToBBValue = True
                        elif  int(currentBBMeshAttrValueFromMaya) == 1:
                            mataToBBValue = False
                    elif dataType == 'mode':        
                        mataToBBValue = int(currentBBMeshAttrValueFromMaya)   
                        
                         
                    elif dataType == 'float':
                        mataToBBValue = float(currentBBMeshAttrValueFromMaya)
                            
                    elif dataType == 'string':
                        mataToBBValue = str(currentBBMeshAttrValueFromMaya)
                   # else:
                    #setAttr "DB_E_N_CrackBlack.bb_mesh_showSubMeshesBoundingBox" 1;
                  #  cmds.setAttr('%s.%s'%(mesh,longName),currentBBMeshAttrValue)
                    #print ('mesh',mesh,longName,dataType,currentBBMeshAttrValueFromMaya)
                    meshDataSel[babylonAttrName] = mataToBBValue

                    #getAttrValueFromBBF = self.babylonFile['meshes']
                elif attrMode == 'Material':
                    currentBBMaterialAttrValueFromMaya = cmds.getAttr('%s.%s'%(mesh,longName))
                    if dataType == 'enum':
                        if int(currentBBMaterialAttrValueFromMaya) == 0:
                            mataToBBValue = True
                        elif  int(currentBBMaterialAttrValueFromMaya) == 1:
                            mataToBBValue = False
                    elif dataType == 'mode':        
                        mataToBBValue = int(currentBBMaterialAttrValueFromMaya)   
                        
                    elif dataType == 'float':
                        mataToBBValue = float(currentBBMaterialAttrValueFromMaya)
                            
                    elif dataType == 'string':
                        mataToBBValue = str(currentBBMaterialAttrValueFromMaya)
                        
                    materialDataSel[babylonAttrName] = mataToBBValue
      
                   # cmds.setAttr('%s.%s'%(mesh,longName),currentBBMeshAttrValue)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    def clickSelBabylonFileBtn(self):
        #print ('aaaaaaaaaaaaa')
        #print self.infoDock
        basicFilter = "*.babylon"
        openBabylonFIle = cmds.fileDialog2(caption="get babylon file",fileFilter=basicFilter, dialogStyle=2,fm=1)[0]
        #self.getBabyLonFileNameInputBox 
        self.babylonFileInputBox.setText(openBabylonFIle)
        exportBabylonFileName = openBabylonFIle.split('.babylon')[0] +'_mod.babylon'
        self.exportBabylonFileName.setText(exportBabylonFileName)
               
        try:
            
            with open(openBabylonFIle , 'r') as reader:
                
                self.babylonFile = json.loads(reader.read())
                
                self.meshData = self.babylonFile['meshes']
                meshCount = len(self.meshData)
                self.materialsData =  self.babylonFile['materials']
                materialsCount = len(self.materialsData)
                
                #print materialsData 
                
                self.meshCountEditInput.setText(str(meshCount))
                self.materialCountEditInput.setText(str(materialsCount))
                

                columnCount = 10
                #columnWidth = 50
                
                rowCount = meshCount
                rowHeight = 25
                self.meshItemTable.setColumnCount(columnCount)
                self.meshItemTable.setRowCount(rowCount)
                self.meshItemTable.setColumnWidth(0, 20)
                self.meshItemTable.setColumnWidth(1, 180)
                self.meshItemTable.setColumnWidth(2, 180)
                self.meshItemTable.setColumnWidth(3, 180)
                self.meshItemTable.setColumnWidth(4, 50)
                self.meshItemTable.setColumnWidth(5, 50)
                self.meshItemTable.setColumnWidth(6, 50)
                self.meshItemTable.setColumnWidth(7, 50)
                self.meshItemTable.setColumnWidth(8, 50)
                self.meshItemTable.setColumnWidth(9, 50)

                for i in range(0,rowCount):
                    meshName = self.meshData[i]['name']
                    materialId = self.meshData[i]['materialId']
                   # print 'meshName',meshName,u'%s'%meshName,type(meshName)
                    self.meshItemTable.setRowHeight(i, rowHeight)
                    self.meshItemTable.setItem(i,0,QtWidgets.QTableWidgetItem())
                    self.meshItemTable.item(i, 0).setText(QtWidgets.QApplication.translate("MainWindow",str(i), None,-1))
                    
                    self.meshItemTable.item(i, 0).setToolTip(QtWidgets.QApplication.translate("MainWindow","SN", None,-1))

                    checkMeshExisted = len(cmds.ls(meshName,typ="transform"))
                    
                    newItem_mesh = QtWidgets.QTableWidgetItem() 
                    newItem_mesh.setText(QtWidgets.QApplication.translate("MainWindow",str(meshName), None,-1)) 
                    
                    
                    

                    
                    
                    
                    if checkMeshExisted == 1:
                        
                        
    
                        newItem_mesh.setForeground(QtGui.QColor(100, 200, 100)) 

                        self.meshItemTable.setItem(i,1,newItem_mesh)

                        

                        if meshName in self.currentMeshList:
                            pass
                        else:
                            self.currentMeshList.append(meshName)
                    else:
    
                        newItem_mesh.setForeground(QtGui.QColor(100, 100, 100)) 

                        self.meshItemTable.setItem(i,1,newItem_mesh)
                    

                    materialDataSel = filter(lambda x:x['id'] == materialId,self.materialsData)[0]
                    selMeshMaterialName = materialDataSel['name']
                    
                    try:
                        textureName =  materialDataSel['diffuseTexture']['name']

                    except:
                        pass
                        
                    checkMaterialExisted = len(cmds.ls(selMeshMaterialName,typ="lambert"))
                    
                    newItem_material = QtWidgets.QTableWidgetItem() 
                    newItem_material.setText(QtWidgets.QApplication.translate("MainWindow",str(selMeshMaterialName), None,-1)) 
                    
    
                        
                    if checkMaterialExisted == 1:
                        
                        
    
                        newItem_material.setForeground(QtGui.QColor(100, 200, 100)) 

                        self.meshItemTable.setItem(i,2,newItem_material)

                        

                        if selMeshMaterialName in self.currentMaterialList:
                            pass
                        else:
                            self.currentMaterialList.append(selMeshMaterialName)
                            
                        try:  
                            meshShapeName = cmds.ls(meshName,dag=2,typ='mesh')[0]
                            shadingGrps = cmds.listConnections(meshShapeName ,type='shadingEngine')[0]
                      #  print shadingGrps


                            shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
                            fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0] 
                            attachmentName = cmds.getAttr("%s.fileTextureName" %fileNode).split('/')[-1]#.split('.')[0]
                            fileSource = cmds.getAttr("%s.fileTextureName" %fileNode)
                                                
                            newItem_texture = QtWidgets.QTableWidgetItem() 
                            newItem_texture.setText(QtWidgets.QApplication.translate("MainWindow",str(attachmentName), None,-1))     
                           # print os.path.isfile(fileSource)
                            if os.path.isfile(fileSource) == True:
                                newItem_texture.setForeground(QtGui.QColor(100, 200, 100)) 
                                self.meshItemTable.setItem(i,3,newItem_texture)
                           # cmds.connectAttr('%s.outAlpha' %newImageFileName, '%s.reflectivity' %newShaderName)
                            else:
                                newItem_texture.setForeground(QtGui.QColor(100, 100, 100)) 

                                self.meshItemTable.setItem(i,3,newItem_texture)

                            opTextCopyCheckBtnItem = babylonMayaUI.buildTableCheckBtnItemA(60,20,14,'D -> O','#223322','#669966','#aaeeaa')
                            opTextCopyCheckBtnItem.setToolTip(meshName)
                            self.meshItemTable.setCellWidget(i, 4, opTextCopyCheckBtnItem)
                            

                            ambientTextCopyCheckBtnItem = babylonMayaUI.buildTableCheckBtnItemA(60,20,14,'D -> A','#223322','#669966','#aaeeaa')
                            ambientTextCopyCheckBtnItem.setToolTip(meshName)
                            self.meshItemTable.setCellWidget(i, 5, ambientTextCopyCheckBtnItem)
                            
                            emisTextCopyCheckBtnItem = babylonMayaUI.buildTableCheckBtnItemA(60,20,14,'D -> E','#223322','#669966','#aaeeaa')
                            emisTextCopyCheckBtnItem.setToolTip(meshName)
                            self.meshItemTable.setCellWidget(i,6, emisTextCopyCheckBtnItem)
           
                            autoAnimateFrom = self.meshData[i]['autoAnimateFrom']
                            autoAnimateLoop = self.meshData[i]['autoAnimateLoop']
                            autoAnimateTo = self.meshData[i]['autoAnimateTo']

                            ### mesh animationFrom
                            autoAnimateFromItem = QtWidgets.QTableWidgetItem() 
                            autoAnimateFromItem.setText(QtWidgets.QApplication.translate("MainWindow",str(autoAnimateFrom), None,-1))     
                            autoAnimateFromItem.setForeground(QtGui.QColor(100, 200, 100)) 
                            self.meshItemTable.setItem(i,7,autoAnimateFromItem)
                            ### mesh animationLoop
                            autoAnimateLoopItem = QtWidgets.QTableWidgetItem() 
                            autoAnimateLoopItem.setText(QtWidgets.QApplication.translate("MainWindow",str(autoAnimateLoop), None,-1))     
                            autoAnimateLoopItem.setForeground(QtGui.QColor(100, 200, 100)) 
                            self.meshItemTable.setItem(i,8,autoAnimateLoopItem)
                            ### mesh animationTo
                            autoAnimateToItem = QtWidgets.QTableWidgetItem() 
                            autoAnimateToItem.setText(QtWidgets.QApplication.translate("MainWindow",str(autoAnimateTo), None,-1))     
                            autoAnimateToItem.setForeground(QtGui.QColor(100, 200, 100)) 
                            self.meshItemTable.setItem(i,9,autoAnimateToItem)                            
                            
                            
    
          
                        except:
                            pass
                            


                    
                        
                            
                            
                        #print fileNode                          
                        
                            
                    else:
    
                        newItem_material.setForeground(QtGui.QColor(100, 100, 100)) 

                        self.meshItemTable.setItem(i,2,newItem_material)
                    

        except:
            pass
    

        
    def meshInfo(self):
        #print ('meshInfo')
        currentItem = self.meshItemTable.currentItem()
       # print currentItem,currentItem.toolTip()
        
        #columnCount = 3
                
        #rowCount = meshCount
        rowHeight = 20
        
        self.itemAttrInfoTable.setColumnCount(2)
        self.itemAttrInfoTable.setRowCount(50)
        for i in range(0,50):
            self.itemAttrInfoTable.setRowHeight(i, rowHeight)

    def delMeshBabylonAttr(self):

        selObjList = cmds.ls( sl=True , type="transform")
        for obj in selObjList:
            attrList = cmds.listAttr(obj)
            bb_attrList =  filter(lambda x:x.split('_')[0] == 'bb',attrList)#[0]
            for attr in bb_attrList:
                cmds.deleteAttr('%s.%s'%(obj,attr))

  

                
            
    def addMeshBabylonAttr(self):
       # cmds.currentTime()
        cmds.currentTime( 0, edit=True )    
        print '323232323223232323',self.currentMeshList
        for mesh in self.currentMeshList:
            #print self.meshAttrDataList
            
            for i in self.meshAttrDataList:
                dataType = i['dataType']
                longName = i['ln']
                keyable = i['keyable']
                dafaultValue = i['dafaultValue']
                try:
                    if dataType == 'string':
                        cmds.addAttr( mesh , ln = longName , sn = longName ,  dt = "string" , k = keyable )
                    elif dataType == 'float':
                        cmds.addAttr( mesh , ln = longName , sn = longName ,  at="float" , dv  =float(dafaultValue) , k = keyable )
                    elif dataType == 'enum':
                        options = i['options']
                        cmds.addAttr(mesh , ln = longName, sn = longName, at = "enum",en=options, k=keyable ) 
                    elif dataType == 'mode':
                        options = i['options']
                        cmds.addAttr(mesh , ln = longName, sn = longName, at = "enum",en=options, k=keyable ) 
                
                except:
                    pass
            babylonMeshData =  self.babylonFile['meshes']
            currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
           # print currentMeshData

            #### connect attribute
            
            try:  
                meshShapeName = cmds.ls(mesh,dag=2,typ='mesh')[0]

                shadingGrps = cmds.listConnections(meshShapeName ,type='shadingEngine')[0]

                shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)

                fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0] 
                cmds.cutKey('%s.alphaGain'%fileNode)
                cmds.connectAttr('%s.bb_mesh_visibility'%mesh, '%s.alphaGain'%fileNode)   
                cmds.pasteKey( mesh, attribute='bb_mesh_visibility' )
                              
            except:
                pass
                
            #### set Attr form babylon file
           # cmds.cutKey( 'pSphere1', time=(0,150), attribute='ffa', option="keys" )
          #  cmds.pasteKey( 'pSphere1', attribute='aav' )


         
               # meshCount = len(self.meshData)
                #self.materialsData =  self.babylonFile['materials']
               # filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
               # self.currentMeshList = []
               # self.currentMaterialList = []
        self.setObjectAttrFromBBF()    
      
        
    def setObjectAttrFromBBF(self):
               
        babylonMeshData = self.babylonFile['meshes']
        materialsData =  self.babylonFile['materials']
        for mesh in self.currentMeshList:
            meshDataSel = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
            materialId = meshDataSel['materialId']
            materialDataSel = filter(lambda x:x['id'] == materialId,self.materialsData)[0]
           # print '22222222222222222222222222222',mesh,materialDataSel
            
            for i in self.meshAttrDataList:
                longName = i['ln']
                dataType = i['dataType']

                attrMode = longName.split('_')[1]
                babylonAttrName = longName.split('_')[2]
                #print attrMode
            
                if attrMode == 'mesh':
                    try:
                        currentBBMeshAttrValue = meshDataSel[babylonAttrName]
                       # print '11111111111111111122222222222333333333',babylonAttrName,currentBBMeshAttrValue
     
                        
                        if dataType == 'enum' :
                            if currentBBMeshAttrValue == True:
                                bbToMayaValue = 0  ### by index number, not booling
                            elif currentBBMeshAttrValue == False:
                                bbToMayaValue = 1
                        elif dataType == 'mode' :
                            bbToMayaValue = int(currentBBMeshAttrValue)
                            
                        elif dataType == 'float' :
                            bbToMayaValue = float(currentBBMeshAttrValue)

                        else: 
                            bbToMayaValue = str(currentBBMeshAttrValue)
                       # else:
                        cmds.setAttr('%s.%s'%(mesh,longName),bbToMayaValue)
                       # print ('mesh',mesh,longName,dataType,currentBBMeshAttrValue)
                       

                        #getAttrValueFromBBF = self.babylonFile['meshes']
                    except:
                        pass
                    
                elif attrMode == 'Material':
                    try:
                        currentBBMaterialAttrValue = materialDataSel[babylonAttrName]
                      #  print '3333333333333333333333333333333333333333',babylonAttrName,currentBBMaterialAttrValue
                   
                        if dataType == 'enum':
                            if currentBBMaterialAttrValue == True:
                                bbToMayaValue = 0
                            elif currentBBMaterialAttrValue == False:
                                bbToMayaValue = 1
                                
                        elif dataType == 'mode' :
                            bbToMayaValue = int(currentBBMaterialAttrValue)
                        elif dataType == 'float' :
                            bbToMayaValue = float(currentBBMaterialAttrValue)

                        else: 
                            bbToMayaValue = str(currentBBMaterialAttrValue)
                       # else:
                        cmds.setAttr('%s.%s'%(mesh,longName),bbToMayaValue)
        
                    except:
                        pass
                            
            
        
        
        
        
def mayaToBabylon_2018Main():
#def main():
    global ui
    app = QtWidgets.QApplication.instance()
    if app == None: app = QtWidgets.QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
    
#if __name__ == '__main__':
#   main()



