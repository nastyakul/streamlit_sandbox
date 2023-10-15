# Retrospective summarizer :memo:

This is a simple "sandbox" project that allows one to summarize retrospective notes. 


https://github.com/nastyakul/streamlit_sandbox/assets/22914830/1d9c3dff-bc47-4591-99ca-da2389157229




## Tech stack
- [Streamlit](https://streamlit.io/) UI
- [DigitalOcean](https://www.digitalocean.com/try/developer-brand?utm_campaign=emea_brand_kw_en_cpc&utm_adgroup=digitalocean_exact_exact&_keyword=digital%20ocean&_device=c&_adposition=&utm_content=conversion&utm_medium=cpc&utm_source=google&gad=1&gclid=Cj0KCQjwm66pBhDQARIsALIR2zCUBVb8ysDlpgt2d2JbUDlaIb8nGsDwBpMdrXDXDxo4TWgNJZMDFv8aAm5lEALw_wcB) deployment (currently discontinued)
- [OpenAI](https://platform.openai.com/docs/models/overview) for natural language processing
- [Google Cloud Vision API](https://cloud.google.com/vision/docs/libraries)  for image to text

## Running locally
1. Build 
``docker build -t streamlit_sandbox .``
2. Run
``docker run --platform=linux/amd64 -p 8501:8501 -t streamlit_sandbox``
