import pandas as pd

csv_df = pd.read_csv("poster_assignments.csv")
csv_df['PDFURL'] = ''
camready_df = pd.read_csv("camera_ready.csv")

# csv_df = pd.read_csv("spotlights.csv")

item_template_str = \
"""\n
<!-- 12/12 = full width on mobile, 6/12 = 1/2 screen on laptop -->
<div class="col-xs-12 col-md-6"> 
<div class="thumbnail">
    <div class="caption">
        <h5><a href="{{PDFURL}}">{{TITLE}}</a></h5>
        <p>{{AUTHORS}}</p>
    </div>
</div>
</div>
\n"""

out_md_str = "Title: Spotlights\nDate: 2017-11-15\nSkipNavBar: 1"
out_md_str += (
"""\n
<!-- THIS PAGE SRC IS AUTO GENERATED. At terminal: $ make spotlights -->
\n""")

#n_per_row = 100
out_md_str += \
"""
Congratulations to the 16 papers below selected for spotlight presentations!

These will be presented in rapid succession (2 min. each) during the 9:45 - 10:15 slot of <a href="program.html">our workshop program</a> to give our audience a taste of exciting work happening in the ML+Health space.

<div class="row display-flex" style="display:flex; display:-webkit-flex;  flex-wrap:wrap;">
"""

spotlight_df = csv_df[csv_df['SPOTLIGHT'] == 'Y']

for item_id, row_obj in enumerate(spotlight_df.itertuples()):
    row_dict = row_obj.__dict__
    item_str = item_template_str + ""

    q_df = camready_df.query("PAPERID == %d" % row_dict['PAPERID'])
    if q_df.shape[0] == 1:
        url_str = q_df['PDFURL'].values[0]
        if not pd.isnull(url_str) and url_str[:4] == 'http':
            # only keep good arxiv links
            row_dict['PDFURL'] = url_str

    for key, val in row_dict.items():
        default_val = ""
        cur_val = str(val)
        if len(cur_val) == '' or cur_val == 'nan':
            cur_val = default_val
        item_str = item_str.replace("{{%s}}" % str(key), cur_val)
    out_md_str += item_str


out_md_str += "</div>\n"

with open("../pages/spotlights.md", 'w') as f:
    f.write(out_md_str)