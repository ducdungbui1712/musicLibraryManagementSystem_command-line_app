from track import Track
from playlist import Playlist

class LibraryManager:
    def __init__(self):
        self.library = []
        self.playlists = []

    def run(self):
        self.load_library()
        self.load_playlists()

        while True:
            print("\n----- Music Library Management System -----")
            print("1. Add a new music track")
            print("2. View the details of a specific music track")
            print("3. Update the details of an existing music track")
            print("4. Delete a music track from the library")
            print("5. Display a list of all music tracks in the library")
            print("6. Create a playlist")
            print("7. Add tracks to a playlist")
            print("8. Search for tracks or playlists")
            print("9. Exit")

            choice = input("Enter your choice (1-9): ")
            if choice == "1":
                self.add_track()
            elif choice == "2":
                self.view_track()
            elif choice == "3":
                self.update_track()
            elif choice == "4":
                self.delete_track()
            elif choice == "5":
                self.display_all_tracks()
            elif choice == "6":
                self.create_playlist()
            elif choice == "7":
                self.add_tracks_to_playlist()
            elif choice == "8":
                self.search()
            elif choice == "9":
                self.save_library()
                self.save_playlists()
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def load_library(self):
        try:
            with open("library.txt", "r") as file:
                for line in file:
                    title, artist, album, genre, release_year, duration = line.strip().split(",")
                    track = Track(title, artist, album, genre, release_year, duration)
                    self.library.append(track)
            print("Library loaded successfully!")
        except FileNotFoundError:
            print("Library file not found. Starting with an empty library.")

    def load_playlists(self):
        try:
            with open("playlists.txt", "r") as file:
                for line in file:
                    # for each line, it splits the line by commas to extract the playlist name and track titles.
                    playlist_data = line.strip().split(",")
                    playlist_name = playlist_data[0]
                    track_titles = playlist_data[1:]

                    playlist = Playlist(playlist_name)
                    for title in track_titles:
                        track = self.find_track_by_title(title)
                        if track:
                            playlist.tracks.append(track)

                    self.playlists.append(playlist)

            print("Playlists loaded successfully!")
        except FileNotFoundError:
            print("Playlists file not found. Starting with no playlists.")

    def find_track_by_title(self, title):
        for track in self.library:
            if track.title == title:
                return track
        return None
    
    def save_library(self):
        with open("library.txt", "w") as file:
            for track in self.library:
                line = f"{track.title},{track.artist},{track.album},{track.genre},{track.release_year},{track.duration}\n"
                file.write(line)
        print("Library saved successfully!")

    def save_playlists(self):
        with open("playlists.txt", "w") as file:
            for playlist in self.playlists:
                file.write(f"{playlist.name}")
                for track in playlist.tracks:
                    file.write(f",{track.title}")
                file.write("\n")
        print("Playlists saved successfully!")

    
    def add_track(self):
        print("Enter the details of the new track:")
        title = input("Title: ")
        artist = input("Artist: ")
        album = input("Album: ")
        genre = input("Genre: ")
        release_year = input("Release Year: ")
        duration = input("Duration (mm:ss): ")

        track = Track(title, artist, album, genre, release_year, duration)
        self.library.append(track)
        self.save_library()

        print("Track added successfully!")

    def display_all_tracks(self):
        if not self.library:
            print("\n----- Result -----")
            print("The library is empty.")
        else:
            print("\n----- Result -----")
            print("All tracks in the library:")
            for index, track in enumerate(self.library, start=1):
                print(f"{index}. {track.title} - {track.artist} ({track.album})")

    def view_track(self):
        search_term = input("Enter the title or artist of the track you want to view: ")
        found_tracks = []

        for track in self.library:
            if search_term.lower() in track.title.lower() or search_term.lower() in track.artist.lower():
                found_tracks.append(track)

        if not found_tracks:
            print("\n----- Result -----")
            print("No matching tracks found.")
        else:
            print("\n----- Result -----")
            print("Matching tracks:")
            for index, track in enumerate(found_tracks, start=1):
                print(f"{index}. Title: {track.title}")
                print(f"   Artist: {track.artist}")
                print(f"   Album: {track.album}")
                print(f"   Genre: {track.genre}")
                print(f"   Release Year: {track.release_year}")
                print(f"   Duration: {track.duration}")

    def update_track(self):
        search_term = input("Enter the title or artist of the track you want to update: ")
        found_tracks = []

        for track in self.library:
            if search_term.lower() in track.title.lower() or search_term.lower() in track.artist.lower():
                found_tracks.append(track)

        if not found_tracks:
            print("\n----- Result -----")
            print("No matching tracks found.")
        else:
            print("\n----- Result -----")
            print("Matching tracks:")
            for index, track in enumerate(found_tracks, start=1):
                print(f"{index}. Title: {track.title}")
                print(f"   Artist: {track.artist}")
                print(f"   Album: {track.album}")
                print(f"   Genre: {track.genre}")
                print(f"   Release Year: {track.release_year}")
                print(f"   Duration: {track.duration}")

            track_index = int(input("Enter the number of the track you want to update: ")) - 1
            if track_index < 0 or track_index >= len(found_tracks):
                print("\n----- Result -----")
                print("Invalid track number.")
            else:
                track = found_tracks[track_index]
                print("Enter the new details for the track (press Enter to skip):")
                new_title = input(f"Title [{track.title}]: ")
                new_artist = input(f"Artist [{track.artist}]: ")
                new_album = input(f"Album [{track.album}]: ")
                new_genre = input(f"Genre [{track.genre}]: ")
                new_release_year = input(f"Release Year [{track.release_year}]: ")
                new_duration = input(f"Duration (mm:ss) [{track.duration}]: ")

                # Update the track details if new values are provided
                if new_title:
                    track.title = new_title
                if new_artist:
                    track.artist = new_artist
                if new_album:
                    track.album = new_album
                if new_genre:
                    track.genre = new_genre
                if new_release_year:
                    track.release_year = new_release_year
                if new_duration:
                    track.duration = new_duration

                self.save_library()
                print("\n----- Result -----")
                print("Track details updated successfully!")

    def delete_track(self):
        search_term = input("Enter the title or artist of the track you want to delete: ")
        found_tracks = []

        for track in self.library:
            if search_term.lower() in track.title.lower() or search_term.lower() in track.artist.lower():
                found_tracks.append(track)

        if not found_tracks:
            print("\n----- Result -----")
            print("No matching tracks found.")
        else:
            print("\n----- Result -----")
            print("Matching tracks:")
            for index, track in enumerate(found_tracks, start=1):
                print(f"{index}. Title: {track.title}")
                print(f"   Artist: {track.artist}")
                print(f"   Album: {track.album}")
                print(f"   Genre: {track.genre}")
                print(f"   Release Year: {track.release_year}")
                print(f"   Duration: {track.duration}")

            track_index = int(input("Enter the number of the track you want to delete: ")) - 1
            if track_index < 0 or track_index >= len(found_tracks):
                print("\n----- Result -----")
                print("Invalid track number.")
            else:
                track = found_tracks[track_index]
                self.library.remove(track)
                self.save_library()
                print("\n----- Result -----")
                print("Track deleted successfully!")

    def create_playlist(self):
        playlist_name = input("Enter the name of the playlist: ")

        # Check if the playlist name already exists
        for playlist in self.playlists:
            if playlist.name.lower() == playlist_name.lower():
                print("\n----- Result -----")
                print("A playlist with the same name already exists.")
                return

        playlist = Playlist(playlist_name)
        self.playlists.append(playlist)
        self.save_playlists()

        print("\n----- Result -----")
        print("Playlist created successfully!")

    def add_tracks_to_playlist(self):
        if not self.playlists:
            print("\n----- Result -----")
            print("No playlists available. Create a playlist first.")
            return
        
        print("\n----- Result -----")
        print("Available playlists:")
        for index, playlist in enumerate(self.playlists, start=1):
            print(f"{index}. {playlist.name}")

        playlist_index = int(input("Enter the number of the playlist to add tracks to: ")) - 1

        if playlist_index < 0 or playlist_index >= len(self.playlists):
            print("\n----- Result -----")
            print("Invalid playlist number.")
            return

        playlist = self.playlists[playlist_index]

        search_term = input("Enter the search term to find tracks: ")
        found_tracks = []

        for track in self.library:
            if search_term.lower() in track.title.lower() or \
            search_term.lower() in track.artist.lower() or \
            search_term.lower() in track.album.lower() or \
            search_term.lower() in track.genre.lower():
                found_tracks.append(track)

        if not found_tracks:
            print("\n----- Result -----")
            print("No matching tracks found.")
            return

        print("\n----- Result -----")
        print("Matching tracks:")
        for index, track in enumerate(found_tracks, start=1):
            print(f"{index}. Title: {track.title}")
            print(f"   Artist: {track.artist}")
            print(f"   Album: {track.album}")
            print(f"   Genre: {track.genre}")
            print(f"   Release Year: {track.release_year}")
            print(f"   Duration: {track.duration}")

        track_index = int(input("Enter the number of the track to add: ")) - 1

        if track_index < 0 or track_index >= len(found_tracks):
            print("\n----- Result -----")
            print("Invalid track number.")
            return

        
        found_track_index = found_tracks[track_index]
        for track in playlist.tracks:
            if (found_track_index.title.lower() == track.title.lower()):
                print("\n----- Result -----")
                print("Track is already added.")
                return
        playlist.tracks.append(found_track_index)
        self.save_playlists()

        print("\n----- Result -----")
        print("Track added to the playlist successfully!")


    def search(self):
        search_term = input("Enter a search term: ")
        found_tracks = []
        found_playlists = []

        # Search for tracks that match the search term
        for track in self.library:
            if (
                search_term.lower() in track.title.lower()
                or search_term.lower() in track.artist.lower()
                or search_term.lower() in track.album.lower()
                or search_term.lower() in track.genre.lower()
            ):
                found_tracks.append(track)

        # Search for playlists that have tracks matching the search term
        for playlist in self.playlists:
                if search_term.lower() in playlist.name.lower():
                    found_playlists.append(playlist)
                for track in playlist.tracks:
                    if (
                        search_term.lower() in track.title.lower()
                        or search_term.lower() in track.artist.lower()
                        or search_term.lower() in track.album.lower()
                        or search_term.lower() in track.genre.lower()
                    ):
                        found_playlists.append(playlist)
                        # Once a matching track is found, move to the next playlist
                        break 

        if not found_tracks and not found_playlists:
            print("\n----- Result -----")
            print("No matching tracks or playlists found.")
        else:
            print("\n----- Result -----")
            if found_tracks:
                print("Matching tracks:")
                for index, track in enumerate(found_tracks, start=1):
                    print(f"{index}. Title: {track.title}")
                    print(f"   Artist: {track.artist}")
                    print(f"   Album: {track.album}")
                    print(f"   Genre: {track.genre}")
                    print(f"   Release Year: {track.release_year}")
                    print(f"   Duration: {track.duration}")

            if found_playlists:
                print("Matching playlists:")
                for index, playlist in enumerate(found_playlists, start=1):
                    print(f"{index}. Playlist Name: {playlist.name}")