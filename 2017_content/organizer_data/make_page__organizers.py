import pandas as pd

csv_df = pd.read_csv("organizers.csv")
csv_df['LASTNAME'] = [name.split()[-1] for name in csv_df['NAME'].values]
csv_df.sort_values("LASTNAME", inplace=True)

item_template_str = \
"""\n
    <!-- 6/12 = 1/2 width on mobile, 4/12 = 1/3 screen on laptop -->
    <div class="col-xs-6 col-md-4"> 
    <div class="thumbnail">
        <img 
            src="{filename}/images/tmp_100x100.jpg"
            alt="{{NAME}} headshot"
            style="width:88%"
            align="center">
        <div class="caption">
            <h5>{{NAME}}</h5>
            <p>{{AFFIL}}, {{TITLE}}</p>
            <p>Team: {{ROLE}}</p>
            <p></p>
        </div>
    </div>
    </div>
\n"""

out_md_str = "Title: Organizers\nDate: 2017-06-01\n"
out_md_str += (
"""\n
<!-- THIS PAGE SRC IS AUTO GENERATED. At terminal: $ make organizers -->
\n""")

n_per_row = 100

for item_id, row_obj in enumerate(csv_df.itertuples()):

    if item_id % n_per_row == 0:
        out_md_str += '\n<div class="row">'

    row_dict = row_obj.__dict__
    item_str = item_template_str + ""
    #from IPython import embed; embed()
    for key, val in row_dict.items():
        item_str = item_str.replace("{{%s}}" % str(key), str(val))
    out_md_str += item_str


    if item_id % n_per_row == n_per_row - 1:
        out_md_str += "</div>\n"

with open("../pages/organizers.md", 'w') as f:
    f.write(out_md_str)