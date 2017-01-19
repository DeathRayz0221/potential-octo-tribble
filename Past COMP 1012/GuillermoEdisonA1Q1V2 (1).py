# -*- coding: utf-8 -*-
"""

COMP 1012 SECTION A03
INSTRUCTOR: Janjic
ASSIGNMENT: Assignment 1
AUTHOR      Edison Guillermo
VERSION     2016-Jan-7
PURPOSE:    To design a staircase

"""
# imports
import math 
import time

# Constants
CM_PER_INCH = 2.54 # [cm/in] Conversion factor (exact)
                   # from http://physics.nist.gov/Pubs/SP811/appenB9.html#LENGTH
MM_PER_CM = 10 # [mm/cm] standard metric conversion
MM_PER_IN = CM_PER_INCH * MM_PER_CM # [mm/in] conversion factor
TWO_INCH = 1.5 # [in] thickness of 2 inch board
SIX_INCH = 5.5 # [in] width of 5 inch board

CM_SQ_PER_IN_SQ = CM_PER_INCH**2 # [cm^2/in^2]
MM_SQ_PER_CM_SQ = MM_PER_CM**2 # [mm^2/cm^2]
MM_SQ_PER_IN_SQ = CM_SQ_PER_IN_SQ * MM_SQ_PER_CM_SQ # [mm^2/in^2]

RAD_DEG = math.degrees(1) # [deg]

# The following are from http://www.cmhc- schl.gc.ca/en/co/acho/acho_012.cfm]
MIN_RISE_MM = 125 # [mm] limit on allowed rise
MAX_RISE_MM = 200 # [mm] limit on allowed rise

MIN_RISE_P_RUN_IN = 17 # [in]
MAX_RISE_P_RUN_IN = 17.5 # [in]

MIN_TWOXRISE_P_RUN_IN = 24 # [in]
MAX_TWOXRISE_P_RUN_IN = 25 # [in]

MIN_RISEXRUN_IN = 70 # [in]
MAX_RISEXRUN_IN = 75 # [in]

MAX_BALUSTER_GAP_IN = 10 / CM_PER_INCH # [in]
MAX_BALUSTER_GAP_MM = MAX_BALUSTER_GAP_IN * MM_PER_IN # [mm]



# Dimensions
hh = 39.5 # [in] total rise from ground to landing
WIDTH_BALUSTER = TWO_INCH # [in] thickness of baluster

# Calculations
aveRise = (MIN_RISE_MM + MAX_RISE_MM)/2 # [mm]
nPlusOne = math.floor(hh/(aveRise/MM_PER_IN))  #  n+1 in equation for rise
steps = nPlusOne - 1 #number of steps

riseInIN = (hh)/(nPlusOne) # [in]
riseInMM = riseInIN * MM_PER_IN # [mm]

runInIN = 17.5 - riseInIN # [in] 
runInMM = runInIN * MM_PER_IN # [mm]
stringers= 3 # no of stringers

MIN_THREAD_IN = 235 / MM_PER_IN # [in] 
if runInIN > MIN_THREAD_IN :
    MIN_THREAD_IN = runInIN # change boundary if run is more than 235 mm 
MAX_THREAD_IN = (runInMM + 25) / MM_PER_IN # [in] 

risePlusRunIN = riseInIN+runInIN #[in] Rise+Run
risePlusRunMM = risePlusRunIN * MM_PER_IN #[mm] Rise+Run
risePlusRunCheck = (MIN_RISE_P_RUN_IN <=  risePlusRunMM and
    risePlusRunIN <= MAX_RISE_P_RUN_IN) 
    #boolean if rise+run is within boundaries

twoXRisePlusRunIN = 2*riseInIN+runInIN # [in] 2*Rise+Run
twoXRisePlusRunMM = twoXRisePlusRunIN * MM_PER_IN # [mm] 2*Rise+Run
twoXRisePlusRunCheck = (MIN_TWOXRISE_P_RUN_IN <=  twoXRisePlusRunIN and
    twoXRisePlusRunIN <= MAX_TWOXRISE_P_RUN_IN)
    #boolean if 2*rise + run is within boundaries

riseXRunIN = riseInIN*runInIN # [in^2] Rise*Run
riseXRunMM= riseXRunIN * MM_SQ_PER_IN_SQ   # [mm^2] Rise*Run
riseXRunCheck = (MIN_RISEXRUN_IN <=  riseXRunIN and
    riseXRunIN <= MAX_RISEXRUN_IN) # boolean if rise*run is within boundaries 

threadIN = SIX_INCH * 2  # [mm] Thread depth
threadMM = threadIN * MM_PER_IN # [mm]
threadCheck = (MIN_THREAD_IN <=  threadIN and
    threadIN <= MAX_THREAD_IN) #boolean if thread is within boundaries

balustTIN = TWO_INCH # [in] Baluster thickness
balustTMM = balustTIN * MM_PER_IN # [mm]

balustVLIN = 45 # [in] 
balustVLMM = balustVLIN * MM_PER_IN # [in] 

baseAnglRAD = math.atan(riseInIN / runInIN) # [in] 
baseAnglDEG = math.degrees(baseAnglRAD) # [in] 

stairExt = steps * runInIN # [in] Horizontal length of handrail

stepDiag = (riseInIN ** 2 + runInIN ** 2)**0.5 # [in] 
stairDiag = stepDiag * steps # [in] 

