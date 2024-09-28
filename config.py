# config.py

import os

LLM_MODEL_NAME = "gpt2"
LLM_MAX_LENGTH = 512

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = "personalized_learning_platform"

TEZOS_RPC_URL = os.environ.get("TEZOS_RPC_URL", "https://mainnet.api.tez.ie")
POLYGON_RPC_URL = os.environ.get("POLYGON_RPC_URL", "https://polygon-rpc.com")

STREAMLIT_PORT = 8501