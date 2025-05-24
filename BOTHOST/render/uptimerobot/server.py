# Simple HTTP server for Render hosting with UptimeRobot health checks
import http.server
import socketserver
import threading
import os
import sys
import subprocess
import time

# Add root directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

# Port for the web server
PORT = int(os.environ.get('PORT', 8080))

# Health check endpoint handler
class HealthCheckHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Bot is running!')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Not Found')
    
    def log_message(self, format, *args):
        # Suppress logging to keep the console clean
        return

# Function to start the HTTP server
def start_http_server():
    handler = HealthCheckHandler
    httpd = socketserver.TCPServer(("", PORT), handler)
    print(f"Health check server started at port {PORT}")
    httpd.serve_forever()

# Function to start the Discord bot
def start_bot():
    print("Starting Discord bot...")
    try:
        # Import the bot module and run it
        import bot
        # Try to run the bot - using the token from environment variable
        bot.bot.run(bot.TOKEN)
    except Exception as e:
        print(f"Error starting bot: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Start HTTP server in a separate thread
    http_thread = threading.Thread(target=start_http_server, daemon=True)
    http_thread.start()
    
    # Start the bot in the main thread
    start_bot()