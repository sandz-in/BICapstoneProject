getwd()
births <- read.table("/Users/samrudhi/Downloads/island.csv")

birthstimeseries <- ts(births, frequency=12, start=c(2000,1))
birthstimeseries
plot(birthstimeseries)
birthstimeseries.stl = stl(birthstimeseries, s.window="periodic")
plot(birthstimeseries.stl)

plot(birthstimeseries, xaxt = "n")
tsp = attributes(birthstimeseries)$tsp
dates = seq(as.Date("2001-01-01"), by = "month", along = birthstimeseries)
axis(1, at = seq(tsp[1], tsp[2], along = birthstimeseries), labels = format(dates, "%Y-%m"))
df = data.frame(date = seq(as.POSIXct("2001-01-01"), by = "month", length.out = 24), pcp = rnorm(24))
library(ggplot2)
library(scales)
p = ggplot(data = df, aes(x = date, y = pcp)) + geom_line()
p + scale_x_datetime(labels = date_format("%Y-%m"), breaks = date_breaks("months")) + theme(axis.text.x = element_text(angle = 45))

