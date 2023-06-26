import pandas as pd

def read_xls(file):
    df = pd.read_excel(file)
    return df

# Read csv into dataframe
def read_data(file):
    df = pd.read_csv(file, sep="\t")
    return df

def main():
    file = "./Resources/language_ordered_kin_words.tsv"
    df = read_data(file)

    xls_file = "./Corpus_queries/corpus_queries2.xls"
    df2 = read_xls(xls_file)

    firstlanguage=df["Language"][0]
    languages=[firstlanguage]
    language_concepts=[]
    complexities=[]
    total_frequencies=[]
    total_freq=0
    concepts=[]
    complexity=4
    for index, row in df.iterrows():
        if row["Language"]==firstlanguage:
            if row["Concept"] not in concepts:
                concepts.append(row["Concept"])
                complexity += 1
        else:
            firstlanguage=row["Language"]
            languages.append(firstlanguage)
            complexities.append(complexity)
            complexity=5
            concepts.append("father")
            concepts.append("mother")
            concepts.append("son")
            concepts.append("daughter")
            language_concepts.append(concepts)
            concepts = [row["Concept"]]
    complexities.append(complexity)
    concepts.append("father")
    concepts.append("mother")
    concepts.append("son")
    concepts.append("daughter")
    language_concepts.append(concepts)

    i = 0
    for language in language_concepts:
        for index1, row1 in df2.iterrows():
            for concept in language_concepts[i]:
                if concept == row1["Concept"]:
                    total_freq += row1["WeightedFreq"]
        total_frequencies.append(int(total_freq))
        total_freq=0
        i += 1
    #total_frequencies.append(total_freq)
    result = "./Results/language_complexities.tsv"
    df1= pd.DataFrame()
    df1["Language"]=languages
    df1["Complexity"]=complexities
    df1["TotalFreq"]=total_frequencies
    df1.to_csv(result, sep="\t", encoding="utf-8")
main()