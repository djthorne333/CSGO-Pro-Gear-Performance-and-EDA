# CS:GO-Pro-Gear-Performance-Repo

# NOTE: Sometimes Github decides not to render the output of a notebook. If this happens, paste the link of the .ipynb file within the repo to https://nbviewer.org/

# Exploratory Data Analysis of Professional (CS:GO) Gamer's Gear and Settings, and Modeling Player Accuracy  Performance  


#### Author: Thorneinsight@gmail.com

#### FILES: CSGO Gear EDA and Modeling.ipynb is the project notebook, _scrape.py files are what I used for scraping, and the one csv file contains the 118 players' gear/stats.
    
# Project Goals: 
    
* Describe Player equipment and setting choices at the pro level, including frequent combinations of equipment and settings.   
* Look for and describe trends in equipment/settings choices based on their properties (weight, sensitivity, mousepad speed, etc).
* Look to see if there is a relationship between player equipment/setting choices and whether they perform above the median of the dataset in terms of accuracy performance, when player role is accounted for (rifler vs awper).
* Optimise models to see what degree of accuracy player performance (in terms of their aim) can be predicted knowing only their gear and settings, when player role is accounted for.


## Why I'm doing this Project

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*I wanted my first personal Data Science project to be novel, answer questions I personally have, and be associated with data I believed I could obtain through web scraping. Now I don’t game as much as I used too, but I know that players are always talking about the properties of their equipment and settings (mouse weight, in-game-sensitivity, mousepad speed, etc.), and how these properties may give them an edge. I myself used to watch product reviews often, and experiment with different equipment. When I realized that no one had played with the data from prosettings.net, which I used to visit, in combination with player performance, I thought it was a great place to start.*

*What this project is:
-An exploratory data analysis to describe trends in what gear/settings pro players prefer, and an attempt to see what degree of accuracy you can model whether a player has above average aim based only on their gear/settings.*


*What this project not:
-Absolute Proof that the gear/settings/properties found to pass chi2 tests during feature selection, or those features optimizing the performance of certain models, make anyone aim better or worse! We can let ourselves get a little excited, though.*


### Lingo/Description of data

Data was obtained from prosettings.net, leetify.com, and thegamingsetup.com. Data is that of 118 total players.  

"CS:GO": Title of the game, Counter Strike: Global Offensive.  
"Role": Whether a player is an awper or rifler.  
"Awper": Player that has a precision role on the team. Uses the AWP rifle, which is a one-hit elimination.   
"Rifler": Player that has a more general role.  

"dpi": in-mouse sensitivity value, dots per inch    
"sens": in-game sensitivity value, however I immediately created an edpi feature which I refer to as "sens" or "sensitivity" throughout the project. The original value is not referred to again.    
"edpi" ("sens" or "sensitivity"): A player's crosshair will move quicker or slower around the world depending on dpi and in game sensitivity. Edpi gives a universal value, two players with different dpi and in game sensitivities can have the same edpi, and the crosshair will be equally sensitive to how much they move their mice across the pad. Higher edpi's are more sensitive to mouse movement.       
"mouse2": What mouse a player is using  
"width, height, length, size, weight": All mouse dimensions, in centimeters and grams.   
"type": Whether the mouse is designed to be held in right hand (ergonomic) or both right and left hand (ambidextrous).     
"hertz": Monitor setting, defines frame rate  
"resolution": in game setting, pixel density  
"aspect_ratio": in game setting, or how stretched the world appears  
"mouse_pad": The mouse pad a player is using  
"speed": The subjective speed or "control" feeling of the mouse moving on the pad. Higher numbers= slower speed, higher control.    
"acc spotted": The subject of this project, a player’s accuracy on their target when that target is in their field of view (more info on this later). Accuracy spotted will be a focus of this project.   
"scored high spotted", "target", "high-scorer": the class we are predicting during modeling. Whether a player's accuracy score is above or below the median value for his role

Mousepad speeds are written as float values, 1.0-6.0, while clusters are written as integer values, 0-3.



