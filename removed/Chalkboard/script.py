def find_non_matching_lines(file_path):
    flag = ""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                cleaned_line = line.strip()  # Remove leading/trailing whitespace
                if cleaned_line != "I WILL NOT BE SNEAKY":
                    c = ''.join([char for char in cleaned_line if not char.isupper()])
                    c = c.replace(" ", "")
                    flag += c
        print(flag)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
file_path = "text.txt"  # Replace with your file path
find_non_matching_lines(file_path)
