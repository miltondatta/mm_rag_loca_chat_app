import streamlit as st
from chat_api_handler import ChatAPIHandler
from streamlit_mic_recorder import mic_recorder
from utils import get_timestamp, load_config, get_avatar
from audio_handler import transcribe_audio
from pdf_handler import add_documents_to_db
from html_templates import css
from database_operations import save_text_message, save_image_message, save_audio_message, load_messages, get_all_chat_history_ids, delete_chat_history, load_last_k_text_messages_ollama
from utils import list_openai_models, list_ollama_models, command
import sqlite3