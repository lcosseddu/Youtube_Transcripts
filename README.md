# YouTube Transcriptor

YouTube Transcriptor is a Python-based web application that allows users to extract and save transcripts from YouTube videos. It includes user authentication and a simple interface for easy transcript retrieval.

## Features

- Extract video ID from YouTube URLs
- Fetch transcripts in various languages
- Format and save transcripts to text files
- Web interface for easy transcript retrieval
- User authentication system with registration and login
- Secure password hashing
- IP address logging for registered users
- Responsive design for various screen sizes

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Youtube_Transcripts.git
   cd Youtube_Transcripts
   ```

2. Install the required dependencies:
   ```
   pip install flask flask-sqlalchemy flask-login youtube_transcript_api flask-migrate
   ```

## Usage

### Web Application

1. Run the Flask application:
   ```
   python YTT_WebApp.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`

3. Register a new account or log in if you already have one

4. Once logged in, enter the YouTube video URL and desired language code in the form

5. Click "Get Transcript" to download the transcript as a text file

## Project Structure

- `YTT_WebApp.py`: Main Flask application file
- `youtube_transcriptor.py`: Core functionality for fetching and processing transcripts
- `models.py`: Database models for user management
- `templates/`: HTML templates for the web interface
- `static/css/style.css`: CSS styles for the web interface
- `migrations/`: Database migration files

## Key Components

### YouTube Transcript Fetching
