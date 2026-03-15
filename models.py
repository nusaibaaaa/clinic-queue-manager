
from datetime import datetime

class Patient:

    def __init__(self, name, age, symptoms):
        self.name = name
        self.age = age
        self.symptoms = symptoms
        self.arrival_time = datetime.now()

    def arrival_timestamp(self):
        return self.arrival_time.strftime("%H:%M:%S")
