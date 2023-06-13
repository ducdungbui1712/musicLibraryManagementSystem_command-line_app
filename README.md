# Running and Using the Music Library Management System
## Introduction:
* This Music Library Management System is a simple application designed to manage a library of music tracks and playlists with a command-line interface. This report provides instructions on how to run and use the app effectively.

## System Requirements:
Before running the Music Library Management System, ensure that you have the following requirements:
1. Python 3 installed on your system.
2. All .py files have to be in the same directory as the main script.
3. Two text files named "library.txt" and "playlists.txt" will be auto created in the same directory as the main script after you add new tracks or exit the application for the first time. These files will be used to store the library and playlist data.

## Running the App:
To run the Music Library Management System, follow these steps:
1. Open a command-line interface or terminal.
2. Navigate to the directory containing the main script and the required files.
3. Execute the following command to start the app:
```
python .\main.py
```
4. The Music Library Management System will start, and you will see a menu with various options for managing your music library.

## Using the App:
Once the app is running, you can perform the following operations:

1. Add a new music track:
 * Choose option 1 from the menu.
 * Enter the details of the new track as prompted.
 * The track will be added to the library.

2. View the details of a specific music track:
 * Choose option 2 from the menu.
 * Enter the title or artist of the track you want to view.
 * The app will display the matching tracks' details, if any.

3. Update the details of an existing music track:
 * Choose option 3 from the menu.
 * Enter the title or artist of the track you want to update.
 * Choose the track from the list of matching tracks.
 * Enter the new details for the track, or press Enter to skip a field.
 * The track's details will be updated in the library.
 
4. Delete a music track from the library:
 * Choose option 4 from the menu.
 * Enter the title or artist of the track you want to delete.
 * Choose the track from the list of matching tracks.
 * The track will be deleted from the library.
