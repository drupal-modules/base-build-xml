#!/usr/bin/env python
#
#  Original author: Corey Goldberg, Dec 2012
#  Updated by: Mauricio Lima, Jun 2013
#    Improvements detecting differente styles of junit report (Jasmine report)

import os
import sys
import xml.etree.ElementTree as ET


"""Merge multiple JUnit XML files into a single results file.
Output dumps to sdtdout.
example usage:
    $ python merge_junit_results.py results1.xml results2.xml > results.xml
"""


def main():
    args = sys.argv[1:]
    if not args:
        usage()
        sys.exit(2)
    if '-h' in args or '--help' in args:
        usage()
        sys.exit(2)
    merge_results(args[:])


def merge_results(xml_files):
    failures = 0
    tests = 0
    errors = 0
    time = 0.0
    cases = []

    for file_name in xml_files:
        tree = ET.parse(file_name)
        root = tree.getroot()
        test_suites = tree.findall('testsuite')
        if root.tag == 'testsuite':
            test_suites.append(root)
        for test_suite in test_suites:
            failures += int(test_suite.attrib['failures'])
            tests += int(test_suite.attrib['tests'])
            errors += int(test_suite.attrib['errors'])
            time += float(test_suite.attrib['time'] or '0')
            cases.append(test_suite.getchildren())

    new_root = ET.Element('testsuite')
    new_root.attrib['failures'] = '%s' % failures
    new_root.attrib['tests'] = '%s' % tests
    new_root.attrib['errors'] = '%s' % errors
    new_root.attrib['time'] = '%s' % time
    for case in cases:
        new_root.extend(case)
    new_tree = ET.ElementTree(new_root)
    ET.dump(new_tree)


def usage():
    this_file = os.path.basename(__file__)
    print 'Usage:  %s results1.xml results2.xml' % this_file


if __name__ == '__main__':
    main()