#!/bin/bash
#author:samrudhi
#get current directory
path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $path

files=(beach france bridge castle church forest hiking island lake landscape mountains river sculpture snow sunset temple wildlife zoo)

#create folder if not exist
if [ ! -d $path/Plots ] 
then
    mkdir -p $path/Plots
fi
#for each csv file generate
for fileshort in "${files[@]}"
do
	Rscript $path/bi_timeseries.R $fileshort --save
done





