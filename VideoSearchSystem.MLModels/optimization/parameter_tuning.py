from sklearn.model_selection import GridSearchCV

def tune_parameters(model, param_grid, X, y):
    grid = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', verbose=2)
    grid.fit(X, y)
    return grid_search.best_params_, grid_search.best_score_
