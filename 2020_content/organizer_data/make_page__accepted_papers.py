import pandas as pd
import pdb

csv_df = pd.read_csv("papers.csv")
csv_df.fillna(0, inplace=True)

N = len(csv_df)
morning_df = csv_df[csv_df['Session'] == 'Morning']
afternoon_df = csv_df[csv_df['Session'] == 'Afternoon']

out_md_str = "Title: Papers \nDate: 2019-12-11\n"
out_md_str += (
"""\n
<!-- THIS PAGE SRC IS AUTO GENERATED. At terminal: $ make accepted_posters -->
\n""")

#n_per_row = 100
out_md_str += \
"""
We have accepted %d papers to be included in the Volume 136 of the <a href="http://proceedings.mlr.press/v136/">Proceedings of Machine Learning Research</a>.
These are listed below, with links to posters to be added Dec 11. Numbers indicate poster session IDs.

<ul>
<li><a href="#session1"> Poster Session 1 (11:30-12:30) </a></li>
<li><a href="#session2"> Poster Session 2 (17:15-18:15) </a></li>
</ul>
""" % N

ref_str = """<h3 id="session1">Session 1</h3>"""
out_md_str += ref_str

open_div_str = \
"""
<div class="row display-flex" style="display:flex; display:-webkit-flex;  flex-wrap:wrap; margin-top:25px;">
"""
out_md_str += open_div_str
close_div_str = "</div>"
static = "{static}"

for i, row in morning_df.iterrows():
    item_str = f"""
    \n
    <!-- 12/12 = full width on mobile, 6/12 = 1/2 screen on laptop -->
    <div class="col-xs-12 col-md-6"> 
    <div class="thumbnail">
        <div class="caption">
            <h5>{row.Poster_ID}. {row.Title}</h5>
            <p>{row.Authors}</p>
        </div>
    </div>
    </div>
    """
    out_md_str += item_str
out_md_str += close_div_str

ref_str = """<h3 id="session2">Session 2</h3>"""
out_md_str += ref_str

open_div_str = \
"""
<div class="row display-flex" style="display:flex; display:-webkit-flex;  flex-wrap:wrap; margin-top:25px;">
"""
out_md_str += open_div_str
close_div_str = "</div>"
static = "{static}"

for i, row in afternoon_df.iterrows():
    item_str = f"""
    \n
    <!-- 12/12 = full width on mobile, 6/12 = 1/2 screen on laptop -->
    <div class="col-xs-12 col-md-6"> 
    <div class="thumbnail">
        <div class="caption">
            <h5>{row.Poster_ID}. {row.Title}</h5>
            <p>{row.Authors}</p>
        </div>
    </div>
    </div>
    """
    out_md_str += item_str
out_md_str += close_div_str

with open("../pages/accepted_papers.md", 'w') as f:
    f.write(out_md_str)