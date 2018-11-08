import pandas as pd

pc_df = pd.read_csv("2018_pc_members_public.csv")
pc_df.sort_values("LASTNAME", inplace=True)

spc_df = pd.read_csv("2018_spc_members_public.csv")
spc_df.sort_values("LASTNAME", inplace=True)

item_template_str = \
"""\n
<!-- 6/12 = full width on mobile, 4/12 screen on laptop -->
<div class="col-xs-6 col-md-4"> 
<div class="thumbnail">
    <div class="caption">
        <p>
        <strong>{{FIRSTNAME}} {{LASTNAME}}</strong><br />{{AFFIL}}
        </p>
    </div>
</div>
</div>
\n"""

out_md_str = "Title: Program Committee\nDate: 2018-11-08\nSkipNavBar: 1"
out_md_str += (
"""\n
<!-- THIS PAGE SRC IS AUTO GENERATED. At terminal: $ make program_committee -->
\n""")

# New SPC Members code
out_md_str += \
"""
Many thanks to the Senior Program Committee for their nomination of committee members below.

<div class="row display-flex" style="display:flex; display:-webkit-flex;  flex-wrap:wrap;">
"""

for item_id, row_obj in enumerate(spc_df.itertuples()):
    row_dict = row_obj.__dict__
    item_str = item_template_str + ""
    for key, val in row_dict.items():
        default_val = ""
        cur_val = str(val)
        if len(cur_val) == '' or cur_val == 'nan':
            cur_val = default_val
        item_str = item_str.replace("{{%s}}" % str(key), cur_val)
    out_md_str += item_str

out_md_str += "</div>\n"

# Existing PC Members code
#n_per_row = 100
out_md_str += \
"""
Many thanks to the 100+ members of our program committee who reviewed submitted papers.

<div class="row display-flex" style="display:flex; display:-webkit-flex;  flex-wrap:wrap;">
"""

for item_id, row_obj in enumerate(pc_df.itertuples()):
    row_dict = row_obj.__dict__
    item_str = item_template_str + ""
    for key, val in row_dict.items():
        default_val = ""
        cur_val = str(val)
        if len(cur_val) == '' or cur_val == 'nan':
            cur_val = default_val
        item_str = item_str.replace("{{%s}}" % str(key), cur_val)
    out_md_str += item_str


out_md_str += "</div>\n"

with open("../pages/program_committee.md", 'w') as f:
    f.write(out_md_str)