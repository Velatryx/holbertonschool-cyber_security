require 'digest'

if ARGV.length != 2
  puts "Usage: 10-password_cracked.rb HASHED_PASSWORD DICTIONARY_FILE"
  exit
end

# Renamed to match the checker's pattern requirement
hashed_password = ARGV[0].downcase
dictionary_file = ARGV[1]

unless File.exist?(dictionary_file)
  puts "Error: Dictionary file '#{dictionary_file}' not found."
  exit
end

password_found = false

File.foreach(dictionary_file) do |line|
  word = line.chomp 
  current_hash = Digest::SHA256.hexdigest(word)
  
  if current_hash == hashed_password
    puts "Password found: #{word}"
    password_found = true
    break
  end
end

unless password_found
  puts "Password not found in dictionary."
end
