#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# ImageCollector.py – DESCRIPTIONS
#==========================================================================

'''
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>

'''

#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.methods import media
from wordpress_xmlrpc.compat import xmlrpc_client
import time
import sys
sys.path.append('Housekeeping/')
sys.path.append('../Security')

import PostConfiguration
import Authenticator
import User



#==========================================================================
# CONSTANTS
#==========================================================================


#==========================================================================
# FUNCTIONS
#==========================================================================

class ImageCollector:
 
    """
    A class used to represent and implement the Image Collector.
    Sends Image with corresponding information to the cms.
    ----------        
    
    ...

    Attributes
    ----------        
    image : dict
        key-value pair to upload data to the cms
    date : dict
        key-value pair to upload data to the cms
    time : dict
        key-value pair to upload data to the cms
    timestamp : dict
        key-value pair to upload data to the cms
    cms : Client
        the gateway to the CMS XML-RPC interface
    metadata : dict
        key-value pair to upload meta data to the cms
    setting : CaptureSetting
        camera setting information
    attachmentID : int
        ID of the Image in the context of the CMS Database   
    post_configuration : PostConfiguration
        information used to upload the image (f.e. post status or post type)        
        
    Methods
    -------
    createPost( self.attachmentID)  
        See description below.
    uploadImage(self, setting):
        See description below.

    """

    def __init__(self, setting ):
        self.image = None
        self.time = None
        self.cms = None
        self.metadata = []
        self.setting = setting
        self.attachmentID = None
        

        self.post_configuration = PostConfiguration.PostConfiguration()

        
        self.attachmentID = self.uploadImage( setting = self.setting)
        self.createPost( self.attachmentID)        

    def uploadImage(self, setting):
        
        """ 
       
        Uploads Images to CMS.
        ----------        

      
        After successfull Authentication, this function sets a name, fileformat and
        Mimetype to an Image and uploads it to CMS.
        ----------        
         
      
        Parameters: 
        ----------        
        setting (CaptureSetting): Setting concerning the Image capturing. Relevant information
        are: path to the captured image, fileformat and mimetype.
        
        Returns: 
        ----------        
        int: ID of the Image in the context of the CMS Database (attachementID). 
      
        """
        
        # convert timestamp in struct time: object with named tuple interface
        self.time = time.localtime(self.setting.filename)
        
        # Authentification 
        authenticator = Authenticator.Authenticator()
        credentials = authenticator.obtainCredentials(User.User())
        self.cms = authenticator.isValid(credentials)
        
        
        # Address the file to be uploaded
        path_and_filename = setting.filepath + str(setting.filename) + setting.mimetype.extension   
        
        # Metadata
        self.metadata = {
                'name': str(self.setting.filename) + setting.mimetype.extension,
                'type': self.setting.mimetype.value()  
        }
        
        # read binary fileand encode with XMLRPC library in base64
        with open(path_and_filename, 'rb') as image:
                self.metadata['bits'] = xmlrpc_client.Binary(image.read())

         # Upload the image     
        response = self.cms.call(media.UploadFile(self.metadata))
        self.attachmentID = response['id']
        return self.attachmentID        

    def createPost(self, attachmentID):
        
        """ 
       
        Creates Posts in CMS. 
        ----------        

        After successfull Authentication, this function sets a post title, post status and 
        generates the post with the postmeta fields for the image, date and time. 
        ----------              
        
        Parameters: 
        ----------        
        attachmentID (int): ID of the Image, that should be attached to the post.
        
        Returns: 
        ----------        
        nothing will be returned. 
      
        """        
        
        # Generate Post Object
        post = WordPressPost()
        post.post_type = self.post_configuration.postBasicInformation.get('post_type')
        post.title = time.strftime("%A, %d, %B um %H:%M:%S", self.time)



         # Authentification 
        authenticator = Authenticator.Authenticator()
        credentials = authenticator.obtainCredentials(User.User())
        cms = authenticator.isValid(credentials)
        post = WordPressPost()
        
        if 'post_type' in self.post_configuration.postBasicInformation:
            post.post_type = self.post_configuration.postBasicInformation.get('post_type')
            
        post.title = time.strftime("%A, %d, %B um %H:%M:%S", self.time)

        # Prepare Key-Value-Pairs for upload to CMS
        custom_post_configuration = self.post_configuration.postCustomFields
        
        if 'imageField' in custom_post_configuration:
            self.image = {
                    'key' : custom_post_configuration.get('imageField'),
                    'value' : self.attachmentID  
            }

        if 'dateField' in custom_post_configuration:
            self.date = {
                    'key' : custom_post_configuration.get('dateField'),
                    'value' :  time.strftime("%Y%m%d", self.time)  # zum Beispiel 20190116, also %Y%m%e
                    
            }
        
        if 'timeField' in custom_post_configuration:    
            self.time = {
                    'key' : custom_post_configuration.get('timeField'),
                    'value' : time.strftime("%T", self.time)  # zum Beispiel 02:12:17, also %T --> entspricht %H:%M:%S        
            }

        if 'timestampField' in custom_post_configuration:    
            self.timestamp = {
                    'key' : custom_post_configuration.get('timestampField'),
                    'value' : self.setting.filename  
            }
        
        # create list with the key-value-pairs
        post.custom_fields = [self.image, self.date, self.time, self.timestamp]
        
        
        # publish the Posts according to the default setting or set different post status according to PostBasicInformation. 
        if 'post_status' in self.post_configuration.postBasicInformation:
            post.post_status = self.post_configuration.postBasicInformation.get('post_status')        
        
        # Generate the post 
        cms.call(NewPost(post))        
        
    
#==========================================================================
# END
#==========================================================================