__author__ = 'john.young'


class Object(object):

    def toJSON(self):
        return self.__dict__


class GObject(Object):

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Org(GObject):

    def __init__(self, id, login, avatar_url):
        super(Org, self).__init__(id, login)
        self.avatar_url = avatar_url


class Repo(GObject):

    def __init__(self, id, name, html_url, git_url, ssh_url, clone_url):
        super(Repo, self).__init__(id, name)
        self.html_url = html_url
        self.git_url = git_url
        self.ssh_url = ssh_url
        self.clone_url = clone_url


class Tag(GObject):

    def __init__(self, id, name, commit_sha, commit_url):
        super(Tag, self).__init__(id, name)
        self.commit_sha = commit_sha
        self.commit_url = commit_url


class Label(GObject):

    def __init__(self, id, name, color):
        super(Label, self).__init__(id, name)
        self.color = color
