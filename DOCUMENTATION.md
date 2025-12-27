# Antigravity – Sakeena: Project Documentation

**Project:** Spotify Playlist Automation (Delver)
**Version:** 1.0.0
**Author:** Jasmin (TechJas)
**Repository:** [github.com/TechJas/Delving-](https://github.com/TechJas/Delving-)

---

## 1. Project Overview
**Objective:** Create an emotionally intelligent playlist curation engine ("Delver") that automates the creation of a Spotify playlist designed to lift the listener from emotional weight to lightness.

**The "Antigravity Curve":**
The playlist follows a strict emotional progression structure:
1.  **Phase 1: Grounding & Familiarity:** Deep, spiritual, and safe tracks (e.g., Quran recitations, devotional chants).
2.  **Phase 2: Gentle Lift:** Piano, water sounds, and subtle movement to clear the mind.
3.  **Phase 3: Float State:** Weightless lofi, ambient, and airy soundscapes (The "Antigravity" effect).
4.  **Phase 4: Soft Landing:** Gratitude, resolution, and silence.

---

## 2. Technical Architecture
The project is built using **Python** and the **Spotipy** library to interact with the Spotify Web API.

### File Structure:
*   `create_playlist.py`: The main execution script. Handles authentication and API logic.
*   `playlist_data.py`: A separate data file containing the curated track list and metadata (Title, Artist, Phase, Notes).
*   `requirements.txt`: List of dependencies (`spotipy`).
*   `.gitignore`: Safety file to exclude secrets and system files from version control.

### Key Features:
*   **OAuth 2.0 Authentication:** Securely logs in user via Spotify Dashboard credentials.
*   **Smart Search:** Uses `track:name artist:name` specific queries to find the exact song match.
*   **Automated Curation:** Creates a new private playlist and adds songs in the exact strict order defined in the data file.

---

## 3. Setup & Installation Guide

### Prerequisites
*   Python 3.x installed.
*   A Spotify Account.
*   A Spotify Developer App (Client ID & Secret).

### Step-by-Step Instructions

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/TechJas/Delving-.git
    cd Delving-
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables:**
    (Run this in your terminal before starting the script)
    **Windows (CMD):**
    ```cmd
    set SPOTIPY_CLIENT_ID=your_client_id_here
    set SPOTIPY_CLIENT_SECRET=your_client_secret_here
    set SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
    ```

4.  **Run the Script:**
    ```bash
    python create_playlist.py
    ```

---

## 4. Future Maintenance
*   **Adding Songs:** Edit `playlist_data.py` to add new dictionaries to the `track_list`. Run the script again to generate a *new* playlist with the updates.
*   **Security:** Never share your `Client Secret` or upload `.env` files to GitHub.
