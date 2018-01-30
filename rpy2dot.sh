#!/usr/bin/env zsh
if [ $# -lt 1 ] ; then set *.rpy ; fi
for item in "$@" ; do
	echo "subgraph $(echo $item | sed 's/\.rpy$//')"
	cat "$item"	| 
		sed 's/^  *//g' | 
		egrep '^(label|jump)' | egrep -v '[\."]' |
		tr -d ':\r' |
		grep -v 'label _' | awk '
			/^label / { 
				if(curr_label)
					print curr_label " -> " $2 ";"
				curr_label=$2
			} 
			/^jump/ { 
				print curr_label " -> " $2 ";" 
			}' | sort | uniq
done | awk '
		
	BEGIN { 
		print "digraph path {" 
	} 
	/^subgraph /{
		curr_subgraph=$2
		next
	}
	{
		if(x[$1]) 	x[$1]=x[$1] $0
		else {
			x[$1]=$0
			c[$1]=curr_subgraph
		}
	}
	END {
		print "subgraph cluster_" c["start"] " {"
		print x["start"]
		print "style=\"rounded,dashed\";"
		print "color=blue;"
		print "labelalloc=b;"
		print "label=\"" c["start"] "\";"
		print "}"
		for (i in x)
			if(i!="start") {
				print "subgraph cluster_" c[i] "{"
				print x[i]
				print "style=\"rounded,dashed\";"
				print "color=blue;"
				print "labelalloc=b;"
				print "label=\"" c[i] "\";"
				print "}"
			}
		print "}"
	}' 
