class patient:
    def __init__(self, name, base_bill):
        self.name = name
        self.base_bill = base_bill


class insured_patient(patient):
    def __init__(self, name, base_bill, insured_company):
        super().__init__(name, base_bill)
        self.insured_company = insured_company

    def calculate_final_bill(self, discount_percentage):
        if discount_percentage > 100 or discount_percentage < 0:
            raise ValueError("Discount percentage should be between 0 and 100")
        else:

            discount_amount = self.base_bill * (discount_percentage / 100)
            final_bill = self.base_bill - discount_amount

            print(f"The final bill is ₹{final_bill}")


patient1 = insured_patient("Nanda", 2000, "HDFC")
patient2 = insured_patient("Raj", 5000, "EVEN")

try:
    print(f"Generating bill for {patient1.name} via {patient1.insured_company}...")

    patient2.calculate_final_bill(50)

except ValueError as error_message:
    print(f"Bill will not generate: {error_message}")