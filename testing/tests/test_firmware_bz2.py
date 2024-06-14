import os
import binwalk


def test_firmware_bz2():
    '''
    Test: Open firmware.bz2, scan for signatures
    verify that all (and only) expected signatures are detected
    '''
    expected_results = [
        [0, 'bzip2 compressed data, block size = 900k'],
    ]

    input_vector_file = os.path.join(os.path.dirname(__file__),
                                     "input-vectors",
                                     "firmware.bz2")

    scan_result = binwalk.scan(input_vector_file,
                               signature=True,
                               quiet=True)

    # Test number of modules used
    assert len(scan_result) == 1

    # Test number of results for that module
    assert len(scan_result[0].results) == len(expected_results)

    # Test result-description
    for result, (expected_offset, expected_description) in zip(scan_result[0].results, expected_results):
        assert result.offset == expected_offset
        assert result.description == expected_description