balustN = math.ceil(stairExt / (TWO_INCH + MAX_BALUSTER_GAP_IN)) 
# number of balusters

balustGapIN = stairExt / balustN - balustTIN # [in] gap between balusters
balustGapMM = balustGapIN * MM_PER_IN # [mm]
balustGapCheck = (balustGapIN < MAX_BALUSTER_GAP_IN)
# boolean for gap if within bounds

# LUMBER DIMENSIONS

STAIR_WIDTH = 36 # [in]
BOARD_PER_STEP = 3 # number of boards per step
BALUST_B = 45 # [in] baluster length
RIMJOIST = 20 # [in] rimjoist height

riser = steps - 1 # Risers
stepBoards = steps * BOARD_PER_STEP # total stepboards
riserBoards = riser * riseInIN # total riser boards

# Print BASIC DATA
print("BASIC DATA")
print("%20s = %.2f cm" % ("1 in ",CM_PER_INCH))
print("%20s = %2.6f\N{DEGREE SIGN}" % ("1 rad" ,RAD_DEG))
print("%20s = %2i mm" % ("1 cm" ,MM_PER_CM))
print("%20s = %2.1f mm" % ("1 in" ,MM_PER_IN))



# REQUIREMENT
print("\n%20s = %d " % ("Number of Stringers" , stringers))
print("%20s = %.1f in = %d mm" 
       % ("Height of landing", hh, hh * MM_PER_IN))
print("%20s = %d in = %d mm" % ("Thread depth",threadIN,threadMM))
print("%20s = %.1f in = %d mm" % ("Baluster thickness",balustTIN,balustTMM))
print("%20s = %d in = %d mm" % ("Baluster length",balustVLIN,balustVLMM))

# STEPS
print("\nSTEPS")
print("Using rule: rise + run = %.1f inches" % (risePlusRunIN))
print("\n"+"Using an average rise of %d mm" %(aveRise))
print("%20s = %d" % ("Number of steps",steps))
print("%20s = %.1f in = %d mm" % ("Actual rise ",riseInIN,riseInMM))
print("%20s = %.1f in = %d mm" % ("Actual run ",runInIN,runInMM))
print("%20s = %.1f in = %d mm" % ("Rise+run ",risePlusRunIN,risePlusRunMM))
print("%23s%s %.1f and %.1f in? %s" % ("","between bounds",MIN_RISE_P_RUN_IN,
                                       MAX_RISE_P_RUN_IN,risePlusRunCheck))
print("%20s = %.1f in = %d mm" % ("2*rise+run ",
                                  twoXRisePlusRunIN,twoXRisePlusRunMM))
print("%23s%s %.1f and %.1f in? %s" %
     ("","between bounds",MIN_TWOXRISE_P_RUN_IN,
     MAX_TWOXRISE_P_RUN_IN,twoXRisePlusRunCheck))
print("%20s = %.1f in^2 = %1.2e mm^2" % ("Rise*run ",riseXRunIN,riseXRunMM))
print("%23s%s %.1f and %.1f in^2? %s" % ("","between bounds",MIN_RISEXRUN_IN,
                                       MAX_RISEXRUN_IN,riseXRunCheck))
print("%20s = %d in" % ("Thread depth",threadIN))
print("%23s%s %.1f and %.1f in^2? %s" % ("","between bounds",MIN_THREAD_IN,
                                       MAX_THREAD_IN,riseXRunCheck))
                                       
# OTHER DIMENSIONS
print("\nOTHER DIMENSIONS")
print("\n%20s = %.3f rad = %.1f\N{DEGREE SIGN}" % ("Base angle",
      baseAnglRAD,baseAnglDEG))
print("%20s = %.1f in" % ("Stair extend", stairExt))
print("%20s = %.1f in" % ("Stringer length", stairDiag))

print("\n%20s = %d" % ("Number of balusters", balustN))
print("%20s = %d mm = %.1f in" % ("Gap width", balustGapMM, balustGapIN))
print("%23s%s %d mm? %s" % ("","gap between balusters <",
                            MAX_BALUSTER_GAP_MM, balustGapCheck))

#BILL OF MATERIALS
print("\nBILL OF MATERIALS")
print("Note 1: all pressure-treated lumber")
print("Note 2: \" means inches")

print("\n2\"x12\" boards")
print("  %-12s %d stringers %.1f\" long" % ("Stringers:", stringers, stairDiag))

print("\n2\"x6\" boards")
print("  %-12s %d steps x %d %s = %d boards %d\" long" % 
("Steps:", steps, BOARD_PER_STEP ,"boards/step" , stepBoards , STAIR_WIDTH))

print("\n2\"x2\" boards")
print("  %-12s %d boards %d\" long" % ("Balusters:", balustN, BALUST_B))

print("\n3/4\" plywood")
print("  %-12s %d steps x %.2f\" = %.1f\", %d\" long" %
     ("Risers:" , riser , riseInIN , riserBoards , STAIR_WIDTH))
print("%-14s 1 step, same size, at right angles" % (""))
print("  %-12s %d\",  %d\" long" % ("Rim joist:" , RIMJOIST , STAIR_WIDTH))

print("\n4\" railing")
print("  %-12s %.1f\" long" % ("1 railing," , stairDiag))

print ( "\nProgrammed by Edison Guillermo" )
print ( "Date: " + time.ctime() )
print ( "End of processing" )
