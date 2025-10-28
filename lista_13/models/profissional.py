class Profissional:
    def __init__(self, id, nome, especialidade, conselho,email,senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_email(email)
        self.set_senha(senha)
    def __str__(self):
        return f"{self.__id}-{self.__nome}-{self.__especialidade}–{self.__conselho}"
    def get_id(self): 
        return self.__id
    def get_nome(self): 
        return self.__nome
    def get_especialidade(self): 
        return self.__especialidade
    def get_conselho(self): 
        return self.__conselho
    def get_email(self):
        return self.__email
    def get_senha(self):
        return self.__senha
    def set_email(self,email):
        if email == "": raise ValueError("email inválido")
        self.__email=email
    def set_senha(self,senha):
        if senha == "": raise ValueError("senha inválida")
        self.__senha=senha 
    def set_id(self, id): 
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome inválido") 
        self.__nome = nome
    def set_especialidade(self, especialidade): 
        self.__especialidade = especialidade
    def set_conselho(self, conselho): 
        self.__conselho = conselho
    def to_json(self):
        dict = {"id":self.get_id(),"nome":self.get_nome(),"conselho":self.get_conselho(),"especialidade":self.get_especialidade(),"email":self.get_email(),"senha":self.get_senha()}
        return dict
    def from_json(dict):
        return Profissional(dict["id"],dict["nome"],dict["especialidade"],dict["conselho"],dict["email"],dict["senha"])