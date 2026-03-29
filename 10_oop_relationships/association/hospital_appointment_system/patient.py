class Patient:
    def __init__(self, name: str):
        self._name = name
        self._appointments = []

    @property
    def name(self):
        return self._name

    def add_appointment(self, appointment):
        self._appointments.append(appointment)

    @property
    def doctors(self):
        return [appt.doctor for appt in self._appointments]