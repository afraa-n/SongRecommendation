# Use the official Python image as the base image
FROM python:3.9.7-slim AS base

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files for installing dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage for building the app
FROM base AS builder

# Copy the rest of the application files
COPY . .

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]

# Stage for the final lightweight image
FROM base AS final

# Copy the built app from the builder stage
COPY --from=builder /app /app

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
