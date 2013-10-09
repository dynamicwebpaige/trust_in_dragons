
"load the drinkers db and run statement sequence"


DB = """

COMMENT examples for relational algebra

COMMENT frequents
frequents  = [dr ba pw] (
  'adam'	'lolas'		1,
  'woody'	'cheers'	5,
  'sam'		'cheers'	5,
  'norm'	'cheers'	3,
  'wilt'	'joes'		2,
  'norm'	'joes'		1,
  'lola'	'lolas'		6,
  'norm'	'lolas'		2,
  'woody'	'lolas'		1,
  'pierre'	'frankies'	0
);

COMMENT serves
serves = [ba be qt] (
  'cheers'	'bud'		500,
  'cheers'	'samaddams'	255,
  'joes'	'bud'		217,
  'joes'	'samaddams'	13,
  'joes'	'mickies'	2222,
  'lolas'	'mickies'	1515,
  'lolas'	'pabst'		333,
  'winkos'	'rollingrock'	432,
  'frankies'	'snafu'		5
);

COMMENT likes
likes = [dr be pd] (
  'adam'	'bud'			2,
  'wilt'	'rollingrock'	1,
  'sam'		'bud'			2,
  'norm'	'rollingrock'		3,
  'norm'	'bud'			2,
  'nan'		'sierranevada'	1,	
  'woody'	'pabst'			2,
  'lola'	'mickies'		5
);
"""
   
def runfile2(f):
    from relalg import reloadrelalg
    from string import split, join
    ragram = reloadrelalg()
    context = {}
    #f = open(filename, "r")
    data = f.read()
    #f.close()
    from string import split, strip
    commands = split(data, ";")
    for c in commands:
        if not strip(c): continue
        #print " COMMAND:"
        data = str(c)
        pdata = "  "+join(split(c, "\n"), "\n  ")
        #print pdata
        test = ragram.DoParse1(c, context)
        print

def runStrings(inputString):
    from StringIO import StringIO
    import sys, string, traceback, sys
    fullinputstring = "%s ; \n\n%s" % (DB, inputString)
    inputfile = StringIO(fullinputstring)
    outputfile = StringIO()
    stdoutSave = sys.stdout
    sys.stdout = outputfile
    try:
        runfile2(inputfile)
    except:
        print "******************"
        print "error processing statement(s):"
        print inputString
        print sys.exc_type
        print sys.exc_value
        print "*******************"
    sys.stdout = stdoutSave
    output = string.strip(outputfile.getvalue())
    return output

if __name__=="__main__":
    for st in [
        """
        COMMENT bad expression here, should cause an error
        bad expression here
        """,
        """
        COMMENT list the database
        frequents;
        serves;
        likes
        """,
        """
        COMMENT drinkers who like beers
        projection[dr] likes
        """,
        ]:
        print "==="
        print st
        print "==="
        print runStrings(st)