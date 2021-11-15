import sys
import os
import tarfile
import shutil
import time

argslist = []

for items in range(len(sys.argv)):
    argslist.append(sys.argv[items])
argslist.remove(argslist[0])

#argslist = [r'D:\Python30\dir1\hgfghf',r'D:\Python30\dir1\vuat.tar.gz']
#argslist=[r'D:\Python30\dir1\DictionaryE.txt']

if argslist != []:
    #for arg in argslist:
        #print(arg)
        pass
else:
    print('\n\n\n\t   You must drag one or more files over this script file to work')
    print('\n\n\tDouble clicking this file will only print these two lines of texts!')
    import sys
    input('\n\n\t\t\tPress Enter to quit...')
    sys.exit(0)
print('*'*78)   #   Decoration only
################################################################################
tarfiles = []
others = []
for files in argslist:
    if files.endswith('.tar.gz'):
        tarfiles.append(files)
    else:
        others.append(files)
#print(tarfiles)
#print(others)
################################################################################
def extractor(source,destination):
    if not source.endswith('.tar.gz'):
        pass
    else:
        tar = tarfile.open(source,'r:gz')
        tar.extractall(destination)
        tar.close()

def compressor(srcfile,destination):
    if srcfile.endswith('.tar.gz'):
        shutil.copy2(srcfile,destination)
    elif os.path.isdir(srcfile):
            #destination = os.path.basename(destination)     # Debug
            #destination = os.path.dirname(destination)      #Debug  #Debug(commented)
            tar = tarfile.open(os.path.join(destination , os.path.basename(srcfile)) + '.tar.gz','w:gz')
            os.chdir(os.path.dirname(srcfile)) 
            tar.add(os.path.basename(srcfile))
            tar.close()
    else:
        tar = tarfile.open(os.path.join(destination,os.path.basename(srcfile).split('.')[0]) + '.tar.gz','w:gz')
        os.chdir(os.path.dirname(srcfile))
        tar.add(os.path.basename(srcfile))
        tar.close()

################################################################################
for items in argslist:
    print(items)
print('*'*78)   #   Decoration only
print('\n\nEnter choice(pressing corresponding number from keyboard and then pressing Enter\n\n')
print('\t\t1. Extract each of the tar files to seperate folder\n')
print('\t\t2. Extract all tar files to a single folder\n')
print('\t\t3. Compress each files/folders to individual folder\n')
print('\t\t4. Compress all files/folders to a single folder\n')
print('\n\t\t\t\tPress Enter to abort.\n')
choice = input('\nChoose an option...  ')

#################################################################################
if choice == '1':
    os.system('cls')
    print('\n\n\n\t\tPlease wait while completing the requested operation...')
    for items in tarfiles:
        #print(items)
        destination = items.split('.')[0]
        #print(destination)
        if os.path.exists(destination):
            pass
        else:
            os.mkdir(destination)
        extractor(items,destination)
elif choice == '2':
    os.system('cls')
    dest = input('\n\nPlease enter the name for the folder---> ')
    print('\n\n\n\t\tPlease wait while completing the requested operation...')
    destination = os.path.join(os.path.dirname(tarfiles[0]),dest)
    if os.path.exists(destination):
        pass
    else:
        os.mkdir(destination)
    for items in tarfiles:
        extractor(items,destination)
elif choice == '3':
    os.system('cls')
    print('\n\n\n\t\tPlease wait while completing the requested operation...')
    for items in argslist:
        destination = items.split('.')[0]
        if os.path.exists(destination):
            pass
        else:
            os.mkdir(destination)
        compressor(items,destination)
elif choice == '4':
    os.system('cls')
    dest = input('\n\nPlease enter the name for the folder---> ')
    print('\n\n\n\tPlease wait while completing the requested operation...')
    destination = os.path.join(os.path.dirname(argslist[0]),dest)
    if os.path.exists(destination):
        pass
    else:
        os.mkdir(destination)
    for items in argslist:
        compressor(items,destination)
else:
    os.system('cls')
    a = "\n\n\n\n\n\n\n\t\t\tYou have entered an invalid choice."
    b = "\n\t\t\t   This program is quiting..."
    
    print(a)
    time.sleep(0.9)
    print(b)
    time.sleep(0.9)
    sys.exit(0)

#################################################################################
