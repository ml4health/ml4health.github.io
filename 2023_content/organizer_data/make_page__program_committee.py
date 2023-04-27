import pandas as pd

pc_df = pd.read_csv("2019_pc_members_public.csv")
pc_df.sort_values("LASTNAME", inplace=True)

out_md_str = "Title: Program Committee\nDate: 2019-12-11"
out_md_str += (
"""\n
<!-- THIS PAGE SRC IS AUTO GENERATED. At terminal: $ make program_committee -->
\n""")

# Existing PC Members code
#n_per_row = 100

out_md_str += \
"""
<h3>Program Committee</h3>

Many thanks to the 290 members of our program committee who reviewed >50% of assigned papers.

<div class="row display-flex" style="display:flex; display:-webkit-flex;  flex-wrap:wrap;">
"""

for item_id, row_obj in pc_df.iterrows():
    item_str = f"""
    \n
    <!-- 6/12 = full width on mobile, 4/12 screen on laptop -->
    <div class="col-xs-6 col-md-4"> 
    <div class="thumbnail">
        <div class="caption">
            <p>
            <strong>{row_obj.FIRSTNAME} {row_obj.LASTNAME}</strong><br />{row_obj.AFFIL}
            </p>
        </div>
    </div>
    </div>
    \n"""
    out_md_str += item_str


out_md_str += "</div>\n"


with open("../pages/program_committee.md", 'w') as f:
    f.write(out_md_str)