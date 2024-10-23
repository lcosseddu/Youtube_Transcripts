# Import necessary modules
from flask import Flask, render_template, request, send_file
from youtube_transcriptor import get_and_save_transcript
import os

# Initialize Flask application
app = Flask(__name__)

# Define route for the main page, accepting both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # If it's a POST request, we're receiving form data
        # Get the YouTube URL and language from the form
        video_url = request.form['video_url']
        language = request.form['language']
        
        # Generate a unique filename for this transcript
        # os.urandom(4).hex() creates a random 8-character string
        output_file = f"transcript_{os.urandom(4).hex()}.txt"
        
        try:
            # Call our function to get and save the transcript
            get_and_save_transcript(video_url, output_file, language)
            
            # Send the file to the user for download
            return send_file(output_file, as_attachment=True)
        except Exception as e:
            # If an error occurs, render the template with an error message
            return render_template('index.html', error=str(e))
        finally:
            # Clean up the file after sending or if an error occurred
            if os.path.exists(output_file):
                os.remove(output_file)
    
    # For GET requests, just render the form
    return render_template('index.html')

# Run the Flask app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
