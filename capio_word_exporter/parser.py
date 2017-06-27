"""Module for parsing transcript data for docx genration"""
import logging

_LG = logging.getLogger(__name__)


def _get_time_range(words):
    return {'start': words[0]['from'], 'end': words[-1]['to']}


def _parse_words(words):
    ret = []
    for word in words:
        _LG.debug('  %s', word)
        result = {'word': word['word']}
        if word['confidence'] <= 0.75:
            _LG.debug('   *Low confidence*')
            result['color'] = (255, 0, 0)
        ret.append(result)
    return ret


def _parse_one_result(result):
    if len(result) > 1:
        _LG.warning(
            '`result` data contains more than one entry. '
            'This is unexpected case; %s', result
        )
    if len(result[0]['alternative']) > 1:
        _LG.warning(
            '`alternative` data contains more than one entry. '
            'Using the first entry.'
        )
    alternative = result[0]['alternative'][0]
    _LG.debug('Parsing sentence: `%s`', alternative['transcript'])
    return {
        'time': _get_time_range(alternative['words']),
        'words': _parse_words(alternative['words']),
    }


def parse_transcript(data):
    """Parse transcript data for feeding to Docx generator

    Parameters
    ----------
    data : list
        List of result dictionaries, returned from `fetch_transcript`
        function.

    Returns
    -------
    list
        List of lines.

    # TODO
    Add example I/O once all components are implemented
    """
    return [_parse_one_result(datum['result']) for datum in data]
