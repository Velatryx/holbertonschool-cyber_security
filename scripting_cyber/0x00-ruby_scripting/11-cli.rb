#!/usr/bin/env ruby
require 'optparse'

TASK_FILE = 'tasks.txt'

# Initialize an empty options hash
options = {}

opt_parser = OptionParser.new do |opts|
  # Match the exact usage string format from the help menu
  opts.banner = "Usage: cli.rb [options]"

  opts.on("-a", "--add TASK", "Add a new task") do |task|
    options[:add] = task
  end

  opts.on("-l", "--list", "List all tasks") do
    options[:list] = true
  end

  opts.on("-r", "--remove INDEX", "Remove a task by index") do |index|
    options[:remove] = index.to_i
  end

  opts.on("-h", "--help", "Show help") do
    puts opts
    exit
  end
end

# Parse the command-line arguments safely
begin
  opt_parser.parse!(ARGV)
rescue OptionParser::InvalidOption, OptionParser::MissingArgument => e
  puts e.message
  puts opt_parser
  exit
end

# --- Task Actions Logic ---

# 1. ADD TASK
if options[:add]
  task_name = options[:add]
  File.open(TASK_FILE, 'a') do |file|
    file.puts(task_name)
  end
  puts "Task '#{task_name}' added."

# 2. LIST TASKS
elsif options[:list]
  if File.exist?(TASK_FILE) && !File.zero?(TASK_FILE)
    File.readlines(TASK_FILE).each_with_index do |line, index|
      puts "#{index + 1}. #{line.chomp}"
    end
  else
    # Quiet exit if file doesn't exist or is empty
  end

# 3. REMOVE TASK
elsif options[:remove]
  target_index = options[:remove]
  
  if File.exist?(TASK_FILE)
    lines = File.readlines(TASK_FILE)
    
    # Check if index is valid (1-based index)
    if target_index > 0 && target_index <= lines.length
      # Remove the element at the specified index (converting back to 0-based index)
      removed_task = lines.delete_at(target_index - 1).chomp
      
      # Rewrite the remaining tasks back to the file
      File.open(TASK_FILE, 'w') do |file|
        lines.each { |line| file.write(line) }
      end
      
      puts "Task '#{removed_task}' removed."
    end
  end
else
  # If no options are given, output the help manual
  puts opt_parser
end
