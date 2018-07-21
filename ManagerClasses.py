__author__ = 'john.young'


class Object(object):

    def toJSON(self):
        return self.__dict__

    def obj_keys(self):
        return self.__dict__.keys()

class GObject(Object):

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Org(GObject):

    def __init__(self, id, login, avatar_url):
        super(Org, self).__init__(id, login)
        self.avatar_url = avatar_url


class Repo(GObject):

    def __init__(self, id, name, html_url=None, git_url=None, ssh_url=None, clone_url=None):
        super(Repo, self).__init__(id, name)
        self.html_url = html_url
        self.git_url = git_url
        self.ssh_url = ssh_url
        self.clone_url = clone_url
        self.pushed_at = None
        self.open_issues = None
        self.org_name = None


class Tag(GObject):

    def __init__(self, id, name, commit_sha, commit_url):
        super(Tag, self).__init__(id, name)
        self.commit_sha = commit_sha
        self.commit_url = commit_url


class Label(GObject):

    def __init__(self, id, name, color):
        super(Label, self).__init__(id, name)
        self.color = color


# COMPOSITION

class Orgs(Object):

    def __init__(self):
        self.orgs = []

    def add_org(self, org):
        self.orgs.append(org)

    def remove_org(self, org):
        self.orgs.remove(org)

    def list(self):
        tmp_dic = self.__dict__.copy()
        tmp_arr = []
        for letter, number in tmp_dic.iteritems():
            for el in tmp_dic[letter]:
                tmp_arr.append(el.toJSON())
        return tmp_arr

    def toJSON(self):
        return self.list()
