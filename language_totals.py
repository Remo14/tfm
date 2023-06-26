import pandas as pd

# Read csv into dataframe
def read_data(file):
    df = pd.read_csv(file, sep="\t")
    return df

def main():
    
    file = "./Results/language_costs.tsv"
    df=read_data(file)

    file1 = "./Results/language_complexities.tsv"
    df1=read_data(file1)

    df2=pd.DataFrame()
    df2["Language"]=df1["Language"]
    df2["Complexity"]=df1["Complexity"]
    costs=[]

    firstlanguage=df["Language"][0]
    cost=df["Ci"][0]
    for index, row in df.iterrows():
        if row["Language"]==firstlanguage:
            cost += row["Ci"]
        else:
            firstlanguage=row["Language"]
            costs.append(cost)
            cost=row["Ci"]
    costs.append(cost)
            
    df2["CommunicativeCost"]=costs
    result="./Results/language_totals.tsv"
    df2.to_csv(result, sep="\t", encoding="utf-8")
main()