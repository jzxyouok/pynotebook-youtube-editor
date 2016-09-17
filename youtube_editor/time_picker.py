"""Insert YouTube time picker into Jupyter notebook."""
youtube_edits = """
(
    'entire video',
    (
        'The entire video.',
        (
            '',
            '',
        )
    ),
),
"""

cell_magic = """
<script>\nvar appendYouTubeEdits = function (){\n    var quote = "\'",\n        left = \'(\',\n        right = \')\',\n        space = \' \',\n        append = \'+=\',\n        colon = \':\',\n        comma = \',\',\n        dblQuote = \'"\',\n        spacer = \'    \',\n        cr = \'\\\\n\',\n        startHours = document.getElementById(\'startHours\').value,\n        startMinutes = document.getElementById(\'startMinutes\').value,\n        startSeconds = document.getElementById(\'startSeconds\').value,\n        stopHours = document.getElementById(\'stopHours\').value,\n        stopMinutes = document.getElementById(\'stopMinutes\').value,\n        stopSeconds = document.getElementById(\'stopSeconds\').value,\n        anchor = document.getElementById(\'anchor\').value,\n        description = document.getElementById(\'description\').value,\n        command = [\n        \'youtube_edits\',\n        space,\n        append,\n        space,\n        dblQuote,\n        left,\n        cr,\n        spacer,\n        quote,\n        anchor,\n        quote,\n        comma,\n        \n        cr,\n        spacer,\n        left,\n        cr,\n        spacer,\n        spacer,\n        quote,\n        description,\n        quote,\n        comma,\n        cr,\n        spacer,\n        spacer,\n        left,\n        cr,\n        spacer,\n        spacer,\n        spacer,\n        quote,\n        [\n            startHours,\n            startMinutes,\n            startSeconds,\n        ].join(colon),\n        quote,\n        comma,\n        cr,\n        spacer,\n        spacer,\n        spacer,\n        quote,\n        [\n            stopHours,\n            stopMinutes,\n            stopSeconds,\n        ].join(colon),\n        quote,\n        comma,\n        cr,\n        spacer,\n        spacer,\n        right,\n        comma,\n        cr,\n        spacer,\n        right,\n        comma,\n        cr,\n        right,\n        comma,\n        cr,\n        dblQuote,\n    ].join(\'\'),\n    kernel = IPython.notebook.kernel;\n    kernel.execute(command);\n}\n</script>\n<div>\n<p>start</p>\n<input type="text" id="startHours" size="2" maxlength="2" value="00"></input>:\n<input type="text" id="startMinutes" size="2" maxlength="2" value="00"></input>:\n<input type="text" id="startSeconds" size="2" maxlength="2" value="00"></input><br/>\n<p>stop</p>\n<input type="text" id="stopHours" size="2" maxlength="2" value="00"></input>:\n<input type="text" id="stopMinutes" size="2" maxlength="2" value="00"></input>:\n<input type="text" id="stopSeconds" size="2" maxlength="2" value="00"></input><br/>\n<p>anchor</p>\n<input type="text" id="anchor" size="20" maxlength="20" value="example anchor"></input><br/>\n<p>description</p>\n<input type="text" id="description" size="80" maxlength="200" value="example description"></input><br/><br/>\n<button onClick="appendYouTubeEdits();">set timestamp</button>\n</div>
"""


def write_youtube_edits(youtube_edits):
    """Write a file of YouTube time edits.

    Formats text which is a string representation of tuples.

    :youtube_edits: variable created by cell magic
    """
    text = """edits = (
    {}
)""".format(youtube_edits)
    with open('youtube_edits.py', 'w') as fh:
        fh.write(text)
