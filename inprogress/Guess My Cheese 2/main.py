import hashlib

# Read cheese names from a file
cheeses = []
with open("cheese_list.txt", "r") as f:
    for line in f:
        # Strip whitespace/newlines
        cheese = line.replace("\n", "")
        # Ignore empty lines
        if cheese:
            cheeses.append(cheese)

# Replace with the challenge's target hash
target_hash = "1198c44f1e6f60eab841aa56cd4110f67663d7042ac277a5157a2816fbc5e293"

def sha256(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

# Try all cheese + salt / salt + cheese combos
found_match = False
for cheese in cheeses:
    for i in range(256):
        salt = f"{i:02x}"

        # Option A: cheese + salt
        test_string_1 = cheese + salt
        if sha256(test_string_1) == target_hash or sha256(test_string_1.lower()) == target_hash or sha256(test_string_1.upper()) == target_hash or sha256(test_string_1.strip()) == target_hash:
            print(f"FOUND! Cheese={cheese}, Salt={salt} (appended)")
            found_match = True
            break
        
        # Option B: salt + cheese
        test_string_2 = salt + cheese
        if sha256(test_string_2) == target_hash or sha256(test_string_2.lower()) == target_hash or sha256(test_string_2.upper()) == target_hash or sha256(test_string_2.strip()) == target_hash:
            print(f"FOUND! Cheese={cheese}, Salt={salt} (prepended)")
            found_match = True
            break

    if found_match:
        break

if not found_match:
    print("No matches found.")

