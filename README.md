# Mini_Proj2_Fuyao_Li

### Author name: Fuyao Li

## Overview
This repository uses a dataset which records 'Monthly mean air temperature dataset' from August 1843 to April 2022. All values are in degrees Celsius, to a precision of one decimal place. `main.py` calculate the mean, median, and standard deviation of the temperature from 1795 to 2021.


## Set up
1. Clone the repository:
``` shell
git clone git@github.com:nogibjj/Mini_Proj2_Fuyao_Li.git
```
2. Create a virtual environment
``` shell
conda create --name test python=3.9
conda activate test
```
3. Install required packages
``` shell
pip install -r requirements.txt
```


## Result 
1. This table shows the mean, median, and standard deviation value of the temperature of every month from 1795 to 2021

   | T (&deg;C)         | Jan  | Feb  | Mar  | Apr  | May   | Jun   | Jul   | Aug   | Sep   | Oct  | Nov  | Dec  |
   | ------------------ | ---- | ---- | ---- | ---- | ----- | ----- | ----- | ----- | ----- | ---- | ---- | ---- |
   | Mean               | 2.89 | 3.48 | 4.91 | 7.17 | 9.97  | 13.07 | 14.91 | 14.63 | 12.45 | 9.14 | 5.61 | 3.66 |
   | Median             | 3.09 | 3.71 | 4.80 | 7.10 | 10.05 | 13.03 | 14.85 | 14.60 | 12.50 | 9.10 | 5.60 | 3.74 |
   | Standard deviation | 1.72 | 1.72 | 1.56 | 1.28 | 1.29  | 1.15  | 1.20  | 1.12  | 1.15  | 1.35 | 1.33 | 1.64 |

    

2. The visualization: <br>

  ![figure1](average.png)

![figure2](heatmap.png)