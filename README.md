# static_file_server

Serve static folders. Each static folder is assumed to be a web based report having an index.html file and files required by this html script.
Navigating to a folder will open this html file.

## How to run
`cd static_file_server`

edit the gunicorn/config.py

```sed -i 's+/home/kirub/iCog_tasks/nunet/flask_sfs/static_file_server+'`pwd`'+g' gunicorn/config.py```

start the flask app

`gunicorn -c gunicorn/config.py app:app`

open `localhost:8888` from a web browser.

## How to stop
open another terminal from the `static_file_server` directory

to stop: `kill $(cat gunicorn/log/pid.pid)`

to restart: `kill -HUP $(cat gunicorn/log/pid.pid)`
