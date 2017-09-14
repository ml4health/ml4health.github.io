'''
To add several people to the program committee, write down each PC member in a separate line using the following format:
FirstName LastName <EmailAddress>
'''

import pandas as pd

csv_df = pd.read_csv("../2017_content/organizer_data/organizers.csv")
csv_df['LASTNAME'] = [
    name.split()[-1] for name in csv_df['NAME'].values]
csv_df['FIRSTNAME'] = [
    ' '.join(name.split()[:-1]) for name in csv_df['NAME'].values]
csv_df.sort_values("LASTNAME", inplace=True)

for row_id, row in csv_df.iterrows():
    print '"%s" "%s" <%s>' % (
        row['FIRSTNAME'],
        row['LASTNAME'],
        row['EMAIL'])