#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# PostConfiguration.py – DESCRIPTIONS
#==========================================================================

'''

@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>

'''


#==========================================================================
#  CONSTANTS
#==========================================================================

DEFAULT_POST_STATUS = 'publish'
DEFAULT_POST_TYPE = 'kamerabild'
DEFAULT_MAXPOSTS = 70
IMAGE_FIELD = 'image'
DATE_FIELD = 'date'
TIME_FIELD = 'time'
TIMESTAMP_FIELD = 'timestamp'

#==========================================================================
# FUNCTIONS
#==========================================================================

class PostConfiguration:

    """
    A class used to represent the Post Configuration and for Configuration of 
    the Generation and Querying of Posts in CMS.
    -------          

    Attributes
    ----------
    postBasicInformation : dict
        Basic Post Configuration like post_type, post_status, maxposts. Writable via
        the **kwargs agrument in __init__
    postCustomFields : dict
        Custom Post Configuration like Image Field or Date Field in CMS.
        The Post Custom Fields are being changed via the corresponding Constants.


    """

    def __init__(self, **kwargs):
        
        """ 
       
        Sets the post settings. 
        ----------      
        
        This function sets custom values for post type, post status and
        maxposts if custom values are definied in the object initialization. If not, the
        function will set default values as provided from the Constants section. The Basic Post
        Configuration is configuratable, the postMetaFields only via Constants.
        ----------                
      
        Parameters: 
        ----------
        kwargs (dict): flexible number of key-value-pairs of the Post Settings. 

      
        """          

        self.postBasicInformation = {}

        if 'post_type' in kwargs:
            self.postBasicInformation['post_type'] = kwargs.get('post_type')
        else:
            self.postBasicInformation['post_type'] = DEFAULT_POST_TYPE          
                
        if 'post_status' in kwargs:
            self.postBasicInformation['post_status'] = kwargs.get('post_status')
        else:
            self.postBasicInformation['post_status'] = DEFAULT_POST_STATUS   


        if 'maxposts' in kwargs:
            self.postBasicInformation['maxposts'] = kwargs.get('maxposts')
        else:
            self.postBasicInformation['maxposts'] = DEFAULT_MAXPOSTS   
            
        self.postCustomFields = {
                'imageField' : IMAGE_FIELD,
                'dateField' : DATE_FIELD,
                'timeField' : TIME_FIELD,
                'timestampField' : TIMESTAMP_FIELD
        }

#==========================================================================
# END
#==========================================================================



