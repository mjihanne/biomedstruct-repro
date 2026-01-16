from sklearn.model_selection import KFold, StratifiedGroupKFold


def random_kfold_split(X, y, n_splits=5, random_state=42):
    return KFold(
        n_splits=n_splits,
        shuffle=True,
        random_state=random_state
    ).split(X, y)


def grouped_kfold_split(X, y, groups, n_splits=5):
    return StratifiedGroupKFold(
        n_splits=n_splits
    ).split(X, y, groups)


def temporal_split(data, year_column, train_years, test_years):
    train_idx = data[year_column].between(train_years[0], train_years[1])
    test_idx = data[year_column].between(test_years[0], test_years[1])
    return train_idx, test_idx


def roll_forward_split(data, year_column, start_year, end_year):
    splits = []
    for year in range(start_year + 1, end_year + 1):
        train_idx = data[year_column] < year
        test_idx = data[year_column] == year
        splits.append((train_idx, test_idx))
    return splits
