import pandas as pd

csv_df = pd.read_csv("speakers.csv")
csv_df = csv_df.fillna('') # Fill missing values with blanks

# csv_df['WORKSHOP_ROLE'] = csv_df['WORKSHOP_ROLE'].astype('str')
csv_df['LASTNAME'] = [name.split()[-1] for name in csv_df['NAME'].values]

csv_df.sort_values(["LASTNAME"], inplace=True)

# Two categories: main folks with defined roles and aux folks

main_item_template_str = \
"""\n
    <!-- 6/12 = 1/2 width on mobile, 4/12 = 1/3 screen on laptop -->
    <div class="col-xs-6 col-md-4"> 
    <div class="thumbnail">
        <a href="{{WEBSITE}}">
        <img 
            src="{static}/images/speakers_200x200/{{IMGFILE}}"
            alt="{{NAME}} headshot"
            style="width:88%"
            align="center">
        <div class="caption">
            <h5>{{NAME}}</h5>
            <p>{{AFFIL}}, {{TITLE}}
            </p>
            <p></p>
        </div>
        </a>
    </div>
    </div>
\n"""


out_md_str = "Title: Speakers \nDate: 2019-06-01\n"
out_md_str += (
"""\n
<!-- THIS PAGE SRC IS AUTO GENERATED. At terminal: $ make organizers -->

\n""")

## Main team names, images, + links
out_md_str += '\n\n\n<div class="container">'
out_md_str += '\n<div class="row display-flex">'
for item_id, row_obj in enumerate(csv_df.to_dict('records')):
    # import pdb; pdb.set_trace()
    row_dict = row_obj
    item_str = main_item_template_str + ""
    for key, val in row_dict.items():
        if key == 'IMGFILE':
            default_val = "placeholder.jpg"
        elif key == 'WEBSITE':
            default_val = "#"
        else:
            default_val = ""
        cur_val = str(val)
        if len(cur_val) == '' or cur_val == 'nan':
            cur_val = default_val
        item_str = item_str.replace("{{%s}}" % str(key), cur_val)
    out_md_str += item_str
out_md_str += "</div>\n"
out_md_str += "</div>\n"
out_md_str += "<br />\n"

with open("../pages/speakers.md", 'w') as f:
    f.write(out_md_str)