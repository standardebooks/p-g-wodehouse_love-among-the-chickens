#!/usr/bin/env python3

import re
import sys

for filename in sys.argv[1:]:
    print( filename)
    with open(filename+".fix",'w') as fix_fh:
        with open(filename,'r') as html_fh:
            prev_h3 = ""
            for line in html_fh:
                h3match = re.search(r'<H3[^>]*>\s*(.+\S)\s*</H3>',line)
                if h3match:
                    if prev_h3:
                        #<h2 epub:type="title">
                        #    <span epub:type="z3998:roman">CHAPTER I</span>
                        #    <span epub:type="subtitle">A LETTER WITH A POSTSCRIPT</span>
                        #</h2>
                        print("<h2>", file=fix_fh)
                        print("    <span epub:type=\"z3998:roman\">",
                                end="", file=fix_fh)
                        print(prev_h3, end="", file=fix_fh)
                        print("</span>", file=fix_fh)
                        print("    <span epub:type=\"subtitle\">",
                                end="", file=fix_fh)
                        print(h3match.group(1), end="", file=fix_fh)
                        print("</span>", file=fix_fh)
                        print("</h2>", file=fix_fh)
                        prev_h3 = ""
                    else:
                        prev_h3 = h3match.group(1)
                else:
                    # no extra \n because line has one already
                    print(line, end="", file=fix_fh)
