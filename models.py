from app import db
from app import ma


class Compute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    image = db.Column(db.String(255))
    flavor = db.Column(db.String(255))
    network_id = db.Column(db.Integer, db.ForeignKey('network.id'))
    volume_id = db.Column(db.Integer, db.ForeignKey('volume.id'))
    network = db.relationship('Network')
    volume = db.relationship('Volume')

    def __init__(self, name, image, flavor):
        self.name = name
        self.image = image
        self.flavor = flavor


class Network(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    prefix = db.Column(db.String(255))

    def __init__(self, name, prefix):
        self.name = name
        self.prefix = prefix


class Volume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    size = db.Column(db.Integer)

    def __init__(self, name, size):
        self.name = name
        self.size = size


class ComputeSchema(ma.ModelSchema):
    class Meta:
        model = Compute


class NetworkSchema(ma.ModelSchema):
    class Meta:
        model = Network


class VolumeSchema(ma.ModelSchema):
    class Meta:
        model = Volume


