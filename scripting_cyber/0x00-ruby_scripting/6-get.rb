require 'net/http'
require 'uri'
require 'json'

def get_request(url)
  # Parse the string URL into a URI object
  uri = URI.parse(url)
  
  # Perform the GET request
  response = Net::HTTP.get_response(uri)
  
  # Print the status code along with its message (e.g., "200 OK")
  puts "Response status: #{response.code} #{response.message}"
  
  # Parse and pretty print the response body in neat JSON format
  parsed_body = JSON.parse(response.body)
  puts "Response body:"
  puts JSON.pretty_generate(parsed_body)
end
