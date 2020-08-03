# Read and Save Txt
import os
import shutil

def replace(s):
    aTones = (list("āáǎà"),'a')
    eTones = (list("ēéěè"), 'e')
    iTones = (list("īíǐì"), 'i')
    oTones = (list("ōóǒò"), 'o')
    uTones = (list("ūúǔù"), 'u')
    umTones = (list("ǖǘǚǜü"), 'u')
    tonesLists = (aTones, eTones, iTones, oTones, uTones, umTones)
    for toneList in tonesLists: # a tones, eTones, etc
        for tone in toneList[0]: # each tone in list("āáǎà")
            s = s.replace(tone, toneList[1])    
    return s

def make_dir(dirpath, make_clean=False):
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
        return
    if not os.path.isdir(dirpath):
        # if not a directory, delete first
        os.remove(dirpath)
        os.mkdir(dirpath)
        return
    if make_clean:
        shutil.rmtree(dirpath)
        os.mkdir(dirpath)
        return

def moveAudio(parent_dir, path, audio): # Move mp3 to subdirectory
    # Move mp3 to subdirectory
    src = os.path.join(parent_dir,audio + ".mp3")
    dst = os.path.join(path,audio + ".mp3")
    try: # move mp3s to subfolder
        os.rename(src, dst)
    except:
        audio = "{}-{}.mp3".format(audio,english)
        src = os.path.join(parent_dir,audio)
        dst = os.path.join(path,audio)
        try:
            os.rename(src, dst)
        except:
            print("can't rename file {}".format(audio))
    return

def writeFile(directory, name, o):
    fOut = os.path.join(directory, name)
    f = open(fOut,"w")
    f.write(o)
    return

def run():
    # Read from source file
    d = os.getcwd()
    #f = os.path.join(d, "pCopy.txt")
    f = os.path.join(d, "first625wordsMandarin.txt")
    fle = open(f, "r")
    txt = fle.read()
    fle.close()

    # What do you want to do?
    makeAudio = False
    oneList = False # false creates separate lists
    getLeng = False
    
    o = "" # output string of all flashcards
    sets = txt.split(",\n\n") # Split into thematic vocabulary sets
    leng = 0
    
    for txt in sets:
        if not oneList:
            o = ""
            
        txt = txt.split(":")
        tag = txt[0].replace(" ", "") # make thematic vocabulary list

        # Make SubDirectory for Audio Files
        if makeAudio:
            parent_dir = "/Users/aixgalericulata/Documents/中文/fluentforeverResources/FFMandarinWordList/Audio"
            path = os.path.join(parent_dir, tag) # thematic folder
            make_dir(path)
        
        terms = txt[1].split(", ")
        if getLeng:
            leng = leng + len(terms)
            
        for term in terms:
            term = term.replace("\n(",",").split(" - ")
            try:
                t = term[1].replace(" (", ",").replace(") (", ",").replace(") [", ",").strip().split(",")
            except:
                print("Split fails on term: {}".format(term))

            english = term[0].replace("- ","")
            hanzi = t[0].replace("- ","").strip()
            pinyin = t[1].replace("- ","")
            audio = replace(pinyin).strip()
            
            if makeAudio:
                moveAudio(parent_dir, path, audio)
                
            try: # Add term to output str
                #strOut = "{},{},{},{}\n".format(hanzi,pinyin,english.strip(),tag)
                strOut = "{},{},{}\n".format(hanzi,pinyin,english.strip()) # without tag
            except:
                print("Cannot make strOut on term: {}".format(term))
            o = o + strOut
        if not oneList:
            writeFile(d, "{}.txt".format(tag), o) # for thematic vocab lists only
    if oneList:
        writeFile(d, "wordlist-noTag.txt", o) # for undifferentiated vocab list only
    if getLeng:
        print(leng) # 618
    return

run()
