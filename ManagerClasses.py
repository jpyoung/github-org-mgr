__author__ = 'john.young'


class Object(object):

    class_name = 'Object'

    def to_json(self):
        """
        JSON string representation of the object.
        """

        return self.__dict__

    def obj_keys(self):
        """
        Return a list of the keys in the object.
        """

        return self.__dict__.keys()

    def __str__(self):
        """
        Readable string representation of object
        """

        return '__str__ for Object'


class GObject(Object):

    class_name = 'GObject'

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name


class Org(GObject):

    class_name = 'Organization'

    def __init__(self, id, login, avatar_url):
        super(Org, self).__init__(id, login)
        self.avatar_url = avatar_url

    def __str__(self):
        return self.name


class Repo(GObject):

    class_name = 'Repository'

    def __init__(self, id, name, html_url=None, git_url=None, ssh_url=None, clone_url=None):
        super(Repo, self).__init__(id, name)
        self.html_url = html_url
        self.git_url = git_url
        self.ssh_url = ssh_url
        self.clone_url = clone_url
        self.pushed_at = None
        self.open_issues = None
        self.org_name = None

    def set_fields(self, data):
        self.html_url = data['html_url']
        self.git_url = data['git_url']
        self.ssh_url = data['ssh_url']
        self.clone_url = data['clone_url']
        self.pushed_at = data['pushed_at']
        self.open_issues = data['open_issue']
        self.org_name = data['org_name']

    def _rep(self):
        return '<{0} [{1}]>'.format(self.class_name, self)

    def __str__(self):
        return self.name + "Jack"


class Tag(GObject):

    class_name = 'Tag'

    def __init__(self, id, name, commit_sha, commit_url):
        super(Tag, self).__init__(id, name)
        self.commit_sha = commit_sha
        self.commit_url = commit_url

    def __str__(self):
        return self.name


class Label(GObject):

    class_name = 'Label'

    def __init__(self, id, name, color=None):
        super(Label, self).__init__(id, name)
        self.color = color

    def set_fields(self, data):
        self.color = data['color']

    def __str__(self):
        return self.name + " " + self.color

    def create_label(self, name, color):
        """Create a label for this repository.
        :param str name:
            (required), name to give to the label
        :param str color:
            (required), value of the color to assign to the
            label, e.g., '#fafafa' or 'fafafa' (the latter is what is sent)
        :returns:
            the created label
        :rtype:
            :class:`~github3.issues.label.Label`
        """
        self.color = color  #remove this line not needed
        json = None
        if name and color:
            data = {'name': name, 'color': color.strip('#')}
        # post url data
        # json = json resp
        return json

# COMPOSITION


class Orgs(Object):
    """
    # COMPOSITION
    Organization Composition

    """

    class_name = 'Organizations'

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
                tmp_arr.append(el.to_json())
        return tmp_arr

    def to_json(self):
        return self.list()
