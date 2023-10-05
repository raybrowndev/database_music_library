## This is a process feedback challenge. That means you should record yourself doing it and submit that recording to your coach for feedback. How do I do this?

**Your assignment is to:**

> Test-drive a create method for your AlbumRepository class.
> Test-drive a delete method for your AlbumRepository class.


- create Album class
- create AlbumRepository class
- add .create() to repo 
  - INSERT INTO albums (title, year) VALUES (%s, %s , ['name']) ??
  - append each items to a list
- add .delete() to repo


Method	Job	            Arguments	      SQL query                                           it executes	Returns
all	    Get all artists	    no	        SELECT * FROM artists;        	                     A list of Artists
find	  Get one artist	    id        	SELECT * FROM artists WHERE id = $1;	              A single Artist
create	Insert an artist	   Artist    	INSERT INTO artists (name, genre) VALUES (%s, %s);	Nothing
delete	Delete an artist    	id         	DELETE FROM artists WHERE id = $1;	              Nothing
  - 