contacts={"varshini":1234567890,
          "Riya":2134567890,
          "siya":1123456789}
contacts["Anu"]=9988776655
contacts["Riya"]=9876543210

existing_contact = contacts.get("Riya", "Contact not found")
missing_contact = contacts.get("Eve", "Contact not found")

print("Safe Lookups:")
print("Riya:", existing_contact)
print("Eve:", missing_contact)

print("\nContact List:")


for name, Number in contacts.items():
    print(f"Contact: {name} | Phone: {Number}")
