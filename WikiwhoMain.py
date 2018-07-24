import WikiwhoRelationships_new as ww

from sys import argv,exit
import getopt

def main(my_argv):
    inputfile = ''
    output = ''


    try:
        opts, _ = getopt.getopt(my_argv,"i:o:r:",["inputarticles=","revision="])
    except getopt.GetoptError:
        print 'Usage: Wikiwho.py -i <inputarticles> -o output'
        exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print "WikiWho: An algorithm for detecting attribution of authorship in revisioned content"
            print
            print 'Usage: Wikiwho.py -i <inputarticle>'
            print "-i --inputarticles Articles to analyze "
            print "-o --type of output: <a> for authorship, <r> for relations"
            print "-h --help This help."
            exit()
        elif opt in ("-i", "--inputarticles"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            output = arg

    inputfile = inputfile.split("\\t")

    return (inputfile, output)

if __name__ == '__main__':

    (articles, output) = main(argv[1:])

    for art in articles:
        wikiwho = ww.Wikiwho()
        (revisions, order, relations) = wikiwho.analyseArticle(art)

        print "output for article", art
        if output == 'r':
            wikiwho.printRelationships(relations, order)

        if output == 'a':
            wikiwho.printAllRevisions(order, revisions)
