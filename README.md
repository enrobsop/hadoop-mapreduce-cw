hadoop-mapreduce-cw
===================

A small Hadoop, Python and Gradle dev project. 

# Pre-requisites

## Build / test
The test process pipes data between mappers and reducers (Python scripts) using bash. Hadoop is not required for this.
  
To build and test the following are needed:

  - **Python** Python 2 has been used for development. Python can be downloaded [here](https://www.python.org/download/).
  - **Gradle** The simplest way to install and manage Gradle is with [GVM](http://gvmtool.net). Once GVM is installed, use: `gvm install gradle`.
  
## Hadoop
**Hadoop** should be used to run a full batch job using multiple nodes (e.g. when using the live data). See (http://hadoop.apache.org/releases.html).  
  
# Build

To run everything, type: `gradle`. That's it.

## Gradle tasks

Command | Description
------- | -----------
`gradle`    | Runs default build which runs the tests (below) and creates `./build/distributions/code.tar`.
`gradle tasks` | Lists gradle tasks available
`gradle testStudentTimesJob` | Tests the student times map reduce Python code using `./test/student_test_posts.csv` as input. The output is verified against `./test/expected_student_times_result.txt`.
`gradle testStudyGroups` | See `testStudentTimes`.
`gradle testPopularTags` | See `testStudentTimes`.
`gradle testAverageLength` | See `testStudentTimes`.
`gradle testAllJobs` | Tests all map reduce jobs using the `student_test_posts.csv` as described above.
`gradle codeDistTar` | Archives `./code` into `./build/distributions/code.tar`.

Note: 
The live (non-test) data is version controlled in tar.gz format. Use `tar xvfz *.gz` on archives in the `data` directory before moving to HDFS and running jobs.

