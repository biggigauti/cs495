math <- math

math$Institution <- math$ï..Institution

math = subset(math, select = -c(ï..Institution))

math2 <- math

library(dplyr)

math3 <- transform(math2, UniqueID = as.numeric(factor(Institution)))

institution = subset(math3, select = c("UniqueID", "Institution", "City", "State.Province", "Country"))

teams = subset(math3, select = c("Team.Number", "Advisor", "Problem", "Ranking", "UniqueID"))

write.csv(institution, "Desktop/skóli/spring2022/cs495/problem5/institution.csv", row.names=TRUE)
write.csv(teams, "Desktop/skóli/spring2022/cs495/problem5/teams.csv", row.names=TRUE)
