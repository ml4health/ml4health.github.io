import pandas as pd
import pdb

csv_df = pd.read_csv("papers.csv", sep="|")
csv_df.fillna(0, inplace=True)

out_md_str = "Title: Papers \nDate: 2019-12-11\n"
out_md_str += (
"""\n
<!-- THIS PAGE SRC IS AUTO GENERATED. At terminal: $ make accepted_posters -->
\n""")

#n_per_row = 100
out_md_str += \
"""
We have accepted 17 papers to be included in the 2019 ML4H Proceedings to be published in PMLR.
These are listed below, with links to proof versions. These will be updated with the final links in PMLR shortly. 
Papers will be presented as spotlight talks or poster presentations Friday Dec 13 in Vancouver.
"""

open_div_str = \
"""
<div class="row display-flex" style="display:flex; display:-webkit-flex;  flex-wrap:wrap; margin-top:25px;">
"""
out_md_str += open_div_str
close_div_str = "</div>"
filename = "{filename}"

for i, row in csv_df.iterrows():
    # print(row)
    # if row.URL and len(row.URL) > 3:
    #     item_str = f"""
    #     \n
    #     <!-- 12/12 = full width on mobile, 6/12 = 1/2 screen on laptop -->
    #     <div class="col-xs-12 col-md-12"> 
    #     <div class="thumbnail">
    #         <div class="caption">
    #             <h5><a href="{row.URL}">{row.Title}</a></h5>
    #             <p>{row.Authors}</p>
    #         </div>
    #     </div>
    #     </div>
    #     """
    # else:
    print(row)
    item_str = f"""
    \n
    <!-- 12/12 = full width on mobile, 6/12 = 1/2 screen on laptop -->
    <div class="col-xs-12 col-md-12"> 
    <div class="thumbnail">
        <div class="caption">
            <h5><a href="{filename}/pdf/{row.ID}_ml4h_preprint.pdf">{row.Title}</a></h5>
            <p>{row.Authors}</p>
        </div>
    </div>
    </div>
    """
    out_md_str += item_str
out_md_str += close_div_str
with open("../pages/accepted_papers.md", 'w') as f:
    f.write(out_md_str)