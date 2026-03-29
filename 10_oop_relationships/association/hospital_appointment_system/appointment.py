class Appointment:
    def __init__(self, doctor, patient, room, time: str):
        self._doctor = doctor
        self._patient = patient
        self._room = room
        self._time = time

    @property
    def doctor(self):
        return self._doctor

    @property
    def patient(self):
        return self._patient

    @property
    def room(self):
        return self._room

    @property
    def time(self):
        return self._time