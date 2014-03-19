
mod = lm(y[1:2000] ~ ., X[1:2000, 1:1500])
summary(mod)

mod = lm(y[1:4000] ~ ., X[1:4000, 1:1500])
summary(mod)


mod = lm(log(y[1:4000]) ~ ., X[1:4000, 1:1500])
summary(mod)

res = princomp(X[, 1 : 1500])
top_scores = res$scores[, 1 : 500]

mod = lm(y ~ ., data.frame(top_scores))
summary(mod)


#hack the pairs

n = nrow(X)
ytop = y[seq(1, n - 1, 2)]
Xtop = X[seq(1, n - 1, 2), ]
ybottom = y[seq(2, n, 2)]
Xbottom = X[seq(2, n, 2), ]

y_diff = ytop - ybottom
y_log_diff = log(ytop) - log(ybottom)
X_diff = Xtop - Xbottom

mod = lm(y_diff[1:2000] ~ ., X_diff[1:2000, 1:1500])
summary(mod)

mod = lm(y_log_diff[1:2000] ~ ., X_diff[1:2000, 1:1500])
summary(mod)

res_diff = princomp(X_diff[, 1 : 1500])
top_scores_diff = res_diff$scores[, 1 : 500]

mod = lm(y_diff ~ ., data.frame(top_scores_diff))
summary(mod)

mod = lm(y_log_diff ~ ., data.frame(top_scores_diff))
summary(mod)