# Outline:

### To Run:  
* Under "Importing data from csv", enter your path to the file "CSGO_Scraped_Cleaned.csv". Cells must be run in order.
    
    
### Data web scraping, data importing and cleaning.
    
    
* Data was scraped in early September of 2021 using selenium (code is in repo) from prosettings.net for gear/settings, leetify.com for player performance (stats recorded over 1 year), and thegamingsetup.com / mouse-size-chart-table for mouse dimensions. Then the data was sorted in openrefine and excel so that all rows matched to the associated players, then all rows were dropped  that contained missing data. I then manually entered mouse pad speeds from a "Mousepad Master Sheet" made by a reddit user on r/MouseReview, and loaded in the csv. The code for webscraping comes in 3 files, and they essentially use the same method.

* Units had to be removed from many columns of data, data types were inconsistent, some data had to be manually entered when nans were returned during type conversion.

* Potential issues with data: This project makes the assumption that the player performance stats recorded on Leetify were recorded while players were using the gear/settings on prosettings.net. The data was scraped within the same day. The stats recorded from Leetify were recorded over a year, and this project also assumes that players did not change their equipment/settings during the season. Also, mousepad speeds are subjective, and some of the speeds that I entered manually required me to research the specific reviews and advertising for those pads. Also, our sample contains only 118 players, and so not every feature has enough players actually using it to give us a confident idea of how it fits in the whole population.

    

      
    
    
## Exploratory data analysis: 


