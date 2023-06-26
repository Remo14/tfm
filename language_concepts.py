import pandas as pd

# Read csv into dataframe
def read_data(file):
    df = pd.read_csv(file, sep="\t")
    return df

def main():
    file = "./Resources/language_ordered_kin_words.tsv"
    df = read_data(file)

    file_weights = "./Results/language_complexities.tsv"
    df1 = read_data(file_weights)

    firstlanguage=df["Language"][0]
    firstsubdomain=df["Subdomain"][0]
    firstconcept=df["Concept"][0]
    totalfreq = df1["TotalFreq"][0]
    languages=[firstlanguage, firstlanguage, firstlanguage, firstlanguage]
    subdomains=["parents", "parents", "children", "children"]
    concepts=["father", "mother", "son", "daughter"]
    totalfrequencies=[totalfreq, totalfreq, totalfreq, totalfreq]
    seen_concepts=[]

    for index, row in df.iterrows():
        if row["Language"]==firstlanguage:
            if row["Concept"] not in seen_concepts:
                languages.append(row["Language"])
                subdomains.append(row["Subdomain"])
                concepts.append(row["Concept"])
                seen_concepts.append(row["Concept"])
                totalfrequencies.append(totalfreq)                
        else:
            firstlanguage=row["Language"]
            seen_concepts=[row["Concept"]]
            languages.append(firstlanguage)
            languages.append(firstlanguage)
            languages.append(firstlanguage)
            languages.append(firstlanguage)
            subdomains.append("parents")
            subdomains.append("parents")
            subdomains.append("children")
            subdomains.append("children")
            concepts.append("father")
            concepts.append("mother")
            concepts.append("son")
            concepts.append("daughter")
            for index1, row1 in df1.iterrows():
                if firstlanguage==row1["Language"]:
                    totalfreq=row1["TotalFreq"]
            totalfrequencies.append(totalfreq)
            totalfrequencies.append(totalfreq)
            totalfrequencies.append(totalfreq)
            totalfrequencies.append(totalfreq)
            languages.append(row["Language"])
            subdomains.append(row["Subdomain"])
            concepts.append(row["Concept"])
            totalfrequencies.append(totalfreq)
    # languages.append(row["Language"])
    # subdomains.append(row["Subdomain"])
    # concepts.append(row["Concept"])
    # totalfrequencies.append(totalfreq)

    result = "./Resources/language_concepts.tsv"
    df2= pd.DataFrame()
    df2["Language"]=languages
    df2["Subdomain"]=subdomains
    df2["Concept"]=concepts
    df2["TotalFreq"]=totalfrequencies
    df2.to_csv(result, sep="\t", encoding="utf-8")
main()