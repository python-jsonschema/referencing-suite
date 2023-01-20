from pathlib import Path

import nox

ROOT = Path(__file__).parent

nox.options.sessions = []


def session(default=True, **kwargs):
    def _session(fn):
        if default:
            nox.options.sessions.append(kwargs.get("name", fn.__name__))
        return nox.session(**kwargs)(fn)

    return _session


@session()
def tests(session):
    session.install("jsonschema", "pytest")
    session.run("pytest", *session.posargs)
