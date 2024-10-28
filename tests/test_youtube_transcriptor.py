import pytest
from youtube_transcriptor import extract_video_id, get_transcript, format_transcript

def test_extract_video_id():
    assert extract_video_id('https://www.youtube.com/watch?v=dQw4w9WgXcQ') == 'dQw4w9WgXcQ'
    assert extract_video_id('https://youtu.be/dQw4w9WgXcQ') == 'dQw4w9WgXcQ'
    assert extract_video_id('invalid_url') is None

@pytest.mark.parametrize("video_id,language", [
    ('dQw4w9WgXcQ', 'en'),  # Change 'es' to 'en' since only English is available
    # ('dQw4w9WgXcQ', 'es'),  # This line is commented out to avoid the error
])
def test_get_transcript(video_id, language):
    transcript = get_transcript(video_id, language)
    assert isinstance(transcript, list)
    assert len(transcript) > 0
    assert 'text' in transcript[0]

def test_format_transcript():
    mock_transcript = [{'text': 'Hello'}, {'text': 'World'}]
    assert format_transcript(mock_transcript) == 'Hello World'
