from nltk.tag.stanford import POSTagger
import re
import pickle

class SpellChecker:

    def checker(self, checkfile, algorithm, modelfile, outputfile):

        fcto = open(algorithm+modelfile+"totoo.pickle")
        classifierto = pickle.load(fcto)
        fcto.close()
    
        fcthe = open(algorithm+modelfile+"theirtheyre.pickle")
        classifierthe = pickle.load(fcthe)
        fcthe.close()
        
        fcyou = open(algorithm+modelfile+"youryoure.pickle")
        classifieryou = pickle.load(fcyou)
        fcyou.close()
        
        fclo = open(algorithm+modelfile+"loseloose.pickle")
        classifierlo = pickle.load(fclo)
        fclo.close()
        
        fcit = open(algorithm+modelfile+"itsitas.pickle")
        classifierit = pickle.load(fcit)
        fcit.close()



        st = POSTagger('/home/uma/stanford-postagger/models/english-bidirectional-distsim.tagger','/home/uma/stanford-postagger/stanford-postagger.jar')
        fp = open(checkfile)
        foutput = open(outputfile,"wb")
        data = fp.readlines()
        print "File reading done"

        datalines = []
        count = 0
        for line in data:
            line = re.sub('([.,:;!?()])', r' \1 ', line)
            line = re.sub('\s{2,}', ' ', line)
            line = line.split('\n')[0]
            line = line.split('\r')[0]
            datalines.append(line.split())
        #tagdata = st.batch_tag(datalines)
        
        '''ftag = open("test.tagged","wb")
        pickle.dump(tagdata,ftag)
        ftag.close()'''

        ftag = open("test.tagged")
        tagdata = pickle.load(ftag)
        ftag.close()
        print "File tagging done"

        for taglist in tagdata:
            taglist.insert(0, ('BOS' , 'BOS'))
            taglist.insert(0, ('BOS' , 'BOS'))
            taglist.append(('EOS' , 'EOS'))
            taglist.append(('EOS' , 'EOS'))
            #print cdatalines[count]
            #print taglist
            newline= ""
            for i in range(len(taglist)):
                
                
                tuple = taglist[i]
                if tuple[0] == "too" or tuple[0] == "to":
                    strn = tuple[0] + " pw2:"+ taglist[i-2][0].strip() + " pt2:" + taglist[i-2][1] + " pw1:" + taglist[i-1][0] + " pt1:"+ taglist[i-1][1] + " nw1:" + taglist[i+1][0] + " nt1:" + taglist[i+1][1] + " nw2:"+ taglist[i+2][0] + " nt2:"+ taglist[i+2][1];
                    strn = strn.split("\n")[0]
                    words = strn.split(" ")
                    f=0
                    row = []
                    stuple=dict()
                    for word in words:
                        if f==0:
                            ctype = word
                            f=1 
                        else:
                            wp = word.split(":")
                            stuple.setdefault(wp[0],wp[1])
        
                    classified_class = classifierto.classify(stuple)
                    newline += classified_class + " "

            
                elif tuple[0] == "your" or tuple[0] == "you\'re":
                    strn = tuple[0] + " pw2:"+ taglist[i-2][0].strip() + " pt2:" + taglist[i-2][1] + " pw1:" + taglist[i-1][0] + " pt1:"+ taglist[i-1][1] + " nw1:" + taglist[i+1][0] + " nt1:" + taglist[i+1][1] + " nw2:"+ taglist[i+2][0] + " nt2:"+ taglist[i+2][1];
                    #print strn
                    strn = strn.split("\n")[0]
                    words = strn.split(" ")
                    f=0
                    row = []
                    stuple=dict()
                    for word in words:
                        if f==0:
                            ctype = word
                            f=1
                        else:
                            wp = word.split(":")
                            stuple.setdefault(wp[0],wp[1])
                                
                    classified_class =  classifieryou.classify(stuple)
                    newline += classified_class + " "

                elif tuple[0] == "its" or tuple[0] == "it\'s":
                    strn = tuple[0] + " pw2:"+ taglist[i-2][0].strip() + " pt2:" + taglist[i-2][1] + " pw1:" + taglist[i-1][0] + " pt1:"+ taglist[i-1][1] + " nw1:" + taglist[i+1][0] + " nt1:" + taglist[i+1][1] + " nw2:"+ taglist[i+2][0] + " nt2:"+ taglist[i+2][1];
                    #print strn
                    strn = strn.split("\n")[0]
                    words = strn.split(" ")
                    f=0
                    row = []
                    stuple=dict()
                    for word in words:
                        if f==0:
                            ctype = word
                            f=1
                        else:
                            wp = word.split(":")
                            stuple.setdefault(wp[0],wp[1])
                                       
                    classified_class =  classifierit.classify(stuple)
                    newline += classified_class + " "


                elif tuple[0] == "lose" or tuple[0] == "loose":
                    strn = tuple[0] + " pw2:"+ taglist[i-2][0].strip() + " pt2:" + taglist[i-2][1] + " pw1:" + taglist[i-1][0] + " pt1:"+ taglist[i-1][1] + " nw1:" + taglist[i+1][0] + " nt1:" + taglist[i+1][1] + " nw2:"+ taglist[i+2][0] + " nt2:"+ taglist[i+2][1];
                    #print strn
                    strn = strn.split("\n")[0]
                    words = strn.split(" ")
                    f=0
                    row = []
                    stuple=dict()
                    for word in words:
                        if f==0:
                            ctype = word
                            f=1
                        else:
                            wp = word.split(":")
                            stuple.setdefault(wp[0],wp[1])
                                       
                    classified_class =  classifierlo.classify(stuple)
                    newline += classified_class + " "


                elif tuple[0] == "their" or tuple[0] == "they\'re":
                    strn = tuple[0] + " pw2:"+ taglist[i-2][0].strip() + " pt2:" + taglist[i-2][1] + " pw1:" + taglist[i-1][0] + " pt1:"+ taglist[i-1][1] + " nw1:" + taglist[i+1][0] + " nt1:" + taglist[i+1][1] + " nw2:"+ taglist[i+2][0] + " nt2:"+ taglist[i+2][1];
                    #print strn
                    strn = strn.split("\n")[0]
                    words = strn.split(" ")
                    f=0
                    row = []
                    stuple=dict()
                    for word in words:
                        if f==0:
                            ctype = word
                            f=1
                        else:
                            wp = word.split(":")
                            stuple.setdefault(wp[0],wp[1])
                                       
                    classified_class =  classifierthe.classify(stuple)
                    newline += classified_class + " "

            
                else:
                    if tuple[0]!='EOS' and tuple[0]!='BOS':
                         newline += tuple[0] + " "
            nl = newline.split()
            #print nl
            newline = re.sub(r'\s+([.,:;!?()])', r'\1', newline)
            foutput.write(newline+"\n")
            #print newline   
            count += 1
        print "Output file ready!"


