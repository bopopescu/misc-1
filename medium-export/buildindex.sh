#!/usr/bin/env zsh
(echo "<html><head><title>Medium backup</title> <link rel="stylesheet" type="text/css" href="../vt240.css"></head><body><table>" ; ls 20*.html | tac | while read i ; do  echo '<tr><td>'"$(echo $i | sed 's/_.*$//')"'</td><td><a href="'"$i"'">'"$(grep '<title>' "$i" | head -n 1 | sed 's/^.*<title>//;s/<\/title>.*$//')"'</a></td></tr>' ; done ; echo "</table></body></html>") > index.html
