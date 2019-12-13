import pandas as pd
import pdb

csv_df = pd.read_csv("extended_abstracts.csv", sep="|")
csv_df.fillna(0, inplace=True)

out_md_str = "Title: Extended Abstracts \nDate: 2019-12-11\n"
out_md_str += (
"""\n
<!-- THIS PAGE SRC IS AUTO GENERATED. At terminal: $ make accepted_papers -->
\n""")

#n_per_row = 100
out_md_str += \
"""
We have accepted 97 extended abstracts for presentation at the workshop.

These are listed below, with links to the paper on arXiv if provided by the authors.

The poster acceptances will appear on Friday Dec. 13 in Vancouver.
<ul>
<li><a href="#session1"> Poster Session (11:30-12:30) </a></li>
</ul>
"""

open_div_str = \
"""
<div class="row display-flex" style="display:flex; display:-webkit-flex;  flex-wrap:wrap; margin-top:25px;">
"""
out_md_str += open_div_str
close_div_str = "</div>"

for i, row in csv_df.iterrows():
    # print(row)
    if row.URL and len(row.URL) > 3:
        item_str = f"""
        \n
        <!-- 12/12 = full width on mobile, 6/12 = 1/2 screen on laptop -->
        <div class="col-xs-12 col-md-6"> 
        <div class="thumbnail">
            <div class="caption">
                <h5><a href="{row.URL}">{row.Title}</a></h5>
                <p>{row.Authors}</p>
            </div>
        </div>
        </div>
        """
    else:
        item_str = f"""
        \n
        <!-- 12/12 = full width on mobile, 6/12 = 1/2 screen on laptop -->
        <div class="col-xs-12 col-md-6"> 
        <div class="thumbnail">
            <div class="caption">
                <h5>{row.Title}</h5>
                <p>{row.Authors}</p>
            </div>
        </div>
        </div>
        """
    out_md_str += item_str
out_md_str += close_div_str
with open("../pages/accepted_posters.md", 'w') as f:
    f.write(out_md_str)