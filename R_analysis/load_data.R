X = read.table("data_f.txt", sep = " ")

word_names = read.csv("dictmap2.csv", header = FALSE)
word_names = sapply(word_names, as.character) #convert to characters
colnames(X) = c("y_diff", "y_diff_turk", "y_ratio", "y_ratio_turk", word_names[1 : 9293])
rm(word_names)


#pull out X and y
y_diff = X[, 1]
y_diff_turk = X[, 2]

y_diff_turk_bin = ifelse(y_diff_turk > 0, 1, 0)
y_ratio = X[, 3]
y_ratio_turk = X[, 4]

#checks
sum(y_diff_turk > 0) / length(y_diff_turk)
sum(y_ratio_turk > 1) / length(y_ratio_turk)

#X is just covariates now
X = X[, 5 : ncol(X)]

#now kill all variables that are zer
Xabs = abs(X)
Xabstots = apply(Xabs, 2, sum)
table(Xabstots)

dead_vars = names(Xabstots[Xabstots == 0])
dead_vars = c(dead_vars, names(Xabstots[Xabstots == 1]))
dead_vars = c(dead_vars, names(Xabstots[Xabstots == 2]))

X = X[, !(colnames(X) %in% dead_vars)]


rm(dead_vars)
Xabs = abs(X)
Xabstots = apply(Xabs, 2, sum)

table(Xabstots)
hist(Xabstots,br=500)
Xtotsabs = sort(abs(Xabstots), decr = TRUE)

#barplot(Xtotsabs)

#let's order X by ostensibly the most informative covariates
X = X[, names(sort(Xabstots, decr = TRUE))]

save.image("raw.RData")