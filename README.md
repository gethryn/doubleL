# doubleL
Perl to restore LL to batch of text files where second L is replaced by space


Copy the `fixDoubleL_batch.pl` file to a new directory on your system.  I suggest a subdirectory of your Documents folder.

Create an `html` sub directory, and load all your text files (must have `.html` or `.txt` file extension).

Open Finder, and press Cmd-Shift-U to open utilities menu.  Double click on Terminal to open a terminal window.

Navigate to the directory:

`cd ~/Documents/newdirectory`

Then type the following to begin processing the files:

`perl fixDoubleL_batch.pl` and press return.

The cleaned files are generated in the html directory with a `_clean` designation in the filenames.


### Git Instructions Changes:
`git status` will tell you what's changed/.

`git add filename` for each filename that's changed if you want to commit it to the server.

`git commit -m "What you changed"` to prepare the payload for the server

`git push` to deploy to the server.

### Git Instructions Pull down the latest:

`git pull` to pull doen the latest from the server.
