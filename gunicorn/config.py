# ~/iCog tasks/nunet/static_file_serving$ gunicorn -c gunicorn/config.py file_serv_app:app
#kill $(cat ~/iCog\ tasks/nunet/static_file_serving/gunicorn/log/pid.pid) #kill
#kill -HUP $(cat  ~/iCog\ tasks/nunet/static_file_serving/gunicorn/log/pid.pid) #restart

workers = 5
bind = "0.0.0.0:5000"
errorlog = "/home/kirub/iCog tasks/nunet/static_file_serving/gunicorn/log/error.log"
accesslog = "/home/kirub/iCog tasks/nunet/static_file_serving/gunicorn/log/access.log"
loglevel = "debug"
pidfile = "/home/kirub/iCog tasks/nunet/static_file_serving/gunicorn/log/pid.pid"
chdir = "/home/kirub/iCog tasks/nunet/static_file_serving/html_reports"
timeout = 1900
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%(m)s" "%(U)s" "%(q)s" "%(H)s" %(B)s %(T)s %(p)s "%({Header}i)s" "%({Header}o)s" "%({Header}e)s"'
