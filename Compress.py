# ---------------------------------------------------------------------------
# Compress.py
#
# Description:  This script looks for an SDE admin account sde file and
# compresses the enterprise FGDB that the sde file points to.
#
# The 'pudConnectionFile' variable will need to be changed to match the SDE admin
# account on whatever computer the script is ran from.
# It will also write a log file if you change the 'fileLog' variable.
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy, logging
from datetime import datetime

#-------------------------------------------------------------------------------
#             Set variables that may change from computer to computer
# Local variables:
sdeConnectionFile = "Database Connections\\sde@atlas-edit.sde"

#  Where do you want the log file to go???
fileLog = r'C:\Users\mgrue\Scratch\Compress.log'

#-------------------------------------------------------------------------------
#                   Set variables that shouldn't change
#Flag for errors or not
success = True

#-------------------------------------------------------------------------------
try:
    #                      Set up logger
    #If you need to debug, set the level=logging.INFO to logging.DEBUG

    logging.basicConfig(filename = fileLog, level=logging.DEBUG)

    #Header for the log file
    logging.info('-----------------------------------------------------------' )
    logging.info('                  ' + str(datetime.now()))
    logging.info('                Running Analyze_AllPUDDatasets.py')
    logging.info('-----------------------------------------------------------' )
except:
    print 'WARNING \n fileLog path may not exist.'
#-------------------------------------------------------------------------------
try:
    # PROCESS: Compress
    print ('Starting compress using connection file: ' + sdeConnectionFile)
    logging.info('Starting compress using connection file: ' + sdeConnectionFile)

    arcpy.Compress_management(sdeConnectionFile)

except Exception as e:
    print 'ERROR!!!'
    logging.info('ERROR!!!')
    print str(e)
    logging.info(str(e))
    success = False

#-------------------------------------------------------------------------------
#              Print final message based on if successful or not

if success == True:
    print 'SUCCESS \nDone running Compress.py'
    logging.info('SUCCESS \n           Done running Compress.py')

else:
    print 'ERROR \n Check log at: ' + fileLog
    logging.info('ERROR \n             Check log at: ' + fileLog)

logging.info('--------------------------------------------------------------')
logging.info('                  ' + str(datetime.now()))
logging.info('                   Finished running script')
logging.info('--------------------------------------------------------------\n')
