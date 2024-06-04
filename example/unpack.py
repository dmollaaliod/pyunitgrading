from configparser import ConfigParser
import os
import shutil
import glob

def read_config(configfile):
    """Read config file and set up defaults,
    return a dictionary of config values"""

    r = dict()
    config = ConfigParser()
    config.read(configfile)

    # paths are resolved relative to the config file directory
    configdir = os.path.dirname(configfile)

    r['basedir'] = config.get('default', 'basedir')
    r['targetname'] = config.get('default', 'targetname', fallback=None)
    r['testmodule'] = config.get('default', 'testmodule')
    r['outputname'] = config.get('default', 'outputname',  fallback='test_output.txt')

    expectzip = config.get('default', 'expectzip', fallback='no')
    r['expectzip'] = expectzip == 'yes'

    modules = config.get('default', 'modules')
    # we split modules on whitespace
    r['modules'] = [os.path.join(configdir, m) for m in modules.split()]

    r['csvname'] = config.get('default', 'csvname', fallback="results.csv")

    return r

def unpack(configfile, submissionfolder):
    """Unpack submissions ready for processing"""

    c = read_config(configfile)
    basedir = c['basedir']
    targetname = c['targetname']

    if not os.path.exists(basedir):
        os.makedirs(basedir)

    userIDs = list(set([f[:8] for f in os.listdir(submissionfolder)]))
    for user in userIDs:
        print(user)
        if not os.path.exists(basedir+"/"+user):
            os.makedirs(basedir+"/"+user)
        for f in glob.glob(submissionfolder+"/"+user+"*"):
            print(f)
            filename = os.path.basename(f).split("assignsubmission_file_")[1]
            shutil.copy(f, basedir+"/"+user+"/"+filename)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="unpack an iLearn folder with submissions")
    parser.add_argument('configfile', action="store", type=str, help="Configuration file")
    parser.add_argument('submissionfolder', action="store", type=str, help="Submission folder")
    args = parser.parse_args()

    unpack(args.configfile, args.submissionfolder)