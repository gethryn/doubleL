### Scenario: Apostrophes have been replaced with double quotes
* **Match:** `(?<=\w)(“|”)(?=\w)`
* **Replace:** `’`

### Scenario: There is a linebreak in the middle of a character's dialogue
* **Match:** `(?<=“[^”]*)</p>\s*<p[^>]*>(?!“)`
* **Replace:** `space`

### Scenario: A tag closes, is followed by 0+ spaces or newlines, is then reopened and is then followed by a lowercase letter
* **Match:** `</(?P<tag>\w+)>\s*<(?P=tag) [^/>]+>(?=[a-z])`
* **Match:** `(?<![".!?>*”“…~’])</(?P<tag>\w+)>\s*<(?P=tag) [^/>]+>`
* **Replace:** `space`

>> Notes: The second one is an alternate, which I think is better, but I'm not 100% sure it covers all the cases of the former.

### Scenario: "LL" Ligatures have been replaced with a single "L".
* **Match:** `(l (?=(y|s|ed|ey|ion|en|ar|ars|er|ow|et|owed|enge|age |enging|ected|egal|ections|ect|apse|ular|op|owing| ocks|ied|ier|ies|ing|ingly|ered|icit|est)(\W)))|(l (?![(–<-])(?=\W))|(?<=’)l(?=\W)|(?<= (wi|du|a|we|te|sma|ca|sti|fu|fa|chi|sha|wa|pha|se| bi|ha|ki|pu|ce|ba|ski|hi|fi|fe|he|ro|ta|i|sme|bri| sta|we))l(?=\W)`
* **Replace:** `ll`

>> Notes: This regex doesn't really work that well, but it's faster than doing it manually. I would recommend using the spellcheck afterwards and catching the most common ones. This regex is actually a bunch of individual ones chained together by ORs (|) so it's easier to see what's doing what.

### Scenario: More than 1 space in a row
* **Match:** `(?<=\S) {2,}(?=\S)`
* **Replace:** `space`

### Scenario: There are tags (which may be nested) that are either empty or just have a number in them
* **Match:** `(<[^/>]*>)+\s*\d*\s*(</[^>]*>)+`
* **Replace:** `[blank]`

>> Notes: This may remove things you'd like to keep, such as scenebreaks/whitespace, or the chapter links. 

### Scenario: There's a linebreak or spaces before a closing tag
* **Match:** `(?<![".!?>*”“…~’])</(?P<tag>\w+)>\s*<(?P=tag) [^/>]+>`
* **Replace:** `[blank]`
