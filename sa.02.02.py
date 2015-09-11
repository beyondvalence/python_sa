#! /usr/lib/env/ python34

import ftplib

host = "ftp.ibiblio.org"
root = "/pub/docs/books/gutenberg/"

def directory_list( path ):
	with ftplib.FTP( host, user="anonymous") as connection:
		print( "Welcome", connection.getwelcome() )
		for name, details in connection.mlsd( path ):
			print( name, details['type'], details.get( 'size' ) )

directory_list( root )			