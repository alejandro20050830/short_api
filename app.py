from flask import Flask, render_template, request, jsonify
from keep_alive import *
from flask_cors import CORS  # Importar la extensión CORS



# Habilitar CORS para todos los orígenes


app = Flask(__name__)
CORS(app)

# Parámetros de configuración iniciales
config = {"LS": "4", "LI": "1", "alias": "Xiaomis", "status": "on","redirect_dev_url":"off"}


@app.route("/")
def config_page():
    return render_template("config.html", config=config)


@app.route("/update", methods=["POST"])
def update_config():
    global config
    config["LS"] = request.form.get("LS")
    config["LI"] = request.form.get("LI")
    config["alias"] = request.form.get("alias")
    config["status"] = request.form.get("status")
    config["redirect_dev_url"] = request.form.get("redirect_dev_url")
    
    return "Configuración actualizada", 200


@app.route("/api", methods=["GET"])
def get_config():
    return jsonify(config)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
