import win32api, win32con
from win32api import GetSystemMetrics
import time

def about():
	print("-----------------------------x---------------------------------")
	print("If you like this script, send me a hi message here: ")
	print("Email: gkiranp@gmail.com")

def usage():
	print("-----------------------------x---------------------------------")
	print("Usage:")
	print("Usage is simple, just run the script in Win machine")
	print("Requirement is : Python 3")
	print("Tested in Windows 10, 64-bit")
	print("Close the window to close the script, or Ctrl+C must do")

def lic():
	print("-----------------------------x---------------------------------")
	print("LICENSE: MIT")
	print("Permission is hereby granted, free of charge, to any person" )
	print("obtaining a copy of this software and associated documentation")
	print("files, to deal in the Software without restriction, including ")
	print("without limitation the rights to use, copy, modify, merge, publish, ")
	print("distribute, sublicense, and/or sell copies of the Software, and to ")
	print("permit persons to whom the Software is furnished to do so, subject ")
	print("to the below` conditions:")
	print("THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS ")
	print("OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,")
	print("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE")
	print("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER ")
	print("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, ")
	print("OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR ")
	print("OTHER DEALINGS IN THE SOFTWARE.")
	print("-----------------------------x---------------------------------")

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

# Script stars here
about()
usage()
lic()
# Define start Row,Col
r = 10
c = 10
print("Current screen resolution = " + str(GetSystemMetrics(0)) + "x" + str(GetSystemMetrics(1)))
print("Auto mouse movement started:")
# Let's loop infinitely
while True:
	r = r + 10
	c = c + 10
	# Make sure you are not out of bound from current display resolution
	if(r >= GetSystemMetrics(0)):
		r = 10
	# Make sure you are not out of bound from current display resolution
	if(c >= GetSystemMetrics(1)):
		c = 10
	click(r,c)
	time.sleep(15)