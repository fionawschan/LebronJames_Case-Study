# Generate data
data<-read_excel("lebronAll.xls")

head(data)

# Histogram - Frequency of Points per game
hist(data$PTS)

# Multiple Scatterplot - MINS vs PTS/STL
par(mfrow=c(2,1), mar=c(4,4,2,1))
with(data, plot(data$MIN, data$PTS))
with(data, plot(data$MIN, data$STL))

