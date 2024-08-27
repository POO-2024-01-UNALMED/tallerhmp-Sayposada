class Persona:
  def __init__(self, nombre, edad, altura, sexo):
    self.__nombre = nombre
    self.__edad = edad
    self.__altura = altura
    self.__sexo = sexo 

 
    # Métodos para acceder a los atributos privados (getters)
    def get_nombre(self):
      return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_altura(self):
        return self.__altura

    def get_sexo(self):
        return self.__sexo

    # Métodos para modificar los atributos privados (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_altura(self, altura):
        self.__altura = altura

    def set_sexo(self, sexo):
        self.__sexo = sexo