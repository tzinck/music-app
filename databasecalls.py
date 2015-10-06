import sqlite3

#File to contain all calls to the database

db = sqlite3.connect('music-db')
cursor = db.cursor()

def startup():
	db = sqlite3.connect('music-db')
	cursor = db.cursor()	
	# If you're adding columns, uncomment this and you will delete the old table.
	# cursor.execute('''DROP TABLE IF EXISTS songs''')
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS songs(id INTEGER PRIMARY KEY, name TEXT, progress INT)
			''')
	db.commit()
	print('Connected to DB')

def insert(songname):
	cursor.execute('''INSERT INTO songs(name, progress) VALUES (?,?)''', (songname,0))
	db.commit()
	print('Inserted song: ' + songname)

def printall():
	cursor.execute('''SELECT name FROM songs''')
	all_rows = cursor.fetchall()
	for row in all_rows:
		print('{0} '.format(row[0]))	

def deleteall():
	cursor.execute('''DELETE FROM songs''')
	db.commit()

def deletesong(songname):
	cursor.execute('''
		DELETE FROM songs WHERE NAME = (?)
			''',(songname,))
	db.commit()

def editProgress(songname, songprogress):
	cursor.execute('''
		UPDATE songs SET progress = (?) WHERE name = 
		(?)''',(songprogress, songname,))
	db.commit()
	print('You\'re ' + songprogress + '/10 of the way done for ' 
	+ songname +'.')
	
	

	
	
