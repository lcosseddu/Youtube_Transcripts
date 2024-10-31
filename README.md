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
   gunicorn -w 4 -b 0.0.0.0:8000 YTT_WebApp:app
   ```

2. Open a web browser and navigate to `http://127.0.0.1:8000/`

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

The `youtube_transcriptor.py` file contains the core functionality for fetching and processing YouTube transcripts. It uses the `youtube_transcript_api` library to retrieve transcripts and includes functions for extracting video IDs, fetching transcripts, and saving them to text files.

### User Model

The `models.py` file defines the User model using SQLAlchemy. It includes fields for email, username, password hash, IP address, first name, and last name. The model also includes methods for password hashing and verification.

### Web Application Routes

The `YTT_WebApp.py` file contains the main Flask application and defines the routes for the web interface. It includes routes for the home page, user registration, login, logout, and transcript retrieval.

## Security Features

- Passwords are securely hashed using `werkzeug.security`
- User authentication is managed using Flask-Login
- IP addresses are logged for each registered user
- SQLite database is used for user management
- Password requirements enforced during registration

## Error Handling

The application includes error handling for:
- Invalid YouTube URLs
- Unavailable transcripts
- File writing errors
- User registration and login issues

Errors are logged using Python's logging module and displayed in the web interface.

## Database Management

The project uses Flask-Migrate for database migrations. To update the database schema:

1. Initialize migrations (if not done):
   ```
   flask db init
   ```

2. Create a new migration:
   ```
   flask db migrate -m "Description of changes"
   ```

3. Apply the migration:
   ```
   flask db upgrade
   ```

## Responsive Design

The web interface is designed to be responsive, adapting to different screen sizes. The `static/css/style.css` file contains CSS rules for responsive layout and styling, including:

- Flexible container widths
- Responsive navigation menu
- Adjustable font sizes and spacing
- Mobile-friendly form layouts

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

[![Build Status](https://github.com/yourusername/Youtube_Transcripts/workflows/Python%20application/badge.svg)](https://github.com/yourusername/Youtube_Transcripts/actions)
[![codecov](https://codecov.io/gh/yourusername/Youtube_Transcripts/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/Youtube_Transcripts)
