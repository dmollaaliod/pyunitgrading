# Steps for grading

1. Unpack - will copy the files from folder `submissions` to folder config.ini->basedir
   ```bash
   $ python unpack.py config.ini submissions
   ```
2. Run tests
   ```bash
   (comp3420) $ python ../runtests.py submissions.zip config.ini
   ```
3. Feedback upload - edit line 9 with name of submissions folder
   ```bash
   $ python upload_feedback_files.py
   ```
   