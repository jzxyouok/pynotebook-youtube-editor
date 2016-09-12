"""Helpers to edit YouTube videos and display them in a Jupyter notebook."""
# coding: utf-8


def convert_to_seconds_from(timestring, delimiter=":"):
    """Convert a timestring to seconds.

    :timestring: HH:MM:SS as a str
    :returns: seconds as int
    """
    return sum(
        # raise 60 to power of i in (0, 1, 2) and
        # multiply it by seconds, minutes and then hours
        int(time_value) * (60 ** i)
        for i, time_value
        in enumerate(reversed(timestring.split(delimiter)))
    )


def get_youtube_url_from(video_id):
    """Make a YouTube embed url

    :returns: Notebook safe url
    """
    return 'https://www.youtube.com/embed/{}?rel=0'.format(
        video_id)


def get_embed_string_from(excerpt, video_url):
    """Create some HTML to display the YouTube video excerpts."""
    EMPTY_STRING = ''
    label, times = excerpt
    start_stop = [
        '<br/>'.join([': '.join(item for item in items if item)])
        for items in zip(('start', 'end'), times)
    ]
    start_stop = EMPTY_STRING.join(["<p>{}</p>".format(item)
                                    for item in start_stop])\
        if all(times) else EMPTY_STRING
    embeded_video_template = ''.join((
            '<h3>{label}</h3>',
            '{start_stop}',
            '<br/>',
            '<iframe width="560" height="315" ',
            'src="{video_url}?rel=0&start={start}&end={end}" ',
            'frameborder="0" allowfullscreen></iframe>',
    ))
    start, end = [convert_to_seconds_from(item)
                  for item in times]\
        if all(times) else times
    if not all(times):
        # the ?rel=0 MUST stay or the video does not load
        # for security reasons, Chrome blocks
        needle = '&start={start}&end={end}'
        return embeded_video_template.replace(needle, '').format(
            video_url=video_url,
            label=label,
            start_stop=start_stop,
        )
    return embeded_video_template.format(
        video_url=video_url,
        label=label,
        start_stop=start_stop,
        start=start,
        end=end
    )

# example of how to record times
video_excerpts = (
    (
        'why',
        (
            "Why begin with 'this' and 'bind'?",
            ('00:00:54', '00:01:17', ),
        ),
    ),
    (
        'entire video',
        (
            'The entire video.',
            ('', '', ),
        ),
    ),
)


def get_example_data():
    """Get an example of what needs to be recorded.

    :returns: example
    """
    return video_excerpts


def get_video_excerpts_map(video_excerpts):
    """Make a map from video_excerpts collection.

    :returns: map
    """
    keys, values = zip(*video_excerpts)
    video_excerpts_map = dict(zip(keys, values))
    return video_excerpts_map