### EDA Purpose:    
* Find and describe most frequent individual gear/settings used.
* Find an describe most frequent combinations of gear/settings used (apriori)
* Find and describe trends of gear/settings used based on general properties of those gear/settings (weight, sensitivity, mousepad speed, etc).
* Find and describe trends of gear/settings used based on player role (rifler vs awper)
* Attempt to separate players into clusters based on their gear/settings.
* Perform chi2 tests between all individual choices/freq-combinations/clusters to look for trends between them.
* Look for trends between player accuracy performance and their gear/settings choices through visualizations.
* Perform chi2 tests between all individual choices/freq-combinations/clusters and player accuracy performance.

 
### Methods Used: 
* Descriptive statistics, histograms, regression plots, pairplots, correlation matrices, apriori, chi2 tests, clustering 
    
    
### Feature creation: 
* Binning
* Apriori to find frequent gear/settings patterns and turn them into features
* Clustering to separate players based on their gear/settings choices and turn those clusters into features
* Created new mouse dimension, Volume, and new feature, Aspect + Resolution pair.





    
    

  
### Results of EDA:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*A large imbalance of players use the logitech g pro wireless and g pro superlight over other mice. The current market trend in mouse weight is to make mice as light as possible, often under 60g. Most csgo pro players evidently use heavier mice, at least relative to this trend (75% of players above 63g). Similarly players tend not to lean towards using smaller mice, as mean volume falls around what would be considered a medium sized mouse. Mean edpi is around 886. Most players use mousepads with slower speeds/higher control compared to all options on the market, the top four being the Steelseries qck heavy, Steelseries qck+, Zowie G-SR, and logitech G640. Almost half of players use one of the top 2 monitor settings:(1280x960, 4:03), or (1024x768, 4:03). Most players use over 144hz. Low sensitivity users may seem to prefer the monitor settings: (1920x1080, 16:09) more so than players using other sensitivities. No other interpretable patterns were found in terms of players choosing one gear/setting while using another. There are over three times as many riflers as awpers. More awpers tend to use edpi's above the median value of the dataset than not. Awpers also tend to have greater accuracy scores. Just as many Awpers use the logitech G Pro X Superlight as every other mouse. Most Players use the following gear/settings: 90% of players use refresh rates of 144-240hz, 74% of players medium-sized mice (mice that fit in a box 300-360 cm^3), 74% of players use aspect ratio 4:03, 60% of players use a mousepad surface speed/control rating of 5.0. There is no combination of features that over 50% of players use (outside of combinations of those features). Players could not be separated into well defined clusters based on original dataset features, left as numerical, evaluated based on cluster silhouette scores.*
  
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The following are features passing a chi2 test performed on all features created with respect to whether the player is above or below the median accuracy score of their role(awper/rifler). This displays all features scoring at most p-value=0.1. Note that 0.1 is slightly lenient and that chi2 tests are not reliable on features with fewer players. Some of these features contain only 3 players. Note also that many of the pairs of features created from frequent patterns implicitly describe other individual features, and that many of these features are correlated. A positive result means that over all players that use this feature, more of them are high-scorers than expected given the distributions. These features were used for feature selection during modeling. The visualization displays how many players score above(1)/below(0) the median accuracy of their role when using(1)/not(0) using each feature. Bin and cluster interpretation is written below.*  

    
![image](https://user-images.githubusercontent.com/73368743/141010066-86f6fccf-a806-4a47-920b-96637aed050f.png)  

    
**Bin Interpretation**: (bins are numbered starting from 1, 1<2<3)    
Weight bins (g):  (0.0, 67.7], (67.7, 87.4], (87.4, 200.0]    
Width bins (cm):  (5.2, 6.1], (6.1, 6.7], (6.7, 10.0]    
Length bins (cm):  (11.4, 12.0], (12.0, 12.4], (12.4, 12.8]    
Height bins (cm):  (3.5, 3.846], (3.846, 4.13], (4.13, 10.0]    
Volume bins (cm^3):  (218, 300], (300, 360], (360, 1000]    
Sens Bins (edpi):  (439, 800], (800, 1180], (1180, 3000]    
Hertz bins (hz):  (143, 240], (240, 555]                                                                 
The logitech g pro x superlight falls into bins: wght1, length2, wdth2, hght2, vol2.                                                                                

**Describing clusters:**      
lower bin number are lower values  
cluster 0: players that belong near: vol2, weight2, sens1, speed under 5, hrz1  
cluster 1: players that belong near: vol2, weight2, sens2, speed 5, hrz1, more likely to use (1280x960, 4:03)  
cluster 2: players that belong near: vol3, weight3, sens2, speed 5, hrz1, more likley to use (1024x768, 4:03)  
Cluster 3: players that belong near: vol2, weight2, sens2, speed 5, hrz2     

  



    
  
    
## Modeling: 
* Original features were used to train and evaluate models as baseline 
* Feature Selection:  
    Filter methods: Features that scored high on chi2 test were selected for modeling.   
    Wrapper methods: Forward and Backward Sequential Feature Selection was used to further select Features for Model   Performance        
* Logistic regression, Lasso, knn, and random forest.
* Grid search for parameter optimization was used for each model.

    
### Modeling Results:
**---Managed an increase in model performance of 17% through feature creation (binning, frequent patterns, clustering, separation by player role), filter methods(chi2 tests with target), and wrapper methods (sequential feature selection). Original Accuracies: Around 50%. Best Performing Model: Logistic Regression, Test Accuracy: 0.672, Train Accuracy: 0.678.**
    
*All Models were evaluated on average test and train accuracy scores across all splits of cross validation with k = 50 (nearly leave-one-out). Those average scores were also averaged together anywhere from 10 to 30 times.** 

    
#### Modeling using original features:  

    *Logistic Regression:*
    Test Accuracy: 0.50
    Train Accuracy:N/A
    
    *Logistic regression, Lasso, gridsearched regularization:*
    Best Parameter: C=.25
    Test Accuracy: 0.564
    Train Accuracy: 0.602
    
    *k nearest neighbors, gridsearched parameters:*
    Best Parameter: 'metric': 'euclidean', 'n_neighbors': 15, 'weights': 'uniform'}
    Test Accuracy:0.531
    Train Accuracy: 0.595

    *Random Forest, gridsearched parameters:*
    Best Parameter: {'bootstrap': True, 'criterion': 'gini', 'max_depth': 5, 'max_features': 'auto', 'min_samples_leaf': 5, 'min_samples_split': 3, 'n_estimators': 500}
    Test Accuracy: 0.50
    Train Accuracy: N/A 
    
   
