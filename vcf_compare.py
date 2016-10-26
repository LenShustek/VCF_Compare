# compare two VCF files for missing contact records in either one
# reads: PContacts.vcf, AContacts.vcf
# creates: PContacts_add.vcf, AContacts_add.vcf

# Copyright (c) 2016, Len Shustek; see LICENSE.txt
# 25 Oct 2016, L. Shustek, initial release

import os
import pprint

directory = "C:/data/pimlical/Pimlical/PimlicalContacts"

def readvcf(infile) :
    vcard = list()  # a list of lines in the vcard
    vcards = list() # a list of (name, vcard) tuples
    name = "???"
    org = "???"
    nvcards=0
    print("reading", infile)
    for line in open(infile):
        if line != "\n":
            vcard.append(line)
            if line[0:2] == "N:" and line[0:6] != "N:;;;;":
                name = line[2:-1].replace('\\','') # pimplical escapes special chars like comma!
            if line[0:4] == "ORG:":
                org = line[4:-1].replace('\\','') 
            if line == "END:VCARD\n":
                if name == "???":
                    if org == "???":
                        print("Missing both name and org: ")
                        pprint.pprint(vcard)
                    else:
                        name = org
                        print("  org only:", org)
                vcards.append((name,vcard))
                nvcards += 1
                vcard = list()
                name = "???"
                org = "???"
    print("Parsed", nvcards, "vcards\n")
    # pprint.pprint(vcards)
    return vcards

def findmissing(within, lookfor, filename):
    with open(filename, 'w') as out:
        for cardtofind in lookfor:
            found =any(card[0]==cardtofind[0] for card in within)
            if (not found):
                print("  missing:", cardtofind[0])
                for line in cardtofind[1]:
                    out.write(line)
                out.write("\n")
        out.close()
        
os.chdir(os.path.normpath(directory))
pimlical_vcards = readvcf("PContacts.vcf")
android_vcards  = readvcf("AContacts.vcf")

print("Looking in Pimlical contacts...")
findmissing(pimlical_vcards, android_vcards, "PContacts_add.vcf")
    
print("\nLooking in Android contacts...")
findmissing(android_vcards, pimlical_vcards, "AContacts_add.vcf")

