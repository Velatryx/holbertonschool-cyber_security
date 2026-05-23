def print_arguments
  # Check if any arguments were passed in
  if ARGV.empty?
    puts "No arguments provided."
  else
    # Loop through each argument with its 0-based index
    ARGV.each_with_index do |arg, index|
      puts "#{index + 1}. #{arg}"
    end
  end
end
