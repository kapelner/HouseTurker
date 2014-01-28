#assume data is loaded

#pull out X and y
y = X[, 1]
ybin = ifelse(y > 0, 1, 0)

X = as.matrix(X[, 2 : ncol(X)])
Xsub = X[, 1 : 100]


#run some models


mod = lm(y ~ Xsub)
summary(mod)

Xsub = X[, 1 : 1000]

mod = lm(y ~ Xsub)
summary(mod)

library(glmnet)


mod = cv.glmnet(Xsub, y, alpha = 0)
vars = coef(mod)
vars = which(vars != 0) - 1
vars


Xsuby = cbind(X, y)
Xsuby = Xsuby[order(y), ]
length(y)
dim(Xsuby)
Xsuby = Xsuby[1000 : 3000, ]
Xsub = Xsuby[, 1 : (ncol(Xsuby) - 1)]
y = Xsuby[, ncol(Xsuby)]


Xsub = Xsub[, 1 : 1000]

mod = lm(y ~ Xsub)
summary(mod)

#lasso
mod = cv.glmnet(Xsub, y, alpha = 1)
vars = coef(mod)
vars = which(vars != 0) - 1
vars

#ridge
mod = cv.glmnet(Xsub, y, alpha = 1)
vars = coef(mod)
vars = which(vars != 0) - 1
vars

