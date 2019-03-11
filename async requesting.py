import asyncio
import aiohttp
async def fetch(url):
    """Perform an HTTP GET to the URL and print the response"""
    response =aiohttp.request('GET', url)
    return response.text()
# Get a reference to the event loop
loop = asyncio.get_event_loop()
# Create the batch of requests we wish to execute
requests = [asyncio.ensure_future(fetch("https://github.com")),
            asyncio.ensure_future(fetch("https://google.com"))]
# Run the batch
responses = loop.run_until_complete(asyncio.gather(*requests))
# Examine responses
for resp in responses:
  print(resp.text())
