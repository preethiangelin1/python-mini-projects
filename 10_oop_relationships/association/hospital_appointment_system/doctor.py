class Doctor:
    def __init__(self, name: str, specialization: str):
        self._name = name
        self._specialization = specialization
        self._appointments = []

    @property
    def name(self):
        return self._name

    @property
    def specialization(self):
        return self._specialization

    def add_appointment(self, appointment):
        self._appointments.append(appointment)

    @property
    def patients(self):
        return [appt.patient for appt in self._appointments]