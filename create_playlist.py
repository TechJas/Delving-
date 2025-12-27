import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from playlist_data import playlist_title, playlist_description, track_list
import sys

def create_playlist():
    # 1. Setup Authentication
    # Ensure environment variables are set or prompt user
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI", "http://localhost:8888/callback")

    if not client_id or not client_secret:
        print("Error: SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET environment variables must be set.")
        print("Please set them in your terminal or create a .env file/setup script.")
        print("Example Powershell:")
        print('$env:SPOTIPY_CLIENT_ID="your_id"')
        print('$env:SPOTIPY_CLIENT_SECRET="your_secret"')
        print('$env:SPOTIPY_REDIRECT_URI="http://localhost:8888/callback"')
        return

    scope = "playlist-modify-public playlist-modify-private"
    
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope
        ))
        user_id = sp.me()['id']
        print(f"Authenticated as user: {user_id}")
    except Exception as e:
        print(f"Authentication failed: {e}")
        return

    # 2. Create the Playlist
    try:
        playlist = sp.user_playlist_create(
            user=user_id,
            name=playlist_title,
            public=False, # Default to private for safety
            description=playlist_description
        )
        playlist_id = playlist['id']
        print(f"\nCreated playlist: {playlist_title} ({playlist_id})")
    except Exception as e:
        print(f"Failed to create playlist: {e}")
        return

    # 3. Search and Add Tracks
    track_uris = []
    
    print("\nSearching for tracks...")
    
    for track in track_list:
        query = f"track:{track['title']} artist:{track['artist']}"
        print(f"Searching for: {query}...", end=" ")
        
        try:
            results = sp.search(q=query, type='track', limit=1)
            items = results['tracks']['items']
            
            if items:
                found_track = items[0]
                track_uris.append(found_track['uri'])
                print(f"MATCH: {found_track['name']} by {found_track['artists'][0]['name']}")
            else:
                # Fallback search - sometimes strict key:value search fails if names are slightly different
                # Try a broader search string
                broad_query = f"{track['title']} {track['artist']}"
                results = sp.search(q=broad_query, type='track', limit=1)
                items = results['tracks']['items']
                if items:
                     found_track = items[0]
                     track_uris.append(found_track['uri'])
                     print(f"MATCH (Broad): {found_track['name']} by {found_track['artists'][0]['name']}")
                else:
                    print(f"NOT FOUND: {track['title']} - {track['artist']}")
                
        except Exception as e:
            print(f"ERROR searching: {e}")

    # 4. Add to Playlist
    if track_uris:
        try:
            # Add in batches of 100 if necessary (though our list is small)
            sp.playlist_add_items(playlist_id, track_uris)
            print(f"\nSuccessfully added {len(track_uris)} tracks to '{playlist_title}'.")
            print("Check your Spotify account!")
        except Exception as e:
             print(f"Failed to add tracks: {e}")
    else:
        print("\nNo tracks were found to add.")

if __name__ == "__main__":
    create_playlist()
