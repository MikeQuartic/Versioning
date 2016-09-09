# ---------------------------------------------------------------------------
# Name:     PostToDefault.py

# Description:  This script automates the Reconcile and Post process.
# Conflicts are detected and resolved between DEFAULT and the PUD_Staging
# version according to the rules set in the script (reconcile).
# Then PUD_Staging version is Posted to DEFAULT (Post).
#
#
# The 'pudConnectionFile' variable will need to be changed to match the admin
# account on whatever computer the script is ran from.
# It will also write a log file if you change the 'fileLog' variable.
# It will also write a log file from ESRI if you cahnge the 'esriLog' variable.
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy, logging
from datetime import datetime
arcpy.env.overwriteOutput = True

#-------------------------------------------------------------------------------
#             Set variables that may change from computer to computer
# Connection file:
pudConnectionFile = "Database Connections\\pud@atlas-edit.sde"

#  Where do you want the log file to go???
fileLog = r'C:\Users\mgrue\Scratch\PostToDefault.log'

#This is the log file that ESRI will create with the
#ReconcileVersions_management tool

esriLog = "C:/Users/mgrue/Scratch/ReconcileVersionsLog/ReconcileVersions.log"

#-------------------------------------------------------------------------------
#                   Set variables that shouldn't change
#Flag for errors or not
success = True

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
#****************************  BEGIN MAIN  *************************************
#-------------------------------------------------------------------------------
try:

    print 'Setting workspace to: ' + pudConnectionFile
    logging.info('Setting workspace to: ' + pudConnectionFile)

    arcpy.env.workspace = pudConnectionFile

#-------------------------------------------------------------------------------
#                    Set and Explain the Variables for tool

    input_database = pudConnectionFile
    reconcile_mode="ALL_VERSIONS"

    #This is the parent version or DEFAULT
    target_version="SDE.DEFAULT"

    #Edited child version that we want to have reconciled with the parent
    edit_versions=""""AD\PUDSUPERVISOR".PUD_Staging"""

    #We want to acquire a lock so that we can post to the parent version after
    #the reconciliation
    acquire_locks="LOCK_ACQUIRED"

    #I'm not sure if this one is correct.  The two options are: ABORT_CONFLICTS
    #and NO_ABORT.  If we choose to ABORT_CONFLICTS, then if there are conflicts
    #the script will stop running, this is the safer option,
    #but may be unnecessary
    abort_if_conflicts="ABORT_CONFLICTS"

    #There are two options here:
    #BY_OBJECT?Any changes to the same row or feature in the parent and
    #     child versions will conflict during reconcile. This is the default.
    #BY_ATTRIBUTE?Only changes to the same attribute (column) of the same row
    #     or feature in the parent and child versions will be flagged as a
    #     conflict during reconcile. Changes to different attributes will not
    #     be considered a conflict during reconcile.
    conflict_definition="BY_OBJECT"

    #Will only be used if we change ABORT_CONFLICTS to NO_ABORT
    conflict_resolution="FAVOR_TARGET_VERSION"

    #We want to post the changes
    with_post="POST"

    #We want to keep the PUD_Staging version
    with_delete="KEEP_VERSION"

    #Variable set at the beginning of the script.  This is the log file that
    #Esri will create when the script is run.
    out_log=esriLog

#-------------------------------------------------------------------------------
#                               Run Tool

    print 'Starting to Reconcile: ' + target_version + ' to ' + edit_versions
    logging.info('Starting to Reconcile: ' + target_version + ' to ' + edit_versions)
    print 'And then Post: ' + edit_versions + ' to ' + target_version
    logging.info('And then Post: ' + edit_versions + ' to ' + target_version)

    #Process
    arcpy.ReconcileVersions_management (input_database, reconcile_mode, target_version,
                                  edit_versions, acquire_locks, abort_if_conflicts,
                                  conflict_definition, conflict_resolution,
                                  with_post, with_delete, out_log)

except Exception as e:
    print '\nERROR!!!'
    logging.info('ERROR!!!')
    print str(e)
    logging.info(str(e))
    success = False

#-------------------------------------------------------------------------------
#******************************  END MAIN  *************************************
#-------------------------------------------------------------------------------
#              Print final message based on if successful or not

if success == True:
    print '\nSUCCESS \n           Done running PostToDefault.py'
    logging.info('SUCCESS \n           Done running PostToDefault.py')

else:
    print '\nERROR \n      Check log at: ' + fileLog
    logging.info('ERROR \n      Check log at: ' + fileLog)


logging.info('--------------------------------------------------------------')
logging.info('                  ' + str(datetime.now()))
logging.info('                   Finished running script')
logging.info('--------------------------------------------------------------\n')