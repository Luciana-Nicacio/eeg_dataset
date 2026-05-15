#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 18:27:23 2025

@author: luciana
"""

from os import chdir, path
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import re
# import zipfile
# import pickle


root = Tk()
root.withdraw()
bd_name = askopenfilename(title = 'Select the database to be analyzed.')
data_directory = path.dirname(bd_name)
chdir(data_directory)
Dataset = pd.read_pickle(bd_name)


info_dataset = re.split(r"[_ .]",bd_name)
stimulus_type = info_dataset[2]
 
print('- Datasetitems:',list(Dataset))
print('- Info: Sampling frequency: %.1fHz'%Dataset['info']['fs'])
print('- Info: Modulation frequencies of the left and right stimuli, respectively: %.2fHz and %.2fHz' %(Dataset['info']['fmod'][0],Dataset['info']['fmod'][1]))
print('- Info: Recorded EEG channels: ',Dataset['info']['channels'])
print('- Info: Reference channel of the EEG recording: ', Dataset['info']['reference'])
print('- Type of stimulus used in the experiment:', Dataset['stimulus'])
print('- For each participant, the following data are availables:', list(Dataset['ID32']))
print('- For participant ID32, for example, the following questionnaire questions were asked: ',list(Dataset['ID32']['questions']))
print('- Participant ID32\'s responses to the questionnaire questions were: ',Dataset['ID32']['answers'])
print('- Delay refers to the time interval between the onset of EEG signal acquisition and the onset of stimulation. The delay for each trial, in seconds, for participant ID32 was:: ',Dataset['ID32']['delays'])
