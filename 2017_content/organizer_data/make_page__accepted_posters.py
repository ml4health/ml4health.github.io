import pandas as pd

csv_df = pd.read_csv("poster_assignments.csv")

item_template_str = \
"""\n
<!-- 12/12 = full width on mobile, 6/12 = 1/2 screen on laptop -->
<div class="col-xs-12 col-md-6"> 
<div class="thumbnail">
    <div class="caption">
        <h5>{{TITLE}}</h5>
        <p>{{AUTHORS}}</p>
    </div>
</div>
</div>
\n"""

out_md_str = "Title: Accepted Posters \nDate: 2017-11-15\nSkipNavBar: 1"
out_md_str += (
"""\n
<!-- THIS PAGE SRC IS AUTO GENERATED. At terminal: $ make accepted_posters -->
\n""")

#n_per_row = 100
out_md_str += \
"""
Please attend our poster sessions to hear more about these exciting papers!

Jump to:
<ul>
<li><a href="#session1"> Poster Session 1 (10:20-10:50) </a></li>
<li><a href="#session2"> Poster Session 2 (15:20-15:50) </a></li>
</ul>

These are currently *draft* session assignments, pending last minute author availability issues. Please check back on December 2 for final assignments.

Remember to follow the <a href="poster-instructions.html">posted poster instructions</a>: **Portrait format. Max size: 20 inches wide and 30 inches tall.**

<b>Presenters</b>: if you cannot make your assigned session please fill out this form:
<a href="https://goo.gl/forms/87BCJeTMVfnevKrv2">https://goo.gl/forms/87BCJeTMVfnevKrv2</a>
We will try to reassign you to the opposite session if space is available, but we can make no guarantees.
"""

open_div_str = \
"""
<div class="row display-flex" style="display:flex; display:-webkit-flex;  flex-wrap:wrap; margin-top:25px;">
"""
close_div_str = "</div>"

for sessionid, session_title_html in [
        ('AM',
            '<h2><a name="session1">Poster Session 1 (10:20-10:50)</a></h2>'),
        ('PM',
            '<h2><a name="session2">Poster Session 2 (15:20-15:50)</a></h2>')]:
    out_md_str += session_title_html
    out_md_str += open_div_str
    for item_id, row_obj in enumerate(csv_df.itertuples()):
        row_dict = row_obj.__dict__
        item_str = item_template_str + ""
        if row_dict['SESSION'] != sessionid:
            continue
        for key, val in row_dict.items():
            default_val = ""
            cur_val = str(val)
            if len(cur_val) == '' or cur_val == 'nan':
                cur_val = default_val
            item_str = item_str.replace("{{%s}}" % str(key), cur_val)
        out_md_str += item_str
    out_md_str += close_div_str

with open("../pages/accepted_posters.md", 'w') as f:
    f.write(out_md_str)