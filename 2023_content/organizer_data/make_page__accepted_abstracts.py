import pandas as pd
import pdb

csv_df = pd.read_csv("extended_abstracts.csv")
csv_df.fillna(0, inplace=True)

N = len(csv_df)

morning_df   = csv_df[csv_df['Session'] == 'Morning']
afternoon_df = csv_df[csv_df['Session'] == 'Afternoon']

out_md_str = "Title: Extended Abstracts \nDate: 2020-12-01\n"
out_md_str += (
"""\n
<!-- THIS PAGE SRC IS AUTO GENERATED. At terminal: $ make accepted_papers -->
\n""")

#n_per_row = 100
out_md_str += \
"""
We have accepted %d extended abstracts for presentation at the workshop, which are hosted <a href="https://arxiv.org/html/2011.11554">on the ML4H 2020 arXiv index</a>.

These are listed below, with links to the posters. Numbers indicate poster session IDs.

See the <a href="https://neurips.cc/virtual/2020/protected/workshop_16134.html">NeurIPS workshop page</a> for live video, chat links, and the most updated schedule. We have also created a <a href="https://docs.google.com/document/d/1bE-BoGPpAuqlFlqy_PpljB-t_HSNH0ZFRzgn9yjW0B8/edit?usp=sharing">Guide for Poster Presenters</a> and a <a href="https://docs.google.com/document/d/1p2IjQNUnYWE9iakdy92AlHCJTh9Izto213SoTAPGEUs/edit?usp=sharing">Livestream Guide for Attendees</a>

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

for i, row in morning_df.iterrows():
    # print(row)
    if True:
    # if row.URL and len(row.URL) > 3:
        item_str = f"""
        \n
        <!-- 12/12 = full width on mobile, 6/12 = 1/2 screen on laptop -->
        <div class="col-xs-12 col-md-6"> 
        <div class="thumbnail">
            <div class="caption">
                <h5><a href="{row.URL}">{row.Poster_ID}. {row.Title}</a></h5>
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

for i, row in afternoon_df.iterrows():
    # print(row)
    # if row.URL and len(row.URL) > 3:
    if True:
        item_str = f"""
        \n
        <!-- 12/12 = full width on mobile, 6/12 = 1/2 screen on laptop -->
        <div class="col-xs-12 col-md-6"> 
        <div class="thumbnail">
            <div class="caption">
                <h5><a href="{row.URL}">{row.Poster_ID}. {row.Title}</a></h5>
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
                <h5>{row.Poster_ID}. {row.Title}</h5>
                <p>{row.Authors}</p>
            </div>
        </div>
        </div>
        """
    out_md_str += item_str
out_md_str += close_div_str
with open("../pages/accepted_posters.md", 'w') as f:
    f.write(out_md_str)