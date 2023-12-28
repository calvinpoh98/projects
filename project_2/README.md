<p align="center">
  <img width="700" height="400" src="https://github.com/calvinpoh98/projects/blob/master/project_2/images/us%20house.jpg?raw=true" />
</p>

# Project 2 Ames Housing Data and Kaggle Challenge

### Overiew
This project aims at examining the features of houses in Ames, Iowa which are further elaborated in a table below. After which, a model is trained on the model 
to give sale price predictions based on the features used. A regularised linear regression model (*Lasso & Ridge*) will be used for feature selection.

---
### Problem Statement
This project is for buyers who are planning to get a house but has a hard time offering a proper bid price, in which he/she will not overpay for a certain type of house ([*source*](https://www.businessinsider.com/the-biggest-signs-youre-overpaying-on-a-house-2019-7#:~:text=More%20than%2039%20million%20Americans,1.04%25%20for%20the%20same%20house.)). The important features extracted from the regularised models can also be used for sellers who wants the maximum value when selling their house. With a bid from the buyer and an ask from the seller, the transaction only goes through when both bid and ask matches. Therefore, this machine learning aims to provide better price signals for both the buyers and sellers. The primary stakeholder would be buyers and sellers of houses located in Ames, Iowa. The secondary stakeholder could be online real estate sites like [*Zillow*](https://www.zillow.com/) where they can use the model to give a recommendation on what price the sellers could list their houses for.
['Id', 'PID', 'MS SubClass', 'MS Zoning', 'Lot Frontage', 'Lot Area',
       'Street', 'Alley', 'Lot Shape', 'Land Contour', 'Utilities',
       'Lot Config', 'Land Slope', 'Neighborhood', 'Condition 1',
       'Condition 2', 'Bldg Type', 'House Style', 'Overall Qual',
       'Overall Cond', 'Year Built', 'Year Remod/Add', 'Roof Style',
       'Roof Matl', 'Exterior 1st', 'Exterior 2nd', 'Mas Vnr Type',
       'Mas Vnr Area', 'Exter Qual', 'Exter Cond', 'Foundation', 'Bsmt Qual',
       'Bsmt Cond', 'Bsmt Exposure', 'BsmtFin Type 1', 'BsmtFin SF 1',
       'BsmtFin Type 2', 'BsmtFin SF 2', 'Bsmt Unf SF', 'Total Bsmt SF',
       'Heating', 'Heating QC', 'Central Air', 'Electrical', '1st Flr SF',
       '2nd Flr SF', 'Low Qual Fin SF', 'Gr Liv Area', 'Bsmt Full Bath',
       'Bsmt Half Bath', 'Full Bath', 'Half Bath', 'Bedroom AbvGr',
       'Kitchen AbvGr', 'Kitchen Qual', 'TotRms AbvGrd', 'Functional',
       'Fireplaces', 'Fireplace Qu', 'Garage Type', 'Garage Yr Blt',
       'Garage Finish', 'Garage Cars', 'Garage Area', 'Garage Qual',
       'Garage Cond', 'Paved Drive', 'Wood Deck SF', 'Open Porch SF',
       'Enclosed Porch', '3Ssn Porch', 'Screen Porch', 'Pool Area', 'Pool QC',
       'Fence', 'Misc Feature', 'Misc Val', 'Mo Sold', 'Yr Sold', 'Sale Type',
       'SalePrice']

### Datasets used
['train.csv'](datasets/train.csv): Training and validation dataset for model

['test.csv'](datasets/train.csv): Test dataset for submission to Kaggle

|Feature Group|Features|Type|Description|
|---|---|---|---|
|**ID**| Id & PID| int| These are the identification numbers for each house sold|
|**Sale Details**| SalePrice, Mo Sold, Yr Sold, Sale Type| int | The sale price of the house and when did the transactions was processed|
|**Class and Zoning**| MSSubCLass & MSZoning| object| Houses have different zone on which they are built on such as Agriculture and Commercial. The subclass are various style of properties.|
|**Address**| Street, Alley and Neighborhood|object| This feature group include where the house is located at, giving the alley and the neigborhood too|
|**Land Confiuration**| Lot Area, Lot Shape, Land Contour, Lot Config, Land Slope |int & object| The configuration of the land that the house is built on|
|**Condition of House**| Condition 1 & 2, Overall Qual & Cond, Year Built, Year Remod/Add, Exter Qual, Exter Cond|int & object| This describes the state of the house|
|**Area of House**|Gr Liv Area, Mas Vnr Area, BstFun SF 1 & 2, Total Bsmt SF, 1st & 2nd Flr SF| int| Area of house broken down in a detailed manner|
|**House Specifications**| Bldg Type, Roof style & Matl, Exterior 1st & 2nd, Heating QC, Central Air, Electrical, Full & Half Bath, Fireplaces|object|More details on the house|



### Findings and recommendations
- The project was aimed at giving better price signals for the different type of houses in Ames Iowa. This predicted sale price of houses in Ames Iowa was at 89% accuracy which is considerably good and able to give good guidance for both the buyers and sellers. For the secondary stakeholders, online real estate could adopt this machine learning model to allow sellers to optimally price their houses and could potentially increase their transactions rate and drive more traffic to thier site.
- As for owners of houses that plan to sell their house, the most important feature identified by the models was overall condition of the house. Therefore, in order to get the maximum value for your house, you would want to have a house maintenance every now and then to upkeep it's quality and condition.

