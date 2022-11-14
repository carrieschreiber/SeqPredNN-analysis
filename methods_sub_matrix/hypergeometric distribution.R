# hypergeometric distribution

# x = represents the obtained values
# m = number of total population in top 30% = 6
# n = number of total population **not** in top 30% = 14
# k = number of items in the population (sample size) = 7

x <- 6
m <- 6
n <- 14
k <- 7

# probability 
dhyper(x = x, m = m, n = n, k = k) # 0.07

# expected number of selected in top 30%
k * m / (m + n) # 2.1

# variance
k * m / (m + n) * (m + n - k) / (m + n) * n / (m + n - 1)

library(ggplot2)
library(dplyr)
options(scipen = 999, digits = 2) # sig digits

density = dhyper(x = 0:6, m = m, n = n, k = k)
data.frame(red = 0:6, density) %>%
  mutate(red2 = ifelse(red == 2, "x = 2", "other")) %>%
  ggplot(aes(x = factor(red), y = density, fill = red2)) +
  geom_col() +
  geom_text(
    aes(label = round(density,2), y = density + 0.01),
    position = position_dodge(0.9),
    size = 3,
    vjust = 0
  ) +
  labs(title = "PMF of X = x ranks in top 30%",
       subtitle = "Hypergeometric (k = 7, M = 6, N = 14)",
       x = "Number of ranks in top 30% (max of 6)",
       y = "Density") +
  theme(legend.position = 'none')
