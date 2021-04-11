library (readr)

urlfile="https://raw.githubusercontent.com/fivethirtyeight/data/master/mlb-quasi-win-shares/quasi_winshares.csv"

mydata<-read_csv(url(urlfile))