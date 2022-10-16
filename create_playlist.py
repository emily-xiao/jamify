import os

from spotify_client import SpotifyClient


def main():
    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
                                   os.getenv("SPOTIFY_USER_ID"))

    # get last played tracks=
    
    num_tracks_to_visualise = 50
    #int(input("How many tracks would you like to visualise? "))
    last_played_tracks = spotify_client.get_last_played_tracks(num_tracks_to_visualise)
    last_played_valences = spotify_client.get_valence(last_played_tracks)

    """
    print(f"\nHere are the last {num_tracks_to_visualise} tracks you listened to on Spotify:")
    for index, track in enumerate(last_played_tracks):
        print(f"{index+1}- {track}")
    """

    # choose which tracks to use as a seed to generate a playlist

    user_input = int(input("\nOn a scale from 1-5, how are you feeling today? "))
    seed_tracks = spotify_client.nearest_neighbours(user_input, last_played_tracks, last_played_valences)

    # get recommended tracks based off seed tracks
    recommended_tracks = spotify_client.get_track_recommendations(seed_tracks)
    """
    print("\nHere are the recommended tracks which will be included in your new playlist:")
    for index, track in enumerate(recommended_tracks):
        print(f"{index+1}- {track}")
    """

    # get playlist name from user and create playlist
    playlist_name = input("\nWhat's the playlist name? ")
    playlist = spotify_client.create_playlist(playlist_name)
    #print(f"\nPlaylist '{playlist.name}' was created successfully.")

    # populate playlist with recommended tracks
    spotify_client.populate_playlist(playlist, recommended_tracks)
    #print(f"\nRecommended tracks successfully uploaded to playlist '{playlist.name}'.")

if __name__ == "__main__":
    main()