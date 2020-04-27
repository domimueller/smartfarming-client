#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# ImageProvider.py – DESCRIPTIONS
#==========================================================================

'''

@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>


'''


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

import picamera
import cv2
#==========================================================================
# CONSTANTS
#==========================================================================

#==========================================================================
# FUNCTIONS
#==========================================================================

class ImageProvider:

   """
    A class used to represent and implement the functionality for ImageProvider. 
    The responsibility of the class is to send the relevant information for the
    image capturing to the camera driver.
    -------      

    Attributes
    ----------        
    setting : CaptureSetting
        Setting for the camera, the camera driver respectively.



    Methods
    -------
    triggerImageCapture(self, setting)
        See description below.
    """    

   def equalize_clahe_color_hsv(img):
        """Equalize the image splitting it after conversion to HSV and applying CLAHE
        to the V channel and merging the channels and convert back to BGR
        """
    
        cla = cv2.createCLAHE(clipLimit=4.0)
        H, S, V = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
        eq_V = cla.apply(V)
        eq_image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2BGR)
        return eq_image
    

   def triggerImageCapture(self, setting):
        
        """ 
       
        Triggers the CameraDriver of the Minicomputer. 
        -------      
        
        This function is responsible for the Image Capturing as definied in the 
        CaptureSettings.
        -------      

        Parameters: 
        -------              
        setting (CaptureSetting): Setting concerning the Image capturing. Relevant information
        are: iso, widht, height and the path where the image will be stored.
        
        Returns: 
        -------              
        nothing will be returned. 
      
        """    

        self.setting = setting
        
        
        with picamera.PiCamera() as camera:
        

            camera.resolution = (self.setting.width, self.setting.height ) #resolution
            camera.rotation = 90
            camera.iso = self.setting.iso
            camera.start_preview()
            camera.capture(self.setting.filepath+str(self.setting.filename)+ self.setting.mimetype.extension)    
            camera.stop_preview()
            
            print('Datei mit Dateiname ' + str(self.setting.filename) + ' erstellt!')
            self.setting.filename = self.equalize_clahe_color_hsv(self.setting.filename)

    
        

#==========================================================================
# END
#==========================================================================
