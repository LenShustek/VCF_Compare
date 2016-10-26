VCF_Compare
A tool to assist with synchronizing Android phone contacts with Pimlical 
http://www.pimlicosoftware.com/

This is a Python 3.5 program that compares the exported VCF files from 
Pimlical and Android, reports on which names are missing in each compared 
to the other, and creates an incremental VCF file for each that can be 
imported to add the missing names from the other.

Before importing the incremental VCF files, it's worth reviewing the list
and correcting obvious typos that would otherwise result in duplicate
contacts. There also may be some contacts that you don't want transferred,
in which case you can remove them from the VCF files, which are text and
easy to edit.

This doesn't address the issue that records appearing in both might have 
differences. That's a much more difficult problem that the the "Merge/Update 
Android Contacts" function tries to address, but not well enough to be 
useful for me, at least.

HOW TO USE IT

Here's the process I use for a Windows PC. It may be different for Linux or Mac.

1. From Pimlical/Desktop, display Contacts, and use the Export button to create
a file called PContacts.vcf. 

2. From the Android contacts app (mine is version 3.3.13) use "menu - Settings - 
Contacts - Import/Export - Export to device storage" to create a Contacts.vcf
file in the root directory. Plug the phone into the computer as an MTP device,
and use Windows Explorer -- other file explorers might not work -- to copy the
file to where the PCcontacts.vcf file is. Rename it AContacts.vcf.

3. Change the line near the top of the Python program to point to the directory
where those two files are. Run the program. It will report what it finds to the
console, and it will create the files PContacts_add.vcf and AContacts_add.vcf 
in the same directory.

4. Examine and/or edit the results, and reverse the steps above (approximately)
to import the incremental VCF files into the corresponding applications.

Oh, how I pine for the one-button synchronization of the Palm/Handspring days...