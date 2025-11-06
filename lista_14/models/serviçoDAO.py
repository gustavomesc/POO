import json
from models.serviço import Serviço
from models.DAO import DAO
class ServiçoDAO(DAO):
    _objetos = []
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("serviços.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Serviço.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            cls._objetos = []
    @classmethod
    def salvar(cls):
        with open("serviços.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Serviço.to_json)