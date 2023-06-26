import pandas as pd
import math

# Read csv into dataframe
def read_data(file):
    df = pd.read_csv(file, sep="\t")
    return df

def read_xls(file):
    df = pd.read_excel(file)
    return df

def main():
    file_xls="./Corpus_queries/corpus_queries2.xls"
    df1=read_xls(file_xls)

    file = "./Resources/language_concepts.tsv"
    df=read_data(file)

    languages=df["Language"]
    subdomains=df["Subdomain"]
    concepts=df["Concept"]
    kin_relations=[]
    relative_frequencies=[]
    pis=[]
    sum_pjs=[]
    addition_costs=[]
    communicative_costs=[]
    for index, row in df.iterrows():
        for index1, row1 in df1.iterrows():
            if row["Concept"]==row1["Concept"]:
                kin_relation=row1["KinRelations"]
                kin_relations.append(kin_relation)
                relative_freq=float(row1["WeightedFreq"])/float(row["TotalFreq"])
                relative_frequencies.append(relative_freq)
                pi=relative_freq/float(kin_relation)
                pis.append(pi)
                sum_pj=relative_freq
                sum_pjs.append(sum_pj)
                if sum_pj!=0:
                    addition_cost=-math.log2(pi/sum_pj)
                else:
                    addition_cost=0
                addition_costs.append(addition_cost)
                communicative_cost=pi*addition_cost
                communicative_costs.append(communicative_cost)
                continue
    result = "./Results/language_costs.tsv"
    df2= pd.DataFrame()
    df2["Language"]=languages
    df2["Subdomain"]=subdomains
    df2["Concept"]=concepts
    df2["KinRelations"]=kin_relations
    df2["RelFreq"]=relative_frequencies
    df2["Pi"]=pis
    df2["SumPj"]=sum_pjs
    df2["ci"]=addition_costs
    df2["Ci"]=communicative_costs
    df2.to_csv(result, sep="\t", encoding="utf-8")

main()