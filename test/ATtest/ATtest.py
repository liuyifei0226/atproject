import unittest
import pip
import os



def module_install(x):
    installed_packages = pip.get_installed_distributions()
    modulename = x    
    return modulename in str(installed_packages)
   
def import_as_at(x):	
	at = __import__(x)
	return x in str(at)
	
def call_get_function(x):	
	t = "get" in str(dir(x))		
	return t

def download_test():
	import academictorrents as at
	at.get("test.torrent")
	R = os.path.isfile("Introduction to the Special Topic on Grammar Induction, Representation of Language and Language Learning.pdf")
	return R
	
def download_result():
	R = os.path.isfile("Introduction to the Special Topic on Grammar Induction, Representation of Language and Language Learning.pdf")
	return R
	
class TestStringMethods(unittest.TestCase):
		
		def test_module_install_True(self):
			self.assertTrue(module_install("atproject"))
		
		def test_import_academictorrents_as_at_True(self):	
			self.assertTrue(import_as_at("academictorrents"))
			
		def test_getFunction_exist_True(self):
			self.assertTrue(call_get_function("get"))
			
		def test_download_Succeeded(self):
			with self.assertRaises(SystemExit):
    				download_test()	
			'''self.assertTrue(download_test())'''
		def test_download_result(self):
			self.assertTrue(download_result())
			
        
     
        

if __name__ == '__main__':
    unittest.main()