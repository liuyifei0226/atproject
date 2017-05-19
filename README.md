# Atproject

Becuase this package in under development, so we have not upload it to PyPI yet. When this project is good enough,

we will upload it to PyPI, at that time, user can use "pip install academictorrents" install this module.

# How to Install:
  in termimal copy the following command:
  
  (1) if you have administrator permission:
      
      User$ sudo pip install git+https://github.com/liuyifei0226/atproject
      
  (2) If you do not have administrator permission， please use:
      
      User$ pip install git+https://github.com/liuyifei0226/atproject --user
      
  (3) If you want to install from PyPi:
  
     -- with admin permission:
    
          User$ sudo pip install atproject
    
     -- without permission:
    
          User$ sudo pip install atproject --user
      
      
      
# How to use:
  (1) After installing the Academictorrents, enter python in terminal, get into python commond line:
  
      User$ python
      
  and you'll see
  
      >>>
      
  This means you're in python now.
  
  (2) Import academictorrents in your python. 
  
  For your convinience, you can import it as at for short:
  
      >>>import academictorrents as at
    
  (3) Download the file. 
  Use the command at.get(" ") to download the file you need. Here you should pay attention that your current path should be higher than the folder you save your .torrent file. For example, if you put your .torrent file in the folder /Users/ABC/Downloads, you should at Downloads or ABC to download the file.
  
      >>> at.get("path/torrentname.torrent")
      
 When you see something like
 
      saving:         devinberg.com_471592PB.pdf (0.2 MB)
      percent done:   0.0
      time left:      
      download to:    /Users/ChunjieXu/devinberg.com_471592PB.pdf
      download rate:  0.0 kB/s
      upload rate:    0.0 kB/s
      share rating:   0.000   (0.0 MB up / 0.0 MB down)
      seed status:    1 seen now, plus 0.000 distributed copies
      peer status:    1 seen now, 0.0% done at 0.0 kB/s

      saving:         devinberg.com_471592PB.pdf (0.2 MB)
      percent done:   86.4
      time left:      complete!
      download to:    /Users/ChunjieXu/devinberg.com_471592PB.pdf
      download rate:  29.6 kB/s
      upload rate:    0.0 kB/s
      share rating:   0.000   (0.0 MB up / 0.2 MB down)
      seed status:    4 seen now, plus 0.000 distributed copies
      peer status:    0 seen now, 0.0% done at 0.0 kB/s

      saving:         devinberg.com_471592PB.pdf (0.2 MB)
      percent done:   100
      time left:      Download Succeeded!
      download to:    /Users/ChunjieXu/devinberg.com_471592PB.pdf
      download rate:  
      upload rate:    0.0 kB/s
      share rating:   0.000   (0.0 MB up / 0.2 MB down)
      seed status:    4 seen now, plus 0.000 distributed copies
      peer status:    0 seen now, 0.0% done at 0.0 kB/s
      
 Congratulations! This means your academic torrents works perfect. 
 
 After download finish, it will use exit() to jump out.
 
# How to Uninstall:

  (1) if you have administrator permission, and install to a system path:
      
      sudo pip uninstall atproject
      
  (2) If you do not have administrator permission，and intall to User:
      
      pip uninstall atproject
