# server.rb

require "sinatra"
require "json"

post "/webhooks/nxrm3" do
  urls = JSON.parse(request.body.read)["output_urls"]
  puts "Here are the media URLs: #{urls.inspect}"
end

