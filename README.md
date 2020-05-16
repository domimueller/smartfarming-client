# Description
A Project with Rasperry Pi 4 in order to take pictures in a particular intervall.  This pictures are being used to montior the birth process of cows or the infrastrucutre for hay harvesting.

# Person Responsible
Dominique Müller
dominique_mueller@gmx.ch

# IMPORTANT NOTES

To use the Client, please add a file named Credentials.json to the security package and insert your login data in the following format:

{
		"user": "<<your CMS username>>",
		"password": "<<your CMS Password>>" 
}

Furthermore, go to the file Authenticator.py and substitute the URL constant with the URL of your Webpage's REST-API. 

This Client is developed for the usage with a WordPress Website. Please register a Post Type named "kamerabild" to store and display the data. Other CMS might be used together with this software, in case they are providing a REST-API.


# Contributors And Acknowledgment
## The lecturers   
- Prof. Dr. Patrizio Collovà

For providing Guidance during the Project.


## The Sponsor of the Project and his wife  
- Nelly Müller
- Peter Müller

For proving knowledge and improving the results of image capturing with empirical work.

## The employer of the Author
- cubetech GmbH (www.cubetech.ch) and especially the CEO and Founder Christoph Ackermann

For providing the relevant server infrastructure.

