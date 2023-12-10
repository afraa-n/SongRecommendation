# Use the official Streamlit base image
FROM streamlit/streamlit:0.90.0

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the local directory to the container
COPY . .

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
