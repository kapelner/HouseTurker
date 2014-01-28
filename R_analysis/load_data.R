X = read.table("data_f.txt", sep = " ")
X = X[, 1 : 9296]
X = cbind(abs(X[, 1]), X)
word_names = read.csv("dictmap.csv", header = FALSE)
word_names = sapply(word_names, as.character) #convert to characters
colnames(X) = c("y_diff", "y_diff_turk", "y_ratio", "y_ratio_turk", word_names[1 : 9293])