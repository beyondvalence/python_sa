#! /usr/lib/env/ python34

import sys
import ftplib

host = "ftp.ibiblio.org"
root = "/pub/docs/books/gutenberg/"

def get( fullname, output=sys.stdout ):
	download= 0
	expected= 0
	dots= 0
	def line_save( aLine ):
		nonlocal download, expected, dots
		print( aLine, file=output )
		if output != sys.stdout:
			download += len(aLine)
			show= (5*download)//expected
			if show > dots:
				print( "*", end="", file=sys.stdout )
				sys.stdout.flush()
				dots= show
	with ftplib.FTP( host, user="anonymous" ) as connection:
		print( "Welcome", connection.getwelcome() )
		expected= connection.size( fullname )
		print( "Getting", fullname, "to", output, "size", expected )
		connection.retrlines( "RETR {0}".format(fullname), line_save )
	if output != sys.stdout:
		print() # End the "dots"

# show the README on sys.stdout
get( root+"README" )

# get GUTINDEX.ALL
with open( "GUTINDEX.ALL", "w", encoding="UTF-8" ) as output:
	get( root+"GUTINDEX.ALL", output )
	