

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


class Deportista:
  def __init__(self, deporte, añosPracticando):
    self.__deporte = deporte 
    self.__añosPracticando = añosPracticando

    # Métodos para acceder a los atributos privados (getters)
    def get_deporte(self):
        return self.__deporte

    def get_añosPracticando(self):
        return self.__añosPracticando

    # Métodos para modificar los atributos privados (setters)
    def set_deporte(self, deporte):
        self.__deporte = deporte

    def set_añosPracticando(self, añosPracticando):
        self.__añosPracticando = añosPracticando


class Futbolista(Persona, Deportista):
 # Atributo de clase
    lista_futbolistas = []

    def __init__(self, nombre, edad, altura, sexo, deporte, años_practicando, goles_marcados, tarjetas_rojas, pierna_habil):
        # Inicializa los atributos heredados de Persona y Deportista
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, años_practicando)
        
        # Inicializa los atributos específicos de Futbolista
        self.__goles_marcados = goles_marcados
        self.__tarjetas_rojas = tarjetas_rojas
        self.__pierna_habil = pierna_habil

        # Añade el futbolista a la lista de futbolistas
        Futbolista.lista_futbolistas.append(self)


         # Métodos getters y setters para los atributos privados
    def get_goles_marcados(self):
        return self.__goles_marcados

    def set_goles_marcados(self, goles_marcados):
        self.__goles_marcados = goles_marcados

    def get_tarjetas_rojas(self):
        return self.__tarjetas_rojas

    def set_tarjetas_rojas(self, tarjetas_rojas):
        self.__tarjetas_rojas = tarjetas_rojas

    def get_pierna_habil(self):
        return self.__pierna_habil

    def set_pierna_habil(self, pierna_habil):
        self.__pierna_habil = pierna_habil

    @classmethod
    def get_lista_futbolistas(cls):
        return cls.lista_futbolistas

    def __str__(self):
        return f"Mi nombre es {self.get_nombre()}, soy profesional en el deporte {self.get_deporte()}. Tengo {self.get_edad()} años de edad y llevo {self.get_años_practicando()} años en el deporte."


