# viperlib

A small package consisting of the following utility modules:

- jsd (contains class jsondata)
- misc
- vtime


There is no need to import the aforementioned modules individually, all the methods and classes placed in those modules are accessible through importing the viperlib packages itself.

### jsd - class *jsondata*

A simple interface for working with JSON files.

*Properties:*

    filename - name of the file without the extension (extention '.json' will be added automatically)
    location - location of the file. Once set, the file can be found and read from or write into
    contents - JSON contents of the class instance

*Methods:*

    full_path()
    file_exists()
    is_empty()        - returns True/False depending on whether the contents are empty
    get_from_file()   - reads contents from the JSON file
    save_to_file()    - saves contents in the JSON  file
    clear()           - empties the contents
    destroy()         - empties the contents and erases the file from the disc
    reset()           - empties the contents, destroys the file and sets 'filename' and 'location' to 'None'

*Example of use:*

    x = jsondata()
    x.filename = <filename>
    x.location = <some directory>
    x.contents = <data in JSON format>
    x.contents.update({<new key>: <value>})
    x.save_to_file() *# the updated JSON object is now saved in the file specified*
    print(x.get_from_file()) *# contents are read from file*
    x.destroy()

### misc

*Functions:*

    dir_get(path)                                 - returns directory portion of the 'path' argument
    parent_module_name_get()                      - returns name of the parent module as defined by actual module hierarchy if no argument provided or name of the parent module as defined by module hierarchy represented as a string argument
    months()                                      - returns list of names of months. First element is empty
    strdigit_normalize(digit)                     - normalizes input to format '0x'. Example: '9' -> '09'
    list_of_files_with_extension_get(dir, ext)    - returns list of all files with extension specified in the specified directory


### vtime

*Functions:*

    current_time_24h()         - returns current time in format hh:mm:ss
    secs2time(secs)            - converts integer number of seconds to a time string of format hh:mm:ss
    time2secs(timestr)         - converts time in format hh:mm:ss to number of seconds
    tsleep(timestr)            - custom sleep: pauses execution for time period in format hh:mm:ss
    timefromnow(plustime)      - returns time in format hh:mm:ss which is in hh:mm:ss from now as specified by the argument
    timestamp()                - returns timestamp in format dd-MMM hh:mm PM/AM
