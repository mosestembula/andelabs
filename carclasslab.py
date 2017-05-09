class Car(object):

  def __init__(self, name='General', model='GM', vehicle_type=None,  speed = 0):
    self.name = name
    self.model = model
    self.vehicle_type = vehicle_type
    self.speed = speed
    


    if self.name in ['Porshe', 'Koenigsegg']:
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4

    if self.vehicle_type == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4

    if self.vehicle_type == 'Honda':
      self.vehicle_type = None


  def is_saloon(self):
    if self.vehicle_type is not 'trailer':
        self.vehicle_type == 'saloon'
        return True
    return False

  def is_car(self):
    if self.vehicle_type==None:
      return  "The object should be a type of `Car'"

  def drive(self, moving_speed):
    if moving_speed == 3:
      Car.speed = 1000
    elif moving_speed == 7:
      Car.speed = 77

  def drive(self, parked):
    if not parked:
      return "The Trailer should have speed 0 km/h until you put `the pedal to the metal`"
    else:
     return speed

    return self