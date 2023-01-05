import fabric
import datetime

# Import required functions from the os and tarfile modules
from os import listdir, makedirs
from tarfile import TarInfo, open as taropen

def do_pack():
    # Create the path to the versions folder
    versions_folder = 'versions'

    # Check if the versions folder exists, and if not create it
    if not fabric.contrib.files.exists(versions_folder):
        makedirs(versions_folder)

    # Get the current date and time
    now = datetime.datetime.now()

    # Format the date and time to be used in the archive filename
    date_string = now.strftime('%Y%m%d%H%M%S')

    # Create the archive filename
    archive_name = f'web_static_{date_string}.tgz'

    # Create the path to the archive
    archive_path = f'{versions_folder}/{archive_name}'

    # Open the archive in write mode
    with taropen(archive_path, 'w:gz') as tar:
        # Get a list of all files in the web_static folder
        files = listdir('web_static')

        # Iterate over the files in the web_static folder
        for file in files:
            # Create a TarInfo object for the file
            tarinfo = TarInfo(file)

            # Add the file to the archive
            tar.add('web_static/' + file, tarinfo)

    # Return the path to the archive
    return archive_path
