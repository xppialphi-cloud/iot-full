import streamlit as st
import pandas as pd
from supabase import create_client, Client
from datetime import datetime, timedelta, timezone
import plotly.express as px
import time
import os
from dotenv import load_dotenv

# Wuxuu si toos ah u akhrinayaa faylka .env.local
load_dotenv(dotenv_path=".env.local")

st.set_page_config(
    page_title="Real-Time IoT Dashboard",
    layout="wide"
)

st.title("🔋 Real-Time PostgreSQL SCADA Dashboard")
st.write("Live telemetry environmental streams from remote Supabase cloud")

# Halkaan wuxuu ka akhrisanayaa furayaasha dhabta ah ee ku jira .env.local
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

@st.cache_resource
def init_supabase() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase: Client = init_supabase()

# ====================================================
# KEEP ALL OF YOUR EXISTING DASHBOARD CODE HERE
# (everything from get_latest_telemetry() down to st.rerun())
# ====================================================
