from threading import Thread
from urllib.request import *

def download_file(init, step, d, i):
	try:
		'''req = Request(d.url, headers={'Range':'bytes=%s-%s'%(init,init+1)})
		d.data[i] = bytes(urlopen(req).read())
		for j in range(init+1, init+step+1):
			req = Request(d.url, headers={'Range':'bytes=%s-%s'%(j,j+1)})
			temp_buffer = str(urlopen(req).read())
			d.data[i] = str(d.data[i])
			d.data[i] += temp_buffer
		d.data[i] = bytes(d.data[i])
		'''
		req = Request(d.url, headers={'Range':'bytes=%s-%s'%(init,init+step)})
		for i in range(init, step+init+1):
			
		d.data[i] = bytes(urlopen(req).read())

	except (HTTPError, URLError) as error:
		print('Data of %s not retrieved because %s\nURL: %s', name, error, url)
	except timeout:
		print('socket timed out - URL %s', url)
	except:
		print('What?')
	else:
		pass

def resume_download(start, end, d, i, a):
	req = Request(d.url, headers={'Range':'bytes=%s-%s'%(start,end)})
	a += bytes(urlopen(req).read())
	d.data[i] = a



class D_thread(Thread):	
	def __init__(self, download, arg) :
		Thread.__init__(self, target=download, args = arg)

	def run(self):		
		Thread.run(self)
		
	
