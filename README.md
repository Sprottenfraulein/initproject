INITPROJECT

	DESCRIPTION
	
		A small script that will help to create initial file structure 
		for your Python project.
		
		
	SETUP
	
		1.	Open a terminal and navigate to Initproject root folder
			(where this README.md file is located)
		2.	Run the following command:
		
				python3 setup.py install
			
		3.	Copy 'initproject' from 'bin' folder to '/usr/local/bin
			(you probably will need to use sudo):
		
				cp bin/initproject /usr/local/bin
			
		4.	Done! Now you can use Initproject from anywhere on your
			system.
	
		
	USAGE
	
		1. 	Open a terminal and navigate to the folder inhabited by
			your Python projects.
		2. 	Run the following command, replacing *nameofyourproject* 
			with an actual name of your project:
			
				initproject *nameofyourproject*
				
		3.	If it's the first time you use this script, Initproject will
			ask you for your username and email and then put both in 
			AUTHORS text file in the root folder of your new project.
		4.	If everything is ok, Initproject will end with the following
			message:
			
				Initialized '*nameofyourproject*' successfully.
				Thanks for using Initproject!

