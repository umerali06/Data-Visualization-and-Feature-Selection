from sklearn.feature_selection import chi2, SelectPercentile, mutual_info_classif, SelectKBest, f_classif, SelectFpr, GenericUnivariateSelect, SelectFdr
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X,y = load_breast_cancer(return_X_y=True)
print(X.shape)

print("******* K beast *******")
k_chi = SelectKBest(chi2, k=5).fit_transform(X,y)
k_mu = SelectKBest(mutual_info_classif, k=7).fit_transform(X,y)
k_fclass = SelectKBest(f_classif, k=5).fit_transform(X, y)
print(k_chi.shape)
print(k_mu.shape)
print(k_fclass.shape)

print("******* Percentile *******")
per_chi = SelectPercentile(chi2, percentile=15).fit_transform(X,y)
per_mu = SelectPercentile(mutual_info_classif, percentile=15).fit_transform(X, y)
per_fclass = SelectPercentile().fit_transform(X,y)
print(per_chi.shape)
print(per_mu.shape)
print(per_fclass.shape)

print("****** FRP ******")
fpr_chi = SelectFpr(chi2, alpha=0.001).fit_transform(X,y)
fpr_mu = SelectFpr(chi2, alpha=0.001).fit_transform(X,y)
fpr_fclass = SelectFpr(f_classif, alpha=0.001).fit_transform(X,y)
print(fpr_chi.shape)
print(fpr_mu.shape)
print(fpr_fclass.shape)


print("****** Generic Univariate Select ******")
gen_kbest = GenericUnivariateSelect(score_func=f_classif, mode='k_best', param=5).fit_transform(X, y)
gen_percentile = GenericUnivariateSelect(score_func=f_classif, mode='percentile', param=20).fit_transform(X, y)
gen_fpr = GenericUnivariateSelect(score_func=f_classif, mode='fpr', param=0.05).fit_transform(X, y)

print(gen_kbest.shape)  
print(gen_percentile.shape)  
print(gen_fpr.shape)  


print("****** FDR (False Discovery Rate) ******")

fdr_chi = SelectFdr(chi2, alpha=0.05).fit_transform(X, y)
fdr_fclass = SelectFdr(f_classif, alpha=0.05).fit_transform(X, y)
#fdr_mu = SelectFdr(mutual_info_classif, alpha=0.05).fit_transform(X, y)

print(fdr_chi.shape)  
print(fdr_fclass.shape)  
# print(fdr_mu.shape)  


# Another method for the feature selection:

bc = load_breast_cancer()
A,b = bc.data, bc.target
f_names = bc.feature_names
print(f"features list are:\n {f_names}")

k_chi2 = SelectKBest(mutual_info_classif, k=6).fit(A,b)
get_feature_names = f_names[k_chi2.get_support()]
print(f"selected features list are:\n {get_feature_names}")

k_chi3 = SelectKBest(mutual_info_classif, k=5).fit_transform(A,b)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(k_chi3)

pca = PCA(n_components=2)  
X_pca = pca.fit_transform(X_scaled)

print(f"Explained variance ratio for each component: {pca.explained_variance_ratio_}")
