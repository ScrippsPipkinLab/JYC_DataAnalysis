#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:35:48 2019

@author: yolandatiao
"""

import os
import csv
import glob
import pandas as pd
import time

####################--------------- Define functions ---------------####################
def string_contains_elementoflist(in_str, in_list):
    contains = False
    for i in in_list:
        if i in in_str:
            contains = True
    return(contains)
    
def simp_merge_out(in_txt):
    #in_txt = "merged_Cd200.txt"
    out_file = in_txt.replace(".txt", "_simp.csv")
    with open(in_txt, "r") as fin:
        with open(out_file, "w") as fout:
            rfin = csv.reader(fin, delimiter="\t")
            wfout = csv.writer(fout, delimiter=",")
            header = next(rfin)
            files = header[8:]
            files = ["_".join(f.replace("MACS2_", "").split("_")[:-1]) for f in files]
            files = [f.replace("macs2_", "") for f in files]
            header = header[1:4] + files
            wfout.writerow(header)
            for row in rfin:
                newrow = row[1:4]
                found_list = row[8:]
                #print(found_list)
                out_list = []
                for i in found_list:
                    if i != '':
                        out_list.append("x")
                    else:
                        out_list.append("")
                #print(out_list)
                newrow = newrow + out_list
                wfout.writerow(newrow)
                #print("")
                
def find_file(g_name, f_list):
    find_f = []
    for i in f_list:
        if g_name in i:
            find_f.append(i)
    if len(find_f) > 1:
        print("Multiple match for %s!!"%g_name)
    elif len(find_f) == 0:
        print("No match for %s!!"%g_name)
    else:
        return find_f[0]

def pd_write_csv(in_tb, out_name):
    if os.path.exists(out_name):
        os.remove(out_name)
        print("File exist: %s \n File removed!"%out_name)
    in_tb.to_csv(out_name, index=False)

def peak_combine(simp_csv):
    #simp_csv = "/Volumes/Yolanda/JYC_DataAnalysis/3_MACS2/xls_combined_p0.1/p_0.01/d150_merged/merged_Cxcr5_simp.csv"
    coor_csv = simp_csv.replace("simp.csv", "coor.csv")
    coor_merge_csv = simp_csv.replace("simp.csv", "coor_merge.csv")
    simp_tb = pd.read_csv(simp_csv)
    simp_tb = simp_tb.sort_values(["start"])
    coor_dict = {"chr": list(simp_tb["chr"]), "start": list(simp_tb["start"]), "end": list(simp_tb["end"])}
    coor_tb = pd.DataFrame(data=coor_dict)
    pd_write_csv(coor_tb, coor_csv)
    
    with open(coor_csv, "r") as fin:
        with open(coor_merge_csv, "w") as fout:
            rfin = csv.reader(fin, delimiter=",")
            wfout = csv.writer(fout, delimiter=",")
            header = next(rfin)
            wfout.writerow(header)
            buffer_row = next(rfin)
            for row in rfin:
                row_s = int(row[1])
                if row_s - int(buffer_row[2]) > 150:
                    wfout.writerow(buffer_row)
                    buffer_row = row
                else:
                    buffer_row = [buffer_row[0], buffer_row[1], row[2]]
            wfout.writerow(buffer_row)
    return(coor_merge_csv)
                

def find_summits(merged_csv, in_dir, g_name):
    #merged_csv = "/Volumes/Yolanda/JYC_DataAnalysis/3_MACS2/xls_combined_p0.1/p_0.01/d150_merged/merged_Cd200_simp.csv"
    #g_name = "Cd200"
    #in_dir = "/Volumes/Yolanda/JYC_DataAnalysis/3_MACS2/xls_combined_p0.1/p_0.01/txt"
    
    coor_csv = merged_csv.replace("simp.csv", "coor_merge.csv")
    out_csv = merged_csv.replace("simp.csv", "summits.csv")
    use_files = glob.glob("{use_dir}/*.txt".format(use_dir=in_dir))
    use_files = [f for f in use_files if g_name in f]
    with open(merged_csv, "r") as fin_ref:
        with open(coor_csv, "r") as fin:
            with open(out_csv, "w") as fout:
                rfin_ref = csv.reader(fin_ref, delimiter=",")
                rfin = csv.reader(fin, delimiter=",")
                wfout = csv.writer(fout, delimiter=",")
                header = next(rfin_ref)
                next(rfin)
                wfout.writerow(header)
                for row in rfin:
                    #row = ['chr16', '45389616', '45390097']
                    new_row = row[:3]
                    row_s = int(row[1])
                    row_e = int(row[2])
                    for name_i in header[3:]:
                        #name_i = "Bcl6KO_Th1"
                        file_i = find_file(name_i, use_files)
                        tab_i = pd.read_csv(file_i, sep="\t",header=None)
                        summits_i = list(tab_i.iloc[:,4])
                        sig_sum = False
                        for summit in summits_i:
                            if int(summit) >= (row_s - (row_e-row_s)/1.5) and int(summit) <= (row_e + (row_e-row_s)/1.5):
                                sig_sum = True
                        if sig_sum == True:
                            new_row.append("x")
                        else:
                            new_row.append("")
                    #print(new_row)
                    wfout.writerow(new_row)
                
def gn_from_coor_file(file_n):
    gn = file_n.split("/")[-1].replace("_coor_merge.csv","").replace("merged_","")
    return(gn)

def peak_in_range(peak_identity_list, compare_peak_tab, gene_c_tab, out_writer):
    #peak_identity_list = ["chr5", "113818547", "113830501", "peak_test"]
    #compare_peak_tab = all_coor_tb
    #gene_c_tb = gene_coor_tb
    
    peak_chr = peak_identity_list[0]
    peak_s = int(peak_identity_list[1])
    peak_e = int(peak_identity_list[2])
    peak_len = peak_e - peak_s
    peak_name = peak_identity_list[3]
    
    
    for i in range(0, len(compare_peak_tab)):
        out_list = []
        row_i = list(compare_peak_tab.iloc[i])
        chr_i = row_i[0]
        if peak_chr == chr_i:
            s_i = int(row_i[1])
            e_i = int(row_i[2])
            span_i = max(s_i, e_i, peak_s, peak_e) - min(s_i, e_i, peak_s, peak_e)
            if (span_i < (e_i - s_i + peak_len)):
                gene_i = row_i[3]
                #print(gene_i)
                gene_i_info = list(gene_c_tab.iloc[list(gene_c_tab.iloc[:,0]).index(gene_i)])
                if peak_e < int(gene_i_info[2]):
                    out_list.append("left")
                elif peak_s > int(gene_i_info[3]):
                    out_list.append("right")
                else:
                    out_list.append("within")
                out_list.append(gene_i)
                out_list += [peak_chr, gene_i, peak_name, s_i, e_i]
                out_writer.writerow(out_list)
                print(out_list)
                
def identify_peak(gene_coor_tb, mg_peak_file_list, out_file, all_peak_file):
    #all_peak_file = "/Volumes/Yolanda/JYC_DataAnalysis/z_codes_local/jycATAC_merged_peaks_chr-slt.bed"
    #mg_peak_file_list = glob.glob("{use_dir}/*_coor_merge.csv".format(use_dir="/Volumes/Yolanda/JYC_DataAnalysis/3_MACS2/1_xls_combined_p0.1/p_0.01/d150_merged"))
    #gene_coor_file = "/Volumes/Yolanda/JYC_DataAnalysis/z_codes_local/0_1_MACS_peak_find_genes_transcript_loci.csv" 
    #gene_coor_file = "/Volumes/Yolanda/JYC_DataAnalysis/z_codes_local/0_1_MACS_peak_find_genes_transcript_loci.csv" 
    #all_peak_file = "/Volumes/Yolanda/JYC_DataAnalysis/z_codes_local/jycATAC_merged_peaks_chr1.bed"  
    #out_file = "/Volumes/Yolanda/JYC_DataAnalysis/z_codes_local/0_1_MACS_peak_find_genes_transcript_loci_AllMergedPeaks_chr1.csv" 
    
    all_coor_tb = pd.read_csv(mg_peak_file_list[0])
    all_coor_tb_genes = []
    gene_i = gn_from_coor_file(mg_peak_file_list[0])
    all_coor_tb_genes += [gene_i for x in range(0, len(all_coor_tb))]
    for file_i in mg_peak_file_list[1:]:
        tb_i = pd.read_csv(file_i)
        gene_i = gn_from_coor_file(file_i)
        all_coor_tb = all_coor_tb.append(tb_i, ignore_index=True)
        all_coor_tb_genes += [gene_i for x in range(0, len(tb_i))]
    all_coor_tb["gene_name"] = all_coor_tb_genes
    
    with open(all_peak_file, "r") as fin:
        with open(out_file, "w") as fout:
            rfin = csv.reader(fin, delimiter="\t")
            wfout = csv.writer(fout, delimiter=",")
            header = ["gene_name", "pos", "start", "end", "peak_name"]
            wfout.writerow(header)
            for row in rfin:
                row_peak_info = row[:4]
                peak_in_range(row_peak_info, all_coor_tb, gene_coor_tb, wfout)
                
def slt_DEseq_out(peak_slt_file, files_list):
    #peak_slt_file = "/Volumes/Yolanda/JYC_DataAnalysis/z_codes_local/0_1_MACS_peak_find_genes_transcript_loci_AllMergedPeaks_fixed.csv"
    peak_slt_file_simp = peak_slt_file.split("/")[-1]
    pval_file = peak_slt_file_simp.replace(".csv", "_DEseq_pval.csv")
    log2fc_file = peak_slt_file_simp.replace(".csv", "_DEseq_log2fc.csv")
    peak_slt_tb = pd.read_csv(peak_slt_file)
    peak_slt_pval_tb = peak_slt_tb
    peak_slt_log2fc_tb = peak_slt_tb
    for deseq_file in files_list:
        #deseq_file = "/Volumes/Yolanda/JYC_DataAnalysis/4_DEseq2/DEseq2Output/all.df.numx.c5-Bcl6KO_Th1_vs_Naive.csv"
        deseq_comp = deseq_file.split("/")[-1].replace(".csv", "").split("-")[1]
        deseq_tb = pd.read_csv(deseq_file)
        deseq_tb = deseq_tb.rename(columns={deseq_tb.columns[0] : "matched_peak_name"})
        pval_tb = pd.DataFrame({'matched_peak_name': deseq_tb['matched_peak_name'], 
                                deseq_comp: deseq_tb['pvalue']})
        log2fc_tb = pd.DataFrame({'matched_peak_name': deseq_tb['matched_peak_name'], 
                                  deseq_comp: deseq_tb['log2FoldChange']})
        peak_slt_pval_tb = pd.merge(peak_slt_pval_tb, pval_tb, 
                                    on='matched_peak_name', how='left')
        peak_slt_log2fc_tb = pd.merge(peak_slt_log2fc_tb, log2fc_tb, 
                                    on='matched_peak_name', how='left')
    pd_write_csv(peak_slt_pval_tb, pval_file)
    pd_write_csv(peak_slt_log2fc_tb, log2fc_file)
    
    
        
    
####################--------------- Main ---------------####################

if False:
    wkdir = "/Volumes/Yolanda/JYC_DataAnalysis/2_MACS2/1_xls_combined_p0.1/p_0.01/d150_merged"
    os.chdir(wkdir)
    for file in glob.glob("*.txt"):
        simp_merge_out(file)
        
if False:
    wkdir = "/Volumes/Yolanda/JYC_DataAnalysis/2_MACS2/1_xls_combined_p0.1/p_0.01/d150_merged"
    os.chdir(wkdir)
    
    for file in glob.glob("*simp.csv"):
        print(file)
        peak_combine(file)
        inDir = "/Volumes/Yolanda/JYC_DataAnalysis/2_MACS2/1_xls_combined_p0.1/p_0.01/txt"
        geneN = file.split("_")[1]
        find_summits(file, inDir, geneN)


####---------- Correlate with DEseq.... 
###----- Correlate annoated peaks to DEseq peaks
if False:
    wk_dir = "/Volumes/Yolanda/JYC_DataAnalysis/z_codes_local/0_1_MACS_peak_find_genes_transcript_loci"
    os.chdir(wk_dir)
    mg_peak_file_list_use = glob.glob("{use_dir}/*_coor_merge.csv".format(use_dir="/Volumes/Yolanda/JYC_DataAnalysis/2_MACS2/1_xls_combined_p0.1/p_0.01/d150_merged"))
    peak_file_use_base = "/Volumes/Yolanda/JYC_DataAnalysis/z_codes_local/jycATAC_merged_peaks_chrs/jycATAC_merged_peaks"
    gene_coor_file_use = "/Volumes/Yolanda/JYC_DataAnalysis/z_codes_local/0_1_MACS_peak_find_genes_transcript_loci.csv" 
    gene_coor_tb_use = pd.read_csv(gene_coor_file_use)
    gene_coor_tb_use_chrs = list(set(gene_coor_tb_use["chr"]))
    start_time = time.time()
    for chr_i in gene_coor_tb_use_chrs:
        #chr_i = "chr1"
        gene_coor_tb_i = gene_coor_tb_use[gene_coor_tb_use['chr'] == chr_i]
        genes_i = list(set(gene_coor_tb_i['gene_name']))
        mg_peak_file_list_i = [i for i in mg_peak_file_list_use if string_contains_elementoflist(i, genes_i)]
        peak_file_i = peak_file_use_base + "_" + chr_i + ".bed"
        out_file_i = chr_i + ".csv"
        identify_peak(gene_coor_tb_i, mg_peak_file_list_i, out_file_i, peak_file_i)
    end_time = time.time()
    
    #--- Merge all gene peak files
    all_peak_files = glob.glob("chr*.csv")
    out_file_name = "0_1_MACS_peak_find_genes_transcript_loci_AllMergedPeaks_fixed.csv"
    with open(out_file_name, "w") as fout:
        wfout = csv.writer(fout, delimiter=",")
        wfout.writerow(["pos", "gene_name", "chr", "start", "end", "matched_peak_name"])
        for file_i in all_peak_files:
            with open(file_i, "r") as fin:
                rfin = csv.reader(fin, delimiter=",")
                next(rfin)
                for row in rfin:
                    new_row = [row[0], row[1], row[2], row[5], row[6], row[4]]
                    wfout.writerow(new_row)
                
    
    

###----- Select annotated peaks from DEseq results
if False:
    wk_dir = "/Volumes/Yolanda/JYC_DataAnalysis/2_MACS2/2_Peak_anno"
    os.chdir(wk_dir)
    
    ref_peaks_list = "/Volumes/Yolanda/JYC_DataAnalysis/z_codes_local/0_1_MACS_peak_find_genes_transcript_loci/0_1_MACS_peak_find_genes_transcript_loci_AllMergedPeaks_fixed.csv"
    deseq_out_dir = "/Volumes/Yolanda/JYC_DataAnalysis/4_DEseq2/DEseq2Output"
    deseq_outs = glob.glob("{dir_use}/*.csv".format(dir_use=deseq_out_dir))
    slt_DEseq_out(ref_peaks_list, deseq_outs)























