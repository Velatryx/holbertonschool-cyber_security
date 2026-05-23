require 'net/http'
require 'uri'
require 'json'

def post_request(url, body_params = {})
  # Parse the string URL into a URI object
  uri = URI.parse(url)
  
  # Create the HTTP session
  http = Net::HTTP.new(uri.host, uri.port)
  # Enable SSL/TLS encryption if the URL uses https
  http.use_ssl = (uri.scheme == 'https')
  
  # Set up the POST request
  request = Net::HTTP::Post.new(uri.path.empty? ? '/' : uri.path)
  request['Content-Type'] = 'application/json'
  request.body = JSON.generate(body_params)
  
  # Execute the request
  response = http.request(request)
  
  # Print the status code along with its message (e.g., "201 Created")
  puts "Response status: #{response.code} #{response.message}"
  
  # Parse and pretty print the response body in neat JSON format
  parsed_body = JSON.parse(response.body)
  puts "Response body:"
  puts JSON.pretty_generate(parsed_body)
end
