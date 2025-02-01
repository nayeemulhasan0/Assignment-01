file_name = input("file name: ")

try:
    with open(file_name) as file:
        values = [float(line.split(":")[1]) for line in file if line.startswith("X-DSPAM-Confidence:")]
    print("avr spam confidence:", sum(values) / len(values) if values else "no matching lines found")

except FileNotFoundError:
    print("file not found")


