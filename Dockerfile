# Start with a Python build image
FROM python:3.8 as builder
WORKDIR /app
COPY requirements.txt .
# Install Python packages
RUN pip install -r requirements.txt
EXPOSE 5000

# Use a distroless image
FROM gcr.io/distroless/python3
COPY --from=builder /app /app
WORKDIR /app
CMD ["app.py"]