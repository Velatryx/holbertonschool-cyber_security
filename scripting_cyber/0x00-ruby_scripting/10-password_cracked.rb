require 'digest'

# 1. Ensure exactly two arguments are provided
if ARGV.length != 2
  puts "Usage: 10-password_cracked.rb HASHED_PASSWORD DICTIONARY_FILE"
  exit
end

target_hash = ARGV[0].downcase
dictionary_file = ARGV[1]

# 2. Check if the dictionary file exists before opening
unless File.exist?(dictionary_file)
  puts "Error: Dictionary file '#{dictionary_file}' not found."
  exit
end

password_found = false

# 3. Read the file line-by-line to execute the attack efficiently
File.foreach(dictionary_file) do |line|
  word = line.chomp # Strip out newline characters (\n)
  
  # Compute the SHA-256 hash of the word
  current_hash = Digest::SHA256.hexdigest(word)
  
  if current_hash == target_hash
    puts "Password found: #{word}"
    password_found = true
    break
  end
end

# 4. If the dictionary loop completes without a match
unless password_found
  puts "Password not found in dictionary."
end
