
# github-org-mgr


Example using the **Requestable** wrapper to make API calls. In the following example, the response data
containing the label information will be printed out from the specified repository (repository = user/repo).
```python
ex_auth = {
    'token': "<Add Token>"
}

ex = Requestable(ex_auth, "https://api.github.com")
retd = ex.listLabels("jpyoung/gitflow")

if retd.status_code == 200:
    print(retd.json())
```
