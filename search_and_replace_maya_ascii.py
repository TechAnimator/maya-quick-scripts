import os

def get_anims_in_directory(path=None):
    """ Get all animation files found within the path """
    mayaAnims = []

    # Loop through all animation files in the path
    for root, dirs, files in os.walk(path):
        for file in files:
            # Grab all Maya Ascii files
            if file.endswith('.ma'):
                # Get the full filepath for each file
                mayaFile = root+'/'+file
                # Convert any backslashes to forward slashes because python hates backslashes
                mayaFile = mayaFile.replace('\\', '/')
                # Add file to the list
                mayaAnims.append(mayaFile)

    return mayaAnims

def search_and_replace(path_or_file=None, replace_dict=None):
    # If you state a single Maya file, it gets stored in a list
    if path_or_file.endswith('.ma'):
        anims = [path_or_file]
    else:
        anims = get_anims_in_directory(path=path_or_file)
    
    if anims:
        for anim in anims:
            # Make sure the animation file exists
            if os.path.isfile(anim):
                lines = []
            
                # Open the Maya Ascii file and stores it line for line, replacing the stated strings as they occur
                with open(anim) as infile:
                    for line in infile:
                        for src, target in replace_dict.iteritems():
                            line = line.replace(src, target)
                        lines.append(line)

                # Open a new file named with "_COPY" and populate the text for the new Ascii file
                with open(anim.replace('.ma', '_COPY.ma'), 'w') as outfile:
                    for line in lines:
                        outfile.write(line)

                # If you're feeling dangerous (or you use a versioning tool such as P4) you can change...
                # "with open(anim.replace('.ma', '_COPY.ma'), 'w')" to "with open(anim)" to open the anim file...
                # without a rename and write over it

# Format of dict is, key = "old" string that will get replaced, value = new string
replace_dict = {'CURRENT_STRING_TO_LOOK_FOR_AND_REPLACE':'STRING_TO_REPLACE_WITH',
                'CURRENT_STRING_TO_LOOK_FOR_AND_REPLACE_02':'STRING_TO_REPLACE_WITH_02'}

# If you want to search and replace in a single file
search_and_replace(path_or_file='c:/PATH/TO/A/SINGLE/MAYA/FILE/FILENAME.MA', replace_dict=replace_dict)

# If you want to search and replace in a directory (will search through any and all child folders of the folder you state)
search_and_replace(path_or_file='c:/PATH/TO/A/FOLDER/WITH/MAYA/FILES/', replace_dict=replace_dict)