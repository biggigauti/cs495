math2 <- math

math2$Institution <- math$ï..Institution

math2 = subset(math2, select = -c(ï..Institution))

math3 <- math2

library(dplyr)

teamAverage <- math3 %>%
  select(Institution) %>%
  group_by(Institution) %>%
  summarize(count = n())

teamAverageDesc <- teamAverage[order(-teamAverage$count),]

outstandingTeams <- math3 %>%
  filter(Ranking == "Outstanding Winner")

outstandingTeamsOrdered <- outstandingTeams[order(outstandingTeams$Institution),]

usTeams <- math3 %>%
  filter(Country == "USA", Ranking == "Meritorious")

write.csv(teamAverage, "Desktop/skóli/spring2022/cs495/problem6/teamAverage.csv", row.names=TRUE)
write.csv(teamAverageDesc, "Desktop/skóli/spring2022/cs495/problem6/teamAverageDesc.csv", row.names=TRUE)
write.csv(outstandingTeamsOrdered, "Desktop/skóli/spring2022/cs495/problem6/outstandingTeamsOrdered.csv", row.names=TRUE)
write.csv(usTeams, "Desktop/skóli/spring2022/cs495/problem6/usTeams.csv", row.names=TRUE)




