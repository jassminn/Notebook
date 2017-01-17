#!/usr/bin/python

'''
print "Set-Cookie:UserID=XYZ;\r\n"
print "Set-Cookie:Password=XYZ123;\r\n"
print "Set-Cookie:Expires=Tuesday, 6-Jan-2017 15:00:00 GMT;\r\n"
print "Set-Cookie:Domain=www.tutorialspoint.com;\r\n"
print "Set-Cookie:Path=/perl;\n"
'''
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Post - First CGI Program</title>'
print '</head>'
print '<body>'
print '<form action="/cgi-bin/notebooks/hello_get.py" method="get">'
print 'First Name: <input type="text" name="first_name"> <br/>'
print 'Last Name: <input type="text" name="last_name"> <br/>'
print '<input type="submit" value="Submit" />'
print '</form>'
print '<form enctype="multipart/form-data" '
print '                  action="/cgi-bin/notebooks/save_file.py" method="post">'
print '<p>File: <input type="file" name="filename" /></p>'
print '<p><input type="submit" value="Upload" /></p>'
print '</form>'
print """
<form action="/cgi-bin/notebooks/download_file.py" method="post" target="_blank">
<input type="submit" value="Download"/>
</form>
"""
print '</body>'
print '</html>'

