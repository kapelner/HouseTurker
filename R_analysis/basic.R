#assume data is loaded

X = as.matrix(X[, 2 : ncol(X)])
Xsub = X[, 1 : 100]


#run some models


mod = lm(y_diff ~ Xsub)
summary(mod)

Xsub = X[, 1 : 1000]

mod = lm(y_diff ~ Xsub)
summary(mod)

library(glmnet)


mod = cv.glmnet(Xsub, y_diff, alpha = 0)
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

