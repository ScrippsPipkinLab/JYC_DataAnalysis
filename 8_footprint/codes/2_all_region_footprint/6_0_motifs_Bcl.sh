#!/bin/bash

source_dir=/home/pipkin/Documents/jycATAC/footprint/0_fp
cd $source_dir

Bcl6_dir=/home/pipkin/Documents/jycATAC/footprint/6_mpbs_Bcl6
BCL6_dir=/home/pipkin/Documents/jycATAC/footprint/6_mpbs_BCL6

### Bcl6
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files Bcl6KO_Th1_rep1_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files Bcl6KO_Th1_rep2_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files Bcl6KO_Th1_rep3_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files DKO_Tfh_rep1_fp.bed
wait
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files DKO_Tfh_rep2_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files DKO_Tfh_rep3_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files DKO_Th1_rep1_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files DKO_Th1_rep2_fp.bed
wait
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files DKO_Th1_rep3_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files Naive_rep1_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files Naive_rep2_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files Naive_rep3_fp.bed
wait
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files Prdm1KO_Tfh_rep1_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files Prdm1KO_Tfh_rep2_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files Prdm1KO_Tfh_rep3_fp.bed
wait
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files WT_Tfh_rep1_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files WT_Tfh_rep2_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files WT_Tfh_rep3_fp.bed
wait
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files WT_Th1_rep1_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files WT_Th1_rep2_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:Bcl6" --output-location=$Bcl6_dir --input-files WT_Th1_rep3_fp.bed
wait

### BCL6
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files BCL6KO_Th1_rep1_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files BCL6KO_Th1_rep2_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files BCL6KO_Th1_rep3_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files DKO_Tfh_rep1_fp.bed
wait
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files DKO_Tfh_rep2_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files DKO_Tfh_rep3_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files DKO_Th1_rep1_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files DKO_Th1_rep2_fp.bed
wait
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files DKO_Th1_rep3_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files Naive_rep1_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files Naive_rep2_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files Naive_rep3_fp.bed
wait
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files Prdm1KO_Tfh_rep1_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files Prdm1KO_Tfh_rep2_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files Prdm1KO_Tfh_rep3_fp.bed
wait
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files WT_Tfh_rep1_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files WT_Tfh_rep2_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files WT_Tfh_rep3_fp.bed
wait
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files WT_Th1_rep1_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files WT_Th1_rep2_fp.bed &
rgt-motifanalysis matching --organism=mm10 --filter "name:BCL6" --output-location=$BCL6_dir --input-files WT_Th1_rep3_fp.bed
