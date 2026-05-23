require 'json'

def count_user_ids(path)
  # Read the file content
  file_content = File.read(path)
  
  # Parse the JSON data into a Ruby array of hashes
  data = JSON.parse(file_content)
  
  # Extract all userId values and count their occurrences
  # (Returns a hash like { 1 => 10, 2 => 8 })
  counts = data.map { |item| item['userId'] }.tally
  
  # Sort the counts by the userId (the key) and print them
  counts.sort.each do |user_id, count|
    puts "#{user_id}: #{count}"
  end
end
