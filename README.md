# YouTube Transcriptor

YouTube Transcriptor is a Python tool that allows you to extract and save transcripts from YouTube videos. It now includes a web application interface for easier use.

## Features

- Extract video ID from YouTube URLs
- Fetch transcripts in various languages
- Format and save transcripts to text files
- Error handling and logging
- Web interface for easy transcript retrieval

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Youtube_Transcripts.git
   cd Youtube_Transcripts
   ```

2. Install the required dependencies:
   ```
   pip install youtube_transcript_api flask
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

### Web Interface

The web application interface is available at `http://localhost:5000`. You can use it to easily retrieve transcripts from YouTube videos.

## Module Documentation

### Functions

#### `extract_video_id(url: str) -> Optional[str]`
Extracts the video ID from a YouTube URL.

#### `get_transcript(video_id: str, language: str = 'en') -> list[dict]`
Fetches the transcript for a given video ID in the specified language.

#### `format_transcript(transcript: list[dict]) -> str`
Formats the transcript into a single string.

#### `save_transcript(formatted_transcript: str, output_file: str)`
Saves the formatted transcript to a file.

#### `get_and_save_transcript(video_url: str, output_file: str = 'transcript.txt', language: str = 'en')`
Main function that combines all steps to fetch and save a transcript.

## Error Handling

The script includes error handling for common issues such as:
- Invalid YouTube URLs
- Unavailable transcripts
- File writing errors

Errors are logged using Python's logging module.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
