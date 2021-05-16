print("Enter the following quantities in feet.")

r = float(input("  "+"How long is this row? "))
e = float(input("  "+"How wide is the end-post assembly? "))
s = float(input("  "+"How much space should be between the vines? "))

v = int(((r-(2*e))/s))

print(" ")
print(f"This row has enough space for {v:.0f} vine(s).")
