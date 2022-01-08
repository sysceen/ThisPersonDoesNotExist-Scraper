import requests
from time import sleep
import os
import shutil

# Link to the randomly generated Face 
link = "https://thispersondoesnotexist.com/image"

# Path to the script
path = os.path.dirname(os.path.realpath(__file__))

# Path to folder where the images will be stored
foldname = path+'/pics/'
print(foldname)
# If Folder pics doesn't exist create it
if not os.path.exists(foldname):
    os.makedirs(foldname)

# Number used for file naming
number = 0

try:
    while True:
        # Naming scheme for the images
        filename = "img_" + str(number) + ".jpg"

        # The script will continue from the number that it reached on the last launch
        while os.path.isfile(foldname + filename):
            number += 1
            filename = "img_" + str(number) + ".jpg"

        # Request the link and get an object back
        r = requests.get(link, stream=True)

        # If success status response download the image
        if r.status_code == 200:

            # Open the file as write binary
            with open(foldname + filename, 'wb') as image:
                r.raw.decode_content = True

                # Copy content of the response to the file
                shutil.copyfileobj(r.raw, image)
                
                print('Image sucessfully Downloaded: ', filename)

        # Else print message
        else:
            print('Image Couldn\'t be retreived')

        # Website updates the face at a certain interval and going too fast would give duplicates
        sleep(0.5)

        # Increment Filename
        number += 1
except KeyboardInterrupt:
    print("\nGood luck!")