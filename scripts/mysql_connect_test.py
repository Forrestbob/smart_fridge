import MySQLdb

db = MySQLdb.connect("localhost", "DataBAEs", "DataBAEs", "test")
curs=db.cursor()

try: 
	curs.execute ("INSERT INTO `test`.`test_table` (`name`) VALUES ('you')")

	db.commit()
	print "Data committed"
	
except: 
	print "There was an error."
	db.rollback()