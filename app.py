
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Parámetros de configuración iniciales
config = {
    'LS': '4',
    'LI': '1',
    'alias': 'sas',
    'status': 'on'
}

@app.route('/')
def config_page():
    return render_template('config.html', config=config)

@app.route('/update', methods=['POST'])
def update_config():
    global config
    config['LS'] = request.form.get('LS')
    config['LI'] = request.form.get('LI')
    config['alias'] = request.form.get('alias')
    config['status'] = request.form.get('status')
    return 'Configuración actualizada', 200

@app.route('/api', methods=['GET'])
def get_config():
    return jsonify(config)

if __name__ == '__main__':
    app.run(debug=True)
