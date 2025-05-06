import sys
import maya.OpenMaya as OpenMaya

try:
   # sys.path.append("//mcd-one/database/assets/scripts/python2.7_alpha/22") 
    sys.path.append("D:/my tools/python2.7_alpha/22") 

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
        self.getBBFileBtnGrp =  babylonMayaUI.buildEditWithLabelBtn_stand(self.infoDock,'fileNameLineEdit',10,10,150,650,25,14,'get babylon file name','Get Babylon File','#669966')
       
       
        self.getCharacterFileBtnGrp =  babylonMayaUI.buildEditWithLabelBtn_stand(self.infoDock,'fileNameLineEdit',10,120,150,650,25,14,'get character babylon file name','Get Character File','#669966')

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
        
        self.getChaBabylonFileBtn =self.getCharacterFileBtnGrp[0] 
       # self.getBabyLonFileNameInputBox = self.getBBFileBtnGrp[1] 
        self.chaBabylonFileInputBox =  self.getCharacterFileBtnGrp[1] 
        
        
        ### toolBtn
        self.addMeshAttrBtn = babylonMayaUI.buildOneBtnA(self.infoDock,10,170,200,25,14,'#666666','#666666','add all meshs attributes')
        self.delMeshAttrBtn = babylonMayaUI.buildOneBtnA(self.infoDock,250,170,200,25,14,'#996666','#ff6666','del all meshs attributes')
        self.testABtn = babylonMayaUI.buildOneBtnA(self.infoDock,600,170,150,25,14,'#999966','#ff6666','del Sel Attr')

        self.testABtn.clicked.connect(self.testFun)  


        self.addMeshAttrBtn.clicked.connect(self.addMeshBabylonAttr)  
        self.delMeshAttrBtn.clicked.connect(self.delMeshBabylonAttr)  
        self.exportBabylonDataBtn.clicked.connect(self.exportBabylonFile)  

       # self.getBabylonFileBtn.clicked.connect(self.clickSelBabylonFileBtn)  

        
        ### build get mesh count grp
        self.meshInfoGrp =  babylonMayaUI.buildEditWithLabelA(self.infoDock,'meshCountEdit',450,40,100,20,14,'mesh Count :')
        self.meshCountEditInput =  self.meshInfoGrp[1]
 
        ### build get material count grp
        self.materialInfoGrp =  babylonMayaUI.buildEditWithLabelA(self.infoDock,'materialCountEdit',560,40,100,20,14,'material Count :')
        self.materialCountEditInput = self.materialInfoGrp[1]
       
       
        ### build get Fps grp
        self.fpsInfoGrp =  babylonMayaUI.buildEditWithLabelA(self.infoDock,'fpsEdit',10,40,100,20,14,'FPS :')
        self.fpsEditInput =  self.fpsInfoGrp[1]
        start = str(cmds.playbackOptions( q=True,min=True ))
        end  = str(cmds.playbackOptions( q=True,max=True ))
            
        frameRate =  cmds.currentUnit( query=True, t=True )
        if frameRate == 'film' :
            self.fps = 24.0
        elif  frameRate == 'ntsc' :
            self.fps = 30.0
        elif  frameRate == 'ntscf' :
            self.fps = 60.0    
       
        self.fpsEditInput.setText(str(self.fps)) 

       
        self.startFrameInfoGrp =  babylonMayaUI.buildEditWithLabelA(self.infoDock,'fpsEdit',120,40,100,20,14,'start Frame :')
        self.startFrameInput =  self.startFrameInfoGrp[1]
        self.startFrameInput.setText(start)
       
        self.endFrameInfoGrp =  babylonMayaUI.buildEditWithLabelA(self.infoDock,'fpsEdit',230,40,100,20,14,'end Frame :')

        self.endFrameInput =  self.endFrameInfoGrp[1]
        self.endFrameInput.setText(end)    
        
        self.objScaleInputGrp =  babylonMayaUI.buildEditWithLabelA(self.infoDock,'scaleInputEdit',340,40,100,20,14,'scale :')

        self.objScaleInput =  self.objScaleInputGrp[1]
        self.objScaleInput.setText('1')  


        ### build mesh/material table
       # buildLabelA(parent,x,y,w,h,fontScale,labelText):
        self.meshTableHeaderLabelA = babylonMayaUI.buildLabelA(self.infoDock,30,230,100,20,12,'mesh','#222222','#eeeeee')
        self.meshTableHeaderLabelB = babylonMayaUI.buildLabelA(self.infoDock,210,230,100,20,12,'material','#222222','#eeeeee')
        self.meshTableHeaderLabelC = babylonMayaUI.buildLabelA(self.infoDock,390,230,100,20,12,'texture','#222222','#eeeeee')
        
        self.meshTableHeaderLabelD = babylonMayaUI.buildLabelA(self.infoDock,575,230,300,20,12,'copy diffuse to pass','#222222','#eeeeee')
        
        self.meshTableHeaderLabelE= babylonMayaUI.buildLabelA(self.infoDock,720,230,50,20,12,'from','#222222','#eeeeee')
        self.meshTableHeaderLabelF = babylonMayaUI.buildLabelA(self.infoDock,770,230,50,20,12,'Loop','#222222','#eeeeee')
        self.meshTableHeaderLabelG = babylonMayaUI.buildLabelA(self.infoDock,820,230,50,20,12,'to','#222222','#eeeeee')

        #self.meshTableHeaderCheckE = babylonMayaUI.buildLabelA(self.infoDock,380,230,100,20,12,'texture','#222222','#eeeeee')
        #self.meshTableHeaderCheckF = babylonMayaUI.buildLabelA(self.infoDock,380,230,100,20,12,'texture','#222222','#eeeeee')

        self.meshItemTable = babylonMayaUI.buildInfoTable(self.infoDock,'tableName',10,250,900,750,14)

        self.meshItemTable.itemClicked.connect(self.meshInfo)  


        ### build  attribute info table
        self.itemAttrInfoTable = babylonMayaUI.buildAttrInfoTable(self.infoDock,'tableName',920,250,300,750,12,20,150,130,50)




        ### build optionCheck def buildCheckBoxA(parent,x,y,w,h,fontScale,checkDescText):
        self.setJsonBeauty = babylonMayaUI.buildCheckBoxA(self.infoDock,830,40,300,30,14,'beauty Json format')
        self.setJsonBeauty.setChecked(False)  

        self.delProducerCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,830,60,300,30,14,'delete Producer')
        self.delLightCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,830,80,300,30,14,'delete Light')
        self.delGravityCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,830,100,300,30,14,'delete Gravity')
        self.delSoundsCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,830,120,300,30,14,'delete Sounds')
        self.delMetadataCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,830,140,300,30,14,'delete Metadata')

        self.exportTransformCheck = babylonMayaUI.buildCheckBoxA(self.infoDock,830,180,300,30,14,'export Transform')
        self.exportTransformCheck.setChecked(False)  

        self.exportUVAnuCheck = babylonMayaUI.buildCheckBoxA(self.infoDock,830,200,300,30,14,'export UV Animation')
        self.exportUVAnuCheck.setChecked(False)  



        ### build optionCheck for transform ani
        self.bakeTransformAnimationCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,1000,60,300,30,14,'bake transform')
        self.bakeTransformAnimationCheckBox.setChecked(False)  
        
      #  self.exportSelectObjCheckBox = babylonMayaUI.buildCheckBoxA(self.infoDock,1000,80,300,30,14,'export select object')
        #self.exportSelectObjCheckBox.setChecked(False)  

        self.replaceMaterialWithTheSameTexture = babylonMayaUI.buildCheckBoxA(self.infoDock,1000,120,300,30,14,'replace Material')
        self.replaceMaterialWithTheSameTexture.setChecked(False)  

        self.parentToChaDummy = babylonMayaUI.buildCheckBoxA(self.infoDock,1000,160,300,30,14,'parentTo Character')
        self.parentToChaDummy.setChecked(False)  

        self.combineToOtherFile = babylonMayaUI.buildCheckBoxA(self.infoDock,1000,180,300,30,14,'combine to file')
        self.combineToOtherFile.setChecked(False)  

        self.parentToChaDummy.clicked.connect(self.clickParentChaCheck)   ### load dafault babylon file

        self.combineToOtherFile.clicked.connect(self.clickParentToFileCheck)   ### load dafault babylon file


        self.getBabylonFileBtn.clicked.connect(self.clickSelBabylonFileBtn)   ### load dafault babylon file
        self.getChaBabylonFileBtn.clicked.connect(self.clickSelChaBabylonFileBtn)   ### load dafault babylon file
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
                ##diffuseTexture has alpha
                
                ##use alpha from diffuse texture
                {'ln':'bb_Material_useAlphaFromDiffuseTexture','dataType':'enum','keyable':True,'dafaultValue':'true','options':"true:false"},

                
                {'ln':'bb_Material_useLightmapAsShadowmap','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_Material_useSpecularOverAlpha','dataType':'enum','keyable':True,'dafaultValue':'true','options':"true:false"},
                {'ln':'bb_Material_disableLighting','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_Material_useEmissiveAsIllumination','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_Material_linkEmissiveWithDiffuse','dataType':'enum','keyable':True,'dafaultValue':'true','options':"true:false"},
                {'ln':'bb_Material_twoSidedLighting','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_Material_useGlossinessFromSpecularMapAlpha','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                {'ln':'bb_Material_alphaCutOff','dataType':'float','keyable':True,'dafaultValue':0.5},
                {'ln':'bb_Material_diffuseLevel','dataType':'float','keyable':True,'dafaultValue':1.0},
                {'ln':'bb_Material_OpacityLevel','dataType':'float','keyable':True,'dafaultValue':1.0},

              # {'ln':'bb_Material_maxSimultaneousLights','dataType':'float','keyable':True,'dafaultValue':4},
                {'ln':'bb_Material_backFaceCulling','dataType':'enum','keyable':True,'dafaultValue':'true','options':"true:false"},
               # {'ln':'bb_Material_wireframe','dataType':'enum','keyable':True,'dafaultValue':'false','options':"true:false"},
                ### extra Attribute
                {'ln':'bb_Material_theSameMaterial','dataType':'string','keyable':False,'dafaultValue':'none'},
             #   cmds.addAttr('bg_fog_01', longName='bb_Material_theSameMaterial', dataType="string")

      
            ]
        #print self.meshAttrDataList
        self.currentMeshList = []    ### all mesh name List
        self.currentMaterialList = []
      
      
      #### initial Set


      
      
      
      
      
    def testFun(self):
        print ("test test test")
        
        
        
        selObjList = cmds.ls( sl=True , type="transform")
        for obj in selObjList:
            attrList = cmds.listAttr(obj)
            bb_attrList =  filter(lambda x:x.split('_')[0] == 'bb',attrList)#[0]
            for attr in bb_attrList:
                cmds.deleteAttr('%s.%s'%(obj,attr))
                        
                
                
        
        
        
       # self.checkUsingTheSameTexture()
        
    def clickParentChaCheck(self):
        
        if self.combineToOtherFile.isChecked() == True:
            
            self.combineToOtherFile.setChecked(False)
        
    def clickParentToFileCheck(self):
        if self.parentToChaDummy.isChecked() == True:
            
            self.parentToChaDummy.setChecked(False)



    def setExportDirFn(self):   ### set export dir

        basicFilter = "*.babylon"
        openBabylonFile = cmds.fileDialog2(caption="get babylon file",fileFilter=basicFilter, dialogStyle=2,fm=0)[0]
        #self.getBabyLonFileNameInputBox 
       # self.babylonFileInputBox.setText(openBabylonFile)
       # exportBabylonFileName = openBabylonFile.split('.babylon')[0] +'_mod.babylon'
        self.exportBabylonFileName.setText(openBabylonFile)



        
        # = self.exportBabylonFileName.text()


    def exportBabylonFile(self):
        print 'exportBabylonFile'
        
        self.openBabylonFileFn()
 
        exportFileName =  self.exportBabylonFileName.text()



        getMaterialData = self.getTextureData()
        
        #print 'getMaterialData_______________________1',getMaterialData
        
        self.getAllMeshAnimationData()
        
        
        
        self.delCheckedInfo() #### delect unnecessary data
        
       # self.copyPassToSelPass()  ####  copy diffusse pass to selected pass, opacityTexture, ambientTexture, emissiveTexture
        
        self.checkTexturePassAndBlendMode()   #### 
        
        self.updataAnimationLoop() ## renew animaiton loop
        
        #self.updateUV_animation()
            
        if self.delMetadataCheckBox.isChecked() == True:
            self.clearMetaData()
            
            
        
        if self.replaceMaterialWithTheSameTexture.isChecked() == True:
            self.checkUsingTheSameTexture()
        
        
        self.changeAllMeshScale()
        
        
        #self.simplifyJsonFile()
        
        
        #print self.babylonFile
        #writeData = json.dumps(self.babylonFile, sort_keys=True , indent =4) 
        
        
        
        
        if self.parentToChaDummy.isChecked() == True:
            chaBabylonData = self.combineToChaBabylonFile()
            
            if self.setJsonBeauty.isChecked() == True:
                writeData = json.dumps(chaBabylonData, sort_keys=True , indent =4) 
            else:
                
                writeData = json.dumps(chaBabylonData) 
                
            with open(exportFileName, 'w') as the_file:
                the_file.write(writeData)  
        elif self.combineToOtherFile.isChecked() == True:
            combineBabylonData = self.combineToBabylonFile()
            
            if self.setJsonBeauty.isChecked() == True:
                writeData = json.dumps(combineBabylonData, sort_keys=True , indent =4) 
            else:
                
                writeData = json.dumps(combineBabylonData) 
                
            with open(exportFileName, 'w') as the_file:
                the_file.write(writeData)  
       
        
        else:
        
            if self.setJsonBeauty.isChecked() == True:
                writeData = json.dumps(self.babylonFile, sort_keys=True , indent =4) 
            else:
                
                writeData = json.dumps(self.babylonFile) 
                
            with open(exportFileName, 'w') as the_file:
                the_file.write(writeData)  
       
   
    #def simplifyJsonFile(self):
        #obj = self.babylonFile(String.format("{\"price\": %.2f}", f)
        
        
    def combineToChaBabylonFile(self):
        print 'combineToChaBabylonFile'
        openChaBabylonFile = self.chaBabylonFileInputBox.text()
        
        with open(openChaBabylonFile , 'r') as reader:
                
            chaBabylon = json.loads(reader.read())
         
            #print chaBabylon['meshes']
            #print chaBabylon['materials']
            
           # babylonMeshData = self.babylonFile['meshes']
           # babylonMaterialData =  self.babylonFile['materials']
            #print chaBabylon['meshes'][0]
            if chaBabylon['meshes'][0]['parentId'] == None:
                topDummy = chaBabylon['meshes'][0]['id']

                print topDummy
            
            
            
            for meshData in self.babylonFile['meshes']:
                if meshData.get('normals') is None and meshData.get('tangents') is None and meshData.get('positions') is None:
                    pass
                else:
                    ## check the mesh is dammy
                    meshData['parentId'] = topDummy
                    chaBabylon['meshes'].append(meshData)
                #meshDataSel = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
 
            for materialData in self.babylonFile['materials']:
                chaBabylon['materials'].append(materialData)  
        return chaBabylon
        
        
        
    def combineToBabylonFile(self):
        print 'combineToBabylonFile'
        openChaBabylonFile = self.chaBabylonFileInputBox.text()
        
        with open(openChaBabylonFile , 'r') as reader:
                
            otherBabylon = json.loads(reader.read())
         

            
            
            for meshData in self.babylonFile['meshes']:
               # if meshData.get('normals') is None and meshData.get('tangents') is None and meshData.get('positions') is None:
                    #pass
               # else:
                    ## check the mesh is dammy
               # meshData['parentId'] = topDummy
                otherBabylon['meshes'].append(meshData)
                #meshDataSel = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
 
            for materialData in self.babylonFile['materials']:
                otherBabylon['materials'].append(materialData)  
                
        return otherBabylon
        
        
        
    def changeAllMeshScale(self):
        print ('changeAllMeshScale')
        
        newObjScaleing = float(self.objScaleInput.text())
       # allMeshData = self.babylonFile['meshes']
        babylonMeshData = self.babylonFile['meshes']

        for mesh in self.currentMeshList:
          #  print 'mesh__________',mesh babylonMeshData
            meshDataSel = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]

            if meshDataSel.get('normals') is None and meshDataSel.get('tangents') is None and meshDataSel.get('positions') is None:  ## check the mesh is dammy
               # meshDataSel = None
                materialId = None
                materialDataSel = None
            else:
                #print meshDataSel
                newScaleList = [meshDataSel['scaling'][0]*newObjScaleing,meshDataSel['scaling'][1]*newObjScaleing,meshDataSel['scaling'][2]*newObjScaleing]
                meshDataSel['scaling'] = newScaleList
               # print mesh,newObjScaleing , meshDataSel['scaling']
               # animationData = filter(lambda x:x['property'] == mesh,meshDataSel)[0]
                #selMaterial_ani_Attr = filter(lambda x:x['property'] == bbAttrName,materialData['opacityTexture']['animations'])[0]
                
                ####change animation scalingd8
                selMaterial_ani_Attr = (filter(lambda x:x['property'] == 'scaling',meshDataSel['animations']))
                #print type(selMaterial_ani_Attr),len(selMaterial_ani_Attr)
                if len(selMaterial_ani_Attr) > 0:
                  # print selMaterial_ani_Attr[0]['keys'] 
                   totalFramesCount = len(selMaterial_ani_Attr[0]['keys'] )
                   for i in range(0,totalFramesCount):
                        eachFrameAniData = selMaterial_ani_Attr[0]['keys'][i]['values']
                        #frameKey =  selMaterial_ani_Attr[0]['keys'][i]
                        newScalingList = [eachFrameAniData[0]*newObjScaleing,eachFrameAniData[1]*newObjScaleing,eachFrameAniData[2]*newObjScaleing]
                       # self.babylonFile['meshes']
                        #selMaterial_ani_Attr
                       # eachFrameAniData = newScalingList
                        #selMaterial_ani_Attr[0][i]['values'] = newScalingList
                        selMaterial_ani_Attr[0]['keys'][i]['values'] = [eachFrameAniData[0]*newObjScaleing,eachFrameAniData[1]*newObjScaleing,eachFrameAniData[2]*newObjScaleing]
                     #   print mesh,selMaterial_ani_Attr[0]['keys'][i]['values']#[i]
                       # eachFrameAniData[]
                ## simplify normals positions uvs  tangents
                
                ## change scaling

   
        
    def clearMetaData(self):
        print 'clearMetaData'
        babylonMeshData = self.babylonFile['meshes']
        babylonMaterialData =  self.babylonFile['materials']
        for meshData in babylonMeshData:
            meshData['metadata'] = {}
        for materialData in babylonMaterialData:
            materialData['metadata'] = {}
        
        
    def checkUsingTheSameTexture(self):
        #### blendmode should be the same, and having the same material attribute
        babylonMeshData = self.babylonFile['meshes']
        babylonMaterialData =  self.babylonFile['materials']
        checkMeshMaterialDataListWithTheSameMaterial = []
        checkTheSameMaterialAttrList = []
        checkTheSameMaterialAttrDict = {}



        # build the same material attribute list
        for mesh in self.currentMeshList:
            if mesh in self.allMaterialMeshList:
                theSameMaterialValue = cmds.getAttr('%s.bb_Material_theSameMaterial'%mesh)
                print '11111222333',mesh,theSameMaterialValue
                if theSameMaterialValue == 'none':
                    pass
                else:
                    checkTheSameMaterialAttrDict.update({theSameMaterialValue:[]})
                    
                    
                    
                    
        
        for mesh in self.currentMeshList:
            if mesh in self.allMaterialMeshList:
                theSameMaterialValue = cmds.getAttr('%s.bb_Material_theSameMaterial'%mesh)     
                if theSameMaterialValue == 'none':
                    pass     
                else:
                    if mesh in checkTheSameMaterialAttrDict[theSameMaterialValue]:
                        pass
                    else:
                        currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
                        materialID = currentMeshData['materialId']

                       # print materialID
                        checkTheSameMaterialAttrDict[theSameMaterialValue].append({mesh:materialID})
                        #materialData =  filter(lambda x:x['id'] == materialID,babylonMaterialData)[0]
                       # print materialData
                       
                       
        for key in checkTheSameMaterialAttrDict.keys():
            if len(checkTheSameMaterialAttrDict[key]) == 1:
                pass
            else:
               # print '123412341234',checkTheSameMaterialAttrDict[key]
              #  usingMaterialID = checkTheSameMaterialAttrDict[key][0].keys()[0]
              #  print '22232323234456565656',meshName

                for i in range(0,len(checkTheSameMaterialAttrDict[key])):
                    usingMaterialID = checkTheSameMaterialAttrDict[key][0][checkTheSameMaterialAttrDict[key][0].keys()[0]]

                    print '123412341234',checkTheSameMaterialAttrDict[key][i],usingMaterialID#,checkTheSameMaterialAttrDict[key][0][checkTheSameMaterialAttrDict[key][i].keys()[0]]
                    meshName = checkTheSameMaterialAttrDict[key][i].keys()[0]
                    oldMaterialID = checkTheSameMaterialAttrDict[key][i][meshName]
                    
                    currentMeshData = filter(lambda x:x['name'] == meshName,babylonMeshData)[0]
                    currentMeshData['materialId'] = usingMaterialID
                    materialData =  filter(lambda x:x['id'] == oldMaterialID,babylonMaterialData)[0]
                    if oldMaterialID == usingMaterialID:
                        pass#print "asdsadsdsadsdsadsdsadsadsad"
                    else:
                        self.babylonFile['materials'].remove(materialData)
                        #
                        
                        #filter(lambda x:x['id'] == oldMaterialID,babylonMaterialData)[0] = 
                   # else:
                        
                    
                    print '22232323234456565656',meshName,oldMaterialID#,currentMeshData['materialId']
  
        
      #  for key in checkTheSameMaterialAttrDict.keys():
      #      if len(checkTheSameMaterialAttrDict[key]) == 1:
       #         pass
      #      else:
           #     print  '22232323234456565656',checkTheSameMaterialAttrDict[key]
       #         
              #  materialData =  filter(lambda x:x['id'] == materialID,self.babylonFile['materials'])[0]
           # for i in range(0,len(checkTheSameMaterialAttrDict[key])):  
                
            
        print checkTheSameMaterialAttrDict

                
        
        
    def checkUsingTheSameTexture2(self):
        print 'checkUsingTheSameTexture'
        babylonMeshData = self.babylonFile['meshes']
        babylonMaterialData =  self.babylonFile['materials']
        

        checkMeshMaterialDataList = []
        checkTextureList = []
        allTextureMaterialMeshDataList = []
        allSecOptiTextureList = []
        for mesh in self.currentMeshList:
            
            if mesh in self.allMaterialMeshList:
                selMeshBlendMode = cmds.getAttr('%s.bb_Material_alphaMode'%mesh)
                currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
                meshShapeName = cmds.ls(mesh,dag=2,typ='mesh')[0]
                shadingGrps = cmds.listConnections(meshShapeName ,type='shadingEngine')[0]
                shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
                fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0] 
                attachmentName = cmds.getAttr("%s.fileTextureName" %fileNode).split('/')[-1]#.split('.')[0]
                
                materialID = currentMeshData['materialId']
                blendMode = cmds.getAttr("%s.bb_Material_alphaMode"%mesh)
                
                

               # materialData =  filter(lambda x:x['id'] == materialID,self.babylonFile['materials'])[0]
                
                alphaGainTextureNode = cmds.listConnections('%s.alphaGain' % (fileNode),type='file')
               # print 'alphaGainTextureNode________________________',alphaGainTextureNode
                
               # if alphaGainTextureNode is None:
                   # print 'dfddddddddddddddddddddddddddddddddddddddddddddddddddddd'
              #  try:
                if alphaGainTextureNode is None:
                    pass
                else:
                    ### get info from 2nd opti texture
                    attachmentOptiAlphaTextureFileName = cmds.getAttr("%s.fileTextureName" %alphaGainTextureNode[0]).split('/')[-1]#.split('.')[0]
                   # attachmentOptiAlphaTextureFileNameFullPath = cmds.getAttr("%s.fileTextureName" %alphaGainTextureNode[0])#.split('.')[0]
                   # placement2DTextureNode =  cmds.listConnections(alphaGainTextureNode[0],type = 'place2dTexture')[0]
                    print 'attachmentOptiAlphaTextureFileName___________________________5',attachmentOptiAlphaTextureFileName
                    if attachmentOptiAlphaTextureFileName in checkTextureList:
                        pass
                    else:
                        checkTextureList.append(attachmentOptiAlphaTextureFileName)
                
                    if attachmentOptiAlphaTextureFileName in allSecOptiTextureList:
                        pass
                    else:
                        allSecOptiTextureList.append(attachmentOptiAlphaTextureFileName)
                
               # materialData =  filter(lambda x:x['id'] == materialID,self.babylonFile['materials'])[0]
               
                if attachmentName in checkTextureList:
                    pass
                else:
                    checkTextureList.append(attachmentName)
                
                meshMaterialDataDict = {"texture":attachmentName,"meshName":mesh,"materialID":materialID,"blendMode":blendMode}

                checkMeshMaterialDataList.append(meshMaterialDataDict)
        print 'allSecOptiTextureList________________________________999',allSecOptiTextureList,len(allSecOptiTextureList)
        for texture in checkTextureList:
           # allTextureMaterialMeshDataList.append({texture:{"1":{},"2":{},"3":{},"4":{},"5":{},"6":{},"7":{}}})
             allTextureMaterialMeshDataList.append({texture:{"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[]}})

           # allTextureMaterialMeshDataList.append({texture:{"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"9":[],"10":[],"11":[],"12":[],"13":[],"14":[],"15":[],"16":[],"17":[],"18":[],"19":[],"20":[],"21":[],"22":[],"23":[],"24":[],"25":[],"26":[],"27":[],"28":[],"29":[],"30":[],"32":[],"33":[],"34":[],"35":[],"36":[],"37":[],"38":[],"39":[],"40":[]}})
            #allTextureMaterialMeshDataList.append({texture:{"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"9":[],"10":[],"11":[],"12":[],"13":[],"14":[],"15":[],"16":[],"17":[],"18":[],"19":[],"20":[],"21":[],"22":[],"23":[],"24":[],"25":[],"26":[],"27":[],"28":[],"29":[],"30":[],"32":[],"33":[],"34":[],"35":[],"36":[],"37":[],"38":[],"39":[],"40":[]}})

            
        for mesh in self.currentMeshList:
            if mesh in self.allMaterialMeshList:
                selMeshBlendMode = cmds.getAttr('%s.bb_Material_alphaMode'%mesh)
                currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
                meshShapeName = cmds.ls(mesh,dag=2,typ='mesh')[0]
                shadingGrps = cmds.listConnections(meshShapeName ,type='shadingEngine')[0]
                shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
                fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0] 
                attachmentName = cmds.getAttr("%s.fileTextureName" %fileNode).split('/')[-1]#.split('.')[0]
                materialID = currentMeshData['materialId']

                blendModeKey = str(cmds.getAttr("%s.bb_Material_alphaMode"%mesh))
                currentTextureDataList = filter(lambda x:x.keys()[0] == attachmentName,allTextureMaterialMeshDataList)[0][attachmentName]
                currentTextureDataList[blendModeKey].append({materialID:mesh})
                #currentTextureData[]
                #print 'currentTextureDataList',currentTextureDataList
            
        ### assign the same material ID and remove material
        
        allTextureCount = len(allTextureMaterialMeshDataList)
       # print 'allTextureMaterialMeshDataList________________________2',len(allTextureMaterialMeshDataList),allTextureMaterialMeshDataList
        for textueData in allTextureMaterialMeshDataList:
            textureNameKey = textueData.keys()[0]
            
            #print 'textureNameKey________________________3',textureNameKey

            ### blendmode index from 1 to 7
            for i in range(1,8):
                currentBlendModeTextureData = textueData[textureNameKey][str(i)]
                totalTheSameMaterialMeshCount = len(currentBlendModeTextureData)

              #  print 'currentBlendModeTextureData____________________________4', textureNameKey,totalTheSameMaterialMeshCount,currentBlendModeTextureData
                if totalTheSameMaterialMeshCount  == 0:
                    pass
                   # replaceMaterialID = 'None'
                    # print replaceMaterialID,totalTheSameMaterialMeshCount
                else:
                    replaceMaterialID = currentBlendModeTextureData[0].keys()[0]
                   # print "mesh___________________33333",mesh
                    if totalTheSameMaterialMeshCount > 0:
                        for meshMaterial in currentBlendModeTextureData:
                            currentIDKey = meshMaterial.keys()[0]
                            mesh = meshMaterial[currentIDKey]  ## meshName
                          #  print currentIDKey,mesh
                            currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
                           # print currentMeshData[]
                            currentMeshData['materialId'] = replaceMaterialID
                           # print mesh,currentMeshData['materialId']
                            try:
                                if  currentIDKey != replaceMaterialID:
                                    currentMaterialData = filter(lambda x:x['id'] == currentIDKey,babylonMaterialData)[0]
                                    babylonMaterialData.remove(currentMaterialData)
                            except:
                                pass
                                #print mesh,babylonMaterialData
                            
                           # replaceSelMeshMaterialID = 
                        
                       # pass
                   # else:
                       # print currentMeshData['materialId']
                    
                    #print replaceMaterialID,totalTheSameMaterialMeshCount
      
            
        #print 'checkTextureList',checkTextureList
            
       # print 'textureMaterialMeshDataList',allTextureCount,allTextureMaterialMeshDataList

    
        
    def checkTexturePassAndBlendMode(self):
        babylonMeshData = self.babylonFile['meshes']

        #print self.currentMeshList
        for mesh in self.currentMeshList:
            if mesh in self.allMaterialMeshList:
                selMeshBlendMode = cmds.getAttr('%s.bb_Material_alphaMode'%mesh)
            
           # print mesh,selMeshBlendMode
             
            
        
            
                if selMeshBlendMode == 2:
                        
                    currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
                    currentMeshData['visibility'] = 1.0
                    materialID = currentMeshData['materialId']
                    materialData =  filter(lambda x:x['id'] == materialID,self.babylonFile['materials'])[0]
                    materialData['alpha'] = 1

                    meshShapeName = cmds.ls(mesh,dag=2,typ='mesh')[0]
                    shadingGrps = cmds.listConnections(meshShapeName ,type='shadingEngine')[0]
                    shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
                    fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0] 
                    attachmentName = cmds.getAttr("%s.fileTextureName" %fileNode).split('/')[-1]#.split('.')[0]
                    fileFormat = attachmentName.split('.')[-1]
                    try:
                        selMeshVisibilityKeyFrameList = cmds.keyframe(mesh,query=True, at= 'bb_mesh_visibility')
                      #  print "mesh11111111111111111111111111111",mesh,selMeshVisibilityKeyFrameList
                        if selMeshVisibilityKeyFrameList == None:
                            #print "mesh11111111111111111111111111111",mesh,selMeshVisibilityKeyFrameList
                            selMeshVisibilityKeyFrameList = []
                    except:
                #        print "mesh222222222222222222222222222221",mesh

                        selMeshVisibilityKeyFrameList = []
                    checkValueForVis = []
                  #  print "mesh~~~~~~~~~~~~~~~~~~~~~",mesh
                    if len(selMeshVisibilityKeyFrameList) == 0:
                        currentVisValue = cmds.getAttr('%s.bb_mesh_visibility'%mesh, t = 0)

                    else:
                       # checkValueForVis = []
                        for f in selMeshVisibilityKeyFrameList:
                            selVisValue = cmds.getAttr('%s.bb_mesh_visibility'%mesh, t = f)
                            if selVisValue < 1 and selVisValue > 0:
                                checkValueForVis.append(selVisValue)

                           # allValueForVis.append(cmds.getAttr('%s.bb_mesh_visibility'%mesh, t = f))
                        #checkVisSmallThanOne = filter(lambda x:x['id'] == materialID,self.babylonFile['materials'])[0]
                       # print 'asdasdasdsadasasdsadsad',checkValueForVis   
                   # print selMeshVisibilityKeyFrameList
                    
                   # cmds.getAttr('DB_E_N_FreezeRingA1.bb_mesh_visibility', t = 0)
                   # print fileFormat
                    if len(checkValueForVis) == 0:
                        if fileFormat == "png" or fileFormat == "PNG":
                          #  print fileFormat
                            #print  '11111111111111111111111111111',materialData['diffuseTexture']
                           # print  '22222222222222222222222222222',materialData['opacityTexture']
                            try:
                                materialData['diffuseTexture']['hasAlpha'] =True # = materialData['diffuseTexture']
                                #materialData['opacityTexture']= None #['hasAlpha'] =True
                                
                            except:
                                pass
                    else: 
                        try:
                            materialData['diffuseTexture']['hasAlpha'] =True # = materialData['diffuseTexture']
                            #materialData['opacityTexture']= materialData['diffuseTexture']
                                
                        except:
                            pass
                   # materialData['opacityTexture'] = {}
                   # materialData['emissiveTexture'] = {}
                   # materialData['ambientTexture'] = {}

                   # materialData['diffuseTexture']['hasAlpha'] = True
                   # materialData['alpha'] = 1

                

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


    def getTextureData(self):   ## get all diffuse map from shader  
        print ('fixTextureData')
        babylonMeshData = self.babylonFile['meshes']
        materialsData =  self.babylonFile['materials']
        materialAnimationAttrList = [{'uOffset':'offsetU'},{'vOffset':'offsetV'},{'uScale':'repeatU'},{'vScale':'repeatV'},{'wAng':'rotateUV'}]
        angelAttrList = ['wAng']

        for mesh in self.currentMeshList:
            if mesh in self.allMaterialMeshList:   ### check if mesh get material data
                currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
                meshName = cmds.ls(mesh,dag=2,typ='mesh')[0]
                shadingGrps = cmds.listConnections(meshName ,type='shadingEngine')[0]
                shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
                fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0] 
                diffuseTextureFileNode2Dplacement = cmds.listConnections(fileNode,type='place2dTexture')[0]
                print  'diffuseTextureFileNode2Dplacement',diffuseTextureFileNode2Dplacement
                attachmentName = cmds.getAttr("%s.fileTextureName" %fileNode).split('/')[-1]#.split('.')[0]
                
                materialID = currentMeshData['materialId']
                materialData =  filter(lambda x:x['id'] == materialID,self.babylonFile['materials'])[0]
                
                alphaGainTextureNode = cmds.listConnections('%s.alphaGain' % (fileNode),type='file')
               # print 'alphaGainTextureNode________________________',alphaGainTextureNode wrapU
                
               # if alphaGainTextureNode is None:
                   # print 'dfddddddddddddddddddddddddddddddddddddddddddddddddddddd'
              #  try:
                
               # print cmds.getAttr("%s.wrapU" %diffuseTextureFileNode2Dplacement)
                
                if cmds.getAttr("%s.wrapU" %diffuseTextureFileNode2Dplacement) == True:
                     materialData['diffuseTexture']['wrapU'] = 1
                elif cmds.getAttr("%s.wrapU" %diffuseTextureFileNode2Dplacement) == False:
                    materialData['diffuseTexture']['wrapU'] = 0
                    
                if cmds.getAttr("%s.wrapV" %diffuseTextureFileNode2Dplacement) == True:
                     materialData['diffuseTexture']['wrapV'] = 1
                elif cmds.getAttr("%s.wrapV" %diffuseTextureFileNode2Dplacement) == False:
                    materialData['diffuseTexture']['wrapV'] = 0    
               # materialData['diffuseTexture']['wrapU'] = cmds.getAttr("%s.wrapU" %diffuseTextureFileNode2Dplacement)
               # materialData['diffuseTexture']['wrapV'] = cmds.getAttr("%s.wrapV" %diffuseTextureFileNode2Dplacement)
   
                
                
                
                if alphaGainTextureNode is None:
                    pass
                else:
                    ### get info from 2nd opti texture
                    attachmentOptiAlphaTextureFileName = cmds.getAttr("%s.fileTextureName" %alphaGainTextureNode[0]).split('/')[-1]#.split('.')[0]
                    attachmentOptiAlphaTextureFileNameFullPath = cmds.getAttr("%s.fileTextureName" %alphaGainTextureNode[0])#.split('.')[0]
                    #placement2DTextureNode =  cmds.listConnections('%s.rotateFrame' % (alphaGainTextureNode[0]))[0]
                    placement2DTextureNode =  cmds.listConnections(alphaGainTextureNode[0],type = 'place2dTexture')[0]
                    #print 'placement2DTextureNode____________________3',placement2DTextureNode

               # cmds.listConnections('new:file17',type ='place2dTexture')
                #cmds.nodeType('new:place2dTexture3')
                    exportBabyLonFileName = self.exportBabylonFileName.text().split('/')[-1]
                    exportOptiTextureFileName = self.exportBabylonFileName.text().replace(exportBabyLonFileName,attachmentOptiAlphaTextureFileName)
                   
                    offsetU = cmds.getAttr("%s.offsetU" %placement2DTextureNode)
                    offsetV = cmds.getAttr("%s.offsetV" %placement2DTextureNode)
                    scaleU = cmds.getAttr("%s.repeatU" %placement2DTextureNode)
                    scaleV = cmds.getAttr("%s.repeatV" %placement2DTextureNode)
                  #  wrapU = cmds.getAttr("%s.wrapU" %placement2DTextureNode)
                   # wrapV = cmds.getAttr("%s.wrapV" %placement2DTextureNode)

                    wAng = float(cmds.getAttr("%s.rotateUV" %placement2DTextureNode)) * (math.pi / 180)      
                    try:
                        shutil.copyfile(attachmentOptiAlphaTextureFileNameFullPath, exportOptiTextureFileName)
                    except:
                        pass

               
                    if cmds.getAttr("%s.wrapU" %placement2DTextureNode) == True:
                         materialData['opacityTexture']['wrapU'] = 1
                    elif cmds.getAttr("%s.wrapU" %placement2DTextureNode) == False:
                        materialData['opacityTexture']['wrapU'] = 0
                        
                    if cmds.getAttr("%s.wrapV" %placement2DTextureNode) == True:
                         materialData['opacityTexture']['wrapV'] = 1
                    elif cmds.getAttr("%s.wrapV" %placement2DTextureNode) == False:
                        materialData['opacityTexture']['wrapV'] = 0    


                        
                    materialData['opacityTexture']['name'] = attachmentOptiAlphaTextureFileName
                    
                    materialData['opacityTexture']['uOffset'] = offsetU
                    materialData['opacityTexture']['vOffset'] = offsetV
                    materialData['opacityTexture']['uScale'] = scaleU
                    materialData['opacityTexture']['vScale'] = scaleV
                   # materialData['opacityTexture']['wrapU'] = wrapU
                   # materialData['opacityTexture']['wrapV'] = wrapV

                    materialData['opacityTexture']['wAng'] = wAng
    

                        
                    '''
                    try:
                        for i in range(0,len(materialAnimationAttrList)):
                            bbAttrName = materialAnimationAttrList[i].keys()[0]
                            print 'bbAttrName____________________3',bbAttrName,materialOpacityAnimAtionData
                            
                            try:
                                material_ani_Attr = filter(lambda x:x['property'] ==bbAttrName , materialOpacityAnimAtionData)[0]
                                print 'material_ani_Attr____________________3',material_ani_Attr

                                materialOpacityAnimAtionData.remove(material_ani_Attr)
                            except:
                                pass
                            materialData['opacityTexture']['animations'] = materialOpacityAnimAtionData
                           # print 'materialOpacityAnimAtionData_________________________________2345___681',materialOpacityAnimAtionData

                    except:
                        pass
                        
                    '''
                    try:
                        materialData['opacityTexture']['animations'] = []
                        for i in range(0,len(materialAnimationAttrList)):
                            bbAttrName = materialAnimationAttrList[i].keys()[0]
                            

                            mayaAttrName = materialAnimationAttrList[i][bbAttrName]
                            #print 'bbAttrName____________________3',bbAttrName,mayaAttrName

                            if bbAttrName == 'wAng':
                              #  print "sdsfdsfdsfdfdsfdfdsf2222"
                                attr_startFrameValue = cmds.getAttr('%s.%s'%(placement2DTextureNode,mayaAttrName),t=1)
                                #initSelAttrValueFromMayaObj = (((attr_startFrameValue%360))*math.pi)/180.0
                                initSelAttrValueFromMayaObj = float(attr_startFrameValue) * (math.pi / 180)  
                                      
                            else:
                              #  print 'fdssssssssssssssssssssssssssssssssssss',bbAttrName
                                initSelAttrValueFromMayaObj = cmds.getAttr('%s.%s'%(placement2DTextureNode,mayaAttrName) ,t = 1)
                            material_Ani_Attr= {
                                    "blendingSpeed": 0.01, 
                                    "dataType": 0,   #int (0 = float, 1 = vector3, 2 = quaternion, 3 = matrix),
                                   # "enableBlending": False, 
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
                                   #     "autoAnimate": True,
                                      #  "autoAnimateFrom": int(float(self.startFrameInput.text())),
                                      #  "autoAnimateTo": int(float(self.endFrameInput.text())),
                                     #   "autoAnimateLoop": True
                                   # "loopBehavior": int (0 = relative, 1 = cycle, 2 = constant),
                                            } 
                            materialData['opacityTexture']['animations'].append(material_Ani_Attr)
                                
                                
                    except:
                        pass    
                                    
                        
                    for i in range(0,len(materialAnimationAttrList)):  ### update if 2splacement node has key
                        bbAttrName = materialAnimationAttrList[i].keys()[0]
                        mayaAttrName = materialAnimationAttrList[i][bbAttrName]
                        attr_DataList = []
                        
                       # print 'asdsadsdsdsad________________1',cmds.keyframe(placement2DTextureNode,at = mayaAttrName,q=True)  

                       # try:
                        if cmds.keyframe(placement2DTextureNode,at = mayaAttrName,q=True)   is None:
                            pass
                        else:
                        ##### get keyframe from maya mesh transform
                            selAttrKeyFrameListFromMayaObj = cmds.keyframe(placement2DTextureNode,at = mayaAttrName,q=True)  
                           # print '11111111111111111111111',mayaAttrName,selAttrKeyFrameListFromMayaObj
                          #  if len(selAttrKeyFrameListFromMayaObj) >0:
                            if selAttrKeyFrameListFromMayaObj  is None:
                                pass
                            else:
                                for f in selAttrKeyFrameListFromMayaObj:
                                    attr_SelFrameValue = cmds.getAttr('%s.%s'%(placement2DTextureNode,mayaAttrName),t=f)
                                   # print 'bbAttrName' ,bbAttrName
                                    if bbAttrName == 'wAng' :
                                        
                                        #angleValueTrans = (((attr_SelFrameValue%360))*math.pi)/180.0
                                        angleValueTrans = float(attr_SelFrameValue) * (math.pi / 180)
                                        attr_DataList.append({"frame":f,"values":[float('%.3f'%angleValueTrans)]})

                                    else:
                                        
                                        attr_DataList.append({"frame":f,"values":[float('%.3f'%attr_SelFrameValue)]})
                                
                            selMaterial_ani_Attr = filter(lambda x:x['property'] == bbAttrName,materialData['opacityTexture']['animations'])[0]
                            selMaterial_ani_Attr['keys'] = attr_DataList

                         
                            
                       # except:
                       #     pass
          
                        

                #except:
                #    pass
               # print 'materialData',materialData
               # print 'attachmentName',attachmentName
                
                #### fix material texture file
                materialData['diffuseTexture']['name'] = attachmentName
                
                
                #### set Color to ambient and diffuse 
                ambientColorR = float(cmds.getAttr("%s.ambientColor" %shaders[0])[0][0])
                ambientColorG =  float(cmds.getAttr("%s.ambientColor" %shaders[0])[0][1])
                ambientColorB =  float(cmds.getAttr("%s.ambientColor" %shaders[0])[0][2])
                
                diffuseTextureLevel = float(cmds.getAttr("%s.bb_Material_diffuseLevel" %mesh))
                opacityTextureLevel = float(cmds.getAttr("%s.bb_Material_diffuseLevel" %mesh))
                materialData['diffuseTexture']['level'] =  float('%.2f'%diffuseTextureLevel)
                materialData['opacityTexture']['level'] =  float('%.2f'%opacityTextureLevel)
                
                
                
               # cmds.getAttr()
                


                try:
                    if ambientColorR + ambientColorG + ambientColorB > 0.0:
                        materialData['ambient']= [ambientColorR,ambientColorG,ambientColorB]
                        materialData['emissive']= [ambientColorR,ambientColorG,ambientColorB]

                        materialData['diffuse']= [ambientColorR,ambientColorG,ambientColorB]


                    else:
                        pass
                except:
                    pass
            else:
                pass
            #print 'sfdfdfdf_____________ggggg',ambientColorR,ambientColorG,ambientColorB
            
           # materialData = 
           
           
           
           
           
        return materialData
            
    def getAllMeshAnimationData(self):  ###  function, get all meshes animation data
    
      #  print '_________________getAllMeshAnimationData____________________'
        getCurrentMeshVisibilityAniData = self.getAlphaGainMod()  ### 
       # print 'getCurrentMeshVisibilityAniDat____________________11111111111111111',getCurrentMeshVisibilityAniData

        getMaterialsData = self.updateMaterialValueFromMaya() ###
      #  print 'getMaterialsData____________________222222222222222222',getMaterialsData
  
        if self.exportUVAnuCheck.isChecked() == True:
          #  print "exportUVAnuCheck is checked"

            self.updateMaterialUVFromMaya()
        
        if self.exportTransformCheck.isChecked() == True:
           # print "exportTransformCheck is checked"
            self.updateMeshTranslateFromMaya()
        
  
    
      

    def updataAnimationLoop(self):
        
        babylonMeshData = self.babylonFile['meshes']
        

        for mesh in self.currentMeshList:
            if mesh in self.allMaterialMeshList:
                currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
              #  print ' currentMeshData_______________________4',currentMeshData

                currentMeshAniData = currentMeshData['animations']
                currentMeshData['metadata'] = {}
                currentMeshData['autoAnimateFrom'] = int(float(self.startFrameInput.text()))

                currentMeshData['autoAnimateTo'] = int(float(self.endFrameInput.text()))

           #     print ' currentMeshData________________________5',currentMeshData['autoAnimateFrom'] ,currentMeshData['autoAnimateTo']

                try:
                    allKeyFrameSelMeshFromMaya = list(dict.fromkeys(cmds.keyframe(mesh,q=True)))
                    meshKeyFrom = 0
                    meshKeyTo = allKeyFrameSelMeshFromMaya[-1]
                    currentMeshData['autoAnimateFrom'] = 0
                   # print 'meshKeyTo________________________6',mesh,meshKeyTo
                    #currentMeshData['autoAnimateTo'] = meshKeyTo
                except:
                    pass

          
        
        
        
        
        
    def getAlphaGainMod(self):   ### function get alphaGain , visibility animation
       # print 'currentMeshList_______________1111111111111111111111',self.currentMeshList
        print 'getAlphaGainMod'
        babylonMeshData = self.babylonFile['meshes']
        for mesh in self.currentMeshList:
            
            if mesh in self.allMaterialMeshList: 
                currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
                
                if currentMeshData.get('animations') is None:
                
                
               # if currentMeshData['animations'] == None:
                    currentMeshData['animations'] = []
                else:
                    pass
               # print 'currentMeshData..................',currentMeshData

                try:
                    currentMeshAniData = currentMeshData['animations']
                  #  
                #    print 'aaaaaaaaaaaaaaaa'
                except:
                    currentMeshAniData.append({'animations':[]})
                  #  print 'bbbbbbbbbbbbbbb'

                    
               # print '12341232144123213213213',mesh,currentMeshAniData
                if cmds.getAttr('%s.bb_mesh_autoAnimate'%mesh) == 0 :
                    autoAnimate = True
                elif cmds.getAttr('%s.bb_mesh_autoAnimate'%mesh) == 1:
                    autoAnimate = False
                
                                       
                if cmds.getAttr('%s.bb_mesh_autoAnimateLoop'%mesh) == 0 :
                    autoLoop = True
                elif cmds.getAttr('%s.bb_mesh_autoAnimateLoop'%mesh) == 1:
                    autoLoop = False
                    
                try:
                    
                    

                    
                    currentMeshVisibilityAniData = filter(lambda x:x['name'] ==  "visibility animation" , currentMeshAniData)[0]  ### get mesh visibility ani data
                    currentMeshAniData.remove(currentMeshVisibilityAniData)
                    currentMeshAniData.append(
                                    {
                                        "name": "visibility animation",
                                        "property": "visibility",
                                        "dataType": 0,
                                       # "enableBlending": False,
                                        "blendingSpeed": 0.01,
                                        "loopBehavior": 1,
                                        "framePerSecond": int(self.fps),
                                        "keys":["%s"%mesh],
                                        "autoAnimate":autoAnimate,
                                        "autoAnimateFrom": int(float(cmds.getAttr('%s.bb_mesh_autoAnimateFrom'%mesh))),
                                        "autoAnimateTo": int(float(cmds.getAttr('%s.bb_mesh_autoAnimateTo'%mesh))),
                                        "autoAnimateLoop": autoLoop
                                        
                                    }  
                        
                                )
                 #   print "77777777777777777777777"
                except:
                  #  print 'currentMeshAniData______________2',currentMeshAniData\\
                  
                  
                  
                  
                    currentMeshAniData.append(
                                    {
                                        "name": "visibility animation",
                                        "property": "visibility",
                                        "dataType": 0,
                                      #  "enableBlending": False,
                                        "blendingSpeed": 0.01,
                                        "loopBehavior": 1,
                                        "framePerSecond": int(self.fps),
                                        "keys":[],
                                        "autoAnimate":autoAnimate,
                                        "autoAnimateFrom": int(float(cmds.getAttr('%s.bb_mesh_autoAnimateFrom'%mesh))),
                                        "autoAnimateTo": int(float(cmds.getAttr('%s.bb_mesh_autoAnimateTo'%mesh))),
                                        "autoAnimateLoop": autoLoop
                                    }  
                        
                                )
                    
                    
                    
                    
                 #   print "99999999999999999999999"
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
                    
        return babylonMeshData
        
        

        
        
        
        
        
        
            
    def updateMaterialUVFromMaya(self):
        babylonMeshData = self.babylonFile['meshes']
        materialsData =  self.babylonFile['materials']
        materialAnimationAttrList = [{'uOffset':'offsetU'},{'vOffset':'offsetV'},{'uScale':'repeatU'},{'vScale':'repeatV'},{'wAng':'rotateUV'}]
        angelAttrList = ['wAng']
        
        
        
        
        
        for mesh in self.currentMeshList:
            
            if mesh in self.allMaterialMeshList:
             #   print 'mesh_________________1',mesh
                currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
                currentMeshAniData = currentMeshData['animations']
                materialID = currentMeshData['materialId']

                materialData =  filter(lambda x:x['id'] == materialID,self.babylonFile['materials'])[0]
                materialDiffuseAnimAtionData = materialData['diffuseTexture']['animations']

                meshShapeName = cmds.ls(mesh,dag=2,typ='mesh')[0]
                shadingGrps = cmds.listConnections(meshShapeName ,type='shadingEngine')[0]
                
                shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)

                fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0]
              #  print 'mesh_________________1',mesh,fileNode

               # print 'gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg',fileNode
               # print cmds.listConnections('%s.offsetU'%fileNode,type='place2dTexture') #offsetU
                placementNode = cmds.listConnections('%s.rotateFrame'%fileNode,type='place2dTexture')[0] 
               # print 'placementNode_---------------------2323232',placementNode
                ###remove Select Animation list from bb
                try:
                    for i in range(0,len(materialAnimationAttrList)):
                        bbAttrName = materialAnimationAttrList[i].keys()[0]
                        
                       # print 'bbAttrName_________________________________2345',bbAttrName
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
                   # materialData['diffuseTexture']['animations']
                    
                   # materialData['diffuseTexture']['uOffset'] = 0
                   # materialData['diffuseTexture']['vOffset'] = 0
                   # materialData['diffuseTexture']['uScale'] = 1
                   # materialData['diffuseTexture']['vScale'] = 1

                   # materialData['diffuseTexture']['wAng'] = 0
        
                            
                    
                    
                    
                    
                    for i in range(0,len(materialAnimationAttrList)):
                        bbAttrName = materialAnimationAttrList[i].keys()[0]
                        mayaAttrName = materialAnimationAttrList[i][bbAttrName]
                        if bbAttrName == 'aawAng':
                            attr_startFrameValue = cmds.getAttr('%s.%s'%(placementNode,mayaAttrName),t=1)
                            #initSelAttrValueFromMayaObj = (((attr_startFrameValue%360))*math.pi)/180.0
                            initSelAttrValueFromMayaObj = float(attr_startFrameValue) * (math.pi / 180)

           
                        else:
                            initSelAttrValueFromMayaObj = cmds.getAttr('%s.%s'%(placementNode,mayaAttrName) ,t = 1)
                            material_Ani_Attr= {
                                    "blendingSpeed": 0.01, 
                                    "dataType": 0, 
                                   # "enableBlending": False, 
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
                                    "property": "%s"%bbAttrName#,
                                       # "autoAnimate": True,
                                       # "autoAnimateFrom": int(float(self.startFrameInput.text())),
                                       # "autoAnimateTo": int(float(self.endFrameInput.text())),
                                       # "autoAnimateLoop": True
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
                                     
                                    #angleValueTrans = (math.PI / 180)###float(attr_SelFrameValue)## (((attr_SelFrameValue%360))*math.pi)/180.0
                                    angleValueTrans = float(attr_SelFrameValue) * (math.pi / 180)
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
        

        frameStart = int(float(self.startFrameInput.text()))
        frameEnd = int(float(self.endFrameInput.text()))
 
        meshCountInBB = len(self.currentMeshList)
        babylonMeshData = self.babylonFile['meshes']


     
        ##check if object freeze in bb
        
        for mesh in self.currentMeshList:
            meshDataSel = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]

            if meshDataSel.get('normals') is None and meshDataSel.get('tangents') is None and meshDataSel.get('positions') is None:  ## check the mesh is dammy
               # meshDataSel = None
                materialId = None
                materialDataSel = None
            else:
                
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
       # print "999999999999999999999999999999999999999999999999999999996546546"
        for mesh in self.currentMeshList:
            meshDataSel = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]

            if meshDataSel.get('normals') is None and meshDataSel.get('tangents') is None and meshDataSel.get('positions') is None:  ## check the mesh is dammy
               # meshDataSel = None
                materialId = None
                materialDataSel = None
            else:
            
                currentMeshData = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
               # print ' currentMeshData_______________________4',currentMeshData

                currentMeshAniData = currentMeshData['animations']
                currentMeshData['metadata'] = {}
                currentMeshData['autoAnimateFrom'] = int(float(self.startFrameInput.text()))
                currentMeshData['autoAnimateTo'] = int(float(self.endFrameInput.text()))
              #  print ' currentMeshData________________________5',currentMeshData['autoAnimateTo']

                try:
                    allKeyFrameSelMeshFromMaya = list(dict.fromkeys(cmds.keyframe(mesh,q=True)))
                    meshKeyFrom = 0
                    meshKeyTo = allKeyFrameSelMeshFromMaya[-1]
                    currentMeshData['autoAnimateFrom'] = 0
                  #  print 'meshKeyTo________________________6',meshKeyTo
                    currentMeshData['autoAnimateTo'] = meshKeyTo
                except:
                    pass
        
            
                for i in  range(0,len(transformAttrList)):
                    bbTransAttrName = transformAttrList[i].keys()[0]
                    mayaAttrName =  transformAttrList[i][bbTransAttrName]
                  #  print 'mayaAttrName______________________________1234',mayaAttrName
                            
                    if cmds.getAttr('%s.bb_mesh_autoAnimate'%mesh) == 0 :
                        autoAnimate = True
                    elif cmds.getAttr('%s.bb_mesh_autoAnimate'%mesh) == 1:
                        autoAnimate = False
                    
                                           
                    if cmds.getAttr('%s.bb_mesh_autoAnimateLoop'%mesh) == 0 :
                        autoLoop = True
                    elif cmds.getAttr('%s.bb_mesh_autoAnimateLoop'%mesh) == 1:
                        autoLoop = False
                    
                            
                            
                    mesh_ani_AttrList =  {
                                            "name": "%s animation"%bbTransAttrName,
                                            "property": "%s"%bbTransAttrName,
                                            "dataType": 1,
                                           # "enableBlending": False,
                                            "blendingSpeed": 0.01,
                                            "loopBehavior": 1,
                                            "framePerSecond": int(self.fps), 
                                            "keys": [],
                                            "autoAnimate":autoAnimate,
                                            "autoAnimateFrom": int(float(cmds.getAttr('%s.bb_mesh_autoAnimateFrom'%mesh))),
                                            "autoAnimateTo": int(float(cmds.getAttr('%s.bb_mesh_autoAnimateTo'%mesh))),
                                            "autoAnimateLoop": autoLoop
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
        
       # try:
        for mesh in self.currentMeshList:
          #  print '00000000000000000000000000000',mesh
            meshDataSel = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]

            if meshDataSel.get('normals') is None and meshDataSel.get('tangents') is None and meshDataSel.get('positions') is None:  ## check the mesh is dammy
               # meshDataSel = None
                materialId = None
                materialDataSel = None
            else:
          

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
                                    "values":[float('%.4f'%currentFrameAttrValue[0]),float('%.4f'%currentFrameAttrValue[1]),-float('%.4f'%currentFrameAttrValue[2])]
                                    })
                                    
                               # print "333333333333333333333333333333333",attrValueList
                            if bbTransAttrName == "scaling":
                                currentFrameAttrValue = cmds.getAttr('%s.%s'%(mesh,mayaAttrName),t = f)[0]

                                attrValueList.append({
                                    "frame":f,
                                    "values":[float('%.4f'%currentFrameAttrValue[0]),float('%.4f'%currentFrameAttrValue[1]),float('%.4f'%currentFrameAttrValue[2])]
                                    })
                               # print "4444444444444444444444444444",attrValueList

                           # if bbTransAttrName == "rotationQuaternion":
                                
                           #     rq = self.getQuatRotation(mesh,f)
                                
                          #      attrValueList.append({
                            #        "frame":f,
                            #        "values":[-float('%.4f'%rq[0]),-float('%.4f'%rq[1]),float('%.4f'%rq[2]),float('%.4f'%rq[3])]
                             #       })
                    
                    if len(selAttrKeyFrameList) == 0: 
                       # print "21212121212"
                        attrValueList = []
                        if bbTransAttrName == "position":
                            currentFrameAttrValue = cmds.getAttr('%s.%s'%(mesh,mayaAttrName),t = 1)[0]

                            attrValueList.append({
                                        "frame":0.0,
                                        "values":[float('%.4f'%currentFrameAttrValue[0]),float('%.4f'%currentFrameAttrValue[1]),-float('%.4f'%currentFrameAttrValue[2])]
                                        })   
                                        
                           # print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",currentFrameAttrValue,attrValueList

                        elif bbTransAttrName == "scaling":
                            currentFrameAttrValue = cmds.getAttr('%s.%s'%(mesh,mayaAttrName),t = 1)[0]

                            attrValueList.append({
                                "frame":0.0,
                                "values":[float('%.4f'%currentFrameAttrValue[0]),float('%.4f'%currentFrameAttrValue[1]),float('%.4f'%currentFrameAttrValue[2])]
                                })               
                           
                           # print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",currentFrameAttrValue,attrValueList
             
                      #  elif bbTransAttrName == "rotationQuaternion":
                          #  print "cccccccccccccccccccccccccccccccccccccccccccc"
                       #     rq = self.getQuatRotation(mesh,0)
                            
                       #     attrValueList.append({
                         #       "frame":0.0,
                          #      "values":[-float('%.4f'%rq[0]),-float('%.4f'%rq[1]),float('%.4f'%rq[2]),float('%.4f'%rq[3])]
                          #      })                
                                    
                        
                    else:
                        self.errorMsgLabel.setText( 'updateMeshTranslateFromMaya error 04 ,no keys for select mesh attribute')
                        
                    mesh_ani_AttrList = filter(lambda x:x['property'] ==bbTransAttrName , currentMeshAniData)[0]
                  #  print '77777777777777777777',mesh_ani_AttrList

                    sortedAttrValueList = list(sorted(attrValueList, key = lambda x: float(x['frame'])))
                    mesh_ani_AttrList['keys'] = sortedAttrValueList
                  #  print '88888888888888888888888',sortedAttrValueList

                    
       # except:
        #    self.errorMsgLabel.setText( 'updateMeshTranslateFromMaya error 03 ,add animation value from maya attr to bb mesh animation dict')
        
       # cmds.getAttr('DB_E_N_FreezePlan_A.rotate')

        
        
        
        
        



        
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
            #meshDataSel = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]
            #materialId = meshDataSel['materialId']
           # materialDataSel = filter(lambda x:x['id'] == materialId,materialsData)[0]    
            meshDataSel = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]

            if meshDataSel.get('normals') is None and meshDataSel.get('tangents') is None and meshDataSel.get('positions') is None:  ## check the mesh is dammy
               # meshDataSel = None
                materialId = None
                materialDataSel = None
            else:
                
           # print 'babylonMeshData____________1',babylonMeshData
                materialId = meshDataSel['materialId']
                materialDataSel = filter(lambda x:x['id'] == materialId,self.materialsData)[0]
        
        
        
            if mesh in self.allMaterialMeshList:
        
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
                        if mesh in self.allMaterialMeshList:    
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
           
        return materialsData
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def clickSelChaBabylonFileBtn(self):
        print 'clickSelChaBabylonFileBtn'
                #print self.infoDock
        basicFilter = "*.babylon"
        openBabylonFIle = cmds.fileDialog2(caption="get character babylon file",fileFilter=basicFilter, dialogStyle=2,fm=1)[0]
        #self.getBabyLonFileNameInputBox 
        #self.babylonFileInputBox .setText(openBabylonFIle)
        #exportBabylonFileName = openBabylonFIle.split('.babylon')
        self.chaBabylonFileInputBox .setText(openBabylonFIle)
               
        
    def openBabylonFileFn(self):
        
        openBabylonFile = self.babylonFileInputBox.text()
        if openBabylonFile == 'get babylon file name':
            self.clickSelBabylonFileBtn()
        else:
            with open(openBabylonFile , 'r') as reader:
                
                self.babylonFile = json.loads(reader.read())
                
                self.meshData = self.babylonFile['meshes']
                #meshCount = len(self.meshData)
                
                self.materialsData =  self.babylonFile['materials']
                #materialsCount = len(self.materialsData) 
            
           # print openBabylonFile

    def clickSelBabylonFileBtn(self):
        #print ('aaaaaaaaaaaaa')
        #print self.infoDock
        basicFilter = "*.babylon"
        openBabylonFIle = cmds.fileDialog2(caption="get babylon file",fileFilter=basicFilter, dialogStyle=2,fm=1)[0]
        #self.getBabyLonFileNameInputBox 
        self.babylonFileInputBox.setText(openBabylonFIle)
        exportBabylonFileName = openBabylonFIle.split('.babylon')[0] +'_mod.babylon'
        
        self.exportBabylonFileName.setText(exportBabylonFileName)
        #self.exportBabylonFileName.setText('D:/sanTool/resources/app/ArtTest/Assets/Character/d5_mod.babylon')      
        #self.exportBabylonFileName.setText('D:/sanTool/resources/app/ArtTest/Assets/Scene/ChangAn/SG2_S_ChangAn.babylon')      

        
        try:
            
            with open(openBabylonFIle , 'r') as reader:
                
                self.babylonFile = json.loads(reader.read())
                
                self.meshData = self.babylonFile['meshes']
                meshCount = len(self.meshData)
                
                self.materialsData =  self.babylonFile['materials']
                materialsCount = len(self.materialsData)
              #  print 'meshCount_______________!234',meshCount,materialsCount

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


                #####get all 'mesh' List 
                self.allMeshList = []
                self.allMaterialMeshList = []
                for i in range(0,rowCount):
                    currentMeshData = self.meshData[i]
                    meshName = self.meshData[i]['name']
                    meshID = self.meshData[i]['id']
                    materialId = self.meshData[i]['materialId']
                    
                    
                    
                    
                    #print 'meshName______________________________5678',meshName,materialId
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
                    
                    if materialId == None:
                   
                        if self.meshData[i].get('normals') is None and self.meshData[i].get('tangents') is None and self.meshData[i].get('positions') is None:  ## check the mesh is dammy
                            selMeshMaterialName = 'dummy'
                            textureName = 'dummy'
                            if self.meshData[i].get('parentId') is None:
                                parentID = 'none'
                            else: 
                                parentID = self.meshData[i]['parentId']

                            
                            self.allMeshList.append({'meshName':meshName,'id':meshID,'meshType':'dummy','parentID':parentID})
                        else:
                            selMeshMaterialName = None
                            textureName = None
                            
                        
                        
                    else:
                        materialDataSel = filter(lambda x:x['id'] == materialId,self.materialsData)[0]
                        selMeshMaterialName = materialDataSel['name']
                        textureName =  materialDataSel['diffuseTexture']['name']
                        if self.meshData[i].get('parentId') is None:
                            parentID = 'none'
                        else: 
                            parentID = self.meshData[i]['parentId']

                        self.allMeshList.append({'meshName':meshName,'id':meshID,'meshType':'mesh','parentID':parentID})
                        self.allMaterialMeshList.append(meshName)
                   # try:
                   #     textureName =  materialDataSel['diffuseTexture']['name']

                   # except:
                   #     pass
                        
                    checkMaterialExisted = len(cmds.ls(selMeshMaterialName,typ="lambert"))
        
                        
                    newItem_material = QtWidgets.QTableWidgetItem() 
                    newItem_material.setText(QtWidgets.QApplication.translate("MainWindow",str(selMeshMaterialName), None,-1)) 
       
                        
                        
                        
                    if checkMaterialExisted == 1:
                        
          
                        
                        #try:
                       # if type(self.meshData[i]['normals']) == 'list':
                       #     print 'gggggggggggggggggggghgfhgfhghgfh',len(self.meshData[i]['normals'])
                       # else:
                       #     print 'dddddddddddddddaaaaaaaaaaaaaaaaaaaaaaammmmmmmmmmmmmmmmmy'
                      #  if self.meshData[i]['normals'] == Null:
                        #    print 'dddddddddddddddaaaaaaaaaaaaaaaaaaaaaaammmmmmmmmmmmmmmmmy'
    
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
                       #     print 'attachmentName_____________________43434',attachmentName
                            fileSource = cmds.getAttr("%s.fileTextureName" %fileNode)
                                                
                            newItem_texture = QtWidgets.QTableWidgetItem() 
                            newItem_texture.setText(QtWidgets.QApplication.translate("MainWindow",str(attachmentName), None,-1))     
                            
                            selMeshBlendMode = cmds.getAttr('%s.bb_Material_alphaMode'%meshName)
                            
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
                           # if selMeshBlendMode == 0:
                        
      
                                
                            self.meshItemTable.setCellWidget(i, 4, opTextCopyCheckBtnItem)
                            

                            ambientTextCopyCheckBtnItem = babylonMayaUI.buildTableCheckBtnItemA(60,20,14,'D -> A','#223322','#669966','#aaeeaa')
                            ambientTextCopyCheckBtnItem.setToolTip(meshName)
                            self.meshItemTable.setCellWidget(i, 5, ambientTextCopyCheckBtnItem)
                            
                            emisTextCopyCheckBtnItem = babylonMayaUI.buildTableCheckBtnItemA(60,20,14,'D -> E','#223322','#669966','#aaeeaa')
                            emisTextCopyCheckBtnItem.setToolTip(meshName)
                            self.meshItemTable.setCellWidget(i,6, emisTextCopyCheckBtnItem)
           
                            if selMeshBlendMode == 1:
                                opTextCopyCheckBtnItem.setChecked(True)
                            elif selMeshBlendMode == 2:
                                opTextCopyCheckBtnItem.setChecked(False)
                                emisTextCopyCheckBtnItem.setChecked(False)
                                ambientTextCopyCheckBtnItem.setChecked(False)

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
        
      #  print  'self.allMeshList________________',self.allMeshList,len(self.allMeshList)
        return self.allMeshList
        
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
        
        print 'self.allMeshList_______________2',self.allMeshList
        #selObjList = cmds.ls( sl=True , type="transform")
       # for obj in selObjList:
       #     attrList = cmds.listAttr(obj)
        #    bb_attrList =  filter(lambda x:x.split('_')[0] == 'bb',attrList)#[0]
        #    for attr in bb_attrList:
        #        cmds.deleteAttr('%s.%s'%(obj,attr))
                
                
        for i in self.allMeshList:
            mesh = i['meshName']
            meshId = i['id']
            meshType =  i['meshType']
            #if meshType == 'dummy':
            #    pass
            #else:
            attrList = cmds.listAttr(mesh)
            bb_attrList =  filter(lambda x:x.split('_')[0] == 'bb',attrList)#[0]
            for attr in bb_attrList:
                cmds.deleteAttr('%s.%s'%(mesh,attr)) 
            
            #print 'mesh,meshId,meshType',mesh,meshId,meshType,attrList
    
  
    


                
            
    def addMeshBabylonAttr(self):
        print 'addMeshBabylonAttr___________________55555'
       # cmds.currentTime()
        cmds.currentTime( 0, edit=True )    
     #   print '323232323223232323',self.currentMeshList
        
     #   print self.meshAttrDataList

        for mesh in self.currentMeshList:
            print mesh
            print self.allMaterialMeshList

            if mesh in self.allMaterialMeshList:
                print'22222222222222222', mesh

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
                  #  print 'shaders______________________________5678',shaders

                    fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0] 
                    alphaGainTextureNode = cmds.listConnections('%s.alphaGain' % (fileNode),type='file')
                    
                    
                    if alphaGainTextureNode == None:
                        
                        cmds.cutKey('%s.alphaGain'%fileNode)
                        cmds.connectAttr('%s.bb_mesh_visibility'%mesh, '%s.alphaGain'%fileNode)   
                        cmds.pasteKey( mesh, attribute='bb_mesh_visibility' )
                    else:
                        
                        if len(alphaGainTextureNode) == 1 and cmds.nodeType(alphaGainTextureNode[0]) =='file':
                            extraAlphaGainTextureNode = alphaGainTextureNode[0]
                            
                          #  print "sdsfdsfdsfdsfdfdsfd",extraAlphaGainTextureNode

                            cmds.cutKey('%s.alphaGain'%extraAlphaGainTextureNode)
                            cmds.connectAttr('%s.bb_mesh_visibility'%mesh, '%s.alphaGain'%extraAlphaGainTextureNode)   
                            cmds.pasteKey( mesh, attribute='bb_mesh_visibility' )

                    #    pass
                    
                    

                   # cmds.setAttr('%s.bb_Material_theSameMaterial'%mesh, 'none' , typ= "string")
                    # cmds.setAttr('%s.%s'%(mesh,longName),currentBBMeshAttrValue)
          
                except:
                    pass
                
                #### add extra attr defaut value
                try:
                    print 'mesh______________name',mesh
                    cmds.setAttr('%s.bb_Material_theSameMaterial'%mesh, 'none' , typ= "string")
        
        
                except:
                    pass
        self.setObjectAttrFromBBF()    
      
        
    def setObjectAttrFromBBF(self):
               
        babylonMeshData = self.babylonFile['meshes']
        materialsData =  self.babylonFile['materials']
        for mesh in self.currentMeshList:
          #  print 'mesh__________',mesh
            meshDataSel = filter(lambda x:x['name'] == mesh,babylonMeshData)[0]

            if meshDataSel.get('normals') is None and meshDataSel.get('tangents') is None and meshDataSel.get('positions') is None:  ## check the mesh is dammy
               # meshDataSel = None
                materialId = None
                materialDataSel = None
            else:
                
           # print 'babylonMeshData____________1',babylonMeshData
                materialId = meshDataSel['materialId']
                materialDataSel = filter(lambda x:x['id'] == materialId,self.materialsData)[0]
                
           # print '22222222222222222222222222222',materialId, materialDataSel
            
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
                            
            
        
        
        
        
def mayaToBabylon2_2018Main():
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



