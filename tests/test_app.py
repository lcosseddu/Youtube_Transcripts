import pytest
from YTT_WebApp import app, db
from models import User
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 302  # Redirect to login page

def test_register(client):
    response = client.post('/register', data={
        'email': 'test@example.com',
        'password': 'TestPassword1!',
        'confirm_password': 'TestPassword1!',
        'first_name': 'Test',
        'last_name': 'User'
    }, follow_redirects=True)
    assert b'Registered successfully' in response.data

def test_login(client):
    # First register a user
    client.post('/register', data={
        'email': 'test@example.com',
        'password': 'TestPassword1!',
        'confirm_password': 'TestPassword1!',
        'first_name': 'Test',
        'last_name': 'User'
    })

    # Then try to login
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'TestPassword1!'
    }, follow_redirects=True)
    assert b'Welcome, Test!' in response.data

def test_index_page_get_authenticated(client):
    # Simulate a GET request for an authenticated user
    client.post('/register', data={
        'email': 'test@example.com',
        'password': 'TestPassword1!',
        'confirm_password': 'TestPassword1!',
        'first_name': 'Test',
        'last_name': 'User'
    })
    client.post('/login', data={
        'email': 'test@example.com',
        'password': 'TestPassword1!'
    })
    
    response = client.get('/')
    assert response.status_code == 200  # Check if the page loads successfully
    assert b'Welcome, Test!' in response.data  # Check for the welcome message

def test_index_page_post_valid_data(client):
    # Simulate a POST request with valid data
    client.post('/register', data={
        'email': 'test@example.com',
        'password': 'TestPassword1!',
        'confirm_password': 'TestPassword1!',
        'first_name': 'Test',
        'last_name': 'User'
    })
    client.post('/login', data={
        'email': 'test@example.com',
        'password': 'TestPassword1!'
    })

    response = client.post('/', data={
        'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'language': 'en'
    }, follow_redirects=True)
    
    assert response.status_code == 200  # Check if the page loads successfully
    assert b'[Music]' in response.data  # Check if the transcript content is present

def test_index_page_post_invalid_url(client):
    # Simulate a POST request with an invalid YouTube URL
    client.post('/register', data={
        'email': 'test@example.com',
        'password': 'TestPassword1!',
        'confirm_password': 'TestPassword1!',
        'first_name': 'Test',
        'last_name': 'User'
    })
    client.post('/login', data={
        'email': 'test@example.com',
        'password': 'TestPassword1!'
    })

    response = client.post('/', data={
        'video_url': 'invalid_url',
        'language': 'en'
    }, follow_redirects=True)
    
    assert b'Invalid YouTube URL' in response.data  # Check for error message

def test_index_page_post_missing_fields(client):
    # Simulate a POST request with missing fields
    client.post('/register', data={
        'email': 'test@example.com',
        'password': 'TestPassword1!',
        'confirm_password': 'TestPassword1!',
        'first_name': 'Test',
        'last_name': 'User'
    })
    client.post('/login', data={
        'email': 'test@example.com',
        'password': 'TestPassword1!'
    })

    response = client.post('/', data={
        'video_url': '',  # Missing video URL
        'language': 'en'
    }, follow_redirects=True)
    
    assert b'Please fill out this field' in response.data  # Check for error message

def test_index_page_post_exception_handling(client):
    # Simulate a POST request that raises an exception
    client.post('/register', data={
        'email': 'test@example.com',
        'password': 'TestPassword1!',
        'confirm_password': 'TestPassword1!',
        'first_name': 'Test',
        'last_name': 'User'
    })
    client.post('/login', data={
        'email': 'test@example.com',
        'password': 'TestPassword1!'
    })

    with patch('youtube_transcriptor.get_and_save_transcript', side_effect=Exception("An error occurred")):
        response = client.post('/', data={
            'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'language': 'en'
        }, follow_redirects=True)
    
    assert b'An error occurred' in response.data  # Check for error message

def test_index_page_get_unauthenticated(client):
    # Simulate a GET request from an unauthenticated user
    response = client.get('/')
    assert response.status_code == 302  # Check for redirection to login page
    assert response.headers['Location'].startswith('/login')  # Check redirection URL

