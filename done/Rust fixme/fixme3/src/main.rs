use xor_cryptor::XORCryptor;

fn decrypt(encrypted_buffer: Vec<u8>, borrowed_string: &mut String) {
    // Key for decryption
    let key = String::from("CSUCKS");

    // Editing our borrowed value
    borrowed_string.push_str("PARTY FOUL! Here is your flag: ");

    // Create decryption object
    let xrc = match XORCryptor::new(&key) {
        Ok(x) => x,
        Err(e) => {
            eprintln!("Error creating XORCryptor: {:?}", e);
            return;
        }
    };

    // Decrypt the flag safely
    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);

    // Convert decrypted bytes to a UTF-8 string safely
    let decrypted_text = String::from_utf8_lossy(&decrypted_buffer);
    borrowed_string.push_str(&decrypted_text);

    // Print final result
    println!("{}", borrowed_string);
}

fn main() {
    // Encrypted flag values
    let hex_values = [
        "41", "30", "20", "63", "4a", "45", "54", "76", "12", "90", "7e", "53", "63", "e1", "01",
        "35", "7e", "59", "60", "f6", "03", "86", "7f", "56", "41", "29", "30", "6f", "08", "c3",
        "61", "f9", "35",
    ];

    // Convert hex strings to bytes
    let encrypted_buffer: Vec<u8> = hex_values
        .iter()
        .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
        .collect();

    // Create a mutable string
    let mut party_foul = String::from("Using memory unsafe languages is a: ");

    // Decrypt and modify the string
    decrypt(encrypted_buffer, &mut party_foul);
}
