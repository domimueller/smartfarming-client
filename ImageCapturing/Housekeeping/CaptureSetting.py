#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# CaptureSetting.py – DESCRIPTIONS
#==========================================================================

'''

@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>


'''
#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================
import sys
sys.path.append('/media/usb/smartfarming/ImageCapturing/Housekeeping')
import MimeType

#==========================================================================
# CONSTANTS
#==========================================================================

DEFAULT_ISO = 800
DEFAULT_WIDTH = 2592
DEFAULT_HEIGHT = 1944
DEFAULT_FILEPATH = '/media/usb/smartfarming/ImageCapturing/Housekeeping/images/'
DEFAULT_FILENAME = 'Unbekannte Datei'
DEFAULT_FILEFORMAT = '.jpg'
DEFAULT_MIME_MAJOR = 'image'
DEFAULT_MIME_MINOR = 'jpeg'




#==========================================================================
# FUNCTIONS
#==========================================================================

class CaptureSetting:
  
    """
    A class used to represent and implement the functionality for Capture Setting. 
    This includes the setting for the camera.
    -------          

    Attributes
    ----------        
    iso : int
        iso setting for camera. influences the brightness/ darkness of the image 
    width : int
        width of the image
    height : int
        height of the image
    filepath : String
        path where the image will be stored
    mimetype : MimeType
        mimetype of the image


    """    
    def __init__(self, **kwargs):
        
        """ 
       
        Sets the capture settings. 
        ----------        

      
        This function sets custom values for iso, width, height, path  and
        mimetype if custom values are definied in the object initialization. If not, the
        function will set default values as provided of the Constants section.
        ----------        
      
        Parameters: 
        ----------        
        kwargs (dict): flexible number of key-value-pairs of the Capture Settings. 

      
        """           
       
        if 'iso' in kwargs:
            self.iso  = kwargs.get('iso')
        else:
            self.iso = DEFAULT_ISO          
            
        if 'width' in kwargs:
            self.width  = kwargs.get('width')
        else:
            self.width = DEFAULT_WIDTH   

        if 'height' in kwargs:
            self.height  = kwargs.get('height')
        else:
            self.height = DEFAULT_HEIGHT   

        if 'filepath' in kwargs:
            self.filepath  = kwargs.get('filepath')
        else:
            self.filepath  = DEFAULT_FILEPATH   
        
        if 'filename' in kwargs:
            self.filename  = kwargs.get('filename')
        else:
            self.filename  = DEFAULT_FILENAME              

        #MimeType is beeing configured via Constants from above
        self.mimetype = MimeType.MimeType( major = DEFAULT_MIME_MAJOR, minor = DEFAULT_MIME_MINOR,  extension = DEFAULT_FILEFORMAT) 




#==========================================================================
# END
#==========================================================================