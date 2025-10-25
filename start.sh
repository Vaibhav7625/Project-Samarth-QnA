#!/bin/bash

# Start FastAPI backend in the background on port 8000
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Give backend a few seconds to start
sleep 5

# Start Streamlit frontend on Render's assigned port
streamlit run frontend.py --server.port $PORT --server.headless true
