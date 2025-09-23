class Serviço:
    def __init__(self,id,descricao,valor ):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)
    def __str__(self):
        return f"{self.__id}-{self.__descricao}-{self.__valor}"
    def get_id(self): 
        return self.__id
    def get_descricao(self): 
        return self.__descricao
    def get_valor(self): 
        return self.__valor
    def set_id(self, id): 
        self.__id = id
    def set_descricao(self, descricao): 
        self.__descricao = descricao
    def set_valor(self, valor): 
        self.__valor = valor
    def to_json(self):
        dict = {"id":self.get_id(),"descricao":self.get_descricao(),"valor":self.get_valor()}
        return dict
    def from_json(dict):
        return Serviço(dict["id"],dict["descricao"],dict["valor"])
    