require 'json'

def merge_json_files(file1_path, file2_path)
  # 1. Read and parse the source file
  file1_content = File.read(file1_path)
  data1 = JSON.parse(file1_content)

  # 2. Read and parse the destination file
  file2_content = File.read(file2_path)
  data2 = JSON.parse(file2_content)

  # 3. Combine both arrays of objects
  merged_data = data2 + data1

  # 4. Write the merged array back into the destination file
  File.open(file2_path, 'w') do |f|
    f.write(JSON.pretty_generate(merged_data))
  end

  # 5. Output message required by the checker
  puts "Merged JSON written to #{file2_path}"
end
