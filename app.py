from flask import Flask, render_template, request, jsonify
from keep_alive import *
from flask_cors import CORS  # Importar la extensión CORS


# Habilitar CORS para todos los orígenes


app = Flask(__name__)
CORS(app)

# Parámetros de configuración iniciales
config = {
    "short.ultinoticias.online": {
        "LS": "8",
        "LI": "1",
        "alias": "Xiaomis",
        "status": "off",
        "redirect_dev_url": "off",
        "redirection_url": "off",
        
    },
    "curiosidadesenlinea": {
        "LS": "8",
        "LI": "1",
        "alias": "Xiaomis",
        "status": "off",
        "redirect_dev_url": "off",
        "redirection_url": "off",
    },
    "1": {
        "LS": "8",
        "LI": "1",
        "alias": "Xiaomis",
        "status": "off",
        "redirect_dev_url": "off",
        "redirection_url": "off",
    },
    "3": {
        "LS": "8",
        "LI": "1",
        "alias": "Xiaomis",
        "status": "off",
        "redirect_dev_url": "off",
        "redirection_url": "off",
    },
    "2": {
        "LS": "8",
        "LI": "1",
        "alias": "Xiaomis",
        "status": "off",
        "redirect_dev_url": "off",
        "redirection_url": "off",
    },
    "4": {
        "LS": "8",
        "LI": "1",
        "alias": "Xiaomis",
        "status": "off",
        "redirect_dev_url": "off",
        "redirection_url": "off",
    },
}


@app.route("/")
def config_page():
    return render_template("config.html", config=config)


@app.route("/update/<string:id>", methods=("GET", "POST"))
def update_config(id):
    global config
    if id not in config:
        return "Error", 201
    if request.method == "POST":

        config_ = config[id]
        config_["LS"] = request.form.get("LS")
        config_["LI"] = request.form.get("LI")
        config_["alias"] = request.form.get("alias")
        config_["status"] = request.form.get("status")
        config_["redirect_dev_url"] = request.form.get("redirect_dev_url")
        config_["redirection_url"] = request.form.get("redirection_url")

        return "Configuración actualizada", 200
    return render_template("config.html", config=config[id])


@app.route("/api/<string:id>", methods=["GET"])
def get_config(id):
    if id not in config:
        return "Error", 201
    return jsonify(config[id])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
