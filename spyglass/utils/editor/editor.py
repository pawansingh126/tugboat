# Copyright 2018 AT&T Intellectual Property.  All other rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import click
import json
import os
import socket
import sys
import yaml

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap


app_path = os.path.dirname(os.path.abspath(__file__))
print(app_path, os.getcwd())
app = Flask('Yaml Editor!',
            template_folder=os.path.join(app_path, 'templates'),
            static_folder=os.path.join(app_path, 'static'))
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Renders index page to edit provided yaml file."""
    with open(app.config['YAML_FILE']) as file_obj:
        data = yaml.safe_load(file_obj)
    return render_template('yaml.html',
                           data=json.dumps(data),
                           change_str=app.config['STRING_TO_CHANGE'])


@app.route('/save', methods=['POST'])
def save():
    """Save current progress on file."""
    out = request.json.get('yaml_data')
    with open(app.config['YAML_FILE'], 'w') as file_obj:
        yaml.safe_dump(out, file_obj, default_flow_style=False)
    return "Data saved successfully!"


@app.route('/saveExit', methods=['POST'])
def save_exit():
    """Save current progress on file and shuts down the server."""
    out = request.json.get('yaml_data')
    with open(app.config['YAML_FILE'], 'w') as file_obj:
        yaml.safe_dump(out, file_obj, default_flow_style=False)
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()
    return "Saved successfully, Shutting down app! You may close the tab!"


@app.errorhandler(404)
def page_not_found(e):
    """Serves 404 error."""
    return '<h1>404: Page not Found!</h1>'


def run(*args, **kwargs):
    """Starts the server."""
    port = kwargs.get('port', None)
    if not port:
        port = 8161
    app.run(host='0.0.0.0', port=port, debug=False)


@click.command()
@click.option(
    '--file',
    '-f',
    required=True,
    type=click.File(),
    multiple=False,
    help="Path with file name to the intermediary yaml file."
)
@click.option(
    '--port',
    '-p',
    default=8161,
    type=click.INT,
    multiple=False,
    help="Optional port parameter to run Flask on."
)
@click.option(
    '--string',
    '-s',
    default='#CHANGE_ME',
    type=click.STRING,
    multiple=False,
    help="Text which is required to be changed on yaml file."
)
def main(*args, **kwargs):
    try:
        yaml.load(kwargs['file'], Loader=yaml.Loader)
    except Exception:
        print('Please provide a valid yaml file.')
        sys.exit(2)
    print("Please go to http://{0}:{1}/ to edit your yaml file.".format(
        socket.gethostbyname(socket.gethostname()), kwargs['port']))
    app.config['YAML_FILE'] = kwargs['file'].name
    app.config['STRING_TO_CHANGE'] = kwargs['string']
    run(kwargs)


if __name__ == '__main__':
    """Invoked when used as a script."""
    main()
