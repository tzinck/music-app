import os
import sys
import actions
from databasecalls import *


#File to contain the bulk of the application (for now, in the preliminary stages)

startup()

print('Done Startup')

#This is a very messy way to handle taking user input, need to rework this
while(1):
	action = input('Enter a Command: ')
	if(action == 'add'):
		#handle adding
		name = input('Enter song name: ')
		insert(name)
	if(action == 'printall'):
		#handle printing
		printall()
	if(action == 'deleteall'):
		#handle deletion
		deleteall()
	if(action == 'delete'):
		#handle delete single song
		name = input('Delete which song?: ')
		deletesong(name)
