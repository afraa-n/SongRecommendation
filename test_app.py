import unittest
import sys
from unittest.mock import patch, MagicMock
from io import StringIO
from app import st  # Import the streamlit app instance

class TestApp(unittest.TestCase):

    @patch("streamlit.button")
    @patch("streamlit.text_input")
    def test_tell_us_how_you_feel(self, mock_text_input, mock_button):
        # Mock user input
        mock_text_input.return_value = "Happy"
        
        # Simulate button click
        mock_button.return_value = MagicMock(name="ButtonMock")

        # Redirect stdout to capture print/log statements
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        # Run the Streamlit app
        with patch('streamlit._is_running_with_streamlit'):
            # Simulate button click by calling the button's 'on_click' method
            st.button('Simulated Button')
            mock_button().on_click()

        # Reset redirect
        sys.stdout = original_stdout

        # Add assertions based on the expected behavior of your app

if __name__ == '__main__':
    unittest.main()
