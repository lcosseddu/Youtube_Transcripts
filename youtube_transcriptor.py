# Import the logging module for error and info logging
import logging
# Import Optional type for type hinting
from typing import Optional
# Import the YouTube Transcript API
from youtube_transcript_api import YouTubeTranscriptApi

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Create a logger object for this module
logger = logging.getLogger(__name__)

# Funzione per estrarre l'ID del video dall'URL di YouTube
def extract_video_id(url: str) -> Optional[str]:
    """
    Extract the video ID from a YouTube URL.
    
    Args:
        url (str): The YouTube video URL.
    
    Returns:
        Optional[str]: The video ID if found, None otherwise.
    """
    # Check if the URL contains 'v=' (common format)
    if 'v=' in url:
        # Split the URL at 'v=' and take the second part
        # Then split at '&' and take the first part (in case of additional parameters)
        return url.split('v=')[1].split('&')[0]
    # Check if the URL is in the shortened youtu.be format
    elif 'youtu.be' in url:
        # Split the URL at '/' and take the last part
        return url.split('/')[-1]
    # If neither format matches, return None
    else:
        return None

# Funzione per ottenere la trascrizione
def get_transcript(video_id: str, language: str = 'en') -> list[dict]:
    """
    Fetch the transcript for a given video ID.
    
    Args:
        video_id (str): The YouTube video ID.
        language (str): The language code for the desired transcript.
    
    Returns:
        list[dict]: The transcript as a list of dictionaries.
    
    Raises:
        Exception: If the transcript cannot be retrieved.
    """
    try:
        return YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
    except Exception as e:
        logger.error(f"Failed to retrieve transcript: {e}")
        raise

# Funzione per formattare la trascrizione
def format_transcript(transcript: list[dict]) -> str:
    """
    Format the transcript into a single string.
    
    Args:
        transcript (list[dict]): The transcript as a list of dictionaries.
    
    Returns:
        str: The formatted transcript as a single string.
    """
    return " ".join(entry['text'] for entry in transcript)

# Funzione per salvare la trascrizione
def save_transcript(formatted_transcript: str, output_file: str):
    """
    Save the formatted transcript to a file.
    
    Args:
        formatted_transcript (str): The formatted transcript.
        output_file (str): The path to the output file.
    
    Raises:
        IOError: If there's an error writing to the file.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(formatted_transcript)
        logger.info(f"Transcript saved to {output_file}")
    except IOError as e:
        logger.error(f"Failed to save transcript: {e}")
        raise

# Funzione principale per ottenere e salvare la trascrizione
def get_and_save_transcript(video_url: str, output_file: str = 'transcript.txt', language: str = 'en'):
    """
    Main function to get and save the transcript for a given YouTube video URL.
    
    Args:
        video_url (str): The YouTube video URL.
        output_file (str): The path to the output file.
        language (str): The language code for the desired transcript.
    """
    try:
        # Extract the video ID from the URL
        video_id = extract_video_id(video_url)
        # If no valid video ID is found, raise an error
        if not video_id:
            raise ValueError("Invalid YouTube URL or video ID not found")
        
        # Get the transcript for the video
        transcript = get_transcript(video_id, language)
        # Format the transcript into a single string
        formatted_transcript = format_transcript(transcript)
        # Save the formatted transcript to a file
        save_transcript(formatted_transcript, output_file)
        
        # Log a preview of the transcript
        logger.info("\nPreview of the transcript:")
        logger.info(formatted_transcript[:200] + "...")
    except Exception as e:
        # Log any errors that occur during the process
        logger.error(f"An error occurred: {e}")

# Esempio di utilizzo
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    language = input("Enter the language code (e.g., 'en' for English, 'it' for Italian): ")
    get_and_save_transcript(video_url, language=language)
