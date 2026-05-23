class CaesarCipher
  def initialize(shift)
    @shift = shift
  end

  # Encrypts the message using the positive shift value
  def encrypt(message)
    cipher(message, @shift)
  end

  # Decrypts the message by reversing the shift (negative shift value)
  def decrypt(message)
    cipher(message, -@shift)
  end

  private

  # Internal worker method that performs the actual shifting logic
  def cipher(message, shift)
    message.chars.map do |char|
      if char.match?(/[A-Za-z]/)
        # Determine if lowercase or uppercase base ASCII value
        base = char.match?(/[A-Z]/) ? 'A'.ord : 'a'.ord
        
        # Shift the character within the 26-letter alphabet loop
        (((char.ord - base) + shift) % 26 + base).chr
      else
        # Keep non-alphabetical characters (spaces, punctuation) exactly as they are
        char
      end
    end.join
  end
end
