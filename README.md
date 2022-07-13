# task-manager
Everything related to the task is done here via seperating the backend and the frontend please note that the architecture in order to provide a restapi backend that the frontend consumes is well defined 

IMPORTANT NOTE: 

Images get dissappered after some time that are being uploaded for the below reason on reupload it works fine

What Heroku does every time you push to them is:

    Creates a new app space with its own virtual machine, virtual environment, and packages installed through pip.
    Swaps the subdomain over to the new location.
    Deletes the old app space.
    
    
What this means is that anything added to the app that is not in Git, won’t last between pushes. Even more, this exact same process happens once every 24 hours anyway, so uploaded files have to go somewhere other than Heroku like aws s3 bucket or some default media storage.

The task of providing a sub tasks can't be obtained due to time constarians but is based on the same architecture 

The task of assigning a user is obtained by providing a default user as login forms are not made same because of time constrain

all well is in this project deployed too on heroku it fullfils every need and the restapi with frontend architecture is well defined 


Kindly check it and if any doubt arises please let me know

Thank You

you can go on the admin panel and login as 

username = 123456
password = 123456
