import shlex
import subprocess as sp
import platform

if 'windows' not in platform.platform().lower():
    raise NotImplementedError("Use the `sh` module's `git` from PyPI instead!")
else:
    pass


def _call_process(execcmd, _ok_code=None, return_data=False):
    proc = sp.Popen(shlex.split(execcmd), stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    (stdout, stderr) = proc.communicate()
    retcode = proc.returncode
    if retcode != 0:
        if _ok_code and retcode not in _ok_code:
            raise sp.CalledProcessError(retcode, execcmd, stdout, stderr)
        else:
            raise sp.CalledProcessError(retcode, execcmd, stdout, stderr)

    if return_data:
        return stdout, stderr, retcode
    else:
        pass


class Git:
    # add
    @staticmethod
    def add(*args):
        execcmd = "git add " + " ".join(args)
        _call_process(execcmd)

    # branch
    @staticmethod
    def branch(*args):
        execcmd = "git branch " + " ".join(args)
        _call_process(execcmd)

    # Checkout
    @staticmethod
    def checkout(*args):
        execcmd = "git checkout " + " ".join(args)
        _call_process(execcmd)

    # commit
    @staticmethod
    def commit(*args):
        execcmd = "git commit " + " ".join(args)
        _call_process(execcmd)

    # Config
    @staticmethod
    def config(*args, _ok_code=None):
        execcmd = "git config " + " ".join(args)
        _call_process(execcmd, _ok_code=_ok_code)

    # merge
    @staticmethod
    def merge(*args):
        execcmd = "git merge " + " ".join(args)
        _call_process(execcmd)

    # push
    @staticmethod
    def push(*args):
        execcmd = "git push " + " ".join(args)
        _call_process(execcmd)

    # remote.update
    class remote:
        @staticmethod
        def update(*args):
            execcmd = "git remote update " + " ".join(args)
            _call_process(execcmd)

    # reset
    @staticmethod
    def reset(*args):
        execcmd = "git reset" + " ".join(args)
        _call_process(execcmd)

    # rev-parse
    @staticmethod
    def rev_parse(*args):
        execcmd = "git rev-parse" + " ".join(args)
        return _call_process(execcmd, return_data=True)[0]

    # status
    @staticmethod
    def status(*args):
        execcmd = "git " + " ".join(args)
        return _call_process(execcmd, return_data=True)[0]

    # status
    @staticmethod
    def status_stripped(*args):
        execcmd = "git -c color.status=false " + " ".join(args)
        return _call_process(execcmd, return_data=True)[0]
