__author__ = 'john.young'


class Object(object):

    def toJSON(self):
        return self.__dict__


class Org(Object):

    def __init__(self, id, login, avatar_url):
        self.id = id
        self.name = login
        self.avatar_url = avatar_url


class Repo(Object):

    def __init__(self, id, name, html_url, git_url, ssh_url, clone_url):
        self.id = id
        self.name = name
        self.html_url = html_url
        self.git_url = git_url
        self.ssh_url = ssh_url
        self.clone_url = clone_url


class Tag(Object):

    def __init__(self, id, name, commit_sha, commit_url):
        self.id = id
        self.name = name
        self.commit_sha = commit_sha
        self.commit_url = commit_url


class Label(Object):

    def __init__(self, name, color):
        self.name = name
        self.color = color




