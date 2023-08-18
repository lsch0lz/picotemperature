FROM python:3.11.4-slim

COPY . /application
RUN pip install -r /application/requirements.txt

WORKDIR /application
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

CMD ["streamlit", "run", "frontend/streamlit_app.py",  "--server.port=8501", "--server.address=0.0.0.0"]

