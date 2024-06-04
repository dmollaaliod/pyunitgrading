# Steps for grading

1. Unpack
   ```bash
   $ python unpack.py config.ini submissions
   ```
2. Run tests
   ```bash
   (comp3420) $ python ../runtests.py submissions.zip config.ini
   ```
3. Feedback upload (but the resulting file for upload did not update the feedback to iLearn)
   ```bash
   $ python upload_feedback_files.py
   ```
   