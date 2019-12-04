# ~/iCog_tasks/nunet/flask_sfs/static_file_server$ gunicorn -c gunicorn/config.py app:app
#kill $(cat ~/iCog_tasks/nunet/flask_sfs/static_file_server/gunicorn/log/pid.pid) #kill
#kill -HUP $(cat ~/iCog_tasks/nunet/flask_sfs/static_file_server/gunicorn/log/pid.pid) #restart

workers = 3
bind = "0.0.0.0:8888"
errorlog = "/home/kirub/iCog_tasks/nunet/flask_sfs/static_file_server/gunicorn/log/error.log"
accesslog = "/home/kirub/iCog_tasks/nunet/flask_sfs/static_file_server/gunicorn/log/access.log"
loglevel = "debug"
pidfile = "/home/kirub/iCog_tasks/nunet/flask_sfs/static_file_server/gunicorn/log/pid.pid"
chdir = "/home/kirub/iCog_tasks/nunet/flask_sfs/static_file_server/flask_app"
timeout = 1900
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%(m)s" "%(U)s" "%(q)s" "%(H)s" %(B)s %(T)s %(p)s "%({Header}i)s" "%({Header}o)s" "%({Header}e)s"'
