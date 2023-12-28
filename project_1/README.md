<p align="center">
  <img src="https://github.com/calvinpoh98/projects/blob/master/project_1/imgs/SAT_and_ACT.png?raw=true" />
</p>

### Overview

This project aims are exploring both the **ACT** and **SAT**, which are standardized tests in which colleges in the US use to gauge the apititude of the student during the admission process. While it is a major part when it comes to the admission selection, the other achievements of the student are also considered, for example the grade point average (GPA) and could also include their athletic profile.

---

### Problem Statement

The states in the US have varying participation rate and total scores from the datasets reviewed from 2017 to 2019. Therefore, there will states that will have lower participation rate and total/composite scores relative to the other states. As colleges do take SAT and ACT into consideration when admitting a student, it is vital for states to push for higher participation rate and increase the chances of such students getting into the colleges of their wanting. 

Therefore we consider a few things:
> - The states with the lowest participation rate for all 3 years in the SAT and ACT
> - Potentially correlation between the participation rate and the composite/total score of the SAT and ACT
> - Identify which states have decreasing participation rates

Finally we make a recommendation based on the findings above.

--- 

### Datasets used

* [`act_2017.csv`](./data/act_2017.csv): 2017 ACT Scores by State ([source](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows))
* [`act_2018.csv`](./data/act_2018.csv): 2018 ACT Scores by State ([source](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows))
* [`act_2019.csv`](./data/act_2019.csv): 2019 ACT Scores by State ([source](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows))
* [`sat_2017.csv`](./data/sat_2017.csv): 2017 SAT Scores by State ([source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/))
* [`sat_2018.csv`](./data/sat_2018.csv): 2018 SAT Scores by State ([source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/))
* [`sat_2019.csv`](./data/sat_2019.csv): 2019 SAT Scores by State ([source](https://blog.prepscholar.com/average-sat-scores-by-state-most-recent))

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**State**|object|ACT & SAT|This columns contains the 50 states in the US, not counting Puerto Rico| 
|**Composite**|Float|ACT|There are 3 columns that contains the composite scores for all three years; 2017, 2018 & 2019. The composite score is the average of the English, Math, Reading and Science scores| 
|**Participation**|Float|ACT& SAT|Similar to the Composite columns, there are 3 columns for the 3 years. It is represent in decimals where 0.95 means 95% participation rate.| 
|**Total**|int|SAT|This is the sum of both EBRW and Math scores in the SAT test| 

---
### Findings and recommendation
- Maine is constantly having low ACT participation rates and is not on the on the high participation list of SAT. Likewise, North Dakota is having the lowest SAT participation rate. Therefore, there should be a push for these two states to get their students to participate and promote the benefits of doing so.
- There are no state with equal SAT and ACT participation rate. One usually precedes the other. Based on the map below with different colours depicting the participation rate of each state, we could see that the east coast and west coast of US do prefer the SAT over the ACT. While in the Middle America, majority of them takes ACT.


![](https://git.generalassemb.ly/calvinpoh98/labs/blob/1a710094ac833c2104174067479189f886b26b98/project_1/imgs/SAT%20map%202019.png) ![](https://git.generalassemb.ly/calvinpoh98/labs/blob/1a710094ac833c2104174067479189f886b26b98/project_1/imgs/ACT%20map%202019.png)  

