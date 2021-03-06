#assume data is loaded

res = princomp(X[, 1 : 1500])
top_scores = res$scores[, 1 : 500]

mod = lm(log(y_diff) ~ ., data.frame(top_scores))
summary(mod)
plot(coef(summary(mod))[, 4])



Xsub = as.matrix(X[, 1 : 500])
mod = lm(y_diff ~ Xsub)
summary(mod)

Xsub = as.matrix(X[, 1 : 1000])
mod = lm(y_diff ~ Xsub)
summary(mod)

Xsub = as.matrix(X[, 1 : 4000])
mod = lm(y_diff ~ Xsub)
summary(mod)


hist(log(y_ratio_turk), br = 1000)

Xsub = as.matrix(X[, 1 : 500])
mod = lm(log(y_ratio_turk) ~ Xsub - 1)
summary(mod)

Xsub = as.matrix(X[, 1 : 1000])
mod = lm(log(y_ratio_turk) ~ Xsub - 1)
summary(mod)

Xsub = as.matrix(X[, 1 : 2000])
mod = lm(log(y_ratio_turk) ~ Xsub - 1)
summary(mod)


hist(log(y_ratio), br = 1000)

Xsub = as.matrix(X[, 1 : 500])
mod = lm(log(y_ratio) ~ Xsub - 1)
summary(mod)

Xsub = as.matrix(X[, 1 : 5])
mod = lm(log(y_ratio) ~ Xsub - 1)
summary(mod)

Xsub = as.matrix(X[, 1 : 2000])
mod = lm(log(y_ratio) ~ Xsub - 1)
summary(mod)


Xsub = as.matrix(X[, 1 : 500])
mod = lm((log(y_ratio_turk) > 0) ~ Xsub - 1)
summary(mod)

Xsub = as.matrix(X[, 1 : 1000])
mod = lm((log(y_ratio_turk) > 0) ~ Xsub - 1)
summary(mod)

Xsub = as.matrix(X[, 1 : 2000])
mod = lm((log(y_ratio_turk) > 0) ~ Xsub - 1)
summary(mod)




#run some models


mod = lm(y_diff_turk ~ Xsub)
summary(mod)
mod_coefs = coef(summary(mod))
mod_coefs = mod_coefs[order(mod_coefs[, 4]), ]
head(mod_coefs, 100)

mod = lm(y_ratio_turk ~ Xsub - 1)
summary(mod)

mod = lm(y_diff_turk_bin ~ Xsub)
summary(mod)

Xsub = as.matrix(X[, 1 : 2000])

mod = lm(y_diff ~ Xsub)
summary(mod)

library(glmnet)


library(glmnet)
mod = cv.glmnet(Xsub, y_diff_turk, alpha = 1) #lasso
#mod = cv.glmnet(Xsub, y_diff_turk, alpha = 0) #ridge
#mod = cv.glmnet(Xsub, y_diff_turk, alpha = 0.5) #even elastic net
vars = coef(mod)
vars = which(vars != 0) - 1
vars





















Xsuby = cbind(X, y_diff)
Xsuby = Xsuby[order(y_diff), ]
length(y_diff)
dim(Xsuby)
Xsuby = Xsuby[1000 : 3000, ]
Xsub = Xsuby[, 1 : (ncol(Xsuby) - 1)]
y_diff = Xsuby[, ncol(Xsuby)]


Xsub = Xsub[, 1 : 1000]

mod = lm(y_diff ~ Xsub)
summary(mod)

#lasso
mod = cv.glmnet(Xsub, y_diff, alpha = 1)
vars = coef(mod)
vars = which(vars != 0) - 1
vars

#ridge
mod = cv.glmnet(Xsub, y_diff, alpha = 1)
vars = coef(mod)
vars = which(vars != 0) - 1
vars

