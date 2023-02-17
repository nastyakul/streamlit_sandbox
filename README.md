## Streamlit-sandbox

A sample project for playing around with deployment on DigitalOcean.

### Running locally
1. Build 
``docker build -t streamlit_sandbox .``
2. Run
``docker run --platform=linux/amd64 -p 8501:8501 -t streamlit_sandbox``