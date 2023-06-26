library(ggplot2)

df = read.csv('language_scores.tsv', sep = '\t')

# Main results plot (Figure 2)
ggplot(data=df, aes(x=Complexity, y=CommunicativeCost, label=Language)) + geom_point(colour="red", position=position_jitter(width=.05,height=.05)) + xlim(-0.1,100) + ylim(-0.1,4)
  
summary(df)
df$Language = as.factor(df$Language)
df$X = NULL


df2 = read.csv('language_costs.tsv', sep = '\t')
summary(df2)
df2$Language = as.factor(df2$Language)
df2$Subdomain = as.factor(df2$Subdomain)
df2$Concept = as.factor(df2$Concept)
df2$X = NULL


# Plots by subdomain (Figure 3)
ggplot(data=subset(df2, Subdomain %in% "parents"), aes(x=Pi, y=Ci, label=Language)) + geom_point(colour="red") + xlim(0,0.5) + ylim(0,0.25)

ggplot(data=subset(df2, Subdomain %in% "children"), aes(x=Pi, y=Ci, label=Language)) + geom_point(colour="red") + xlim(0,0.5) + ylim(0,0.25)

ggplot(data=subset(df2, Subdomain %in% "grandparents"), aes(x=Pi, y=Ci, label=Language)) + geom_point(colour="red") + xlim(0,0.5) + ylim(0,0.25)

ggplot(data=subset(df2, Subdomain %in% "siblings"), aes(x=Pi, y=Ci, label=Language)) + geom_point(colour="red") + xlim(0,0.5) + ylim(0,0.25)

ggplot(data=subset(df2, Subdomain %in% "nephews and nieces"), aes(x=Pi, y=Ci, label=Language)) + geom_point(colour="red") + xlim(0,0.5) + ylim(0,0.25)

ggplot(data=subset(df2, Subdomain %in% "uncles and aunts"), aes(x=Pi, y=Ci, label=Language)) + geom_point(colour="red") + xlim(0,0.5) + ylim(0,0.25)

ggplot(data=subset(df2, Subdomain %in% "cousins"), aes(x=Pi, y=Ci, label=Language)) + geom_point(colour="red") + xlim(0,0.5) + ylim(0,0.25)

ggplot(data=subset(df2, Subdomain %in% "grandchildren"), aes(x=Pi, y=Ci, label=Language)) + geom_point(colour="red") + xlim(0,0.5) + ylim(0,0.25)



                                                                                                  