class Usuario:
    def __init__(self, nombre, edad, username, password):
        self.nombre = nombre
        self.edad = edad
        self.username = username
        self.password = password
    
    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad

    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setEdad(self, edad):
        self.edad = edad

    def setUsername(self, username):
        self.username = username
    
    def setPassword(self, password):
        self.password = password
    