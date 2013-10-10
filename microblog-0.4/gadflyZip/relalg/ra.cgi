#!/usr/local/bin/python


"""
Extremely simple cgi script for running relational algebra expressions and viewing
the results.
"""

print "content-type: text/html"
print


template = """
<h3>Run a relational algebra expression</h3>

<blockquote>
This interface allows you to run a relational algebra expression against the
drinkers/beers/bars database with schema.
<pre>
      frequents[dr ba pw] (dr=drinker, ba=bar, pw=per week)
      serves[ba be qt]    (ba=bar, be=beer, qt=quantity)
      likes[dr be pd]     (dr=drinker, be=beer, pd=per day)
</pre>
Please see below for example expressions.  To save the results of
a query please use "cut and paste".
</blockquote>

%(lastexpression)s

%(lastresult)s

<h3>Submit expression below</h3>

<form action="ra.cgi">
<textarea cols="80" rows="10" name="expression">%(expression)s</textarea><br>
<input type="submit" name="submit" value="submit">
</form>

<h3>Example expressions</h3>

<table border>
<tr> <th> Expression </th> <th> Explanation </th> </tr>

<tr>
<td>
<pre>
frequents; serves; likes
</pre>
</td>
	<td>
	List the contents of all the tables.
	</td>
</tr>

<tr>
<td>
<pre>
projection[dr pd] likes
</pre>
</td>
	<td>
	List only the drinkers and perday values from likes.
	</td>
</tr>

<tr>
<td>
<pre>
selection(dr='norm') likes
</pre>
</td>
	<td>
	List the likes entries where the drinker is norm
	</td>
</tr>

<tr>
<td>
<pre>
rename[dr]to[person] likes;
</pre>
</td>
	<td>
	List the contents of the likes table, but rename "dr" to "person".
	</td>
</tr>

<tr>
<td>
<pre>
ld = projection[dr] likes;
fd = projection[dr] frequents;
ld;
fd;
nondrinkers = fd-ld;
nondrinkers;
bardrinkers = fd intersect ld;
bardrinkers;
alldrinkers = fd U ld;
alldrinkers;
</pre>
</td>
	<td>
	This example illustrates how to create name subexpressions using assignment (ld,fd),<br>
        relational difference (fd-ld), <br>
        relational intersection (fd intersect ld), <br>
        and relational union (fd U ld).
	</td>
</tr>

<tr>
<td>
<pre>
frequents join likes
</pre>
</td>
	<td>
	List natural join of frequents and likes (drinker who frequent bars and like beers with
        the bars they frequent and the beers they like).
	</td>
</tr>

<tr>
<td>
<pre>
selection(be='bud' &amp; ba='cheers') (frequents join likes);
selection(be='bud' | ba='cheers') (frequents join likes);
selection(be='bud' &amp; ~ba='cheers') (frequents join likes);
</pre>
</td>
	<td>
	Drinkers who like bud and frequent cheers.  <br>
	Drinkers who like bud or frequent cheers.  <br>
	Drinkers who like bud and frequent some bar that is not cheers.  <br>
        This example illustrates how
        relational algebra subexpressions can be combined to form more complex expressions.
	</td>
</tr>
</table>
"""

import string, sys, cgi, relalg1

def quote(s):
    s = string.strip(s)
    s = string.replace(s, "&", "&amp;")
    s = string.replace(s, "<", "&lt;")
    s = string.replace(s, "<", "&lt;")
    return s

def go():
    fs = cgi.FieldStorage()
    expression = "enter expression here"
    lastexpression = ""
    lastresult = "<br><em>No expression entered</em><br>"
    try:
        expression = fs["expression"].value
    except KeyError:
        pass
    else:
        lastexpression = "<br><b>Last expression</b> <pre>%s</pre>" % quote(expression)
        lastresult = string.strip(relalg1.runStrings(expression))
        if not lastresult:
            lastresult = "<br><b>No result returned for last expression</b><br>"
        else:
            lastresult = "<b>Result</b><br><pre>%s</pre>" % quote(lastresult)
    D = {"expression": quote(expression), "lastresult": lastresult, "lastexpression": lastexpression}
    text = template % D
    print text
    
    
if __name__=="__main__":
    go()

