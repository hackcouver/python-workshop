import twint

c = twint.Config()
c.Username = "realDonaldTrump"  # switch to whichever Twitter account you would like
c.Output = "data/trump.txt"

s = twint.run.Search(c)