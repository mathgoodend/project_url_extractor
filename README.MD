# Read Me
This program is a simple python script written by me to solve a particular problem, maybe you'll find it useful too. All it does is search one or more files stored in the *./files* directory and fetch the urls it finds. 

By default, the program looks at the *./filter* folder to get a list of specific urls you're looking for, so it will only extract those. This list of filters is just a plain *.txt* file with one site per line, without https or www written. 

You can type the argument **nofilter** when running the script to instead of using filters just extracting every possible url from the files.

## Installing
Download the project, and inside it's directory run `pip3 install -e .`. To uninstall you can just run `pip3 uninstall url_extractor`

Then, you can just run `url_extractor` or  `url_extractor nofilter`.

If you type `url_extractor man` or `url_extractor manual`, the script will print it's user manual.