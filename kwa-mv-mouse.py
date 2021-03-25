import win32api as w32api
import win32con as w32con
from win32api import GetSystemMetrics as gsm
import threading
import time


class MoveMouse (threading.Thread):
	ExitFlag = False
	Timeout = 30

	def disp(self, msg:str):
		print ('{:^24s}'.format(msg))

	def about(self):
		self.disp("-----------------------------x---------------------------------")
		self.disp("If you like this script, send me a Hi Email")
		self.disp("Email: gkiranp@gmail.com")

	def usage(self):
		self.disp("-----------------------------x---------------------------------")
		self.disp("Usage:")
		self.disp("Run the script in a Windows machine, where Python 3 is installed.")
		self.disp("Close the window to close the script, or Ctrl+C must do.")

	def license(self):
		self.disp("-----------------------------x---------------------------------")
		self.disp("LICENSE: MIT")
		self.disp("Permission is hereby granted, free of charge, to any person" )
		self.disp("obtaining a copy of this software and associated documentation")
		self.disp("files, to deal in the Software without restriction, including ")
		self.disp("without limitation the rights to use, copy, modify, merge, publish, ")
		self.disp("distribute, sublicense, and/or sell copies of the Software, and to ")
		self.disp("permit persons to whom the Software is furnished to do so, subject ")
		self.disp("to the below` conditions:")
		self.disp("THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS ")
		self.disp("OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,")
		self.disp("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE")
		self.disp("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER ")
		self.disp("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, ")
		self.disp("OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR ")
		self.disp("OTHER DEALINGS IN THE SOFTWARE.")
		self.disp("-----------------------------x---------------------------------")

	def click(self, x, y):
		w32api.SetCursorPos((x,y))
		w32api.mouse_event(w32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
		w32api.mouse_event(w32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.about()
		self.license()
		self.usage()
	
	def run(self):
		r = int((gsm(0)/2) - 10)
		c = int((gsm(1)/2) - 10)
		while not self.ExitFlag:
			if self.Timeout == 0:
				if(r >= int(gsm(0)) or c >= int(gsm(1))):
					r = int((gsm(0)/2) - 10)
					c = int((gsm(1)/2) - 10)
				self.click(r,c)
				self.Timeout = 30
			else:
				self.Timeout -= 1
			time.sleep(0.5)

# Main program
if __name__ == "__main__":
	th = MoveMouse()
	th.start()
	# Let's keep main thread alive
	while th.is_alive():
		try:
			# synchronization timeout of threads kill
			th.join(1)
		except KeyboardInterrupt:
			# Ctrl-C handling and send kill to threads
			th.ExitFlag = True
