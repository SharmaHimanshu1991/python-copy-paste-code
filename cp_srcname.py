#!usr/bin/python2

import sys,time,os,os.path

#only src and destination file will be selected 

cp_oprtion=sys.argv[1:3]
src_file=cp_oprtion[0]
dst_file=cp_oprtion[1]

src=src_file.split("/")[-1]


if os.path.isdir(dst_file):
	print "it is a directory"
	des=(dst_file + src)
	print des

elif os.path.isfile(dst_file):
	print "it is a normal file :"
	des = dst_file
	print des


else :
	print "path is incorrect"


#function define and reading source file

def cp(src_file,dst_file) :
	sf=open(src_file,'r')
	df=open(des,'w')
	
	for i in sf:
		df.writelines(i)
		print "file copy successfully"

		df.close()
		sf.close()
		return;


#To check file alredy exist or not

if os.path.isfile(des):
	print "file alredy exists"
	ans=raw_input("do you want to overwrite? y/n :")

	if ans == 'n':
		exit()
	elif ans == 'y':
		cp(src_file,des)

	else :	
		exit()

else :
		cp(src_file,des)
