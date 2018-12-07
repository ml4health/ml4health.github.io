import pandas as pd

csv_df = pd.read_csv("travel_awards.csv")

item_template_str = \
"""\n
<!-- 6/12 = 1/2 width on mobile, 4/12 = 1/3 screen on laptop -->
<div class="col-xs-6 col-md-4"> 
<div class="thumbnail">
    <div class="caption">
        <h5>{{NAME}}</h5>
    </div>
</div>
</div>
\n"""

"""
<!-- 6/12 = 1/2 width on mobile, 4/12 = 1/3 screen on laptop -->
<div class="col-xs-6 col-md-4"> 
<div class="thumbnail">
    <div class="caption">
        <h5>{{NAME}}</h5>
        <p>{{INSTITUTION}}</p>
    </div>
</div>
</div>
"""

out_md_str = "Title: Travel Awards\nDate: 2017-11-15\nSkipNavBar: 1"
out_md_str += (
"""\n
<!-- THIS PAGE SRC IS AUTO GENERATED. At terminal: $ make travel_awards -->
\n""")

#n_per_row = 100
out_md_str += \
"""
Congratulations to the participants below selected for travel awards.

Thanks also to our <a href="sponsors.html">sponsors</a> for the generous support to fund these awards.

<div class="row display-flex" style="display:flex; display:-webkit-flex;  flex-wrap:wrap;">
"""

for item_id, row_obj in enumerate(csv_df.itertuples()):
    row_dict = row_obj.__dict__
    item_str = item_template_str + ""
    #from IPython import embed; embed()
    for key, val in row_dict.items():
        default_val = ""
        cur_val = str(val)
        if len(cur_val) == '' or cur_val == 'nan':
            cur_val = default_val
        item_str = item_str.replace("{{%s}}" % str(key), cur_val)
    out_md_str += item_str


out_md_str += "</div>\n"

with open("../pages/travel_awards.md", 'w') as f:
    f.write(out_md_str)