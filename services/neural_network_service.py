# -*- coding: utf-8 -*-

def calculate_imputation_error(feature, numerical_data, numerical_features):
    numerical_data = numerical_data.copy(deep=True);
    feature_data = numerical_data[feature][0:200].copy().reset_index(drop = True);
    numerical_data[feature][0:200] = np.nan
    completed_numerical_data = pd.DataFrame(MICE(verbose = False).complete(numerical_data));
    completed_numerical_data.columns = numerical_features;
    imputed_feature = completed_numerical_data[feature][0:200];
    imputed_data = pd.DataFrame([feature_data, imputed_feature]).T
    imputed_data.columns =['Real value', 'Imputed value'];
    imputed_data['Imputation error (%)'] = np.abs((imputed_data['Real value']-imputed_data['Imputed value']) / imputed_data['Real value'])*100
    imputation_error = np.mean(imputed_data['Imputation error (%)'])
    print('Imputation error for',feature,': ', imputation_error);
    return [feature, imputation_error];