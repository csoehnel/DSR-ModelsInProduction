{
    'dataset_loader_train': {
        # like call: Table(path = iris.data, names = ["sepal length", ...]
        '__factory__': 'palladium.dataset.Table',
        'path': 'iris.data',
        'names': [
            'sepal length',
            'sepal width',
            'petal length',
            'petal width',
            'species',
        ],
        'target_column': 'species',
        'sep': ',',
        'nrows': 100,
    },

    'dataset_loader_test': {
        # copies properties of dataset_loader_train and overrides the following
        '__copy__': 'dataset_loader_train',
        'nrows': None,
        'skiprows': 100,
    },

    'model': {
        '__factory__': 'sklearn.linear_model.LogisticRegression',
        'C': 0.5,
    },

    'model_persister': {
        '__factory__': 'palladium.persistence.Database',
        'url': 'sqlite:///iris-model.db',
    },
}
