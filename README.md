# doubleL
Perl script to restore LL to batch of text files where second L is replaced by space.  The github url is [https://github.com/gethryn/doubleL](https://github.com/gethryn/doubleL).

### Run the Cleaning Script (works with multiple files):

* Add your input files to the `html` subdirectory `~/Documents/BookFixScripts/doubleL/html` using Finder.

* Open a Terminal. (Open Finder, and press Cmd-Shift-U to open utilities menu.  Double click on Terminal to open a terminal window).
> I recommend you download [iTerm](https://iterm2.com) instead of the basic terminal. Pin it to your dock.

* Use `git pull` to bring down the latest scripts (see below for details). 

* Navigate to the working directory: `cd ~/Documents/BookFixScripts/doubleL` (note, this is the same as `/Users/gramps/Documents/BookFixScripts/doubleL`).

* Type the following to begin processing the files: `perl fixDoubleL_batch.pl` and press return.  

> The script will automatically use the filename `doubleL_words.txt` for the list of LL words.  If you want to specify a different one, just give the name after the perl script name in the command line: `perl fixDoubleL_batch.pl other_LL_file.txt`.

* The cleaned files are generated in the `html` directory with a `_clean` designation in the filenames.


### Git Instructions to Publish Your Changes:
* `git status` will tell you what's changed.

* `git add filename` for each filename that's changed if you want to commit it to the server.

* `git commit -m "What you changed"` to prepare the payload for the server

* `git push` to deploy to the server.


### Git Instructions Pull down the latest files from the server.

* `git pull` to pull doen the latest from the server.

> If you get an error that the information on your machine is newer than server local copy, just run `git push` to send your changes to the server, and then run `git pull` again.  You don't need to worry about one overwriting the other.  Git will merge the changes as long as we haven't bioth changed the same part of a file.


### What directory am I in? Get me home!
* Enter the command `pwd` (print working directory) to tell you where you are.
* Enter the command `cd` on it's own to take you to your home folder `~` (i.e. `/Users/gramps/`).
* Use `cd -` to go back to the directory you were last at (useful if you use `cd` to go home, and then want to go back to `~/Documents/BooxFixScripts/doubleL` without all that typing).
* Use up arrow to scroll through previous commands.


### For Geth's reference later
* Use the command `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"` to install [OhMyZSH](https://github.com/ohmyzsh/ohmyzsh) (better command line prompts/tools). 

* We may also need [powerline fonts](https://github.com/powerline/fonts), which can be installed with the following:
```sh
# clone
git clone https://github.com/powerline/fonts.git --depth=1
# install
cd fonts
./install.sh
# clean-up a bit
cd ..
rm -rf fonts
```
