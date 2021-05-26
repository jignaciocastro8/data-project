import twint

# Configure
c = twint.Config()
c.Username = "JanitoElJano"
c.Limit = 10
c.Store_csv = True
# Run
twint.run.Search(c)