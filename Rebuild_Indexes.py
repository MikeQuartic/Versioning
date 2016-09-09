# ---------------------------------------------------------------------------
# Rebuild_Indexes.py

# Description:  This script looks for an SDE admin account sde file and
# builds indexes for the enterprise FGDB that the sde file points to.
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
sdeConnectionFile = "Database Connections\\sde@atlas-editdev.sde"

#  Where do you want the log file to go???
fileLog = r'C:\Users\mgrue\Scratch\Rebuild_Indexes.log'

#-------------------------------------------------------------------------------
#                   Set variables that shouldn't change
#Flag for errors or not
success = True

#-------------------------------------------------------------------------------
try:
    #                        Set up logger
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

    # Process: Rebuild Indexes
    """
    This tool is used in databases and enterprise, workgroup, and desktop
    geodatabases to rebuild existing attribute or spatial indexes. In enterprise,
    workgroup, and desktop geodatabases, indexes can also be rebuilt on states and
    state_lineage geodatabase system tables and the delta tables of versioned
    datasets. Out-of-date indexes can lead to poor query performance.
    """
try:
    print 'Rebuilding Indexes at: ' + sdeConnectionFile
    logging.info('Rebuilding Indexes')

    arcpy.RebuildIndexes_management(sdeConnectionFile, "SYSTEM", "", "ALL")


except Exception as e:
    print 'ERROR!!!'
    logging.info('ERROR!!!')
    print str(e)
    logging.info(str(e))
    success = False

#-------------------------------------------------------------------------------
#              Print final message based on if successful or not

if success == True:
    print '\nSUCCESS \n           Done running Rebuild_Indexes.py'
    logging.info('SUCCESS \n           Done running Rebuild_Indexes.py')

else:
    print '\nERROR \n      Check log at: ' + fileLog
    logging.info('ERROR \n      Check log at: ' + fileLog)

logging.info('--------------------------------------------------------------')
logging.info('                  ' + str(datetime.now()))
logging.info('                   Finished running script')
logging.info('--------------------------------------------------------------\n')

