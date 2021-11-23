for f in *.fasta
do
    echo $f
    python ../BIOS-IN9410/seq_length.py $f
done
