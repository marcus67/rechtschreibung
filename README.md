<IMG SRC="https://raw.githubusercontent.com/marcus67/rechtschreibung/master/lib/rechtschreibung_64.png">
#  rechtschreibung
A little Python app to be used with Pythonista to test different rule sets for German spelling.

## Requirements

You need to have Pythonista installed on iOS.

## Basic Functionality

This project allows you to test different combinations of German spelling rules with a simple GUI. Each change of rules is immediately reflected in a text especially written for this purpose. The GUI can be used to store favorite combinations and compare them.

<CENTER>
<IMG SRC="https://raw.githubusercontent.com/marcus67/rechtschreibung/master/doc/main_screen.png" WIDTH="800px">
</CENTER>

## Installation

The source code is available as a self-extracting Python script. See file `build/rechtschreibung_zip.py`. Download this file and follow the instructions contained therein.

## Usage

### Main View

The main view is shown upon start of the application. It looks different for small devices (iPhone) and large devices (iPad). We'll concentrate on the version for larger devices first.

<CENTER>
<IMG SRC="https://raw.githubusercontent.com/marcus67/rechtschreibung/master/doc/main_screen.png" WIDTH="800px">
</CENTER>

On the left an especially crafted text (see screenshot above) is displayed. It serves two purposes. The first purpose is to explain the motivation behind the app and introduce to fictional characters (Casimir and Wendy) representing the two opposing positions in the discussion about German spelling: Casimir is the conservative person trying to main the status quo and Wendy is the progressive person trying to change rules to make them easier and more consistent.

The second purpose of the text is to display the impact of the various rules on a text, meaning everytime the user changes one of the rules the changes in the text are immediately reflected. For a short period of time the actual changes are highlighted: letters which are to be deleted are shown with grey background and striked out. Letters which are to be inserted are shown with green background. Usually (unless deactivated) the highlighted sections are removed after a certain delay (e.g. 5 seconds). 

Since some of the rules have very little impact on a standard text, it has been seen to it that in the conversation between 
Casimir and Wendy there are especially designed sample sentences showing the differences.

#### Rule Sets

The spelling rules are organized in currently six sections (see upper right navigation area in screen shot above). Actually, the term "spelling" is a little wider than just the correct use of letters for words. The rule sets also contain aspects of punctuation ("Zeichensetzung") and layout.

##### App Control View

The App Control view in the lower right corner shows some setting influencing the behaviour of the app.

##### Highlighting of Changes
There are three modes for highlighting the changes after an applied rule change:

 * The highlighting is off ("aus").
 * The highlighting is done compared to the immediately previous rule set ("Delta").
 * The highlighting is done compared to the reference rule set ("Referenz"). The initial reference rule set is the currently valid spelling rule set as proposed by the book "Duden". It can be changed by loaded other rule sets.


Have fun!

