import json

from ...business.componentes.componente import ComponenteR

class ComponenteRRepository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_componenteR_bd(self, componente: ComponenteR):
        return componente.getValues(self.db, self.mongodb)

    def post_componenteR(self, req):
        self.mongodb.componentes.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
