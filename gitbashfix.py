#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys


# In[2]:


# Check to see if current OS is windows.  If not no fix is required, so terminate
import platform
if platform.system() != "Windows":
    print("This program only works and is only necessary for windows systems")
    exit(-1)


# In[3]:


# The user's home folder is stored in the environment variable HOME.  Grab this and store it in a variable
import pathlib
home_folder = stpathlib.Path.home()


# In[6]:


str(home_folder)


# In[4]:


# make a list of the different parts of the home folder
home_folder_parts = home_folder.split('\\')
# the last part of the home folder is the username
username = home_folder_parts[-1]


# In[ ]:


home_folder_parts[1].upper()


# In[ ]:


# check to make sure that home folder is in c:/Users -- if not code needs to be improved
if home_folder_parts[0].upper() != "C:" or home_folder_parts[1].upper() != "USERS":
    print(f"program assumes that user's home folder is in C:\\Users, but was found to be {home_folder}.  Aborting...")
    exit(-3)


# In[ ]:


# the file we need to modify is called .bashrc.  To implement the fix we need to add lines that look like:
#   . /c/Users/"$username"/anaconda3/etc/profile.d/conda.sh
#   alias python="winpty /c/Users/$username/anaconda3/python.exe"
#   alias jupyter="/c/Users/$username/anaconda3/envs/dev/Scripts/jupyter.exe"
#   export PATH=$PATH:/c/Users/thoma/anaconda3/envs/dev/Scripts

# the filename for this file is .bashrc, and is in the home folder
import pathlib
bashrc_filename = pathlib.Path(f"{home_folder}/.bashrc")


# In[ ]:


# open the file and append the lines
with open(bashrc_filename, "a", newline="\n") as bashrc:
    bashrc.write(f". /c/Users/{username}/anaconda3/etc/profile.d/conda.sh\n")
    bashrc.write(f'alias python="winpty /c/Users/{username}/anaconda3/python.exe"\n')
    bashrc.write(f'alias jupyter="/c/Users/{username}/anaconda3/envs/dev/Scripts/jupyter.exe"\n')
    bashrc.write(f'export PATH=$PATH:/c/Users/{username}/anaconda3/envs/dev/Scripts\n')
    print("fix successfully applied")
    exit(0)


# In[ ]:


# this section of code should only be reached if the above section failed, i.e. if there was a file I/O error
print(f"There was a problem opening the .bashrc file hopefully located at {bashrc_filename}.  Please contact support for assistance")
exit(-2)


# In[ ]:




