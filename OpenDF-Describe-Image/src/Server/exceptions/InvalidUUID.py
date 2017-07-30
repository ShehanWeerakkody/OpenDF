from flask import jsonify


class InvalidUUID(Exception):

    def __init__(self, payload=None):
        Exception.__init__(self)
        self.message = "UUID Not Valid"
        self.status_code = 400
        self.payload = payload

    def to_dict(self):
        error = dict(self.payload or ())
        error['message'] = self.message
        return error