#### Modeling using Sequential Feature Selector (scoring for accuracy) on features passing chi2 test, pvalue=.1, from list of over 300 features, including original features, frequent patterns, and clusters, all seperated by role:    


    *Logistic Regression:*
    Test Accuracy: 0.672
    Train Accuracy: 0.678
    Sfs chosen Features: ['Logitech G Pro X Superlight rifler', 'wght1+hrz1 rifler', '1 rifler', 'hght3 rifler', 'hrz2 awper', '6.0 awper', 'Zowie G-SR awper', '3 awper']
    Aproximate model coeeficients (taken from one cv run):
    (0.37847194  0.20237742  0.48302971 -0.92805684 -0.56933603 -0.72778813 1.0131123  -0.56933603)
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Logistic Regression is our best performing model, and its classification accuracy has improved over 17% compared to our models that use the original features only. Our test and train accuracy are 0.672 and 0.678 respectivley, which suggests we are not overfitting. This is far better than a coin flip! Notice however how many of the chosen features end up in the model just to classify the 3 or so players that use them. Specifically, the features: '6.0 awper','hrz2 awper', and '3 awper'. There is no guarantee that the distribution of high-scorers using those features is the same across all players in reality, it's just that way in our sample of 118 players. However my goal was to see with what degree of accuracy you could currently model whether a players aim was above average based on their gear/settings alone, and I am happy with these results. I’m very curious what performance could be accomplished if I had more data, but also how this current model performs on the whole population.*   &nbsp;                           
&nbsp;

    *Random Forest, gridsearched parameters:*
    Best Params: {'bootstrap': True, 'criterion': 'gini', 'max_depth': 3, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 500}
    Test Accuracy:0.669
    Train Accuracy:0.67  

    *K Nearest Neighbors, gridsearched parameters:*
    Best Parameters: {'metric': 'euclidean', 'n_neighbors': 3, 'weights': 'uniform'}
    Test Accuracy: 0.64
    Train Accuracy: 0.665
    sfs Chosen Features:['wght1 rifler', 'wght1+hrz1 rifler', '1 rifler', 'hght3 rifler', 'hrz2 awper', '6.0 awper', 'Zowie G-SR awper', '3 awper']
    
  
    

    
    
    

    
    

### Possible Recommendations of equipment/settings to use:
*If you are a rifler:*

Use lighter mice or the Logitech g pro x superlight, avoid larger sized mice.

This is because players using certain features have a significant imbalance in high/low scoring players. The following features all passed the (lenient) chi2 test with the scored_high_spotted target, but also have at least 15 players using them: 

The Logitech g pro x superlight, weight1, clust1 (the Logitech g pro x superlight accounts for most of the mice in the weight1 bin and cluster 1) tend to have an imbalance favoring high-scoring players.  

More players using features hght3, wth3, vol3, and clust2 rifler (which contains vol3, weight3), tend to have an imbalance favoring low-scoring players.  


However, we can still only guess who is a high-scoring player with 67.2% accuracy based on their gear/settings, and we had a small sample of players to analyze. At the end of the day, it's important to use what works best for you!   
                     
                     

### Issues with data that could affect analysis and model accuracy:

* We have not accounted for sponsorships, for instance, the logitech g pro x superlight has a few high scoring players, what if a few of them are forced to use the mouse, as they became sponsored by logitech because they were recognized as good players in the first place?
* Some of the features that end up in the models after chi2 tests are represented by only 3 players.
* Clusters were not generated to maximize model accuracy nor could they be well defined.
* We only have 118 players in this sample
* Features like mousepad speed are subjective
* The player's gear and stats may not match
* We are relying on Leetify's accuracy scoring system
* We are relying on the mouse measurements of one source
* Even if these results were certain and represent the whole professional player population, they may not apply to the average player. 

