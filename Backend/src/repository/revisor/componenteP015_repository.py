import json

from ...business.componentes.componente import ComponenteP015

class ComponenteP015Repository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_componenteP015_bd(self, componente: ComponenteP015):
        return componente.getValues(self.db, self.mongodb)

    def post_componenteP015(self, req):
        self.mongodb.componentes.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
