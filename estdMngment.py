#~ #!usr/bin/python
#~
#~ DESCRIPTION: 
#~ Hotel Room management system
#~ : system is supposed to access previous data
#~ from available file of previous current_process
#~ if previous customer is available it will allow booking otherwise 
#~ ask for registration of the said customer 
#~ 
#~ current scenario: 
  #~   menu : 
   #~      1 accept new entry to customer dictionary
   #~      2 allocate room if available 
   #~      3 query if a certain room is available for booking purposes
   #~      4 display all consumed rooms of the hotel
   #~      5 display the details of the user provided the userID given is true and available
#~    
#~    

from os import *   
try:
    raw_input             #Python2.x
except NameError:
    raw_input = input     #Python3.x

def raw_start(val):
    ''' Start a Raw Database for the code 
         or allow access to previously created database '''
    pass

def accessPrevious(filename):
    ''' Access previous records of a user '''
    pass

def roomAvailable(roomNo):
    '''  Return information of a room availability'''
    pass

def databaseTraceback(filepath,'IDcontrol'):
    ''' traceback for fetching ID of user/staff '''
    pass
def databaseTraceback(filepath,'BookAccess'):
    ''' traceback for access to booking data '''
    pass
def databaseTraceback(filepath,'RoomDetail'):
    ''' traceback for fetching details of room  '''
    pass

def userNewReg(details):
    ''' Register a new user to the system'''
    pass

def estNewDetails(details):
    ''' Register a new Establishment to the system'''
    pass

def newRoomDetail(fields):
    ''' Add information a new availability of a room
         to an already existing establishment '''
    pass

def newStaffDetails(fields):
    ''' Add details of newly recruited staff '''
    #~ access to this function is only allowed if user has root access/Owner access
    pass

def bookAccess(estd,room,usrid):
    ''' Add booking details for a new user on site '''
    #~ access to this function is restricted to staff/owner 
    pass

def checkBooked(estd,room):
    ''' Check booking status of a given room '''
    #~ access locked to the site package(allowed to staff/owner)
    #~ not accessible to users
    pass

def masterControl(codeid,passkey):
    ''' UserEnd '''
    db1=databaseTraceback(filepath,'BookAccess')
    pass
def masterControl(codeid,passkey,staffID):
    ''' StaffEnd '''
    db1=databaseTraceback(filepath,'BookAccess')
    db2=databaseTraceback(filepath,'RoomDetail')
    pass
def AccessControl(codeid,passkey):
    rootAccess=(estOwner1654, pass956487)
    acCtrl=(codeid,passkey)
    ctrlIDm=False
    if acCtrl is rootAccess:
        ctrlIDm=True
    path2folder=raw_input('Enter path to the folder :')
    dbx=databaseTraceback(path2folder,'IDcontrol')
    dbxS=dbx.next()             # staffend
    dbxU=dbx.next()             # userend 
    if codeid in dbxS:
        staffID=raw_input(" Input Staff ID ")
        masterControl(codeid,passkey,staffID)
    elif codeid in dbxU:
        sterControl(codeid,passkey)
    else:
        print(" Data not existent in the database ")
    

    

    