#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# ImagesPerTimeUnit.py – DESCRIPTIONS
#==========================================================================

'''

@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>


'''


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

import TimeUnit


#==========================================================================
# CONSTANTS
#==========================================================================

NUMBER = 3
ENUM_SELECT = 2


#==========================================================================
# FUNCTIONS
#==========================================================================

class ImagesPerTimeUnit:
   
    """
    A class used to represent the Value Object for the numbers of
    Images captured per Time Unit.
    -------      
    
    Possible Values for  ENUM_SELECT:
    - 1 corresponds to seconds
    - 2 corresponds to minutes
    - 3 corresponds to hours

    Any other Values are not allowed and end up with an error message.    
    -------      

    Attributes
    ----------
    number : int
        Number of Images captured per Time Unit.
    unit : int
        Corresponding to the Time Unit: seconds, minutes or hours


    """    


    def __init__(self):
        
        """ 
       
        Definies the number of images captured per TimeUnit.
        ----------        
      
        This function sets the Number of images and Selects a TimeUnit from the 
        TimeUnit enumeration.
        ----------                
      
        Parameters: 
        ----------        
        no parameter allowed (except self)        
      
        Returns: 
        ----------                
        nothing will be returned. 
      
        """                 
        self.number = NUMBER
        
        time_unit_enum = TimeUnit.TimeUnit
        time_unit_enum_selection = time_unit_enum(ENUM_SELECT)
        time_unit_enum_name = time_unit_enum_selection.name
    
        self.unit = time_unit_enum_name

#==========================================================================
# END
#==========================================================================


