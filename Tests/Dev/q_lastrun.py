#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on January 06, 2019, at 12:46
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'q'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'H:\\GitHub\\Precision_tES_tACS_tRNS_tDCS\\Tests\\q.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1024, 768], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "ins"
insClock = core.Clock()
## Choose desired keymap
import string

# Set up the desired key names

# entryChars holds the keynames that we will accept from 
# the keyboard.
# Here we're making a list of all lower case letters 
# on an English-US keyboard.
entryChars = [x for x in string.ascii_letters]
# could put extra keynames here if desired, use
# keynameFinder demo to get name of keys
extraChars = []
# The exception map is for when the keyname is
# not what you want to display. i.e. the keyname
exceptionMap = {"space": u" ",
            u"q": u"й",
            u"w": u"ц",
            u"e": u"у",
            u"r": u"к",
            u"t": u"е",
            u"y": u"н",
            u"u": u"г",
            u"i": u"ш",
            u"o": u"щ",
            u"p": u"з",
            u"[": u"х",
            u"]": u"ъ",
            u"a": u"ф",
            u"s": u"ы",
            u"d": u"в",
            u"f": u"а",
            u"g": u"п",
            u"h": u"р",
            u"j": u"о",
            u"k": u"л",
            u"l": u"д",
            u";": u"ж",
            u"'": u"э",
            u"z": u"я",
            u"x": u"ч",
            u"c": u"с",
            u"v": u"м",
            u"b": u"и",
            u"n": u"т",
            u"m": u"ь",
            u",": u"б",
            u".": u"ю",
            u"/": u".",
}

# add extra characters into expected
# key list
for exChar in extraChars:
    if not exChar in entryChars:
        entryChars.append(exChar)

# same with exception keys
for exKey in exceptionMap.keys():
    if not exKey in entryChars:
        entryChars.append(exKey)

enterKeys = ['return', 'num_enter']
backspaceKeys = ['backspace']
escapeKey = 'escape'
instText = visual.TextStim(win=win, name='instText',
    text='OK. Ready for the real thing?\n\n(Esc will quit)\n\nPress any key to continue',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()

ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    pos=[-0.2, 0], height=0.2, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-3.0);
textEntryStim = visual.TextStim(win=win, name='textEntryStim',
    text=None,
    font='Arial',
    pos=(0.3, 0), height=0.2, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "resp"
respClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text='This is the end of the experiment.\n\nThanks!',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "ins"-------
t = 0
insClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

ready = event.BuilderKeyResponse()
# keep track of which components have finished
insComponents = [instText, ready]
for thisComponent in insComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ins"-------
while continueRoutine:
    # get current time
    t = insClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *instText* updates
    if t >= 0.0 and instText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instText.tStart = t
        instText.frameNStart = frameN  # exact frame index
        instText.setAutoDraw(True)
    
    # *ready* updates
    if t >= 0.0 and ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready.tStart = t
        ready.frameNStart = frameN  # exact frame index
        ready.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ready.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in insComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ins"-------
for thisComponent in insComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('word.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    keyboard = event.BuilderKeyResponse()
    textEntryStim.text = u""
    text_3.setText(q)
    # keep track of which components have finished
    trialComponents = [keyboard, ISI, text_3, textEntryStim]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *keyboard* updates
        if t >= 0.0 and keyboard.status == NOT_STARTED:
            # keep track of start time/frame for later
            keyboard.tStart = t
            keyboard.frameNStart = frameN  # exact frame index
            keyboard.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(keyboard.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if keyboard.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                keyboard.keys.extend(theseKeys)  # storing all keys
                keyboard.rt.append(keyboard.clock.getTime())
        if len(keyboard.keys) > 0: #make sure not empty, prevent list index error
            currentText = textEntryStim.text
            key = keyboard.keys.pop(-1) # get the last key entered
        
            if key in backspaceKeys: #allow backspacing
                # set the text to the current text, except the last character
                textEntryStim.text = currentText[:-1]
            elif key in enterKeys: #allows return or other keys to end routine
                continueRoutine = False
            else:
                if key in entryChars:
                    if key in exceptionMap:
                        key = exceptionMap[key]
                    textEntryStim.text = currentText + key
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        
        # *textEntryStim* updates
        if t >= 0.0 and textEntryStim.status == NOT_STARTED:
            # keep track of start time/frame for later
            textEntryStim.tStart = t
            textEntryStim.frameNStart = frameN  # exact frame index
            textEntryStim.setAutoDraw(True)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(1)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyboard.keys in ['', [], None]:  # No response was made
        keyboard.keys=None
    trials.addData('keyboard.keys',keyboard.keys)
    if keyboard.keys != None:  # we had a response
        trials.addData('keyboard.rt', keyboard.rt)
    trials.addData("responseText", textEntryStim.text)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "resp"-------
t = 0
respClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
respComponents = [thanksText]
for thisComponent in respComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "resp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = respClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if t >= 0.0 and thanksText.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksText.tStart = t
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thanksText.status == STARTED and t >= frameRemains:
        thanksText.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in respComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "resp"-------
for thisComponent in respComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
