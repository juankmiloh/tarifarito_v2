from ...repository import ComponenteGRepository

class ComponenteGService:

    def get_componenteG(self, r_componenteG_repository: ComponenteGRepository, componenteG):
        data = r_componenteG_repository.get_componenteG_bd(componenteG)
        cpte = []
        for result in data:
            cpte.append(
                {
                    'ANO': result[19],
                    'MES': result[20],
                    'EMPRESA': result[21],
                    'MERCADO': result[22],
                    'values': {
                        'DCR': [
                            result[24], # C16
                            result[0],  # C12
                            result[9],  # C13
                            result[1],  # C14
                            result[10], # C15
                        ],
                        'Qc': [
                            result[25], #C17
                        ],
                        'Pc': [
                            result[26], #C22
                            result[4],  #C1
                            result[2],  #C2
                            result[5],  #C3
                            result[6],  #C4
                            result[3],  #C5
                            result[11], #C6
                        ],
                        'Qb': [
                            result[27], #C18
                        ],
                        'Pb': [
                            result[28], #C23
                            result[7],  #C7
                            result[8],  #C8
                        ],
                        'Qagd': [
                            result[29], #C21
                            result[12], #C19
                            result[13], #C20
                        ],
                        'McAplicado': [
                            result[30], #C11
                            result[23], #C9
                            result[18], #C10
                        ],
                        'FAJ': [
                            result[14], #C24
                        ],
                        'ALFA': [
                            result[15], #C25
                        ],
                        'GTransitorio': [
                            result[16], #C26
                        ],
                        'GContratos': [
                            result[31], #C29
                        ],
                        'GBolsa': [
                            result[32], #C30
                        ],
                        'CFNC': [
                            result[17], #C27
                        ],
                        'CGeneracion': [
                            result[33]  #C28
                        ],
                    },
                }
            )
        return cpte

    def post(self, r_componenteG_repository: ComponenteGRepository, req):
        print("_________ POST MODEL _____________")
        print(req)
        print("_________________________________")
        # Insertar datos
        result = r_componenteG_repository.post_componenteG(req)
        return result
