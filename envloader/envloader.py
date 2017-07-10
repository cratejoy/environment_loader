import os


__all__ = ['load_environment']


def _get_vars(path):
    env = {}
    with open(path, 'r') as env_file:
        rows = env_file.readlines()
        for v in rows:
            v = v.strip().replace('"', '').replace("'", '')
            if not v or v[0] == '#':
                continue

            key, value = v.split('=')
            env[key] = value

    return env


def load_environment(default_env='config/env', custom_env='.env'):
    env = _get_vars(default_env)
    if custom_env and os.path_exists(custom_env):
        env.update(_get_vars(custom_env)

    os.environ.update(env)

