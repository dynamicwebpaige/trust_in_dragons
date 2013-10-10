"""Interface to xsdbXML functionality.

This module is somewhat experimental.

To use this module you need the
xsdbXML package available from http://xsdb.sourceforge.net
installed.

As illustrated in the test function below you can "mount" an
xsdb context into a gadfly database, for example, as follows

    connection = database.gadfly()
    connection.startup("dummy", "dummy", 1) # scratch database
    # map in S (suppliers table) from athos.rutgers.edu.
    viewXSDB(connection, "S", ["snum", "sname", "status", "city"],
        '<consult href="http://athos.rutgers.edu/~aaron/supplier.xsdb"/>')
    cursor = connection.cursor()
    cursor.execute("select * from s")
    print cursor.pp()
    cursor.execute("select * from s where city='London'")
    print cursor.pp()

Using this facility a gadfly database may query remote relations in xml
format, among other possibilities.
"""

#import store, string

from gadfly import store, database, semantics
from gadfly.semantics import kjbuckets

import string, types

def viewXSDB(connection, name, namelist, assertionText, semijoin=True):
    theview = XSDBView(name, namelist, assertionText)
    connection.add_remote_view(name, theview)

class XSDBView(store.View):
    def __init__(this, name, namelist, text, semijoin=True):
        this.semijoin = semijoin
        this.name = name
        this.namelist = namelist
        this.XSDBtext = text
        capsToNames = {}
        uppers = [ (string.upper(n), n) for n in namelist ]
        this.mapUpper = kjbuckets.kjDict(uppers)
        this.mapUpper.Wash()
    
    def __repr__(this):
        return "xsdb view %s on %s as %s" % (this.name, this.namelist, this.XSDBtext)

    irepr = __repr__

    def attributes(this):
        return map(string.upper, this.namelist)
    
    def relbind(self, db, atts):
        return self

    def rows(this, andseqs=0, assignment=None, transform=None, subseq=None):
        from xsdbXMLpy import interp
        #print "assignment", assignment
        #print "transform", transform
        #print "subseq", subseq
        result = []
        # compute the rows by evaluating the text...
        # simple case: just make a query and map the results
        mapUpper = this.mapUpper
        invUpper = ~mapUpper
        namelist = this.namelist
        uppernamelist = invUpper.dump(namelist)
        nnames = len(namelist)
        namestring = string.join(namelist)
        if not this.semijoin or subseq is None:
            # simple case: just make a query and map the results
            theQuery = """
            <query names="%s">
                <select names="%s">

                    %s

                </select>
            </query>
            """ % ( namestring, namestring, this.XSDBtext )
        else:
            # complicated case: make a query with a semijoin
            invTransform = ~transform
            #print "invTransform is", invTransform
            fullTransform = invUpper * invTransform
            #print "fullTranform is", fullTransform
            transformedSubseq = []
            transformedAssignment = invUpper * assignment
            for s in subseq:
                t = s.remap(fullTransform)
                #print "t is", t
                if t is not None:
                    t = t+transformedAssignment
                    if t.Clean():
                        #print "transformed t", t
                        transformedSubseq.append(t)
            disj = disjunction(transformedSubseq)
            theQuery = """
            <query names="%s">
                <select names="%s">
                <and>
                
                    %s
                    
                    %s
                    
                </and>
                </select>
            </query>
            """ % ( namestring, namestring, disj, this.XSDBtext )
        #print "thequery", theQuery
        q = interp.Query(theQuery)
        #print "result", q.stringResult()
        for t in q.tuples():
            if nnames<1:
                d = kjbuckets.kjDict()
            elif nnames==1:
                d = kjbuckets.kjDict()
                d[ string.upper(namelist[0]) ] = t[0]
            else:
                d = kjbuckets.kjUndump(uppernamelist, t)
            #print "appending", d
            result.append(d)
        if andseqs:
            return (result, range(len(result)))
        else:
            return result

def atom(name, value):
    tv = type(value)
    if tv is types.StringType:
        return '<s at="%s">%s</s>' % (name, value)
    elif tv is types.IntType:
        return '<i at="%s">%s</i>' % (name, value)
    elif tv is types.FloatType:
        return '<f at="%s">%s</f>' % (name, value)
    else:
        raise ValueError, "don't know what to do with "+repr((name, tv, value))

def conjunction(D):
    if not D:
        return "<anything/>"
    keys = D.keys()
    if len(keys)==1:
        k = keys[0]
        return atom(k, D[k])
    keys.sort()
    L = []
    for k in keys:
        L.append(atom(k, D[k]))
    return "<and> %s </and>" % string.join(L)

def disjunction(L):
    L2 = map(conjunction, L)
    if not L2:
        return "<nothing/>"
    if len(L2)==1:
        return L2[0]
    L2.insert(0, "<or>")
    L2.append("</or>")
    return string.join(L2, "\n")

def test0():
    #import database
    connection = database.gadfly()
    connection.startup("dummy", "dummy", 1) # scratch database
    #print connection.database
    viewXSDB(connection, "X", ["a", "b"], """
    <or>
    <and> <i at="a">1</i> <i at="b">1</i> </and>
    <and> <i at="a">2</i> <i at="b">1</i> </and>
    <and> <i at="a">1</i> <i at="b">2</i> </and>
    <and> <i at="a">2</i> <i at="b">2</i> </and>
    </or>
    """)
    viewXSDB(connection, "S", ["snum", "sname", "status", "city"],
        '<consult href="http://athos.rutgers.edu/~aaron/supplier.xsdb"/>')
    cursor = connection.cursor()
    cursor.execute("select a,b from x where b=1")
    print cursor.pp()
    cursor.execute("select * from s")
    print cursor.pp()
    cursor.execute("select * from s where city='London'")
    print cursor.pp()

if __name__=="__main__":
    test0()

    