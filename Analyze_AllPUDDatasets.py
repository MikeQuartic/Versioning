# ---------------------------------------------------------------------------
# Analyze_AllPUDDatasets.py

# Description:  This script looks for a PUD admin account sde file and
# Analyzes the PUD datasets for the enterprise FGDB that the PUD file points to.
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
pudConnectionFile = "Database Connections\\pud@atlas-editdev.sde"

#  Where do you want the log file to go???
fileLog = r'C:\Users\mgrue\Scratch\Analyze_AllPUDDatasets.log'

#-------------------------------------------------------------------------------
#                   Set variables that shouldn't change
#Flag for errors or not
success = True

PUD_Datasets = ['EDIT.PUD.WATER', 'EDIT.PUD.SEWER', 'EDIT.PUD.RECYCLED',
                'EDIT.PUD.CATHODIC_PROTECTION', 'EDIT.PUD.MISC']

PUD_Datasets = ['EDITDEV.PUD.WATER', 'EDITDEV.PUD.SEWER', 'EDITDEV.PUD.RECYCLED',
                'EDITDEV.PUD.CATHODIC_PROTECTION', 'EDITDEV.PUD.MISC']

#-------------------------------------------------------------------------------
try:

    #                                   Set up logger
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
    print 'Changing workspace to: ' + pudConnectionFile
    logging.info('Changing workspace to: ' + pudConnectionFile)

    arcpy.env.workspace = pudConnectionFile
    allDatasets = arcpy.ListDatasets()

    for data_set in allDatasets:
        if data_set in PUD_Datasets:
            print 'Analyzing: ' + data_set + ' data set'
            logging.info('Analyzing: ' + data_set + ' data set')
            arcpy.Analyze_management(data_set, 'BUSINESS;FEATURE')

except Exception as e:
    print '\nERROR!!!'
    logging.info('ERROR!!!')
    print str(e)
    logging.info(str(e))
    success = False

#-------------------------------------------------------------------------------
#              Print final message based on if successful or not

if success == True:
    print '\nSUCCESS \n           Done running Analyze_AllPUDDatasets.py'
    logging.info('SUCCESS \n           Done running Analyze_AllPUDDatasets.py')

else:
    print '\nERROR \n      Check log at: ' + fileLog
    logging.info('ERROR \n      Check log at: ' + fileLog)


logging.info('--------------------------------------------------------------')
logging.info('                  ' + str(datetime.now()))
logging.info('                   Finished running script')
logging.info('--------------------------------------------------------------\n')



