import re
from pathlib import Path
import os


def buildDoLift
	#x = unknown.2bit
	#twoBitPrefix = re.search('\w+', x)
	y = re.search('\w+', twoBit)
	twoBitPrefix = y[0]
	print("Creating doLift.sh file...\n")
	OUT = open('doLift.sh', 'w+')
	#commenting out the lines below because I think I can just include them in the example script
	##	OUT.write("#\! /bin/csh\n")
	OUT.write( "#\$ -V\n")
	OUT.write( "#\$ -cwd\n")
	OUT.write( "#\$ -N $twoBit-doLift\n")
	OUT.write( "#\$ -o \$JOB_NAME.o.\$JOB_ID\n")
	OUT.write( "#\$ -e \$JOB_NAME.e.\$JOB_ID\n")
	OUT.write( "#\$ -q omni\n")
	OUT.write( "#\$ -pe sm 1\n")
	OUT.write( "#\$ -P quanah\n")
	print OUT <<_EOF_ #???????????
	partitionDir=Path(os.getcwd())
	OUT.write(partitionDir"/..\n")
	#cd partitionDir/..
	#os.chdir(partitionDir.parent)
	#os.chdir("..") do we need to specify partitionDir?

	with open("doLift-template.sh") as n:
		for line in n:
			OUT.write(line)


#also no idea what "1;" does at the end of hte file 
--------- #OR		
##	OUT.write("#\! /bin/csh\n")
##	OUT.write( "#\$ -V\n")
##	OUT.write( "#\$ -cwd\n")
##	OUT.write( "#\$ -N $twoBit-doLift\n")
##	OUT.write( "#\$ -o \$JOB_NAME.o.\$JOB_ID\n")
##	OUT.write( "#\$ -e \$JOB_NAME.e.\$JOB_ID\n")
##	OUT.write( "#\$ -q omni\n")
##	OUT.write( "#\$ -pe sm 1\n")
##	OUT.write( "#\$ -P quanah\n")
			
##	OUT.write('foreach d0 ( RMPart/??? )')
##	OUT.write('  set bNum = \$d0:t')
##	OUT.write('  $ucscBinDir/liftUp -type=.out stdout \$d0/\$bNum.lft error \$d0/\$bNum.fa.out > \$d0/\$bNum.fa.liftedOut')
##	OUT.write('  if ( -e \$d0/\$bNum.fa.align ) then')
##	OUT.write('    $ucscBinDir/liftUp -type=.align stdout \$d0/\$bNum.lft error \$d0/\$bNum.fa.align > \$d0/\$bNum.fa.liftedAlign')
##	OUT.write('  endif')
##	OUT.write('end')
##
##	OUT.write('$ucscBinDir/liftUp $twoBitPrefix.fa.out /dev/null carry RMPart/???/*.liftedOut')
##	OUT.write('$ucscBinDir/liftUp $twoBitPrefix.fa.align /dev/null carry RMPart/???/*.liftedAlign')
##
##	OUT.write(' ##Create a summary file')
##	OUT.write('# In some cases the file system delays cause the *.out file not to be available ')
##	OUT.write('# Give it some time for things to settle down')
##	OUT.write('sleep 30')
##	OUT.write('$repeatMasker/util/buildSummary.pl -useAbsoluteGenomeSize -genome $twoBit $twoBitPrefix.fa.out > $twoBitPrefix.summary')
##	OUT.write('gzip -f $twoBitPrefix.summary')
##
##	OUT.write(' ##Generate RepeatLandscape')
##	OUT.write('perl $repeatMasker/util/calcDivergenceFromAlign.pl -s $twoBitPrefix.divsum $twoBitPrefix.fa.align')
##	OUT.write('perl $repeatMasker/util/createRepeatLandscape.pl -div $twoBitPrefix.divsum -twoBit $twoBit > $twoBitPrefix-landscape.html')
##	OUT.write('gzip -f $twoBitPrefix.divsum')
##	OUT.write('gzip -f $twoBitPrefix-landscape.html')
##
##
##
##	OUT.write(' ##NOTE NOTE NOTE: Only useful for UCSC')
##	OUT.write(' ##Generate data for the UCSC browser tracks')
##
##	OUT.write('if ( -e $twoBitPrefix.fa.out && -e $twoBitPrefix.fa.align ) then')
##	OUT.write('  $repeatMasker/util/rmToUCSCTables.pl -out $twoBitPrefix.fa.out -align $twoBitPrefix.fa.align')
##	OUT.write('  gzip -f $twoBitPrefix.fa.out.tsv')
##	OUT.write('  gzip -f $twoBitPrefix.fa.align.tsv')
##	OUT.write('  gzip -f $twoBitPrefix.fa.join.tsv')
##	OUT.write('endif ')
##
##
##	OUT.write(' ##NOTE NOTE NOTE: Only useful to ISB ')
##	OUT.write(' ##Generate files for loading into RMDB')
##
##	OUT.write('cat $twoBitPrefix.fa.out | /home/rhubley/cAlign > $twoBitPrefix.fa.out.c')
##	OUT.write('cat $twoBitPrefix.fa.align | /home/rhubley/cAlign > $twoBitPrefix.fa.align.c')
##	OUT.write('gzip -f $twoBitPrefix.fa.out.c')
##	OUT.write('gzip -f $twoBitPrefix.fa.align.c')
##
##	OUT.write(' ##Zip up final results')
##	OUT.write('gzip -f $twoBitPrefix.fa.out')
##	OUT.write('gzip -f $twoBitPrefix.fa.align')
##
##	OUT.write('_EOF_')
##
##	OUT.write('  close OUT;')
##1;
##


