import pandas as pd

csv_df = pd.read_csv("organizers.csv")
csv_df = csv_df.fillna('') # Fill missing values with blanks

csv_df['WORKSHOP_ROLE'] = csv_df['WORKSHOP_ROLE'].astype('str')
csv_df['LASTNAME'] = [name.split()[-1] for name in csv_df['NAME'].values]

csv_df.sort_values(["WORKSHOP_ROLE", "LASTNAME"], inplace=True)

# Two categories: main folks with defined roles and aux folks
main_team_df = csv_df.query("WORKSHOP_ROLE != '' & WORKSHOP_ROLE != 'Senior Advisory Committee'")
advise_team_df = csv_df.query("WORKSHOP_ROLE == 'Senior Advisory Committee'")
aux_team_df = csv_df.query("WORKSHOP_ROLE == ''")
# assert aux_team_df.shape[0] > 0

main_item_template_str = \
"""\n
    <!-- 6/12 = 1/2 width on mobile, 4/12 = 1/3 screen on laptop -->
    <div class="col-xs-6 col-md-4"> 
    <div class="thumbnail">
        <a href="{{WEBSITE}}">
        <img 
            src="{static}/images/headshots_200x200/{{IMGFILE}}"
            alt="{{NAME}} headshot"
            style="width:88%"
            align="center">
        <div class="caption">
            <h5>{{NAME}}</h5>
            <p>{{AFFIL}}, {{TITLE}}
            <br />
            <emph>{{WORKSHOP_ROLE}}</emph>
            </p>
            <p></p>
        </div>
        </a>
    </div>
    </div>
\n"""

senior_advisory_item_template_str = \
"""\n
    <!-- 6/12 = 1/2 width on mobile, 4/12 = 1/3 screen on laptop -->
    <div class="col-xs-6 col-md-4"> 
    <div class="thumbnail">
        <a href="{{WEBSITE}}">
        <img 
            src="{static}/images/headshots_200x200/{{IMGFILE}}"
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

aux_item_template_str = \
"""\n
    <!-- 6/12 = 1/2 width on mobile, 4/12 = 1/3 screen on laptop -->
    <div class="col-xs-6 col-md-4"> 
    <div class="thumbnail">
        <a href="{{WEBSITE}}">
        <div class="caption">
            <h5>{{NAME}}</h5>
            <p>{{AFFIL}}, {{TITLE}}
            <br />
            <emph>{{WORKSHOP_ROLE}}</emph>
            </p>
            <p></p>
        </div>
        </a>
    </div>
    </div>
\n"""


out_md_str = "Title: Organizers\nDate: 2018-06-01\n"
out_md_str += (
"""\n
<!-- THIS PAGE SRC IS AUTO GENERATED. At terminal: $ make organizers -->

Our team of many organizers is excited to work together to make this workshop possible.

Please direct all workshop-related questions to: <a href="mailto:ml4h.workshop.nips.2020@gmail.com">ml4h.workshop.nips.2020@gmail.com</a>

<!-- Thanks also to the
<a href="program-committee.html">many members of our program committee</a>
for helping peer review all submissions. -->

\n""")

out_md_str += "\n<h2><a name='primary'>Primary Organizers</a></h2>"

## Main team names, images, + links
out_md_str += '\n\n\n<div class="container">'
out_md_str += '\n<div class="row display-flex">'
for item_id, row_obj in enumerate(main_team_df.to_dict('records')):
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

out_md_str += '\n\n\n<div class="container">'
out_md_str += "\n<h2><a name='additional'>Senior Advisory Committee</a></h2>"
## Auxiliary team names + links
out_md_str += '\n<div class="row display-flex">'
for item_id, row_obj in enumerate(advise_team_df.to_dict('records')):
    row_dict = row_obj
    item_str = senior_advisory_item_template_str + ""
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
        
        if key != 'WORKSHOP_ROLE':
            item_str = item_str.replace("{{%s}}" % str(key), cur_val)
    out_md_str += item_str
out_md_str += "</div>\n"
out_md_str += "</div>\n"
out_md_str += "<br />\n"

# out_md_str += '\n\n\n<div class="container">'
# out_md_str += "\n<h2><a name='additional'>Other Organizers</a></h2>"
## Auxiliary team names + links
# out_md_str += '\n<div class="row display-flex">'
# for item_id, row_obj in enumerate(aux_team_df.itertuples()):
#     row_dict = row_obj.__dict__
#     item_str = aux_item_template_str + ""
#     for key, val in row_dict.items():
#         if key == 'IMGFILE':
#             default_val = "placeholder.jpg"
#         elif key == 'WEBSITE':
#             default_val = "#"
#         else:
#             default_val = ""
#         cur_val = str(val)
#         if len(cur_val) == '' or cur_val == 'nan':
#             cur_val = default_val
#         item_str = item_str.replace("{{%s}}" % str(key), cur_val)
#     out_md_str += item_str
# out_md_str += "</div>\n"
# out_md_str += "</div>\n"

with open("../pages/workshop-organizers.md", 'w') as f:
    f.write(out_md_str)