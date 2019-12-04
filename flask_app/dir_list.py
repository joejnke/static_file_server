import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def dir_tree():
    path = os.path.expanduser(u'~/iCog_tasks/nunet/flask_sfs/static_file_server/flask_app/static')
    return render_template('dir_tree.html', tree=make_tree(path))


def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try:
        lst = os.listdir(path)
    except OSError:
        pass  # ignore errors
    else:
        for name in lst:
            # print(name)
            # fn = os.path.join(path, name)
            tree['children'].append(dict(name=name))

            # if os.path.isdir(fn):
            #     tree['children'].append(make_tree(fn))
            # else:
            #     tree['children'].append(dict(name=name))
        # print(sorted(tree.items(), reverse=True))
    return tree


if __name__ == "__main__":
    app.run(host='localhost', port=8888, debug=True)