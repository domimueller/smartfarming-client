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


#==========================================================================
# END
#==========================================================================
