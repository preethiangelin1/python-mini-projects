from room import Room
from doctor import Doctor
from patient import Patient
from appointment import Appointment

if __name__ == "__main__":
    room1 = Room("101", 1)
    room2 = Room("202", 2)

    doc1 = Doctor("Dr. Ryan", "Cardiologist")
    doc2 = Doctor("Dr. Meera", "Dermatologist")
    doc3 = Doctor("Dr. Arjun", "Neurologist")

    pat1 = Patient("Ravi")
    pat2 = Patient("Anjali")
    pat3 = Patient("Kiran")

    appt1 = Appointment(doc1, pat1, room1, "10:00")
    appt2 = Appointment(doc1, pat2, room1, "10:30")
    appt3 = Appointment(doc2, pat1, room2, "11:00")
    appt4 = Appointment(doc3, pat3, room2, "11:30")
    appt5 = Appointment(doc2, pat3, room1, "12:00")

    appointments = [appt1, appt2, appt3, appt4, appt5]

    for appt in appointments:
        appt.doctor.add_appointment(appt)
        appt.patient.add_appointment(appt)

    print("\n--- Doctors and their Patients ---")
    for doc in [doc1, doc2, doc3]:
        print(f"{doc.name} treats:")
        for p in doc.patients:
            print(f"  - {p.name}")

    print("\n--- Patients and their Doctors ---")
    for pat in [pat1, pat2, pat3]:
        print(f"{pat.name} visited:")
        for d in pat.doctors:
            print(f"  - {d.name}")

    print("\n--- Appointment Details ---")
    for appt in appointments:
        print(
            f"{appt.time}: {appt.patient.name} meets {appt.doctor.name} "
            f"in Room {appt.room.number}"
        )