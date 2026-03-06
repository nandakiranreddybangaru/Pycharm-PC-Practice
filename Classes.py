class Clinic:
    def __init__(self, location, doctor_name):
       self.location = location
       self.doctor_name = doctor_name
       self.patients_today = 0

    def add_patients(self):
        self.patients_today = self.patients_today + 1





clinic1 = Clinic("Bangalore", "Dr.Rao")
clinic1.add_patients()
clinic1.add_patients()
clinic1.add_patients()


print(clinic1.location)

print(clinic1.doctor_name)



print(f"In {clinic1.location} Patients walked in without Appointment!: Today total {clinic1.patients_today} patients")

clinic2 = Clinic("Hyderabad", "Dr. Sharma")
print(clinic2.location)
print(clinic2.doctor_name)

clinic2.add_patients()
clinic2.add_patients()
clinic2.add_patients()
clinic2.add_patients()


print(f"In {clinic2.location} Patients walked in without appointment: Today total {clinic2.patients_today} patients")


print(f"The One Ayush Clinic in {clinic2.location} is run by {clinic2.doctor_name}")



