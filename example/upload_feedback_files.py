"""Copy feedback files
This program copies feedback files for upload to iLearn."""

import pathlib
import shutil
import os

from_dir = "tmp"
submissions_dir = "submissions"
to_dir = "upload"

from_path = pathlib.Path(from_dir)
to_path = pathlib.Path(to_dir)
submissions_path = pathlib.Path(submissions_dir)

if not os.path.exists(to_dir):
    os.makedirs(to_dir)


for feedback_file_path in list(from_path.glob("*/test_output.txt")) + list(from_path.glob("*/test_errors.txt")):
    base_dir, student_dir, feedback_file = feedback_file_path.parts
    print(student_dir, feedback_file)
    submission_filepath = [f for f in submissions_path.glob(student_dir+"*")]

    if len(submission_filepath) > 0:
        submission_filepath = submission_filepath[0]
    else:
        print("No submission information found for student", student_dir)
        continue

    submission_filename = submission_filepath.parts[-1]
#    to_filepath = to_dir+"/"+"_".join(str(submission_filename).split("_")[:-1])+"_test_output.txt"
    to_filepath = to_dir+"/"+"_".join(str(submission_filename).split("_")[:4])+"_"+feedback_file

#    to_filepath = to_dir+"/"+str(submission_filename).split("_")[0]+"_test_output.txt"
    print(to_filepath)
#    print([f for f in to_path.glob(student_dir+"*")])
#    outfile_path = "_".join(list(to_path.glob(student_dir+"*"))[0].split("_")[:-1])+"_Feedback.txt"
#    print(student_dir, feedback_file, outfile_path)
    shutil.copy(feedback_file_path, to_filepath)
