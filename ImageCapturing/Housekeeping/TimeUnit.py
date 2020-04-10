#!/usr/bin/env python3
#-*- coding: utf-8 -*-


#==========================================================================
# TimeUnit.py – DESCRIPTIONS
#==========================================================================

'''

@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>

'''

#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

from enum import Enum


#==========================================================================
# FUNCTIONS
#==========================================================================

class TimeUnit(Enum):
    
    """
    A class used to represent the enumeration of the possible Time Units
 
    """
    seconds = 1
    minutes = 2
    hours = 3
