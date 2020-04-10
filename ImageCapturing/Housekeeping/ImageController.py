#!/usr/bin/env python3
#-*- coding: utf-8 -*-


#==========================================================================
# ImageController.py – DESCRIPTIONS 
#==========================================================================

"""
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>


"""


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

import schedule
import time
import sys
sys.path.append('/media/usb/smartfarming/ImageCapturing')
sys.path.append('/media/usb/smartfarming/ImageCapturing/Housekeeping')
sys.path.append('/media/usb/smartfarming/Housekeeping')
sys.path.append('/media/usb/smartfarming/Security')




import ImagesPerTimeUnit  
import CaptureSetting
import ImageDeleter  


import ImageProvider
import ImageCollector


#==========================================================================
# CONSTANTS
#==========================================================================

#Time Units for comparison with selected Time Unit according to amountPerTime
SECONDS = 'seconds'
MINUTES = 'minutes'
HOURS = 'hours'

#==========================================================================
# FUNCTIONS
#==========================================================================

def main():

    amountPerTime = ImagesPerTimeUnit.ImagesPerTimeUnit()
    imageProvider = ImageProvider.ImageProvider()
    imageDeleter = ImageDeleter.ImageDeleter()       
    
    ImageController(amountPerTime = amountPerTime, provider = imageProvider,  deleter = imageDeleter) 


class ImageController:

    """
    A class used to represent and implement the functionality for the Image Controller.
    Controls the point in time, the filenaming and the managing of other classes in the project.

    ...

    Attributes
        ----------        
    amountPerTime : amountPerTime
        Value Object for the numbers of Images captured per Time Unit.
    provider : ImageProvider
        brings the data and functionality of the ImageProvider
    deleter : ImageDeleter
        brings the data and functionality of the ImageDeleter
    collector : ImageCollector
        brings the data and functionality of the ImageCollector
    setting : CaptureSetting
        Setting for the Camera and Image Capturing. f.e. iso-value 


    Methods
    -------
    planCapturing(self, amountPerTime)
    controlImageCollector(self)
    controlImageDeleter(self) 
    controlImageDeleter(self)     
         See descriptions below.

    """    

    def __init__(self, amountPerTime, provider, deleter):
        
        self.amountPerTime = amountPerTime
        self.provider = provider
        self.deleter = deleter
        self.setting = None
        self.collector = None

        
        self.planCapturing(amountPerTime)

    def planCapturing(self, amountPerTime):

        """ 
       
        Controls the Execution of the Image Provider.
        -------              
      
        This function plans and schedules the Execution of the Image Provider. 
        -------              
      
        Parameters: 
        -------              
        amountPerTime (String): definies how many Images per seconds, minute or hour will be captured.
        provider (ImageProvider): brings the functionality for Image Providing
        
        Returns: 
        -------              
        nothing will be returned. 
      
        """   
        
        
        #execute function controlImageProvider according to Value Object amountPerTime 
        if self.amountPerTime.unit == SECONDS :
            schedule.every(self.amountPerTime.number).seconds.do(self.controlImageProvider)  
            
        elif self.amountPerTime.unit == MINUTES :
            schedule.every(self.amountPerTime.number).minutes.do(self.controlImageProvider)      

        elif self.amountPerTime.unit == HOURS :
            schedule.every(self.amountPerTime.number).hours.do(self.controlImageProvider) 

        else:
            schedule.every().hour.do(self.controlImageProvider)         
        
        while True:
            schedule.run_pending()            
            time.sleep(1)
            

    def controlImageProvider(self):
        
        """ 
       
        Controls the Execution of the Image Capturing.
        -------              
            
        Parameters: 
        -------              
        no parameter allowed (except self)
        
        Returns: 
        -------              
        nothing will be returned. 
      
        """   
        self.setting = CaptureSetting.CaptureSetting( filename = time.time() )    
        self.provider.triggerImageCapture(setting = self.setting )  
        self.controlImageCollector() 

    def controlImageCollector(self ):
        
        
        """ 
       
        Controls the Execution of the Image Collector.
        -------              
            
        Parameters: 
        -------              
        no parameter allowed (except self)
        
        Returns: 
        -------              
        nothing will be returned. 
      
        """
        
        try: 
            self.collector = ImageCollector.ImageCollector( setting = self.setting )
            self.controlImageDeleter()        
        except: 
            print("Es ist etwas schief gelaufen. Vermutlich hat der Smartfarmer keine Internetverbindung. Versuche es später erneut.")
     

    def controlImageDeleter(self):
        
        """ 
       
        Controls the Execution of the Image Deletion.
        -------              
            
        Parameters: 
        -------              
        no parameter allowed (except self)
        
        Returns: 
        -------              
        nothing will be returned. 
        
        """
          
        self.deleter.deleteImage()
         

#==========================================================================
# MAIN
#==========================================================================

if __name__ == '__main__':
    main()
       
#==========================================================================
# END
#==========================================================================




