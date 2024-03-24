DROP TABLE adult_income;
CREATE TABLE adult_income (
    age INT NOT NULL,
    workclass VARCHAR(50), 
    fnlwgt INT NOT NULL,
    education VARCHAR(50) NOT NULL,
    education_num INT NOT NULL,
    marital_status VARCHAR(50) NOT NULL,
    occupation VARCHAR(50), 
    relationship VARCHAR(50) NOT NULL,
    race VARCHAR(50) NOT NULL,
    sex VARCHAR(10) NOT NULL,
    capital_gain INT NOT NULL,
    capital_loss INT NOT NULL,
    hours_per_week INT NOT NULL,
    native_country VARCHAR(50), 
    income VARCHAR(10) NOT NULL
);

ALTER TABLE demographics
ADD CONSTRAINT chk_workclass
CHECK (workclass IN ('Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked'));

ALTER TABLE demographics
ADD CONSTRAINT chk_education
CHECK (education IN ('Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool'));

ALTER TABLE demographics
ADD CONSTRAINT chk_marital_status
CHECK (marital_status IN ('Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse'));

ALTER TABLE demographics
ADD CONSTRAINT chk_occupation
CHECK (occupation IN ('Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces'));

ALTER TABLE demographics
ADD CONSTRAINT chk_relationship
CHECK (relationship IN ('Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'));

ALTER TABLE demographics
ADD CONSTRAINT chk_race
CHECK (race IN ('White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black'));

ALTER TABLE demographics
ADD CONSTRAINT chk_sex
CHECK (sex IN ('Female', 'Male'));

ALTER TABLE demographics
ADD CONSTRAINT chk_native_country
CHECK (native_country IN ('United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands'));
