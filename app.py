import os

from flask import Flask, jsonify, request, render_template

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import models

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir,
                                                   "my_graph_ql.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    return render_template("home.html")


@app.route("/compute", methods = ['GET', 'POST'])
def compute():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        vm = models.Compute(json_data['name'], json_data['image'],
                            json_data['flavor'])
        net1 = models.Network.query.first()
        vol1 = models.Volume.query.first()
        vm.network_id = net1.id
        vm.volume_id = vol1.id
        db.session.add(vm)
        db.session.commit()
    if request.method == 'GET':

        result = models.Compute.query.first()
        compute_schema = models.ComputeSchema()
        output = compute_schema.dump(result).data
    return jsonify({'vm': output})


@app.route("/network", methods = ['GET', 'POST'])
def network():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        net = models.Network(json_data['name'], json_data['prefix'])
        db.session.add(net)
        db.session.commit()
    if request.method == 'GET':
        result = models.Network.query.first()
        network_schema = models.NetworkSchema()
        output = network_schema.dump(result).data
    return jsonify({'vm': output})


@app.route("/volume", methods = ['GET', 'POST'])
def volume():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        vol = models.Volume(json_data['name'], json_data['size'])
        db.session.add(vol)
        db.session.commit()
    if request.method == 'GET':
        result = models.Volume.query.first()
        volume_schema = models.VolumeSchema()
        output = volume_schema.dump(result).data
    return jsonify({'vm': output})


if __name__ == "__main__":
    app.run(port=5001, debug=True)
