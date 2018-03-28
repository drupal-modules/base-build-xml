Base Ant build
==============

Base Ant build config to be imported for Drupal projects.

### Build status

Build status: [![base-build-xml CI status](https://api.travis-ci.org/National-Theatre/base-build-xml.svg?branch=master)](https://travis-ci.org/National-Theatre/base-build-xml)

### Prerequisites

- Apache Ant

### Usage

In your own project, create `build.xml` Ant's file which imports `base.xml`. For example:

    <project name="MyProject" default="build">
      <!-- Override any needed settings -->
      <property name="drupalroot" value="docroot"/>
      <property name="drupalmodules" value="${basedir}/${drupalroot}/sites/all/modules/custom"/>
      <property name="composerdir" value="${basedir}/tests"/>
      <property name="project" value="mysite"/>
      <import>
        <url url="https://raw.githubusercontent.com/National-Theatre/base-build-xml/master/base.xml"/>
      </import>
      <!-- Your other targets here. -->
    </project>

For the full support, include it as Composer package, e.g.

    {
      "require": {
        "NT/base-build-xml": "*@dev",
      },
      "repositories": [
        {
          "type": "git",
          "url": "https://github.com/National-Theatre/base-build-xml.git"
        }
      ],
    }

To run the build, execute the following command in shell:

    ant build
