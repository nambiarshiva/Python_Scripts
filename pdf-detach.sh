# !/bin/bash
i=9999
until [ $i -le 2 ]
do
pdfdetach -save 1 pdf$i.pdf
rm pdf$i.pdf
i=`expr $i - 1`
done
