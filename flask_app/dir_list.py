from os import listdir
from os.path import expanduser
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def dir_tree():
    path = expanduser(u'~/iCog_tasks/nunet/flask_sfs/static_file_server/flask_app/static')
    dir_list = list()
    try:
        dir_list = sorted(listdir(path), reverse=True)
    except OSError:
        pass  # handle errors due to empty list of html directories
    return render_template('dir_tree.html', html_report_dir_list=dir_list)


if __name__ == "__main__":
    app.run(host='localhost', port=8888, debug=True)
