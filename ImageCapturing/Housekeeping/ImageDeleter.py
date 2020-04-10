#!/usr/bin/env python3
#-*- coding: utf-8 -*-



#==========================================================================
# ImageDeleter.py – DESCRIPTIONS
#==========================================================================

'''

@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>

'''

#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

from wordpress_xmlrpc.methods import posts
import sys
sys.path.append('../../Security')

import Authenticator
import User
import PostConfiguration

#==========================================================================
# CONSTANTS
#=========================================================================

OFFSET = 0
INCREMENT = 71 # Achtung: Increment muss grösser als maxpost sein, sonst werden keine Posts gelöscht.
ORDERBY_FIELD = 'timestamp'
ORDER_DIRECTION = 'ASC'

#==========================================================================
# FUNCTIONS
#=========================================================================

class ImageDeleter:
  
    """
    A class used to represent and implement the functionality for Image Deletion in the CMS.

    ...

    Attributes
    ----------        
    cms : Client
        the gateway to the CMS XML-RPC interface
    images : dict
        the images queried from the cms
    post_configuration : PostConfiguration
        the Post Configuration for the cms


    Methods
    -------
    deleteImage()
        See description below.
    """

    def __init__(self):
        self.cms = None
        self.images = []

        # PostConfiguration according to Default-Values
        self.post_configuration = PostConfiguration.PostConfiguration()

        # Customizing of PostConfiguration possible with usage of **kwargs in __init__ of PostConfiguration. for instance:
        # self.post_configuration = PostConfiguration.PostConfiguration(post_type = 'kamerabild', post_status = 'publish', maxposts = 10)        

    def deleteImage(self ):
        
        """ 
       
        Delets Images.
        -------              
      
        This function deletes images in regard with the maxpost setting, that definies
        how many images are stored in the cms database. Per default, the oldest Images will be deleted
        due to the ORDER_DIRECTION = 'ASC' Constant.
        -------      

        Parameters: 
        -------              
        no parameter allowed (except self)        
      
        Returns: 
        -------              
        nothing will be returned. 
      
        """          
       
        # Authentication
        authenticator = Authenticator.Authenticator()
        credentials = authenticator.obtainCredentials(User.User())
        self.cms = authenticator.isValid(credentials)
        
        amount = OFFSET
        while True:
                ## Get posts serverfriendly 
                if 'post_type' in self.post_configuration.postBasicInformation:
                    self.images = self.cms.call(posts.GetPosts({'post_type': self.post_configuration.postBasicInformation.get('post_type'),'number': INCREMENT, 'offset': amount, 'orderby': ORDERBY_FIELD , 'order': ORDER_DIRECTION }))
                
                # Delete the oldest post
                for image in self.images:
                    if len(self.images) > self.post_configuration.postBasicInformation.get('maxposts'):
                        del self.images[-1]
                        self.cms.call(posts.DeletePost(image.id))
                        
                    else:
                        return                       
                        
                amount = amount + INCREMENT   


#==========================================================================
# END
#==========================================================================