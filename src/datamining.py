import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

def show_metrics(y_pred, y_test, y_score, plot_auc_curve = True):
    conf_matrix = metrics.confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = conf_matrix.ravel()

    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)

    fpr, tpr, _= metrics.roc_curve(y_test, y_score)
    auc = metrics.roc_auc_score(y_test, y_score)


    print(f'Accuracy: {metrics.accuracy_score(y_test, y_pred)}')
    print(f'Confusion Matrix: {conf_matrix}')
    print(f'Sensitivity: {sensitivity}')
    print(f'Specificity: {specificity}')
    print(f'MCC: {metrics.matthews_corrcoef(y_test, y_pred)}')
    print(f'F1 Score: {metrics.f1_score(y_test, y_pred)}')
    print(f'AUC: {auc}')


    # Citation: https://stackoverflow.com/a/38467407/10583094
    if plot_auc_curve:
        plt.title('Receiver Operator Characteristic')
        plt.plot(fpr, tpr, 'b', label=f"AUC={auc}")
        plt.legend(loc = 'lower right')
        plt.plot([0, 1], [0, 1],'r--')
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.ylabel('True Positive Rate')
        plt.xlabel('False Positive Rate')
        plt.show()

def main():
    '''
    TODO: 
    implement id3 and c4.5
    experiment with different parameters 
    experiment with undersampling dataset
    '''
    dataset_filename = 'src/clean_adult.csv'
    adult_income = pd.read_csv(dataset_filename, index_col=False)
    X = adult_income.iloc[:, 0:-1]
    y = adult_income.iloc[:, -1].to_numpy()

    test_size = 0.3

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=1)

    clf = DecisionTreeClassifier()

    
    # k_folds = 10
    # scores = cross_val_score(clf, X_train, y_train, cv=k_folds)
    # print(scores)
    # print(scores.mean())

    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    y_score = clf.predict_proba(X_test)[:, 1]

    show_metrics(y_pred, y_test, y_score)



if __name__ == '__main__':
    main()