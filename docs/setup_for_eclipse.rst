README for Eclipse users
                                          Apr.21, 2013 yoshi

This is a readme document for the use of moztrap under Eclipse (only tested under Juno)

[SETUP]

Software as the pre-requisite is
  
  PyDev plug-in (www.pydev.org)

After installing the above plug-in under Eclipse, one can take the following steps:

1. Create the moztrap project (through cloning from GitHub)

  1.1 Go to Window > Open Perspective > Other 
      Then, choose "Git Repository Exploring"
 
  1.2 Click the button "Clone a Git Repository and add the clone to this view"
      Then, fill in the info. about the GitHub remote repository in the pop-up window.
      (For details, please see http://wiki.eclipse.org/EGit/User_Guide#Cloning_Remote_Repositories)
  
2. Modify a file to let Django under Eclipse recognize the moztrap settings

   Add "from .default import *" in __init__.py under /moztrap/moztrap/settings
   
   NOTE: This appears to be necessary so that Django running under Eclipse can recognize
   the settings of moztrap and override its default settings with them.

3. Set the Debug (or Run) configuration for the project
   
   1.1 Go to Run > Debug Configurations
   
   1.2 Click the button "New launch configuration" located in the upper-left of the Configuration 
       Window. Then, fill in the followings:

       Name: (for example, moztrap_manage)
       Main:
          Project: moztrap
          Main Module: ${workspace_loc:moztrap/manage.py}
       Arguments:
          Program arguments: runserver -noreload
           
[USAGE]

   Go to Run > Debug History > moztrap_manage (the name set in the above configuration)
