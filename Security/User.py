#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# User.py– DESCRIPTIONS
#==========================================================================

'''

@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>

'''

#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

import json


#==========================================================================
# CONSTANTS
#==========================================================================

IDENTITY_FILE_PATH = '/media/usb/smartfarming/Security/Credentials.json'


#==========================================================================
# FUNCTIONS
#==========================================================================

class User:
    
    """
    class used to represent an User.
    -------      
    ...

    Attributes
    ----------        
    identity : Credentials
        represents identity and login information to CMS,
    """

    def __init__(self):
        
        self.identity = json.load(open(IDENTITY_FILE_PATH, 'r'))


#==========================================================================
# END
#==========================================================================




