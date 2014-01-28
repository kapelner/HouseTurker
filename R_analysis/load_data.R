X = read.table("data_f.txt", sep = " ")
X = X[, 1 : 9296]
X = cbind(abs(X[, 1]), X)
word_names = read.csv("dictmap.csv", header = FALSE)
word_names = sapply(word_names, as.character) #convert to characters
colnames(X) = c("y_diff", "y_diff_turk", "y_ratio", "y_ratio_turk", word_names[1 : 9293])

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

save.image("raw.RData")