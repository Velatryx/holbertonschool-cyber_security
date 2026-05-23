#!/usr/bin/env ruby
require 'optparse'

TASK_FILE = 'tasks.txt'

options = {}

opt_parser = OptionParser.new do |opts|
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
    puts "Tasks:"
    File.readlines(TASK_FILE).each do |line|
      puts line.chomp
    end
  end

# 3. REMOVE TASK
elsif options[:remove]
  target_index = options[:remove]
  
  if File.exist?(TASK_FILE)
    lines = File.readlines(TASK_FILE)
    
    if target_index > 0 && target_index <= lines.length
      removed_task = lines.delete_at(target_index - 1).chomp
      
      File.open(TASK_FILE, 'w') do |file|
        lines.each { |line| file.write(line) }
      end
      
      puts "Task '#{removed_task}' removed."
    end
  end
else
  puts opt_parser
end
