import math

class Sensor:
    def __init__(self,id:int,x_position:float,y_position:float):
        self.id=id
        self.x_position=x_position
        self.y_position=y_position
    def __str__(self):
        return "ID {} X: {} Y: {}".format(self.id,self.x_position,self.y_position)
class POI:
    def __init__(self,id:int,x_position:float,y_position:float):
        self.id=id
        self.x_position=x_position
        self.y_position=y_position
        self.sensors_list = []
    def __str__(self):
        string = "ID {} X: {} Y: {}".format(self.id,self.x_position,self.y_position)
        for sensor in self.sensors_list:
            string += str(sensor)
        return string
    def __add_sensor(self,sensor:Sensor):
        self.sensors_list.append(sensor)
    #sprawdzanie czy POI jesst w zasięgu sensora
    def is_POI_in_range(self,sensor:Sensor,r:float):
        #jeżeli tak dodaje sensor do listy sensorów które widzą punkt
        print("Dystans = {}".format(math.dist([self.x_position,self.y_position], [sensor.x_position,sensor.y_position])))
        if(math.dist([self.x_position,self.y_position], [sensor.x_position,sensor.y_position])<=r):
            self.__add_sensor(sensor)
        