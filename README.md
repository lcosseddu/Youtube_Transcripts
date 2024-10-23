# YouTube Transcriptor

YouTube Transcriptor is a Python tool that allows you to extract and save transcripts from YouTube videos. It now includes a web application interface with user authentication for easier and more secure use.

## Features

- Extract video ID from YouTube URLs
- Fetch transcripts in various languages
- Format and save transcripts to text files
- Error handling and logging
- Web interface for easy transcript retrieval
- User authentication system
- Secure password hashing
- IP address logging for registered users

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Youtube_Transcripts.git
   cd Youtube_Transcripts
   ```

2. Install the required dependencies:
   ```
   pip install youtube_transcript_api flask flask-sqlalchemy flask-login
   ```

## Usage

### Command Line Interface

Run the script from the command line:

```
python youtube_transcriptor.py
```
You will be prompted to enter:
1. The YouTube video URL
2. The desired language code for the transcript (e.g., 'en' for English, 'it' for Italian)

The transcript will be saved in a file named `transcript.txt` in the same directory.

### Web Application

To use the web interface:

1. Run the Flask application:
   ```
   python YTT_WebApp.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`

3. Register a new account or log in if you already have one

4. Once logged in, enter the YouTube video URL and desired language code in the form

5. Click "Get Transcript" to download the transcript as a text file

## Module Documentation

### Functions in youtube_transcriptor.py

```python:youtube_transcriptor.py
startLine: 14
endLine: 35
```

```python:youtube_transcriptor.py
startLine: 38
endLine: 56
```

```python:youtube_transcriptor.py
startLine: 59
endLine: 69
```

```python:youtube_transcriptor.py
startLine: 72
endLine: 89
```

```python:youtube_transcriptor.py
startLine: 92
endLine: 120
```

### User Model in models.py

```python:models.py
startLine: 8
endLine: 23
```

## Web Application Structure

The web application (`YTT_WebApp.py`) includes the following routes:
- `/`: Main page for transcript retrieval (requires authentication)
- `/register`: User registration page
- `/login`: User login page
- `/logout`: User logout functionality

## Security Features

- Passwords are securely hashed using `werkzeug.security`
- User authentication is managed using Flask-Login
- IP addresses are logged for each registered user
- SQLite database is used for user management

## Error Handling

The application includes error handling for:
- Invalid YouTube URLs
- Unavailable transcripts
- File writing errors
- User registration and login issues

Errors are logged using Python's logging module and displayed in the web interface.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
