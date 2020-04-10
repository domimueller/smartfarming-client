#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#==========================================================================
# Authenticator.py – DESCRIPTIONS
#==========================================================================
'''

@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>

'''

#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

from wordpress_xmlrpc import Client


#==========================================================================
# CONSTANTS
#==========================================================================

URL = 'https://smartfarming.domi.dev.cubetech.ch/xmlrpc.php'


#==========================================================================
# FUNCTIONS
#==========================================================================
class Authenticator:
    """
    A class used to authenticate an User at a CMS.
    -------      

    Attributes
    ----------        
    cms : Client
        the gateway to the CMS XML-RPC interface


    Methods
    -------
   obtainCredentials(self, user):
        see Descripton below
    isValid(self, credentials):        
        see Descripton below    
    """

    def __init__(self):
        self.cms = None 
        
    def obtainCredentials(self, user):
        
        """ 
       
        Obtains Credentials of User.
        ----------        

        This function obtains Credentials of a User and returns it for further processing.
        ----------        
      
        Parameters: 
        ----------                
        user (User) : User, of whom the Credentials will be obtained          
      
        
        Returns: 
        ----------        
        Credentials: Credentials of the specified User 
      
        """                 
       
        # get Credentials
        credentials = user.identity
        return credentials
        

    def isValid(self, credentials):
        
        """ 
       
        Validates Credentials.
        -------              
      
        This function uses the Credentials as parameter to call the Client Class, which 
        is the gateway to the CMS XML-RPC interface. The Client class validates the Credentials.
        -------              
      
        Parameters: 
        -------              
        credentials (Credentials) : Credentials that will be validated          
      
        
        Returns: 
        -------              
        cms (Client) : the CMS XML-RPC interface
       
       """ 

        self.cms = Client(URL, credentials['user'], credentials['password'])

        return self.cms

#==========================================================================
# END
#==========================================================================
