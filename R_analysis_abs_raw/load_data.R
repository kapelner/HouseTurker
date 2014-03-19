X = read.table("data_f_raw.txt", sep = " ")

word_names = read.csv("dictmap.csv", header = FALSE)
word_names = sapply(word_names, as.character) #convert to characters
colnames(X) = c("y", word_names[1 : 9294])
rm(word_names)

#kill last col
X = X[, 1 : (ncol(X) - 1)]

#pull out X and y
y = X[, 1]
X = X[, 2 : ncol(X)]

word_freq = colSums(X)


word_freq = sort(word_freq, decr = T)
plot(word_freq, log = "xy")

X = X[, names(word_freq)]

rm(word_freq)

save.image("raw.RData")