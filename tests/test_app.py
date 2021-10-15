from app import app
from unittest import TestCase
from werkzeug.wrappers import response
from flask import session
from boggle import Boggle
import json

app.config['TESTING'] = True
app.config['DEBUG_TB_HOST'] = ['dont-show-debug-toolbar']

class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_game(self):
        """Test game starting"""
        with app.test_client() as client:
            response = client.get('/game')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<p class="highScore"> Current Score : </p>', html)


    def test_words(self):
        with app.test_client() as client:

            response = client.post('/words', data={'word': "W"})
            self.assertEqual(response['results'], 'ok')


    def test_session_update(self):
        """Check for session update"""
        with app.test_client() as client:

            response = client.post('/update', {'high score': 10,'times played': 15})
            self.assertEqual(response['High Score'],10)
            self.assertEqual(response['# of games played'], 10)
