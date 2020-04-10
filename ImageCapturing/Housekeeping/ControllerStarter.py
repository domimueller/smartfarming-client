#!/usr/bin/env python3
#-*- coding: utf-8 -*-


#==========================================================================
# ControllerStarter.py – DESCRIPTIONS
#==========================================================================

'''

@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>


'''


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

import os

#==========================================================================
# CONSTANTS
#==========================================================================

SHELL_COMAND = 'python3'
PATH_TO_SMARTFARMING = '/media/usb/smartfarming/ImageCapturing/Housekeeping/ImageController.py'

#==========================================================================
# FUNCTIONS
#==========================================================================
class ControllerStarter:
  
    """
    A class used to represent and implement the functionality for ControllerStarter.
    The only purpose of this class is to start the ImageController.
    ----------

    Attributes
    ----------        
    SHELL_COMAND : String
        the shell command to be used to execute the ImageController
    PATH_TO_SMARTFARMING : String
        path to the ImageController to be launched.
    """

    def main():
        
        """ 
       
        Starts the ImageController. 
        -------              
      
        This function will be executed after the startup of the minicomputer and only
        has the responsibility to start the ImageController.
        -------      

        Parameters: 
        -------              
        no parameters allowed.
        
        Returns: 
        -------              
        nothing will be returned. 
      
        """   
        
        os.system(SHELL_COMAND + ' ' +  PATH_TO_SMARTFARMING)


#==========================================================================
# MAIN
#==========================================================================
if __name__ == '__main__':
    ControllerStarter.main()

#==========================================================================
# END
#==========================================================================

