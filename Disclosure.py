def outer():
    secret = '<some special value you do not know>'
    def inner():
        secret = '<does some magic with secret>'
    return inner

x = outer()
del outer

print(x.func_closure[0].cell_contents)
