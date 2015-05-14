## Python Selenium Tests

### Setup

To run these tests a properties.ini file will need to be created in the same directory as this README file.
The file should contain 4 lines: 

 * line 1 is the id used to log into CNX
 * line 2 is the password for the user
 * line 3 is the base url for the test
 * line 4 is the full path to the test zip file. A sample file is in the /data directory
 
**DO NOT CHECK THIS FILE INTO GITHUB** Use .gitignore to prevent it.
 
**Example**
 
    myID
    mypassword
    http://mydomain.com/somewhere
    /home/username/.../integration-tests/data/zipfilename.zip
 

### Running Tests

The tests can be run on the command line

    cd location/of/tests
    python <test name>.py

License
-------

This software is subject to the provisions of the GNU Affero General Public License Version 3.0 (AGPL). See license.txt for details. Copyright (c) 2015 Rice University.
