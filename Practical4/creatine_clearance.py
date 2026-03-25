# 1. Store patient data: age (years), weight (kg), gender, creatinine concentration (µmol/l)
# 2. Validate each input value against acceptable ranges:
#    - age < 100 years
#    - weight > 20 kg and < 80 kg
#    - creatinine concentration > 0 µmol/l and < 100 µmol/l
#    - gender is either "male" or "female"
# 3. If any validation fails, report which input variable needs correction
# 4. If all inputs are valid, calculate CrCl using formula:
#    CrCl = ((140 - age) × weight) / (72 × creatinine_concentration)
#    Multiply by 0.85 if female
# 5. Display the calculated CrCl value

# Store patient data
age = 35  # years
weight = 70  # kg
gender = "male"  # either "male" or "female"
creatinine_concentration = 80  # µmol/l

# Initialize validation flag
is_valid = True

# Validate age
if age >= 100:
    print("Error: Age must be less than 100 years. Current value: " + str(age))
    is_valid = False

# Validate weight
if weight <= 20:
    print("Error: Weight must be greater than 20 kg. Current value: " + str(weight))
    is_valid = False
elif weight >= 80:
    print("Error: Weight must be less than 80 kg. Current value: " + str(weight))
    is_valid = False

# Validate creatinine concentration
if creatinine_concentration <= 0:
    print("Error: Creatinine concentration must be greater than 0 µmol/l. Current value: " + str(creatinine_concentration))
    is_valid = False
elif creatinine_concentration >= 100:
    print("Error: Creatinine concentration must be less than 100 µmol/l. Current value: " + str(creatinine_concentration))
    is_valid = False

# Validate gender
if gender.lower() != "male" and gender.lower() != "female":
    print("Error: Gender must be either 'male' or 'female'. Current value: " + gender)
    is_valid = False

# Calculate CrCl if all inputs are valid
if is_valid:
    # Calculate base clearance
    crcl = ((140 - age) * weight) / (72 * creatinine_concentration)
    
    # Apply gender adjustment
    if gender.lower() == "female":
        crcl = crcl * 0.85
    
    # Display result
    print("Creatinine Clearance Rate (CrCl): " + str(round(crcl, 2)) + " ml/min")
else:
    print("Unable to calculate CrCl. Please correct the input values above.")
    