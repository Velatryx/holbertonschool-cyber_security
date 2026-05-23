require 'open-uri'
require 'uri'
require 'fileutils'

# 1. Check if exactly two arguments (URL and LOCAL_FILE_PATH) are provided
if ARGV.length != 2
  puts "Usage: 9-download_file.rb URL LOCAL_FILE_PATH"
  exit
end

url = ARGV[0]
local_path = ARGV[1]

begin
  # 2. Print the initial downloading message
  puts "Downloading file from #{url}..."

  # 3. Ensure the destination directory exists (handles nested folders like ./downloads/file.jpg)
  dirname = File.dirname(local_path)
  FileUtils.mkdir_p(dirname) unless Dir.exist?(dirname)

  # 4. Open the remote URL and stream it into the local file
  URI.open(url) do |remote_file|
    File.open(local_path, "wb") do |local_file|
      local_file.write(remote_file.read)
    end
  end

  # 5. Print the success message matching the prompt
  puts "File downloaded and saved to #{local_path}."

rescue StandardError => e
  puts "An error occurred: #{e.message}"
end
