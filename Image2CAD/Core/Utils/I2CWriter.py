# -*- coding: utf-8 -*-
"""

@author: Aditya Intwala
"""


from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment 
from datetime import datetime
import time

class I2CWriter:

       @staticmethod
       def Write(Feature_Manager):
           make_dir_root = Feature_Manager._RootDirectory
           time_str = time.strftime("%Y%m%d-%H%M%S") #datetime.now().isoformat()
           Root = Element("Root")
           Session = SubElement(Root, "Session")
           User = SubElement(Session,"AdityaIntwala")
           Date_Created = SubElement(Session, "Date_Created")
           Date_Created.text = time_str
           Image = SubElement(Session, "Image")
           Image.text = str(Feature_Manager._ImagePath)
           DetectedFeatures = SubElement(Root, "DetectedFeatures")
           comment = Comment('List of Features Detected with parameters')
           DetectedFeatures.append(comment)
           ArrowHeads = SubElement(DetectedFeatures, "ArrowHeads")
           for AH in Feature_Manager._DetectedArrowHead:
               ArrowHead = SubElement(ArrowHeads, "ArrowHead")
               BoundingBoxPoint1 = SubElement(ArrowHead, "BoundingBoxPoint1")
               X = SubElement(BoundingBoxPoint1, "x")
               X.text = str(AH._BoundingBoxP1.x)
               Y = SubElement(BoundingBoxPoint1, "y")
               Y.text = str(AH._BoundingBoxP1.y)
               BoundingBoxPoint2 = SubElement(ArrowHead, "BoundingBoxPoint2")
               X = SubElement(BoundingBoxPoint2, "x")
               X.text = str(AH._BoundingBoxP2.x)
               Y = SubElement(BoundingBoxPoint2, "y")
               Y.text = str(AH._BoundingBoxP2.y)
               Centre = SubElement(ArrowHead, "Centre")
               X = SubElement(Centre, "x")
               X.text = str(AH._ArrowCenter.x)
               Y = SubElement(Centre, "y")
               Y.text = str(AH._ArrowCenter.y)
               Direction = SubElement(ArrowHead, "Direction")
               Direction.text = str(AH._Direction)
           DimensionalLinesLeaders = SubElement(DetectedFeatures, "DimensionalLinesLeaders")
           for DL in Feature_Manager._DetectedDimensionalLine:
              for ls in DL._Leaders:
                       Leader = SubElement(DimensionalLinesLeaders, "Leader")
                       StartPoint = SubElement(Leader, "StartPoint")
                       X = SubElement(StartPoint, "X")
                       X.text = str(ls.startPoint.x)
                       Y = SubElement(StartPoint, "Y")
                       Y.text = str(ls.startPoint.y)
                       EndPoint = SubElement(Leader, "EndPoint")
                       X = SubElement(EndPoint, "X")
                       X.text = str(ls.endPoint.x)
                       Y = SubElement(EndPoint, "Y")
                       Y.text = str(ls.endPoint.y)
           DimensionalTexts = SubElement(DetectedFeatures, "DimensionalTexts")           
           for DT in Feature_Manager._DetectedDimensionalText:
               DimensionalText = SubElement(DimensionalTexts, "DimensionalText")
               Text = SubElement(DimensionalText, "Text")
               Text.text = DT._Text
               BoundingBoxPoint1 = SubElement(DimensionalText, "BoundingBoxPoint1")
               X = SubElement(BoundingBoxPoint1, "x")
               X.text = str(DT._TextBoxP1.x)
               Y = SubElement(BoundingBoxPoint1, "y")
               Y.text = str(DT._TextBoxP1.y)
               BoundingBoxPoint2 = SubElement(DimensionalText, "BoundingBoxPoint2")
               X = SubElement(BoundingBoxPoint2, "x")
               X.text = str(DT._TextBoxP2.x)
               Y = SubElement(BoundingBoxPoint2, "y")
               Y.text = str(DT._TextBoxP2.y)
               OrientationAngle = SubElement(DimensionalText, "OrientationAngle")
               OrientationAngle.text = str(DT._Orientation)
           Lines = SubElement(DetectedFeatures, "Lines")    
           for L in Feature_Manager._DetectedLine:
                        Segment = SubElement(Lines, "Segment")
                        StartPoint = SubElement(Segment, "StartPoint")
                        X = SubElement(StartPoint, "x")
                        X.text = str(L.startPoint.x)
                        Y = SubElement(StartPoint, "y")
                        Y.text = str(L.startPoint.y)
                        EndPoint = SubElement(Segment, "EndPoint")
                        X = SubElement(EndPoint, "x")
                        X.text = str(L.endPoint.x)
                        Y = SubElement(EndPoint, "y")
                        Y.text = str(L.endPoint.y)  
           Circles = SubElement(DetectedFeatures, "Circles")    
           for C in Feature_Manager._DetectedCircle:
               DetectedCircle = SubElement(Circles, "DetectedCircle") 
               Centre = SubElement(DetectedCircle, "Centre")
               X = SubElement(Centre, "x")
               X.text = str(C._centre.x)
               Y = SubElement(Centre, "y")
               Y.text = str(C._centre.y)
               Radius = SubElement(DetectedCircle, "Radius")
               Radius.text = str(C._radius) 
           CorrelatedFeatures = SubElement(Root, "CorrelatedFeatures")
           comment = Comment('List of Detected Features Correlated')
           CorrelatedFeatures.append(comment)
           DimensionalLines = SubElement(CorrelatedFeatures, "DimensionalLines")
           for DL in Feature_Manager._DetectedDimensionalLine:
               DimensionalLine = SubElement(DimensionalLines, "DimensionalLine")
               for ar in DL._ArrowHeads:
                        ArrowHead = SubElement(DimensionalLine, "ArrowHead")
                        p1 = ar._BoundingBoxP1
                        p2 = ar._BoundingBoxP2
                        center = ar._ArrowCenter
                        BoundingBoxPoint1 = SubElement(ArrowHead, "BoundingBoxPoint1")
                        X = SubElement(BoundingBoxPoint1, "X")
                        X.text = str(p1.x)
                        Y = SubElement(BoundingBoxPoint1, "Y")
                        Y.text = str(p1.y)
                        BoundingBoxPoint2 = SubElement(ArrowHead, "BoundingBoxPoint2")
                        X = SubElement(BoundingBoxPoint2, "X")
                        X.text = str(p2.x)
                        Y = SubElement(BoundingBoxPoint2, "Y")
                        Y.text = str(p2.y)
                        Centre = SubElement(ArrowHead, "Centre")
                        X = SubElement(Centre, "X")
                        X.text = str(center.x) 
                        Y = SubElement(Centre, "Y")
                        Y.text = str(center.y) 
                        Direction = SubElement(ArrowHead, "Direction")
                        Direction.text = str(ar._Direction)
               for ls in DL._Leaders:
                       Leaders = SubElement(DimensionalLine, "Leaders")
                       StartPoint = SubElement(Leaders, "StartPoint")
                       X = SubElement(StartPoint, "X")
                       X.text = str(ls.startPoint.x)
                       Y = SubElement(StartPoint, "Y")
                       Y.text = str(ls.startPoint.y)
                       EndPoint = SubElement(Leaders, "EndPoint")
                       X = SubElement(EndPoint, "X")
                       X.text = str(ls.endPoint.x)
                       Y = SubElement(EndPoint, "Y")
                       Y.text = str(ls.endPoint.y)
           Dimensions = SubElement(CorrelatedFeatures, "Dimensions")
           for D in Feature_Manager._DetectedDimension:
               Dimension = SubElement(Dimensions, "Dimension")
               DL = D._DimensionalLines
               DimensionalLine = SubElement(Dimension, "DimensionalLine")
               for ar in DL._ArrowHeads:
                        ArrowHead = SubElement(DimensionalLine, "ArrowHead")
                        p1 = ar._BoundingBoxP1
                        p2 = ar._BoundingBoxP2
                        center = ar._ArrowCenter
                        BoundingBoxPoint1 = SubElement(ArrowHead, "BoundingBoxPoint1")
                        X = SubElement(BoundingBoxPoint1, "X")
                        X.text = str(p1.x)
                        Y = SubElement(BoundingBoxPoint1, "Y")
                        Y.text = str(p1.y)
                        BoundingBoxPoint2 = SubElement(ArrowHead, "BoundingBoxPoint2")
                        X = SubElement(BoundingBoxPoint2, "X")
                        X.text = str(p2.x)
                        Y = SubElement(BoundingBoxPoint2, "Y")
                        Y.text = str(p2.y)
                        Centre = SubElement(ArrowHead, "Centre")
                        X = SubElement(Centre, "X")
                        X.text = str(center.x) 
                        Y = SubElement(Centre, "Y")
                        Y.text = str(center.y) 
                        Direction = SubElement(ArrowHead, "Direction")
                        Direction.text = str(ar._Direction)
               for ls in DL._Leaders:
                       Leaders = SubElement(DimensionalLine, "Leaders")
                       StartPoint = SubElement(Leaders, "StartPoint")
                       X = SubElement(StartPoint, "X")
                       X.text = str(ls.startPoint.x)
                       Y = SubElement(StartPoint, "Y")
                       Y.text = str(ls.startPoint.y)
                       EndPoint = SubElement(Leaders, "EndPoint")
                       X = SubElement(EndPoint, "X")
                       X.text = str(ls.endPoint.x)
                       Y = SubElement(EndPoint, "Y")
                       Y.text = str(ls.endPoint.y)
               DT = D._DimensionalText
               DimensionalText = SubElement(Dimension, "DimensionalText")
               Text = SubElement(DimensionalText, "Text")
               Text.text = DT._Text
               BoundingBoxPoint1 = SubElement(DimensionalText, "BoundingBoxPoint1")
               X = SubElement(BoundingBoxPoint1, "x")
               X.text = str(DT._TextBoxP1.x)
               Y = SubElement(BoundingBoxPoint1, "y")
               Y.text = str(DT._TextBoxP1.y)
               BoundingBoxPoint2 = SubElement(DimensionalText, "BoundingBoxPoint2")
               X = SubElement(BoundingBoxPoint2, "x")
               X.text = str(DT._TextBoxP2.x)
               Y = SubElement(BoundingBoxPoint2, "y")
               Y.text = str(DT._TextBoxP2.y)
               OrientationAngle = SubElement(DimensionalText, "OrientationAngle")
               OrientationAngle.text = str(DT._Orientation)
               SupportLines = SubElement(Dimension, "SupportLines")
               for sl in D._SupportLines:
                   SupportLine = SubElement(SupportLines, "SupportLine")
                   for sls in sl:
                       Segment = SubElement(SupportLine, "Segment")
                       StartPoint = SubElement(Segment, "StartPoint")
                       X = SubElement(StartPoint, "X")
                       X.text = str(sls.startPoint.x)
                       Y = SubElement(StartPoint, "Y")
                       Y.text = str(sls.startPoint.y)
                       EndPoint = SubElement(Segment, "EndPoint")
                       X = SubElement(EndPoint, "X")
                       X.text = str(sls.endPoint.x)
                       Y = SubElement(EndPoint, "Y")
                       Y.text = str(sls.endPoint.y)
           CorrelatedEntities = SubElement(CorrelatedFeatures, "CorrelatedEntities")
           for cE in Feature_Manager._CorrelatedEntities:
               Correlation = SubElement(CorrelatedEntities, "Correlation")
               Dimension = SubElement(Correlation, "Dimension")
               DL = cE._Dimension._DimensionalLines
               DimensionalLine = SubElement(Dimension, "DimensionalLine")
               for ar in DL._ArrowHeads:
                        ArrowHead = SubElement(DimensionalLine, "ArrowHead")
                        p1 = ar._BoundingBoxP1
                        p2 = ar._BoundingBoxP2
                        center = ar._ArrowCenter
                        BoundingBoxPoint1 = SubElement(ArrowHead, "BoundingBoxPoint1")
                        X = SubElement(BoundingBoxPoint1, "X")
                        X.text = str(p1.x)
                        Y = SubElement(BoundingBoxPoint1, "Y")
                        Y.text = str(p1.y)
                        BoundingBoxPoint2 = SubElement(ArrowHead, "BoundingBoxPoint2")
                        X = SubElement(BoundingBoxPoint2, "X")
                        X.text = str(p2.x)
                        Y = SubElement(BoundingBoxPoint2, "Y")
                        Y.text = str(p2.y)
                        Centre = SubElement(ArrowHead, "Centre")
                        X = SubElement(Centre, "X")
                        X.text = str(center.x) 
                        Y = SubElement(Centre, "Y")
                        Y.text = str(center.y) 
                        Direction = SubElement(ArrowHead, "Direction")
                        Direction.text = str(ar._Direction)
               for ls in DL._Leaders:
                       Leaders = SubElement(DimensionalLine, "Leaders")
                       StartPoint = SubElement(Leaders, "StartPoint")
                       X = SubElement(StartPoint, "X")
                       X.text = str(ls.startPoint.x)
                       Y = SubElement(StartPoint, "Y")
                       Y.text = str(ls.startPoint.y)
                       EndPoint = SubElement(Leaders, "EndPoint")
                       X = SubElement(EndPoint, "X")
                       X.text = str(ls.endPoint.x)
                       Y = SubElement(EndPoint, "Y")
                       Y.text = str(ls.endPoint.y)
               DT = cE._Dimension._DimensionalText
               DimensionalText = SubElement(Dimension, "DimensionalText")
               Text = SubElement(DimensionalText, "Text")
               Text.text = DT._Text
               BoundingBoxPoint1 = SubElement(DimensionalText, "BoundingBoxPoint1")
               X = SubElement(BoundingBoxPoint1, "x")
               X.text = str(DT._TextBoxP1.x)
               Y = SubElement(BoundingBoxPoint1, "y")
               Y.text = str(DT._TextBoxP1.y)
               BoundingBoxPoint2 = SubElement(DimensionalText, "BoundingBoxPoint2")
               X = SubElement(BoundingBoxPoint2, "x")
               X.text = str(DT._TextBoxP2.x)
               Y = SubElement(BoundingBoxPoint2, "y")
               Y.text = str(DT._TextBoxP2.y)
               OrientationAngle = SubElement(DimensionalText, "OrientationAngle")
               OrientationAngle.text = str(DT._Orientation)
               SupportLines = SubElement(Dimension, "SupportLines")
               for sl in cE._Dimension._SupportLines:
                   SupportLine = SubElement(SupportLines, "SupportLine")
                   for sls in sl:
                       Segment = SubElement(SupportLine, "Segment")
                       StartPoint = SubElement(Segment, "StartPoint")
                       X = SubElement(StartPoint, "X")
                       X.text = str(sls.startPoint.x)
                       Y = SubElement(StartPoint, "Y")
                       Y.text = str(sls.startPoint.y)
                       EndPoint = SubElement(Segment, "EndPoint")
                       X = SubElement(EndPoint, "X")
                       X.text = str(sls.endPoint.x)
                       Y = SubElement(EndPoint, "Y")
                       Y.text = str(sls.endPoint.y)
               Entity = SubElement(Correlation, "Entity")
               for e in cE._Entity:
                       Segment = SubElement(Entity, "Segment")
                       StartPoint = SubElement(Segment, "StartPoint")
                       X = SubElement(StartPoint, "X")
                       X.text = str(e.startPoint.x)
                       Y = SubElement(StartPoint, "Y")
                       Y.text = str(e.startPoint.y)
                       EndPoint = SubElement(Segment, "EndPoint")
                       X = SubElement(EndPoint, "X")
                       X.text = str(e.endPoint.x)
                       Y = SubElement(EndPoint, "Y")
                       Y.text = str(e.endPoint.y)
           tree = ET.ElementTree(Root)
           tree.write(make_dir_root + "/" + time_str +".I2C")