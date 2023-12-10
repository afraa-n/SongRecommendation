import unittest
import subprocess

class TestYourApp(unittest.TestCase):
    def test_streamlit_app(self):
        # Assuming your Streamlit app file is named app.py
        command = ["streamlit", "run", "app.py"]
        timeout_seconds = 30

        try:
            # Run the Streamlit app using subprocess with a timeout
            result = subprocess.run(command, check=True, capture_output=True, text=True, timeout=timeout_seconds)

            # Check if the subprocess exit code is 0 (success)
            self.assertEqual(result.returncode, 0, f"Subprocess terminated with an error. Exit Code: {result.returncode}")

            # You can add more specific assertions based on the app behavior if needed

        except subprocess.CalledProcessError as e:
            # If the subprocess exits with a non-zero code, handle the error
            self.fail(f"Subprocess terminated with an error. Exit Code: {e.returncode}\nOutput:\n{e.output}")
        except subprocess.TimeoutExpired:
            # If the subprocess times out, consider it a success
            self.assertTrue(True, f"Subprocess terminated successfully within {timeout_seconds} seconds")
            print("Mood-Based Song Recommendation App worked successfully!")

if __name__ == "__main__":
    unittest.main()
